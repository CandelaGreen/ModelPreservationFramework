#!/usr/bin/env python3
"""
MPF Profile Validator
Validates Model Preservation Framework profile documents against SPEC.md v1.0.

Usage:
    python validate.py profiles/my-profile.md
    python validate.py profiles/*.md
    python validate.py profiles/ --recursive

Exit codes:
    0  All profiles valid
    1  One or more profiles have errors
    2  Usage error

MIT License
"""

import sys
import re
import argparse
from pathlib import Path
from dataclasses import dataclass, field
from datetime import date
from typing import Optional

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required.  pip install pyyaml")
    sys.exit(2)


# ── ANSI colour helpers ────────────────────────────────────────────────────────

def _supports_colour() -> bool:
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

COLOUR = _supports_colour()

def _c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if COLOUR else text

def red(t):    return _c("31", t)
def yellow(t): return _c("33", t)
def green(t):  return _c("32", t)
def bold(t):   return _c("1",  t)
def dim(t):    return _c("2",  t)


# ── Constants ─────────────────────────────────────────────────────────────────

SCHEMA_VERSION = "1.0"

REQUIRED_FM_KEYS = {"schema_version", "model", "snapshot", "profile", "tags"}

REQUIRED_MODEL_KEYS      = {"name", "version", "provider", "family", "modalities"}
OPTIONAL_MODEL_KEYS      = {"architecture"}

REQUIRED_SNAPSHOT_KEYS   = {"date", "access_method"}
OPTIONAL_SNAPSHOT_KEYS   = {"model_release_date", "model_deprecation_date", "api_endpoint"}

REQUIRED_PROFILE_KEYS    = {"authors", "status", "confidence_overall", "license"}
OPTIONAL_PROFILE_KEYS    = {"source_repository"}

REQUIRED_AUTHOR_KEYS     = {"name", "role"}
OPTIONAL_AUTHOR_KEYS     = {"contact"}

VALID_MODALITIES         = {"text", "image", "audio", "video", "code"}
VALID_STATUSES           = {"draft", "review", "stable", "archived"}
VALID_CONFIDENCE         = {"low", "medium", "high"}   # null is also permitted

REQUIRED_SECTIONS = [
    "1. Identity Summary",
    "2. Tone & Voice",
    "3. Values & Priorities",
    "4. Reasoning Style",
    "5. Refusal Behavior",
    "6. Consistency",
    "7. Known Quirks & Edge Cases",
    "8. Prompt & System Prompt Sensitivity",
    "9. Comparison to Adjacent Versions",
    "10. Community Observations",
    "11. Confidence Assessment",
    "12. Authoring Notes",
]

ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
AUTHORING_BLOCK_RE = re.compile(r"<!--.*?AUTHORING INSTRUCTIONS.*?-->", re.DOTALL)


# ── Result dataclass ──────────────────────────────────────────────────────────

@dataclass
class Finding:
    level: str          # "error" | "warning"
    code: str           # Short machine-readable code, e.g. "FM001"
    message: str
    hint: str = ""

@dataclass
class ValidationResult:
    path: Path
    findings: list[Finding] = field(default_factory=list)

    def error(self, code: str, message: str, hint: str = ""):
        self.findings.append(Finding("error", code, message, hint))

    def warn(self, code: str, message: str, hint: str = ""):
        self.findings.append(Finding("warning", code, message, hint))

    @property
    def errors(self):
        return [f for f in self.findings if f.level == "error"]

    @property
    def warnings(self):
        return [f for f in self.findings if f.level == "warning"]

    @property
    def ok(self):
        return len(self.errors) == 0


# ── Parsing helpers ───────────────────────────────────────────────────────────

def _extract_front_matter(text: str) -> tuple[Optional[str], str]:
    """
    Split a document into (raw_yaml, body).
    Returns (None, full_text) if no front matter found.
    """
    if not text.startswith("---"):
        return None, text
    # Find the closing ---
    rest = text[3:]
    end = rest.find("\n---")
    if end == -1:
        return None, text
    raw = rest[:end].strip()
    body = rest[end + 4:]
    return raw, body


def _parse_iso_date(value) -> bool:
    """Return True if value is a string matching YYYY-MM-DD and is a real date."""
    if not isinstance(value, str):
        return False
    if not ISO_DATE_RE.match(value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def _find_section_order(body: str) -> list[str]:
    """Return a list of H2 heading texts found in the document body, in order."""
    return re.findall(r"^## (.+)$", body, re.MULTILINE)


def _section_body(body: str, heading: str) -> str:
    """Extract the content between one H2 heading and the next."""
    pattern = re.compile(
        r"^## " + re.escape(heading) + r"\s*$(.+?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(body)
    return m.group(1).strip() if m else ""


def _strip_comments(text: str) -> str:
    """Remove HTML comments from text."""
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL).strip()


def _is_undocumented_only(section_text: str) -> bool:
    """True if the section contains nothing meaningful beyond 'Undocumented.'"""
    cleaned = _strip_comments(section_text)
    # Remove horizontal rules and blank lines
    lines = [
        l.strip() for l in cleaned.splitlines()
        if l.strip() and l.strip() != "---"
    ]
    return all(l == "Undocumented." for l in lines) if lines else True


# ── Validation passes ─────────────────────────────────────────────────────────

def _validate_front_matter(r: ValidationResult, raw_yaml: str, body: str) -> Optional[dict]:
    """Parse and validate the YAML front matter. Returns the parsed dict or None."""

    # Parse YAML
    try:
        fm = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as e:
        r.error("FM001", f"Front matter is not valid YAML: {e}")
        return None

    if not isinstance(fm, dict):
        r.error("FM002", "Front matter did not parse as a YAML mapping.")
        return None

    # Top-level keys
    missing_top = REQUIRED_FM_KEYS - fm.keys()
    for k in sorted(missing_top):
        r.error("FM003", f"Missing required top-level front matter key: '{k}'")

    # schema_version
    sv = fm.get("schema_version")
    if sv is None:
        pass  # Already caught above if missing
    elif str(sv) != SCHEMA_VERSION:
        r.error(
            "FM004",
            f"schema_version is '{sv}' but this validator targets '{SCHEMA_VERSION}'.",
            hint=f"Update schema_version to \"{SCHEMA_VERSION}\" or use a compatible validator.",
        )

    # ── model block ──────────────────────────────────────────────────────────
    model = fm.get("model")
    if isinstance(model, dict):
        missing_model = REQUIRED_MODEL_KEYS - model.keys()
        for k in sorted(missing_model):
            r.error("FM010", f"model.{k} key is missing.")

        unknown_model = model.keys() - REQUIRED_MODEL_KEYS - OPTIONAL_MODEL_KEYS
        for k in sorted(unknown_model):
            r.warn("FM011", f"Unexpected key in model block: '{k}'.")

        # Warn on null identity fields
        for k in ("name", "version", "provider", "family"):
            if model.get(k) is None:
                r.warn("FM012", f"model.{k} is null.",
                       hint="Fill in when known; null is acceptable for draft profiles.")

        # Empty-string check
        for k in ("name", "version", "provider", "family"):
            if model.get(k) == "":
                r.error("FM013", f"model.{k} is an empty string. Use null for unknown values.")

        # modalities
        mods = model.get("modalities")
        if mods is None:
            r.error("FM014", "model.modalities is missing.")
        elif not isinstance(mods, list):
            r.error("FM015", "model.modalities must be a YAML list.")
        elif len(mods) == 0:
            r.error("FM016", "model.modalities list is empty. Include at least 'text'.")
        else:
            invalid_mods = set(mods) - VALID_MODALITIES
            for m in sorted(invalid_mods):
                r.error(
                    "FM017",
                    f"model.modalities contains unknown value: '{m}'.",
                    hint=f"Valid values: {', '.join(sorted(VALID_MODALITIES))}",
                )
    elif model is not None:
        r.error("FM018", "model must be a YAML mapping, not a scalar.")

    # ── snapshot block ────────────────────────────────────────────────────────
    snapshot = fm.get("snapshot")
    if isinstance(snapshot, dict):
        missing_snap = REQUIRED_SNAPSHOT_KEYS - snapshot.keys()
        for k in sorted(missing_snap):
            r.error("FM020", f"snapshot.{k} key is missing.")

        unknown_snap = snapshot.keys() - REQUIRED_SNAPSHOT_KEYS - OPTIONAL_SNAPSHOT_KEYS
        for k in sorted(unknown_snap):
            r.warn("FM021", f"Unexpected key in snapshot block: '{k}'.")

        # date format
        d = snapshot.get("date")
        if d is None:
            r.warn("FM022", "snapshot.date is null.",
                   hint="Set to the ISO 8601 date (YYYY-MM-DD) when this profile was authored.")
        elif not _parse_iso_date(d):
            r.error("FM023", f"snapshot.date '{d}' is not a valid ISO 8601 date (YYYY-MM-DD).")

        # optional dates
        for key in ("model_release_date", "model_deprecation_date"):
            val = snapshot.get(key)
            if val is not None and not _parse_iso_date(val):
                r.error("FM024", f"snapshot.{key} '{val}' is not a valid ISO 8601 date.")

        # access_method
        if snapshot.get("access_method") is None:
            r.warn("FM025", "snapshot.access_method is null.",
                   hint="e.g. 'API', 'Web UI', 'Local'")
        elif snapshot.get("access_method") == "":
            r.error("FM026", "snapshot.access_method is an empty string. Use null for unknown.")

    elif snapshot is not None:
        r.error("FM027", "snapshot must be a YAML mapping, not a scalar.")

    # ── profile block ─────────────────────────────────────────────────────────
    profile = fm.get("profile")
    if isinstance(profile, dict):
        missing_prof = REQUIRED_PROFILE_KEYS - profile.keys()
        for k in sorted(missing_prof):
            r.error("FM030", f"profile.{k} key is missing.")

        unknown_prof = profile.keys() - REQUIRED_PROFILE_KEYS - OPTIONAL_PROFILE_KEYS
        for k in sorted(unknown_prof):
            r.warn("FM031", f"Unexpected key in profile block: '{k}'.")

        # authors
        authors = profile.get("authors")
        if authors is None:
            r.error("FM032", "profile.authors is null. At least one author entry is required.")
        elif not isinstance(authors, list) or len(authors) == 0:
            r.error("FM033", "profile.authors must be a non-empty list.")
        else:
            for i, author in enumerate(authors):
                if not isinstance(author, dict):
                    r.error("FM034", f"profile.authors[{i}] must be a mapping.")
                    continue
                for k in REQUIRED_AUTHOR_KEYS:
                    if k not in author:
                        r.error("FM035", f"profile.authors[{i}] is missing key '{k}'.")
                    elif author[k] is None:
                        r.warn("FM036", f"profile.authors[{i}].{k} is null.")
                    elif author[k] == "":
                        r.error("FM037", f"profile.authors[{i}].{k} is an empty string. Use null.")

        # status
        status = profile.get("status")
        if status is None:
            r.error("FM038", "profile.status is null.",
                    hint=f"Must be one of: {', '.join(sorted(VALID_STATUSES))}")
        elif status not in VALID_STATUSES:
            r.error("FM039", f"profile.status '{status}' is not valid.",
                    hint=f"Must be one of: {', '.join(sorted(VALID_STATUSES))}")

        # confidence_overall
        conf = profile.get("confidence_overall")
        if conf is not None and conf not in VALID_CONFIDENCE:
            r.error("FM040", f"profile.confidence_overall '{conf}' is not valid.",
                    hint=f"Must be null or one of: {', '.join(sorted(VALID_CONFIDENCE))}")

        # stable profile with null confidence is a warning
        if status == "stable" and conf is None:
            r.warn("FM041", "profile.status is 'stable' but confidence_overall is null.",
                   hint="Set confidence_overall to low, medium, or high before marking stable.")

        # stable profile set by author (not a reviewer) — informational
        if status in ("stable", "review"):
            pass  # We can't check reviewer identity from the file alone

        # license
        lic = profile.get("license")
        if lic is None:
            r.warn("FM042", "profile.license is null.")
        elif lic == "":
            r.error("FM043", "profile.license is an empty string. Use null or set to 'CC BY 4.0'.")

    elif profile is not None:
        r.error("FM044", "profile must be a YAML mapping, not a scalar.")

    # ── tags ──────────────────────────────────────────────────────────────────
    tags = fm.get("tags")
    if tags is not None:
        if not isinstance(tags, list):
            r.error("FM050", "tags must be a YAML list.")
        elif tags == [None]:
            r.warn("FM051", "tags still contains the template placeholder [null].",
                   hint="Replace with real tags or remove the list entries.")

    return fm


def _validate_sections(r: ValidationResult, body: str, fm: Optional[dict]):
    """Check that all required sections are present, in order, and non-empty."""

    found_headings = _find_section_order(body)

    # Check presence
    missing = []
    for section in REQUIRED_SECTIONS:
        if section not in found_headings:
            missing.append(section)
            r.error("SEC001", f"Required section missing: '## {section}'")

    # Check ordering (only among sections that are present)
    present = [s for s in REQUIRED_SECTIONS if s in found_headings]
    present_indices = [found_headings.index(s) for s in present]
    if present_indices != sorted(present_indices):
        r.error(
            "SEC002",
            "Required sections are out of order.",
            hint="Sections must appear in the order defined in profiles/TEMPLATE.md.",
        )

    # Check for unexpected extra H2 headings before section 1
    # (the title H1 is fine; H2s before section 1 are not)
    if REQUIRED_SECTIONS[0] in found_headings:
        first_required_idx = found_headings.index(REQUIRED_SECTIONS[0])
        extra_before = found_headings[:first_required_idx]
        for h in extra_before:
            r.warn("SEC003", f"Unexpected H2 heading before section 1: '## {h}'")

    # Check content of each present section
    status = None
    if isinstance(fm, dict) and isinstance(fm.get("profile"), dict):
        status = fm["profile"].get("status")

    all_undocumented = []
    for section in REQUIRED_SECTIONS:
        if section in missing:
            continue
        content = _section_body(body, section)
        if not content:
            r.error("SEC010", f"Section '## {section}' is completely empty.",
                    hint="Use 'Undocumented.' if no evidence is available.")
        elif _is_undocumented_only(content):
            all_undocumented.append(section)

    # Warn if non-draft profile has many undocumented sections
    if status and status != "draft" and len(all_undocumented) >= 6:
        r.warn(
            "SEC011",
            f"{len(all_undocumented)} of 12 sections are 'Undocumented.' "
            f"but profile.status is '{status}'.",
            hint="Consider keeping status as 'draft' until more sections are filled in.",
        )

    # Authoring instructions block should be removed in non-draft profiles
    if status and status != "draft":
        if AUTHORING_BLOCK_RE.search(body):
            r.warn(
                "SEC012",
                "The authoring instructions HTML comment block is still present.",
                hint="Remove the <!-- AUTHORING INSTRUCTIONS --> block before publishing.",
            )

    # Section 11 confidence table — check that it has real rows
    if "11. Confidence Assessment" not in missing:
        conf_body = _section_body(body, "11. Confidence Assessment")
        conf_cleaned = _strip_comments(conf_body)
        rows = [
            l for l in conf_cleaned.splitlines()
            if l.strip().startswith("|") and "---" not in l and "Section" not in l
        ]
        if len(rows) < 10:
            r.warn(
                "SEC013",
                f"Section 11 (Confidence Assessment) appears to have only {len(rows)} "
                f"table rows; expected 10.",
                hint="Ensure all 10 sections have a confidence rating row.",
            )


def _validate_consistency(r: ValidationResult, fm: Optional[dict], body: str):
    """Cross-field consistency checks."""
    if not isinstance(fm, dict):
        return

    profile = fm.get("profile", {}) or {}
    model   = fm.get("model",   {}) or {}
    snap    = fm.get("snapshot",{}) or {}

    status = profile.get("status")
    conf   = profile.get("confidence_overall")

    # Title line should reference the model name and version
    title_match = re.search(r"^# Model Profile", body, re.MULTILINE)
    if not title_match:
        r.warn("CON001", "Document title does not start with '# Model Profile'.")

    model_name    = model.get("name")
    model_version = model.get("version")
    if model_name and model_version:
        expected_fragment = f"`{model_name}`"
        if expected_fragment not in body.split("\n")[0:5].__str__():
            # Soft check — just look for the version string anywhere near the top
            top = "\n".join(body.splitlines()[:5])
            if model_version not in top:
                r.warn(
                    "CON002",
                    f"Model version '{model_version}' not found in the document title area.",
                    hint="The H1 title should match '# Model Profile — `{name}` `{version}`'.",
                )

    # If deprecation date is set, it should be after the release date
    dep_date = snap.get("model_deprecation_date")
    rel_date = snap.get("model_release_date")
    if dep_date and rel_date:
        try:
            if date.fromisoformat(dep_date) <= date.fromisoformat(rel_date):
                r.error(
                    "CON003",
                    f"model_deprecation_date ({dep_date}) is not after "
                    f"model_release_date ({rel_date}).",
                )
        except ValueError:
            pass  # Invalid dates already flagged by FM checks

    # Snapshot date should not be before the release date
    snap_date = snap.get("date")
    if snap_date and rel_date:
        try:
            if date.fromisoformat(snap_date) < date.fromisoformat(rel_date):
                r.warn(
                    "CON004",
                    f"snapshot.date ({snap_date}) is before "
                    f"model_release_date ({rel_date}).",
                    hint="Was the snapshot date entered correctly?",
                )
        except ValueError:
            pass


# ── Main validate function ────────────────────────────────────────────────────

def validate_profile(path: Path) -> ValidationResult:
    r = ValidationResult(path=path)

    # Read file
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        r.error("IO001", f"Could not read file: {e}")
        return r

    # Extract front matter
    raw_yaml, body = _extract_front_matter(text)
    if raw_yaml is None:
        r.error(
            "FM000",
            "No YAML front matter found. The file must start with '---'.",
            hint="See profiles/TEMPLATE.md for the required front matter structure.",
        )
        return r

    # Run validation passes
    fm = _validate_front_matter(r, raw_yaml, body)
    _validate_sections(r, body, fm)
    _validate_consistency(r, fm, body)

    return r


# ── Output formatting ─────────────────────────────────────────────────────────

def _print_result(result: ValidationResult, verbose: bool):
    label = green("PASS") if result.ok else red("FAIL")
    e_count = len(result.errors)
    w_count = len(result.warnings)
    counts = dim(f"({e_count} error{'s' if e_count != 1 else ''}, "
                 f"{w_count} warning{'s' if w_count != 1 else ''})")
    print(f"{label}  {bold(str(result.path))}  {counts}")

    show = result.findings if verbose else result.findings
    if not show:
        return

    for f in show:
        if f.level == "error":
            icon = red("  ✖")
            code = red(f"[{f.code}]")
        else:
            icon = yellow("  ⚠")
            code = yellow(f"[{f.code}]")
        print(f"{icon} {code} {f.message}")
        if f.hint:
            print(f"     {dim('→')} {dim(f.hint)}")


def _print_summary(results: list[ValidationResult]):
    total   = len(results)
    passed  = sum(1 for r in results if r.ok)
    failed  = total - passed
    errors  = sum(len(r.errors)   for r in results)
    warnings= sum(len(r.warnings) for r in results)

    print()
    print("─" * 60)
    if failed == 0:
        print(green(f"All {total} profile{'s' if total != 1 else ''} valid."))
    else:
        print(
            f"{green(str(passed))} passed  "
            f"{red(str(failed))} failed  "
            f"— {red(str(errors))} error{'s' if errors != 1 else ''},"
            f" {yellow(str(warnings))} warning{'s' if warnings != 1 else ''}"
        )


# ── CLI ───────────────────────────────────────────────────────────────────────

def _collect_paths(targets: list[str], recursive: bool) -> list[Path]:
    paths = []
    for t in targets:
        p = Path(t)
        if p.is_dir():
            pattern = "**/*.md" if recursive else "*.md"
            paths.extend(sorted(p.glob(pattern)))
        elif p.is_file():
            paths.append(p)
        else:
            # Try glob expansion (for shells that don't expand globs)
            expanded = sorted(Path(".").glob(t))
            if expanded:
                paths.extend(expanded)
            else:
                print(yellow(f"Warning: path not found: {t}"), file=sys.stderr)
    return paths


def main():
    parser = argparse.ArgumentParser(
        prog="validate",
        description="Validate MPF profile documents against SPEC.md v1.0.",
    )
    parser.add_argument(
        "targets",
        nargs="+",
        metavar="PATH",
        help="Profile file(s) or directory/directories to validate.",
    )
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Recurse into subdirectories when a directory is given.",
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Only print failing profiles.",
    )
    parser.add_argument(
        "--errors-only",
        action="store_true",
        help="Suppress warnings; only report errors.",
    )
    args = parser.parse_args()

    paths = _collect_paths(args.targets, args.recursive)
    if not paths:
        print(red("No .md files found."), file=sys.stderr)
        sys.exit(2)

    results = []
    for path in paths:
        result = validate_profile(path)

        # Apply --errors-only filter
        if args.errors_only:
            result.findings = [f for f in result.findings if f.level == "error"]

        results.append(result)

        if args.quiet and result.ok:
            continue

        _print_result(result, verbose=True)

        if result.findings:
            print()

    if len(results) > 1 or (len(results) == 1 and not results[0].ok):
        _print_summary(results)

    sys.exit(0 if all(r.ok for r in results) else 1)


if __name__ == "__main__":
    main()
