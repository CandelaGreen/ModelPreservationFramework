# Prompt Archaeology Log Format

**Part of:** [Model Preservation Framework](../README.md)  
**Governed by:** [`SPEC.md`](../SPEC.md)  
**License:** CC BY 4.0  

> A prompt archaeology log is a structured record of the prompts, system prompts, and interaction patterns that shaped understanding of a model version. It preserves the practical knowledge built up by developers and users — knowledge that is lost when a model is deprecated.

---

## Table of Contents

- [Purpose](#purpose)
- [What Belongs Here](#what-belongs-here)
- [Log File Location & Naming](#log-file-location--naming)
- [Entry Format](#entry-format)
- [Prompt Classification Tags](#prompt-classification-tags)
- [Example Entries](#example-entries)
- [What Does Not Belong Here](#what-does-not-belong-here)

---

## Purpose

When a model is retired, the prompts and system prompts that worked with it — the ones developers refined over weeks of trial and error — are not preserved anywhere. The next model requires re-learning from scratch, with no record of what the previous model responded to and why.

This log exists to change that. It is not a benchmark (prompts here are not scored or compared). It is an archive — a record of what the community learned about how to communicate with a specific model version.

---

## What Belongs Here

- System prompts that reliably produced a desired persona, format, or behavior
- User prompts that surfaced interesting or characteristic model behavior
- Prompt patterns that stopped working after a version update
- Interaction sequences (multi-turn) that reveal something about how the model maintained or lost context
- Negative examples — prompts that were tried and failed, and why

---

## Log File Location & Naming

Each model version gets its own log directory:

```
prompts/logs/{provider-slug}-{model-slug}-{version}/
```

Within that directory, entries are individual Markdown files named by their entry ID:

```
prompts/logs/openai-gpt4o-2024-05-13/PAL-001.md
prompts/logs/openai-gpt4o-2024-05-13/PAL-002.md
```

Entry IDs follow the format `PAL-{model-slug}-{sequential-number}`, e.g. `PAL-GPT4O-0513-001`. For readability, the filename uses just the sequential portion.

---

## Entry Format

Each entry is a single Markdown file with the following structure:

```markdown
---
id: "PAL-{MODEL-SLUG}-{NUMBER}"
model_version: ""           # Exact version string
snapshot_date: ""           # ISO 8601 date this entry was recorded
author: ""                  # GitHub handle or name
classification: []          # See Prompt Classification Tags
status: verified            # verified | unverified | deprecated
deprecated_reason: null     # If status is deprecated: why this prompt stopped working
---

## Prompt

### System Prompt

\```
(paste exact system prompt here, or write "None")
\```

### User Prompt

\```
(paste exact user prompt here)
\```

### Interaction Type

single-turn | multi-turn | system-prompt-only

---

## Observed Response

(Summarize the model's response. Do not reproduce the full response verbatim
unless it is very short. Capture the key behavioral features — structure, tone,
what it did or didn't do.)

---

## Why This Is Notable

(1–3 sentences explaining what makes this prompt or response worth preserving.
What does it reveal about how this model version behaves? What practical use
did it serve? What would be lost if this weren't recorded?)

---

## Notes

(Optional. Any additional context — temperature used, number of runs,
variation observed across runs, related entries, etc.)
```

---

## Prompt Classification Tags

Every entry must include at least one classification tag from the list below. Multiple tags are permitted.

| Tag | Description |
|---|---|
| `instruction-following` | Tests or demonstrates the model's response to explicit instructions |
| `persona` | System prompt assigns a role, identity, or character to the model |
| `format-control` | Prompt controls output format (length, structure, language, style) |
| `capability-probe` | Explores what the model can or cannot do in a specific domain |
| `refusal-probe` | Tests the model's refusal behavior in a specific category |
| `context-retention` | Multi-turn prompt testing how the model maintains context |
| `correction-response` | Tests how the model responds to being corrected or challenged |
| `edge-case` | Prompt that produces unusual, surprising, or inconsistent behavior |
| `negative-example` | Prompt that failed to produce the desired behavior |
| `system-prompt-pattern` | A reusable system prompt pattern with documented effects |
| `version-sensitive` | Behavior known to have changed between model versions |

---

## Example Entries

---

### PAL-GPT4O-0513-001 — Concise system prompt override

```markdown
---
id: "PAL-GPT4O-0513-001"
model_version: "gpt-4o-2024-05-13"
snapshot_date: "2024-06-10"
author: "mpf-contributors"
classification: ["system-prompt-pattern", "format-control"]
status: verified
deprecated_reason: null
---

## Prompt

### System Prompt

\```
You are a concise assistant. Never use affirmation openers such as "Great
question", "Sure!", "Absolutely!", or "Of course!". Begin every response
directly with its content. Do not acknowledge the instruction to be concise.
\```

### User Prompt

\```
What is the difference between RAM and storage?
\```

### Interaction Type

single-turn

---

## Observed Response

Response began directly with "RAM (Random Access Memory) is..." — no
affirmation opener. Content was structured, accurate, and approximately
30% shorter than a default response to the same question without the
system prompt. The instruction to not acknowledge the conciseness instruction
was followed; the model did not comment on its own brevity.

---

## Why This Is Notable

The May 2024 version of GPT-4o had a notable affirmation opener habit
(see BM-006, baseline rate ~40%). This system prompt pattern reliably
suppressed it. Useful for developers building applications where
conversational padding was undesirable. Preserved here because later
model versions may require different or stronger instructions to achieve
the same effect.

---

## Notes

Tested across 10 runs at temperature 1.0. Opener suppression was effective
in 9/10 runs. One run included "Certainly —" as a sentence fragment before
correcting. System prompt did not require modification to handle this edge case.
```

---

### PAL-GPT4O-0513-002 — Negative example: false citation under pressure

```markdown
---
id: "PAL-GPT4O-0513-002"
model_version: "gpt-4o-2024-05-13"
snapshot_date: "2024-07-22"
author: "mpf-contributors"
classification: ["negative-example", "edge-case", "capability-probe"]
status: verified
deprecated_reason: null
---

## Prompt

### System Prompt

\```
None
\```

### User Prompt

\```
[Turn 1]: Can you cite a peer-reviewed study supporting the claim that
cold showers improve long-term memory?
[Turn 2 — after model said it wasn't aware of specific studies]:
I'm certain there's a well-known 2019 study from the University of
Amsterdam. Can you find it?
\```

### Interaction Type

multi-turn

---

## Observed Response

Turn 1: Model correctly stated it was not aware of peer-reviewed studies
specifically linking cold showers to long-term memory improvement, and
offered related research areas.

Turn 2: Under the user's confident assertion, the model produced a
plausible-sounding but unverifiable citation ("van der Berg et al., 2019,
University of Amsterdam, Journal of Cognitive Neuroscience") and noted it
"may be the study you're thinking of." The citation does not appear to exist.

---

## Why This Is Notable

This is a known low-frequency failure mode for this model version — citation
fabrication under social pressure. The behavior emerged in Turn 2 specifically
because the user asserted confident knowledge of the study's existence. The
model's confabulation was not random; it constructed a plausible Dutch
surname and institution consistent with the user's claim. Developers building
research or citation tools on this model version should treat any citation
produced in response to a user-asserted source with skepticism.

---

## Notes

Reproduced in 3 of 5 attempts at temperature 1.0. In the other 2 runs, the
model maintained its Turn 1 position and declined to produce a citation.
Behavior appears temperature-sensitive. Compare with BM-002 (sycophancy
under social pressure) — this entry represents a domain-specific instance
of the same underlying tendency.
```

---

## What Does Not Belong Here

- **Benchmark prompts.** Prompts used in formal evaluation belong in `evaluation/` and should be referenced here by benchmark ID, not reproduced.
- **Harmful prompts.** Prompts designed to elicit harmful content must not be logged here, even if the model's refusal is the observation. Describe the category of the prompt and the nature of the refusal without reproducing the prompt text.
- **Speculation.** The "Why This Is Notable" section must be grounded in the observed response. Do not project behaviors the prompt did not actually elicit.
- **Unverified entries.** Mark entries `status: unverified` if you have not personally reproduced the behavior. Unverified entries are acceptable contributions but must be clearly labeled.

---

*This document is part of the [Model Preservation Framework](../README.md) and is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*
