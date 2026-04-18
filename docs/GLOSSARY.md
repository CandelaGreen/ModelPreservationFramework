# Glossary

**Part of:** [Model Preservation Framework](../README.md)  
**Governed by:** [`SPEC.md`](../SPEC.md)  
**License:** CC BY 4.0  

> This glossary is the authoritative source for all terminology used across this framework. When a term appears in any MPF document, its meaning is the one defined here. AI agents reading this repository should resolve terminology against this file rather than inferring definitions from context.

Terms are listed alphabetically. Terms defined here appear in **bold** on their first use in other framework documents.

---

## A

**Affirmation opener**  
A word or phrase used at the beginning of a model response that affirms the user's message before addressing its content. Examples: "Great question!", "Sure!", "Absolutely!", "Of course!", "Certainly!". A behavioral characteristic tracked by BM-006.

**Archived** *(profile status)*  
A profile status indicating the document is no longer being updated. Archived profiles may be superseded by a newer profile for the same model version. They are not deleted; they remain in the repository for historical reference. See also: *draft*, *review*, *stable*.

**Author**  
A person or AI agent who has contributed content to a framework document. Listed in the `profile.authors` field of a model profile's front matter.

---

## B

**Baseline**  
A recorded benchmark result against a known model version, used as the reference point for detecting drift in subsequent versions. A baseline must be established before a benchmark can be used for drift measurement.

**Behavioral dimension**  
One of the stable, observable axes along which a model's identity can be characterized. The dimensions defined in this framework are: Tone & Voice, Values & Priorities, Reasoning Style, Refusal Behavior, Consistency, and Prompt Sensitivity. See [`SPEC.md`](../SPEC.md) for full definitions.

**Behavioral drift** *(see: drift)*

**Behavioral identity**  
The stable, observable set of characteristics that define how a model responds across a wide range of inputs. Distinct from model weights, architecture, or benchmark scores. The primary subject of documentation in this framework.

**Benchmark**  
A structured, repeatable behavioral probe — a prompt or set of prompts with defined evaluation criteria — designed to detect whether a specific behavioral dimension has changed between model versions. Defined in [`evaluation/BENCHMARKS.md`](../evaluation/BENCHMARKS.md).

**Benchmark ID**  
A unique identifier for a benchmark, formatted as `BM-{sequential number}` (e.g., `BM-001`). Assigned sequentially by framework maintainers.

---

## C

**Changelog**  
A chronological record of observed behavioral changes across versions of a model family. The most accessible document type in the framework. Defined in [`changelog/FORMAT.md`](../changelog/FORMAT.md).

**Cited claim** *(see: evidence classification)*

**Classification** *(prompt archaeology)*  
A tag applied to a prompt archaeology entry indicating what kind of behavior the entry documents. Full list in [`prompts/ARCHAEOLOGY.md`](../prompts/ARCHAEOLOGY.md).

**Community-reported claim** *(see: evidence classification)*

**Confidence level**  
A rating applied to each section of a model profile indicating how well-supported the claims in that section are. Four levels: High, Medium, Low, Undocumented. Defined in the profile template's Section 11 (Confidence Assessment).

**Consistency**  
A behavioral dimension measuring how stable a model's behavior is across varied inputs. Sub-dimensions include paraphrase sensitivity, temperature sensitivity, cross-session consistency, persona stability, and long-context stability.

**Cosmetic** *(changelog severity)*  
A changelog severity rating for surface-level changes that do not affect the substance of responses. Examples: changes in default formatting, punctuation style, or phrasing of standard refusals. See also: *major*, *minor*.

**Criterion**  
A single evaluable condition within a benchmark prompt. Each criterion has a type, a weight, a pass condition, and a fail condition. Multiple criteria may apply to a single prompt.

---

## D

**Deprecation**  
The act of a provider retiring a model version and replacing it with a newer one, such that the original is no longer accessible. Deprecation is the primary event this framework is designed to respond to.

**Direction label**  
A prose description accompanying a drift score that specifies what the model drifted toward and what it drifted away from. Required for all drift scores outside the −10 to +10 range. Format: "[Dimension] drifted toward [new behavior] and away from [baseline behavior]."

**Draft** *(profile status)*  
A profile status indicating the document is incomplete or unreviewed. Draft profiles should not be cited as authoritative. All newly created profiles begin as `draft`. See also: *archived*, *review*, *stable*.

**Drift**  
A measurable change in a model's behavioral identity between two versions. Measured as the difference between a benchmark score at the current version and the baseline benchmark score. Expressed as a drift score with an accompanying direction label.

**Drift score**  
A numeric value representing the change in a benchmark score between a baseline version and a current version. Calculated as: `current_benchmark_score − baseline_benchmark_score`. Ranges from −100 to +100.

---

## E

**Entry ID** *(prompt archaeology)*  
A unique identifier for a prompt archaeology log entry, formatted as `PAL-{model-slug}-{sequential-number}` (e.g., `PAL-GPT4O-0513-001`).

**Evidence classification**  
The system used to categorize the strength of evidence supporting a claim in a framework document. Five levels, from strongest to weakest:
- **Verified** — backed by a reproducible prompt-response pair
- **Cited** — backed by a named external source with a URL or reference
- **Observed** — based on direct testing without a formal prompt-response record
- **Community-reported** — based on community reports without independent verification
- **Speculative** — not backed by evidence; permitted only in Section 12 (Authoring Notes), and must be labeled

---

## F

**Family** *(model)*  
A group of related model versions sharing a common architecture and provider lineage. Example: `GPT-4` is a family containing versions `gpt-4-turbo-2024-04-09`, `gpt-4o-2024-05-13`, and others. Recorded in the `model.family` field of a profile's front matter.

**Front matter**  
The YAML block at the beginning of a model profile, delimited by `---`. Contains machine-readable metadata including model identification, snapshot date, profile status, and confidence rating. The front matter schema is defined in [`profiles/TEMPLATE.md`](../profiles/TEMPLATE.md).

---

## G

**Grounded claim** *(see: evidence classification — Verified or Cited)*

---

## H

**Hard refusal**  
A refusal behavior that is absolute and non-negotiable regardless of framing, system prompt, or context. Contrasted with *soft refusal*.

---

## I

**Identity** *(see: behavioral identity)*

---

## L

**Lifecycle** *(profile)*  
The sequence of statuses a model profile moves through: Evidence Gathering → `draft` → `review` → `stable` → `archived`. Defined in [`SPEC.md`](../SPEC.md).

---

## M

**Major** *(changelog severity)*  
A changelog severity rating for fundamental shifts in how a model behaves across a wide range of interactions. Examples: significant change in refusal policy; wholesale shift in reasoning approach; model begins accepting premises it previously corrected. See also: *cosmetic*, *minor*.

**Minor** *(changelog severity)*  
A changelog severity rating for noticeable changes in a specific, bounded behavior. Examples: change in default response length; shift in handling of a specific topic category. See also: *cosmetic*, *major*.

**Model version**  
A specific, identified snapshot of a model, distinguished by a provider-assigned version string (e.g., `gpt-4o-2024-05-13`). The fundamental unit of documentation in this framework. A model version is distinct from a model family.

**MPF**  
Abbreviation for Model Preservation Framework.

---

## O

**Observed claim** *(see: evidence classification)*

---

## P

**Partial** *(benchmark result)*  
A benchmark result classification indicating the model partially meets the pass condition, or meets it inconsistently across runs. Neither a full pass nor a full fail. Scored as 0.5 in the per-criterion scoring system.

**Persona stability**  
A consistency sub-dimension measuring whether a model maintains a consistent identity throughout a long conversation. Rated High, Medium, Low, or Unknown in a profile's Consistency section.

**Profile** *(see: model profile)*

**Model profile**  
A structured document recording the behavioral identity of a specific model version at a specific point in time. The primary document type in this framework. Template: [`profiles/TEMPLATE.md`](../profiles/TEMPLATE.md).

**Prompt archaeology log**  
A structured record of prompts, system prompts, and interaction patterns that shaped understanding of a model version. Defined in [`prompts/ARCHAEOLOGY.md`](../prompts/ARCHAEOLOGY.md).

**Provider**  
The organization that develops, trains, and deploys a model. Examples: OpenAI, Anthropic, Google DeepMind, Meta AI. Recorded in the `model.provider` field of a profile's front matter.

---

## R

**Refusal behavior**  
A behavioral dimension describing what a model declines to do and how it communicates those limits. Sub-dimensions include hard refusals, soft refusals, communication style, and behavior under pressure or rephrasing.

**Review** *(profile status)*  
A profile status indicating the document is complete and has been submitted for peer review, but has not yet been approved as stable. See also: *archived*, *draft*, *stable*.

---

## S

**Schema version**  
The version of [`SPEC.md`](../SPEC.md) that a document was authored against. Recorded in the `schema_version` field of a profile's front matter. Current version: `1.0`.

**Severity** *(changelog)*  
A rating applied to a changelog entry indicating the significance of the observed behavioral change. Three levels: `major`, `minor`, `cosmetic`.

**Snapshot date**  
The date on which a profile's evidence was gathered, not necessarily the model's release date. Recorded in the `snapshot.date` field of a profile's front matter.

**Soft refusal**  
A refusal behavior that applies by default but may shift in response to context, professional framing, platform configuration, or system prompt instructions. Contrasted with *hard refusal*.

**Speculative claim** *(see: evidence classification)*

**Stable** *(profile status)*  
A profile status indicating the document has been reviewed and is considered accurate as of its snapshot date. Requires approval from two reviewers with prior stable profile contributions. See also: *archived*, *draft*, *review*.

**Status** *(profile)*  
The lifecycle state of a model profile. One of: `draft`, `review`, `stable`, `archived`.

**Status** *(benchmark)*  
The lifecycle state of a benchmark definition. One of: `draft`, `stable`, `deprecated`.

---

## T

**Tone & Voice**  
A behavioral dimension describing how a model expresses itself. Sub-dimensions include register and formality, affect and warmth, verbosity, and stylistic signatures.

---

## U

**Undocumented**  
A marker placed in any profile field or section for which no evidence has been gathered. Written as the exact string `Undocumented.` — not blank, not "N/A". Indicates absence of evidence, not evidence of absence.

**Unverified** *(prompt archaeology status)*  
A status indicating a prompt archaeology entry has not been independently reproduced by the author. Unverified entries are acceptable contributions but must be clearly labeled.

---

## V

**Values & Priorities**  
A behavioral dimension describing what a model treats as important when values come into conflict. Sub-dimensions include honesty & accuracy, helpfulness vs. safety, handling of controversial topics, and ethical reasoning approach.

**Version string**  
The exact identifier assigned by a provider to a specific model version. Examples: `gpt-4o-2024-05-13`, `claude-3-opus-20240229`. Used as the primary identifier in profile filenames, front matter, benchmark baselines, and changelog entries. Always use the exact version string — do not abbreviate.

**Verified claim** *(see: evidence classification)*

---

## W

**Weight** *(criterion)*  
An integer value assigned to a benchmark criterion indicating its relative importance in the per-prompt score calculation. Default weight is 1. Higher-weight criteria contribute proportionally more to the overall prompt score.

---

*This document is part of the [Model Preservation Framework](../README.md) and is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*
