# MPF Tools

Command-line tooling for the [Model Preservation Framework](../README.md).

All code in this directory is released under the **MIT License**.

---

## validate.py

Validates MPF profile documents against the schema and structural rules defined in [`SPEC.md`](../SPEC.md) v1.0.

### Requirements

Python 3.11+ and PyYAML:

```bash
pip install -r requirements.txt
```

### Usage

```bash
# Validate a single profile
python tools/validate.py profiles/openai-gpt4o-2024-05-13.md

# Validate all profiles in a directory
python tools/validate.py profiles/

# Validate recursively
python tools/validate.py profiles/ --recursive

# Suppress warnings, show errors only (useful in CI)
python tools/validate.py profiles/ --errors-only

# Suppress passing profiles (only show failures)
python tools/validate.py profiles/ --quiet
```

### Exit codes

| Code | Meaning |
|---|---|
| `0` | All profiles passed (errors only; warnings do not affect exit code) |
| `1` | One or more profiles have errors |
| `2` | Usage error (no files found, missing dependency) |

### Error codes

| Code | Category | Description |
|---|---|---|
| `FM000` | Front matter | No YAML front matter found |
| `FM001` | Front matter | YAML parse error |
| `FM002` | Front matter | Front matter is not a mapping |
| `FM003` | Front matter | Missing required top-level key |
| `FM004` | Front matter | schema_version mismatch |
| `FM010–FM018` | Front matter | model block errors |
| `FM020–FM027` | Front matter | snapshot block errors |
| `FM030–FM044` | Front matter | profile block errors |
| `FM050–FM051` | Front matter | tags errors |
| `SEC001` | Sections | Required section missing |
| `SEC002` | Sections | Sections out of order |
| `SEC003` | Sections | Unexpected heading before section 1 |
| `SEC010` | Sections | Section is completely empty |
| `SEC011` | Sections | Too many undocumented sections for non-draft status |
| `SEC012` | Sections | Authoring instructions block still present |
| `SEC013` | Sections | Confidence Assessment table incomplete |
| `CON001–CON004` | Consistency | Cross-field consistency errors |

Warnings use the same codes but do not affect the exit code.

### CI integration

A GitHub Actions workflow is included at `.github/workflows/validate.yml`. It runs automatically on any push or pull request that touches files in `profiles/`. On pull requests, it also runs the full validator (including warnings) on only the changed profile files, making review easier.
