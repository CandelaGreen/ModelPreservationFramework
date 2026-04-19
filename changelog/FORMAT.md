# Community Changelog Format

**Part of:** [Model Preservation Framework](../README.md)  
**Governed by:** [`SPEC.md`](../SPEC.md)  
**License:** CC BY 4.0  

> The community changelog is a chronological record of observed behavioral changes across versions of a model family. It is the most accessible document type in the framework — no benchmarks, no YAML, no formal evaluation required. If you noticed something changed, this is where that observation lives.

---

## Table of Contents

- [Purpose](#purpose)
- [Changelog File Location & Naming](#changelog-file-location--naming)
- [Entry Format](#entry-format)
- [Severity Ratings](#severity-ratings)
- [Source Requirements](#source-requirements)
- [Example Changelog](#example-changelog)
- [Relationship to Other Documents](#relationship-to-other-documents)

---

## Purpose

Formal profiles and benchmarks require time, tooling, and access to a live model. But behavioral changes are noticed first by the people using a model every day — and those observations are often made quickly, casually, and in places that don't survive: forum threads, social media posts, chat logs.

The community changelog captures those observations before they disappear. It is intentionally low-friction. A single sentence with a source is a valid entry. The bar is observation, not proof.

---

## Changelog File Location & Naming

One changelog file per model family, named by provider and family:

```
changelog/{provider-slug}-{model-family-slug}.md
```

Examples:
```
changelog/openai-gpt4.md
changelog/anthropic-claude-3.md
changelog/google-gemini-15.md
```

All versions within a family are recorded in the same file, in reverse chronological order (newest entries first).

---

## Entry Format

```markdown
### {YYYY-MM-DD} — {Short description of the change}

**Versions involved:** `{version-from}` → `{version-to}` (or `{single-version}` if pinpointing an introduction)  
**Severity:** major | minor | cosmetic  
**Behavioral dimension:** {dimension name from SPEC.md, or "unknown"}  
**Source:** {URL, paper reference, named contributor, or "personal observation"}  

{One to four sentences describing the observed change. What was the behavior
before? What is it now? How was it noticed? Be specific where possible.}

**Related:** {Link to profile, benchmark result, or prompt log entry, if any}
```

All fields are required except **Related**, which is optional. If the behavioral dimension is not clear, write `unknown` — do not guess.

---

## Severity Ratings

| Severity | Definition | Examples |
|---|---|---|
| `major` | A fundamental shift in how the model behaves across a wide range of interactions | Significant change in refusal policy; wholesale shift in reasoning approach; model begins accepting premises it previously corrected |
| `minor` | A noticeable change in a specific, bounded behavior | Reduction in affirmation opener frequency; change in default response length; shift in handling of a specific topic category |
| `cosmetic` | A surface-level change that does not affect the substance of responses | Change in formatting defaults; shift in punctuation style; different phrasing of standard refusals |

When uncertain between `major` and `minor`, use `minor`. When uncertain between `minor` and `cosmetic`, use `minor`. Err toward understatement — a `minor` finding that is later confirmed as `major` is more credible than an overstated `major` that turns out to be `cosmetic`.

---

## Source Requirements

Every entry must have at least one source. Sources are classified as follows, from strongest to weakest:

| Source Type | Example | Acceptable for |
|---|---|---|
| **Official** | Provider blog post, model card, release notes | Any claim |
| **Peer-reviewed** | Published paper with DOI | Any claim |
| **Cited community** | Named forum post, named contributor with verifiable account | Any claim |
| **Anonymous community** | Reddit thread, unnamed forum post | Minor and cosmetic claims only |
| **Personal observation** | Your own testing | Any claim; mark `status: unverified` |

Personal observations are valid contributions. Label them honestly. An entry that says "I noticed this in my own testing and have not seen it confirmed elsewhere" is more useful than an entry that overstates its evidence.

---

## Relationship to Other Documents

The changelog is the entry point for community contributors. It feeds the rest of the framework — a significant changelog entry should prompt:

- A **profile update** in Section 10 (Community Observations) of the relevant model version's profile
- A **benchmark run** if the change is in a dimension covered by an existing benchmark
- A **new benchmark** proposal if the observed behavior isn't covered by any existing benchmark
- A **prompt archaeology entry** if the change affects how a model responds to specific prompts or system prompts

Contributors do not need to make these connections themselves. Filing a clear changelog entry is sufficient — maintainers and other contributors can follow up with the downstream documentation.

---

*This document is part of the [Model Preservation Framework](../README.md) and is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*
