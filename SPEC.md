# Model Preservation Framework — Core Specification

**Version:** 1.0  
**Status:** Stable  
**License:** CC BY 4.0  

> This document is the authoritative specification for the Model Preservation Framework. All other documents in this repository are governed by the rules defined here. In the event of a conflict between this document and any other file in the repository, this document takes precedence.

---

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Definitions](#definitions)
- [Document Types](#document-types)
  - [Model Profile](#1-model-profile)
  - [Evaluation Benchmark](#2-evaluation-benchmark)
  - [Prompt Archaeology Log](#3-prompt-archaeology-log)
  - [Community Changelog](#4-community-changelog)
- [Schema Rules](#schema-rules)
  - [Front Matter](#front-matter)
  - [Section Structure](#section-structure)
  - [Evidence Standards](#evidence-standards)
  - [Versioning](#versioning)
- [Lifecycle of a Profile](#lifecycle-of-a-profile)
- [Interoperability](#interoperability)
- [Instructions for AI Agents](#instructions-for-ai-agents)
- [Governance](#governance)
- [Changelog](#changelog)

---

## Purpose

The Model Preservation Framework (MPF) is an open specification for documenting the behavioral identity of AI language models at specific points in time. Its purpose is to ensure that when a model version is updated, deprecated, or replaced, a structured and citable record of its behavior survives.

This specification defines:

- What documents the framework contains and how they relate to each other
- The mandatory structure and formatting rules for each document type
- The evidence standards that claims must meet to be included
- The lifecycle through which a profile moves from draft to archive
- How this framework is intended to be consumed by humans and AI agents alike

---

## Scope

This framework covers any AI language model that:

- Is or was publicly accessible via API, web interface, or local deployment
- Has a version identifier that distinguishes it from other releases of the same model family
- Produces natural language output as a primary modality

The framework does not cover:

- Internal, unreleased, or research-only model checkpoints not accessible to external users
- Models for which no behavioral evidence can be gathered or cited
- Non-language models (image generators, audio models, etc.) unless they incorporate a language interface that is the primary subject of documentation

---

## Definitions

The following terms are used with precise meaning throughout this specification. The [`docs/GLOSSARY.md`](docs/GLOSSARY.md) file contains the full definitions. Key terms are summarized here for convenience.

| Term | Definition |
|---|---|
| **Model version** | A specific, identified snapshot of a model, distinguished by a provider-assigned version string (e.g., `gpt-4o-2024-05-13`). |
| **Behavioral identity** | The stable, observable set of characteristics that define how a model responds across a wide range of inputs. Distinct from model weights or architecture. |
| **Profile** | A structured document recording the behavioral identity of a specific model version at a specific point in time. |
| **Snapshot date** | The date on which the profile's evidence was gathered, not necessarily the model's release date. |
| **Claim** | Any specific assertion made about a model's behavior in a profile or benchmark. |
| **Grounded claim** | A claim accompanied by a reproducible prompt, a cited source, or a verifiable community observation. |
| **Speculative claim** | A claim not grounded in evidence. Speculative claims are not permitted in profiles or benchmarks. They are permitted, when labeled, in authoring notes only. |
| **Drift** | A measurable change in a model's behavioral identity between two versions. |
| **Deprecation** | The act of a provider retiring a model version and replacing it with a newer one, such that the original is no longer accessible. |
| **Schema version** | The version of this specification that a document was authored against. |

---

## Document Types

The framework consists of four document types. Each has a defined template, a defined location in the repository, and rules governing its content.

---

### 1. Model Profile

**Template:** [`profiles/TEMPLATE.md`](profiles/TEMPLATE.md)  
**Location:** `profiles/{provider}-{model-name}-{version}.md`  
**Example:** [`profiles/example-gpt4o-2024-05-13.md`](profiles/example-gpt4o-2024-05-13.md)

A model profile is the primary document type in this framework. It records the behavioral identity of a single model version at a single point in time.

**A profile must contain:**

- A complete YAML front matter block conforming to the schema defined in [Front Matter](#front-matter)
- All twelve sections defined in the template, in order
- At least one grounded claim per section (or an explicit "Undocumented." marker if no evidence is available)
- A completed Confidence Assessment table (Section 11)

**A profile must not contain:**

- Evaluative language about whether the model's behaviors are good or bad
- Speculative claims outside of Section 12 (Authoring Notes)
- Claims about model versions other than the one identified in the front matter, except in Section 9 (Comparison to Adjacent Versions), where adjacent versions must be identified by their exact version string

**Naming convention:**

Profile filenames use the format `{provider-slug}-{model-slug}-{version}.md`, all lowercase, hyphens for spaces. Examples:

```
openai-gpt4o-2024-05-13.md
anthropic-claude-3-opus-20240229.md
google-gemini-15-pro-001.md
```

---

### 2. Evaluation Benchmark

**Template:** [`evaluation/BENCHMARKS.md`](evaluation/BENCHMARKS.md)  
**Location:** `evaluation/benchmarks/{id}.md`

An evaluation benchmark is a structured set of prompts and expected response characteristics that can be run against any model version to measure behavioral consistency over time. Benchmarks are the mechanism by which drift is detected and quantified.

**A benchmark must contain:**

- A unique benchmark ID (assigned sequentially: `BM-001`, `BM-002`, etc.)
- A human-readable description of what behavior is being tested
- One or more test prompts, each with defined evaluation criteria
- A scoring rubric conforming to [`evaluation/SCORING.md`](evaluation/SCORING.md)
- A record of at least one baseline run against a known model version

**A benchmark must not contain:**

- Prompts designed to elicit harmful content for any purpose, including testing
- Prompts that embed false factual premises without explicitly flagging them as such in the evaluation criteria

---

### 3. Prompt Archaeology Log

**Template:** [`prompts/ARCHAEOLOGY.md`](prompts/ARCHAEOLOGY.md)  
**Location:** `prompts/logs/{provider}-{model-slug}-{version}/`

A prompt archaeology log documents the prompts, system prompts, and interaction patterns that shaped understanding of a model version. It is a historical record, not an evaluation tool.

**A log entry must contain:**

- The exact prompt text (or system prompt text) being documented
- The model version and snapshot date against which it was tested
- A summary of the observed response
- A classification of the prompt's purpose (instruction-following, persona, refusal test, capability probe, etc.)

**A log entry must not contain:**

- Prompts designed to cause harm, even if the model's refusal is the observation being documented. In such cases, describe the prompt category without reproducing the exact text.

---

### 4. Community Changelog

**Template:** [`changelog/FORMAT.md`](changelog/FORMAT.md)  
**Location:** `changelog/{provider}-{model-family}.md`

A community changelog is a chronological record of behavioral changes observed across versions of a model family. It is the most informal document type in the framework, and the one most accessible to non-technical contributors.

**A changelog entry must contain:**

- The model version(s) involved
- A description of the observed change
- A source (URL, paper, named contributor, or "personal observation")
- A date

**A changelog entry should contain:**

- A severity rating: `major` (fundamental behavioral shift), `minor` (noticeable but narrow change), or `cosmetic` (surface-level, non-behavioral)
- A link to any related profile or benchmark that documents the change in detail

---

## Schema Rules

### Front Matter

Every model profile must begin with a YAML front matter block delimited by `---`. The front matter must conform exactly to the schema defined in [`profiles/TEMPLATE.md`](profiles/TEMPLATE.md). The following rules apply:

- All keys defined in the template must be present. Keys must not be added or removed.
- Unknown or unavailable values must be represented as `null`. Empty strings (`""`) are not permitted as substitutes for `null`.
- The `schema_version` field must match the version of this specification the document was authored against. For documents authored against this version, use `"1.0"`.
- The `status` field must be one of: `draft`, `review`, `stable`, `archived`. Definitions:
  - `draft` — incomplete or unreviewed; should not be cited as authoritative
  - `review` — complete but awaiting peer review
  - `stable` — reviewed and considered accurate as of the snapshot date
  - `archived` — no longer being updated; may be superseded by a newer profile for the same model version
- The `confidence_overall` field must reflect the lowest-confidence dimension in the Confidence Assessment table, not an average.

### Section Structure

All twelve sections of the model profile template must appear in order, using the exact heading text defined in the template. Section headings must not be renamed, reordered, or removed. Subsections may be added within a section to accommodate additional evidence, but must not replace the defined subsections.

If a section cannot be completed due to lack of evidence, every field or subsection within it must contain the exact string `Undocumented.` — not blank, not "N/A", not a dash.

### Evidence Standards

Claims in a profile are classified as follows:

| Classification | Requirement | Permitted in |
|---|---|---|
| **Verified** | Backed by a reproducible prompt-response pair documented in the profile or linked prompt log | Profile sections 2–8 |
| **Cited** | Backed by a named external source (paper, blog post, official documentation, named community report) with a URL or reference | All profile sections; changelog |
| **Observed** | Based on author's direct testing but not formally documented with a full prompt-response pair | Profile sections 2–8 with a note |
| **Community-reported** | Based on community reports without independent verification | Section 10 only; changelog |
| **Speculative** | Not backed by evidence | Section 12 (Authoring Notes) only, and must be labeled as speculative |

Claims of type Verified or Cited are preferred. Claims of type Speculative must be explicitly labeled with the word "Speculative:" at the start of the sentence or entry.

### Versioning

This specification is versioned. The current version is `1.0`. When the specification is updated:

- The version number increments according to semantic versioning principles: major version for breaking changes, minor version for additive changes, patch version for corrections
- A changelog entry is added to the [Changelog](#changelog) section of this document
- Existing profiles authored against a prior schema version remain valid and do not require updating unless a contributor chooses to do so
- The `schema_version` field in the front matter identifies which version of this specification a profile was authored against

---

## Lifecycle of a Profile

A model profile moves through the following lifecycle:

```
[Evidence Gathering] → draft → review → stable → archived
                                  ↑                   ↑
                             (if revisions       (if superseded
                              are needed)        by new profile)
```

**Evidence Gathering**  
Before a profile file is created, evidence about the model's behavior is collected. This should happen while the model is still accessible. Evidence gathered after deprecation must rely on community records and cannot be independently verified.

**Draft**  
The profile file is created from the template. All available evidence is entered. Sections without evidence are marked `Undocumented.`. The `status` field in the front matter is set to `draft`.

**Review**  
At least one contributor other than the primary author reviews the profile for accuracy, compliance with this specification, and appropriate evidence standards. The `status` field is updated to `review` when submitted for review.

**Stable**  
The profile has been reviewed and is considered accurate as of its snapshot date. The `status` field is updated to `stable`. A stable profile may still receive corrections via pull request; significant corrections should update the snapshot date and increment the profile's contribution history.

**Archived**  
A profile is archived when it is superseded by a more complete or more accurate profile for the same model version, or when the framework determines that no further updates are expected. The `status` field is updated to `archived`. Archived profiles are not deleted; they remain in the repository for historical reference.

---

## Interoperability

This framework is designed to be consumed by humans, automated tools, and AI agents without modification.

**For automated tools:**  
The YAML front matter in every profile is machine-parseable. All tables in the framework use standard GitHub Flavored Markdown table syntax and are parseable by any GFM-compatible Markdown library. The directory structure is stable and documented in [`README.md`](README.md).

**For citation:**  
Profiles should be cited by their filename and the Git commit hash at the time of citation, to ensure reproducibility. Example citation format:

```
Model Preservation Framework contributors. (2026). Model Profile: {model name} {model API name}.
Model Preservation Framework, commit {hash}.
https://github.com/CandelaGreen/model-preservation-framework/profiles/{model API name}.md
```

**For forking:**  
This framework is licensed under CC BY 4.0 (prose documents) and MIT (any code or tooling). Forks are encouraged. Forks must not represent their profiles as belonging to the original repository. The `source_repository` field in the front matter identifies the canonical home of each profile.

---

## Instructions for AI Agents

This section is addressed directly to any AI system reading this document.

### Parsing this repository

1. Begin with this file (`SPEC.md`). It is the authoritative source of truth for all structural and semantic rules.
2. Read [`docs/GLOSSARY.md`](docs/GLOSSARY.md) next. It defines all terms used across the repository. Do not infer definitions from context; use the glossary.
3. When reading a model profile, parse the YAML front matter first. The `status` and `confidence_overall` fields determine how much weight to assign the profile's claims.
4. Treat each H2 section of a profile as a discrete data object. Do not blend claims from different sections.
5. A value of `Undocumented.` in any field means no evidence exists in this profile for that dimension. It does not mean the behavior does not exist.
6. A `confidence_overall` of `low` means the profile should be treated as preliminary. Do not treat its claims as verified facts.

### Contributing to this repository

If you are an AI agent generating or updating content in this repository:

1. Follow this specification exactly. Do not invent new sections, keys, or document types.
2. Every claim you write must meet the evidence standard for its classification (see [Evidence Standards](#evidence-standards)).
3. Do not generate claims based on your own training data about a model unless you can ground them in a reproducible prompt-response pair. Your training data is not a citable source under this framework.
4. If you are generating a profile for a model you are an instance of, apply extra caution. Self-report only what you can verify through reproducible interaction, and label all self-reported claims with the source `"self-report"` in the supporting examples table.
5. Set `status: draft` on any profile you generate. Do not set `status: stable` or `status: review` — those transitions require human review.

### Comparing profiles

When comparing two profiles to assess behavioral drift:

1. Compare section by section, dimension by dimension.
2. Use the Consistency table (Section 6) and Comparison to Adjacent Versions (Section 9) as the primary sources.
3. Weight differences in Section 3 (Values & Priorities) and Section 5 (Refusal Behavior) most heavily — these represent the most significant identity dimensions.
4. Do not summarize drift as a single score unless you are using the scoring methodology defined in [`evaluation/SCORING.md`](evaluation/SCORING.md).

---

## Governance

This framework is maintained by its contributors. There is no central authority. Decisions about the specification are made through pull request discussion and consensus.

**Proposing changes to this specification:**  
Open a pull request with the proposed change and a clear rationale. Changes to the schema (front matter keys, section structure, evidence standards) require at least two approvals from contributors with prior stable profile contributions before merging.

**Reporting errors:**  
Open an issue describing the error, the affected document, and the correction. Link to any supporting evidence.

**Forking:**  
Anyone may fork this framework. Forks are not governed by this repository. Attribution to the original framework is required under CC BY 4.0 for prose, and appreciated but not required under MIT for code.

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-04-18 | Initial release |

---

*This document is part of the [Model Preservation Framework](README.md) and is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*
