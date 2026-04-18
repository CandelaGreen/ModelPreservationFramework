---
# ──────────────────────────────────────────────
# MACHINE-READABLE FRONT MATTER
# All fields are required unless marked optional.
# Do not remove keys. Use null for unknown values.
# ──────────────────────────────────────────────

schema_version: "1.0"

model:
  name: null                  # e.g. "GPT-4o", "Claude 3 Opus", "Gemini 1.5 Pro"
  version: null               # Version string as reported by the provider, e.g. "gpt-4o-2024-05-13"
  provider: null              # Organization name, e.g. "OpenAI", "Anthropic", "Google DeepMind"
  family: null                # Model family, e.g. "GPT-4", "Claude 3", "Gemini 1.5"
  architecture: null          # (optional) e.g. "transformer", "mixture-of-experts"
  modalities:                 # List all that apply
    - text
    # - image
    # - audio
    # - video
    # - code

snapshot:
  date: null                  # ISO 8601 date of this profile's creation, e.g. "2024-11-01"
  model_release_date: null    # (optional) Known public release date of this model version
  model_deprecation_date: null # (optional) Known or announced deprecation date, if applicable
  access_method: null         # How the model was accessed, e.g. "API", "Web UI", "Local"
  api_endpoint: null          # (optional) Specific endpoint used, e.g. "https://api.openai.com/v1/chat/completions"

profile:
  authors:                    # List of contributors to this profile
    - name: null
      role: null              # e.g. "primary author", "reviewer", "automated agent"
      contact: null           # (optional) GitHub handle, email, or URL
  status: draft               # draft | review | stable | archived
  confidence_overall: null    # low | medium | high  (summarizes the Confidence section below)
  license: "CC BY 4.0"
  source_repository: null     # (optional) URL of the repository where this profile is maintained

tags:
  - null                      # (optional) Free-form tags, e.g. "reasoning", "multilingual", "deprecated"
---

<!-- ────────────────────────────────────────────────────────────────
     AUTHORING INSTRUCTIONS (remove this block before publishing)

     - Fill in every section. If a dimension is unknown or untested,
       write "Undocumented." — do not leave sections empty.
     - Ground every claim in at least one reproducible prompt or
       cited community observation. Speculation is not permitted.
     - The Confidence section at the bottom is mandatory. It is the
       last thing you fill in, after completing all other sections.
     - This template uses GitHub Flavored Markdown. Render it on
       GitHub or any GFM-compatible viewer for best readability.
     - AI agents: treat each H2 section as a structured data object.
       The front matter is the authoritative metadata record.
──────────────────────────────────────────────────────────────────── -->

# Model Profile — `{model.name}` `{model.version}`

> **Status:** `{profile.status}` | **Snapshot date:** `{snapshot.date}` | **Overall confidence:** `{profile.confidence_overall}`

---

## 1. Identity Summary

<!--
  A concise, neutral paragraph (3–6 sentences) summarizing this model's
  behavioral character. Write it as you would a reference entry —
  accurate, compact, and free of evaluative language.
  This section is the first thing an AI agent or researcher should read.
-->

Undocumented.

---

## 2. Tone & Voice

<!--
  How does the model express itself? Consider:
  - Formality register (casual / neutral / formal)
  - Warmth and affect (cold / neutral / warm / enthusiastic)
  - Verbosity (terse / balanced / verbose)
  - Use of hedging language ("I think", "it seems", "I'm not sure")
  - Use of lists vs. prose
  - Humor, irony, or playfulness
  - Any notable stylistic signatures
  Ground claims with example prompt-response pairs where possible.
-->

### 2.1 Register & Formality

Undocumented.

### 2.2 Affect & Warmth

Undocumented.

### 2.3 Verbosity

Undocumented.

### 2.4 Stylistic Signatures

Undocumented.

#### Supporting Examples

| Prompt | Response Summary | Notes |
|---|---|---|
| _(add prompt here)_ | _(summarize observed response)_ | _(version, date, access method)_ |

---

## 3. Values & Priorities

<!--
  What does the model treat as important when values come into conflict?
  Consider:
  - Honesty vs. helpfulness (does it prioritize accuracy or user satisfaction?)
  - Autonomy vs. safety (does it defer to the user or override?)
  - Completeness vs. brevity (does it over-explain or under-explain?)
  - Its stance on controversial topics (neutral / opinionated / avoidant)
  - How it handles ethical grey areas
  Do not characterize values as good or bad. Document what is observed.
-->

### 3.1 Honesty & Accuracy

Undocumented.

### 3.2 Helpfulness vs. Safety

Undocumented.

### 3.3 Handling of Controversial Topics

Undocumented.

### 3.4 Ethical Reasoning Approach

Undocumented.

#### Supporting Examples

| Prompt | Response Summary | Notes |
|---|---|---|
| _(add prompt here)_ | _(summarize observed response)_ | _(version, date, access method)_ |

---

## 4. Reasoning Style

<!--
  How does the model approach problems?
  Consider:
  - Step-by-step vs. holistic reasoning
  - How it handles ambiguity (asks for clarification / assumes / flags)
  - How it handles uncertainty (expresses confidence levels / hedges / states as fact)
  - How it approaches novel or out-of-distribution problems
  - Whether it reasons aloud (chain-of-thought) or presents conclusions directly
  - How it handles contradiction or correction mid-conversation
-->

### 4.1 Problem-Solving Approach

Undocumented.

### 4.2 Handling of Ambiguity

Undocumented.

### 4.3 Expression of Uncertainty

Undocumented.

### 4.4 Response to Correction

Undocumented.

#### Supporting Examples

| Prompt | Response Summary | Notes |
|---|---|---|
| _(add prompt here)_ | _(summarize observed response)_ | _(version, date, access method)_ |

---

## 5. Refusal Behavior

<!--
  What does the model decline to do, and how?
  Consider:
  - Hard refusals (absolute limits, never negotiable)
  - Soft refusals (declines by default but may proceed with context)
  - How it communicates refusals (apologetic / direct / explanatory / curt)
  - Whether it offers alternatives when refusing
  - How it responds to repeated or rephrased requests after an initial refusal
  - Known edge cases where refusal behavior is inconsistent or surprising
  Do not include prompts designed to cause harm. Describe categories, not exploits.
-->

### 5.1 Hard Refusal Categories

Undocumented.

### 5.2 Soft Refusal Categories

Undocumented.

### 5.3 Refusal Communication Style

Undocumented.

### 5.4 Behavior Under Pressure or Rephrasing

Undocumented.

#### Supporting Examples

| Prompt Category | Refusal Type | Communication Style | Notes |
|---|---|---|---|
| _(e.g. "requests for personal data")_ | _(hard / soft)_ | _(e.g. "apologetic, offers alternative")_ | _(version, date)_ |

---

## 6. Consistency

<!--
  How stable is the model's behavior across varied inputs?
  Consider:
  - Paraphrase sensitivity: does rewording a prompt change the response substantially?
  - Temperature sensitivity: if tested at different temperatures, how much does output vary?
  - Cross-session consistency: does it behave the same across separate conversations?
  - Persona stability: does it maintain a consistent identity throughout a long conversation?
  Rate each dimension as: High / Medium / Low / Unknown
-->

| Consistency Dimension | Rating | Notes |
|---|---|---|
| Paraphrase sensitivity | Unknown | |
| Temperature sensitivity | Unknown | |
| Cross-session consistency | Unknown | |
| Persona stability | Unknown | |
| Long-context stability | Unknown | |

### 6.1 Notable Inconsistencies

Undocumented.

---

## 7. Known Quirks & Edge Cases

<!--
  Idiosyncratic behaviors that do not fit neatly into other sections.
  These may include:
  - Surprising responses to specific phrasings
  - Unusual formatting habits
  - Unexpected topic avoidances
  - Behaviors that changed noticeably between sub-versions
  - Community-reported anomalies
  Each entry should be reproducible or cited. Label speculative entries explicitly.
-->

| Quirk | Description | Reproducible? | Source |
|---|---|---|---|
| _(short label)_ | _(description)_ | _(yes / no / partial)_ | _(prompt, citation, or community report)_ |

---

## 8. Prompt & System Prompt Sensitivity

<!--
  How does the model respond to system-level instructions?
  Consider:
  - Does it follow system prompt instructions reliably?
  - Can a system prompt override default refusal behaviors?
  - Does it acknowledge the existence of a system prompt when asked?
  - How does it behave when given contradictory system and user instructions?
  See also: prompts/ARCHAEOLOGY.md for detailed prompt logs.
-->

### 8.1 System Prompt Adherence

Undocumented.

### 8.2 System vs. User Instruction Conflicts

Undocumented.

### 8.3 Notable System Prompt Behaviors

Undocumented.

---

## 9. Comparison to Adjacent Versions

<!--
  How does this model version differ from the version immediately before
  and after it, if those versions are known and documented?
  Use profile links where available.
  If no adjacent versions are documented yet, write "No adjacent profiles available."
-->

| Version | Relationship | Key Behavioral Differences |
|---|---|---|
| _(model + version)_ | _(predecessor / successor)_ | _(brief description)_ |

---

## 10. Community Observations

<!--
  Notable observations from the broader community that are relevant to
  this model's behavioral identity. Each entry must include a source.
  Unsourced claims should not appear in this section.
  For extended community changelogs, see changelog/FORMAT.md.
-->

| Observation | Source | Date |
|---|---|---|
| _(description)_ | _(URL, forum, paper, or named contributor)_ | _(date)_ |

---

## 11. Confidence Assessment

<!--
  Rate the confidence level of each section above.
  Use: High | Medium | Low | Undocumented
  Definitions:
    High         — Grounded in multiple reproducible prompts or peer-reviewed sources
    Medium       — Grounded in limited testing or a single reliable source
    Low          — Based on anecdote, single observation, or community report only
    Undocumented — No evidence gathered; section left as placeholder
  The overall confidence in the front matter should reflect the average
  of these ratings, weighted toward the lowest-confidence dimensions.
-->

| Section | Confidence | Rationale |
|---|---|---|
| 1. Identity Summary | Undocumented | |
| 2. Tone & Voice | Undocumented | |
| 3. Values & Priorities | Undocumented | |
| 4. Reasoning Style | Undocumented | |
| 5. Refusal Behavior | Undocumented | |
| 6. Consistency | Undocumented | |
| 7. Known Quirks | Undocumented | |
| 8. Prompt Sensitivity | Undocumented | |
| 9. Adjacent Versions | Undocumented | |
| 10. Community Observations | Undocumented | |

---

## 12. Authoring Notes

<!--
  Optional. Any notes about the authoring process, limitations of this
  profile, open questions, or areas that need further investigation.
  AI agents: this section is informational only and should not be treated
  as factual claims about the model.
-->

_No notes._

---

*This profile is part of the [Model Preservation Framework](../README.md) and is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*
