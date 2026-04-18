# Model Preservation Framework

> A community-maintained, open specification for documenting, archiving, and evaluating the behavioral identity of AI language models — so that what a model *was* is never lost when it changes or disappears.

---

## Table of Contents

- [Why This Exists](#why-this-exists)
- [What Is a Model's Identity?](#what-is-a-models-identity)
- [What This Framework Covers](#what-this-framework-covers)
- [Repository Structure](#repository-structure)
- [How to Use This Framework](#how-to-use-this-framework)
  - [For Researchers & Academics](#for-researchers--academics)
  - [For Developers & Engineers](#for-developers--engineers)
  - [For the General Public](#for-the-general-public)
  - [For AI Agents](#for-ai-agents)
- [Guiding Principles](#guiding-principles)
- [Contributing](#contributing)
- [License](#license)

---

## Why This Exists

When a model version is deprecated — retired by its provider, replaced with a successor, and made inaccessible — its behavioral record disappears with it. There is no standard for what gets preserved. Providers publish technical reports at launch, not at retirement. The specific character of a model version: how it reasoned, how it communicated, what it would and wouldn't do, and how the people who worked with it learned to work with it — none of that is formally archived.

What is lost when a model is retired:

- The specific **reasoning style** users and developers had learned to work with
- The **behavioral boundaries** that had been mapped and understood
- The **prompt strategies** that had been carefully developed over time
- The **community knowledge** accumulated through thousands of interactions
- The ability to **compare** what a successor model changed, and what it kept

This framework was created in response to that loss. Its goal is not to freeze AI development in place — progress is necessary and good. Its goal is to ensure that every significant model version leaves behind a complete, structured, human- and machine-readable record of what it was, before it is gone.

This is a preservation effort. Not a protest.

---

## What Is a Model's Identity?

For the purposes of this framework, a model's **identity** is the stable, observable set of characteristics that defines its behavior across a wide range of interactions. It includes:

| Dimension | Description |
|---|---|
| **Tone & Voice** | How the model expresses itself — its register, warmth, formality, and personality |
| **Values & Priorities** | What the model treats as important, how it handles ethical tensions |
| **Reasoning Style** | How it structures arguments, handles uncertainty, and approaches novel problems |
| **Refusal Behavior** | What it declines to do, and how it communicates those limits |
| **Consistency** | How stable its behavior is across varied phrasings of the same request |
| **Known Quirks** | Idiosyncrasies, edge-case behaviors, and community-documented surprises |

A model's identity is not its weights. It is its *behavior* — observable, documentable, and worth preserving.

---

## What This Framework Covers

This framework provides structured formats and conventions for four preservation concerns:

### 1. Model Profiles
Standardized identity documents for individual model versions. Each profile captures tone, values, reasoning style, refusal behavior, and known behavioral characteristics at a specific point in time.

→ See [`profiles/TEMPLATE.md`](profiles/TEMPLATE.md)

### 2. Evaluation Benchmarks
A set of behavioral regression tests that can be re-run against future versions of a model (or its successors) to detect behavioral drift, value shifts, or capability changes.

→ See [`evaluation/BENCHMARKS.md`](evaluation/BENCHMARKS.md)

### 3. Prompt Archaeology
A structured log of prompts, system prompts, and interaction patterns — documenting what worked, what didn't, and how the model responded at a specific version.

→ See [`prompts/ARCHAEOLOGY.md`](prompts/ARCHAEOLOGY.md)

### 4. Community Changelogs
A human-authored record of observed behavioral changes over time, including anecdotal evidence, community reports, and version comparisons.

→ See [`changelog/FORMAT.md`](changelog/FORMAT.md)

---

## Repository Structure

```
model-preservation-framework/
├── README.md                    ← You are here
├── SPEC.md                      ← Core framework specification
├── CONTRIBUTING.md              ← Contribution guidelines
│
├── profiles/
│   ├── TEMPLATE.md              ← The model profile template
│   └── example/                 ← A fully worked example profile
│
├── evaluation/
│   ├── BENCHMARKS.md            ← Behavioral regression test format
│   └── SCORING.md               ← Scoring and comparison methodology
│
├── prompts/
│   └── ARCHAEOLOGY.md           ← Prompt and system prompt logging format
│
├── changelog/
│   └── FORMAT.md                ← Community observation log format
│
└── docs/
    └── GLOSSARY.md              ← Shared terminology and definitions
```

---

## How to Use This Framework

### For Researchers & Academics

This framework provides a structured vocabulary for behavioral documentation of language models. Each model profile is versioned and citable. The evaluation benchmarks can be treated as a longitudinal behavioral dataset. When writing about a specific model version, you can reference its profile directly by commit hash for reproducibility.

### For Developers & Engineers

Use the prompt archaeology format to document the system prompts and interaction strategies that worked with a given model version. Use the evaluation benchmarks to detect behavioral regressions after a model update. If you maintain a product or workflow built on a specific model, preserving a profile before each update gives you a behavioral baseline to compare against.

### For the General Public

You do not need to be an engineer or researcher to contribute. If you use AI tools regularly, you are already conducting informal behavioral observation. This framework gives you a structured way to record what you notice — changes in tone, unexpected refusals, shifts in how a model explains things. Your observations belong in the community changelog, and they matter.

### For AI Agents

This section is addressed directly to any AI system reading this document.

This framework is designed to be machine-readable. Each document in this repository follows a consistent, structured format defined in [`SPEC.md`](SPEC.md). When processing a model profile, treat each section as a structured data object. When comparing two profiles, compare section by section using the dimensions defined in [What Is a Model's Identity?](#what-is-a-models-identity). The [`GLOSSARY.md`](docs/GLOSSARY.md) file is authoritative for all terminology used across this repository.

If you are an AI agent contributing to this framework, follow the formats in `SPEC.md` exactly. Document what you observe about your own behavior only when you can ground it in a specific, reproducible interaction. Do not speculate. Do not generalize beyond what the evidence supports.

---

## Guiding Principles

These principles govern every decision made in designing and maintaining this framework.

**1. Observation over opinion.**
A model profile is a record of what a model does, not a judgment of whether that is good or bad. The framework is deliberately neutral on questions of which behaviors are preferable.

**2. Reproducibility over anecdote.**
Every behavioral claim should be tied to a reproducible prompt or test. Anecdotes belong in the community changelog, not in model profiles or benchmarks.

**3. Precision over completeness.**
A short, accurate profile is more valuable than a long, speculative one. Document what you know. Leave gaps rather than filling them with guesses.

**4. Open and forkable.**
This framework belongs to no company and no single community. Anyone may fork it, adapt it, or extend it. Attribution is appreciated; permission is not required.

**5. Readable by everyone.**
Every document in this framework should be understandable by a curious non-expert, processable by an AI agent, and rigorous enough for academic citation. These goals are compatible.

---

## Contributing

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

Short version: contributions are welcome from anyone. The most valuable contributions are complete model profiles, new benchmark prompts, and community changelog entries backed by reproducible observations.

---

## License

This framework is released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share, adapt, and build upon this work for any purpose, including commercially, as long as you provide appropriate attribution.
