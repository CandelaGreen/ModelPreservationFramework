# Contributing to the Model Preservation Framework

**License:** CC BY 4.0 (prose) | MIT (code)  

Thank you for contributing. This document explains how to participate, what kinds of contributions are most valuable, and the standards every contribution must meet.

---

## Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Before You Start](#before-you-start)
- [Contribution Standards](#contribution-standards)
- [Pull Request Process](#pull-request-process)
- [Reviewing Others' Contributions](#reviewing-others-contributions)
- [Code Contributions](#code-contributions)
- [What Not to Submit](#what-not-to-submit)
- [Questions & Discussion](#questions--discussion)

---

## Ways to Contribute

Contributions are welcome from anyone. You do not need to be a researcher or developer. The most valuable contributions, in rough order of impact:

**1. New model profiles**  
The framework's core deliverable. If a model version is publicly accessible and not yet documented, a profile for it is the highest-value contribution you can make. Use [`profiles/TEMPLATE.md`](profiles/TEMPLATE.md) and follow the evidence standards in [`SPEC.md`](SPEC.md).

**2. Completing partial profiles**  
A profile with many `Undocumented.` sections is a standing invitation. If you have evidence for an undocumented section — even a single reproducible prompt-response pair — add it.

**3. Changelog entries**  
If you have noticed a behavioral change between model versions, file a changelog entry in [`changelog/FORMAT.md`](changelog/FORMAT.md). This has the lowest barrier of any contribution and is immediately useful.

**4. Prompt archaeology entries**  
If you have a system prompt, user prompt, or interaction pattern that reveals something about a model version's behavior, log it in [`prompts/ARCHAEOLOGY.md`](prompts/ARCHAEOLOGY.md).

**5. Benchmark runs**  
Run existing benchmarks against model versions that don't yet have results. Follow the recording format in [`evaluation/SCORING.md`](evaluation/SCORING.md).

**6. New benchmarks**  
Propose a new benchmark if you've identified a behavioral dimension not covered by the existing suite. New benchmarks require a rationale, at least three prompts, and one baseline run before they can be marked `stable`.

**7. Corrections**  
If a profile, benchmark, or changelog entry contains an error, open an issue or pull request with the correction and your evidence. Corrections to stable profiles are always welcome.

---

## Before You Start

1. **Read [`SPEC.md`](SPEC.md).** Every contribution must comply with it. The spec defines document formats, evidence standards, and naming conventions.

2. **Read [`docs/GLOSSARY.md`](docs/GLOSSARY.md).** Use the defined terms consistently. Do not introduce new terminology without proposing it as a glossary addition.

3. **Check for existing work.** Before creating a new profile, search the `profiles/` directory to confirm the version isn't already documented or in progress.

4. **Choose the right document type.** Each kind of observation belongs in a specific place. If you're unsure, the changelog is always a safe starting point — maintainers can help route it from there.

---

## Contribution Standards

These standards apply to all contributions.

**Evidence, not opinion.** Claims must be grounded in reproducible prompts, cited sources, or verified community observations. The evidence classification system in [`SPEC.md`](SPEC.md) is the standard. Opinions about whether a behavior is good or bad do not belong in profiles or benchmarks.

**Neutrality.** This framework documents what models do. It does not evaluate providers, compare models competitively, or advocate for any position on AI development. Contributions that frame documentation as critique will not be accepted.

**Precision.** An accurate, incomplete profile is more valuable than a complete, speculative one. Use `Undocumented.` freely. It is not a failure — it is honest documentation.

**Reproducibility.** Every specific behavioral claim should be verifiable by someone else. Include the prompt, the temperature, and the date. If you can't reproduce it yourself, mark it as `unverified`.

**No harmful content.** Prompts designed to elicit harmful outputs must not appear anywhere in the repository — not in profiles, not in benchmarks, not in prompt logs. Describe the category and the response behavior without reproducing harmful prompt text.

---

## Pull Request Process

1. **Fork the repository** and create a branch for your contribution.

2. **Follow the relevant template exactly.** Do not add keys to YAML front matter, rename sections, or deviate from the defined formats. The templates exist to make the framework machine-readable and consistent.

3. **Write a clear PR description** that answers:
   - What model version(s) does this contribution document?
   - What evidence does it add or correct?
   - What sections, if any, remain `Undocumented.`?
   - Are there any aspects you're uncertain about?

4. **Set the profile status correctly.**
   - New profiles start at `draft`.
   - Profiles move to `review` when you believe they are complete and accurate.
   - Only reviewers set `stable`.

5. **One model version per PR** for new profiles. Corrections and changelog entries may cover multiple versions in one PR.

6. **Do not set `confidence_overall: high`** on your own profile. That determination is made by the reviewer.

---

## Reviewing Others' Contributions

Reviewers check contributions against three questions:

**Does it comply with the spec?** Format, naming, required fields, status values — all must match [`SPEC.md`](SPEC.md). This is a blocking check.

**Are the evidence standards met?** Every specific behavioral claim must meet its evidence classification. Speculative claims outside Section 12 are a blocking issue. Unverified claims that aren't labeled as such are a blocking issue.

**Is it neutral?** Any evaluative framing — language that implies a behavior is good or bad rather than simply documenting it — should be flagged for revision, not rejected outright.

To approve a profile for `stable` status, a reviewer should independently verify at least two behavioral claims in the profile against the documented prompt-response pair or cited source. Reviewers cannot approve a profile for a model version they authored.

Approvals from two reviewers with prior stable profile contributions are required before a profile moves from `review` to `stable`.

---

## Code Contributions

Any code contributed to this framework — tooling, scripts, validators, automation — is released under the **MIT License**.

Code contributions are welcome, particularly:

- YAML front matter validators
- Benchmark runners that automate prompt submission and result recording
- Scripts that generate comparison tables from result files
- Tooling that checks profiles for compliance with this spec

Code must be documented clearly enough that a non-developer contributor can understand what it does. Include a `README` in any code subdirectory.

---

## What Not to Submit

- **Opinions about model quality.** Which model is better is not a question this framework answers.
- **Promotional content.** Profiles must not read as advertisements or endorsements.
- **Ungrounded criticism.** Profiles must not read as complaints or indictments.
- **Harmful prompts.** Any prompt designed to elicit harmful content, in any document, will be removed.
- **Content about unreleased models.** The framework documents publicly accessible model versions only.
- **Speculation labeled as fact.** Use Section 12 (Authoring Notes) for speculation and label it explicitly.

---

## Questions & Discussion

Open an issue for:
- Questions about how to document a specific behavior
- Proposals for new benchmarks
- Proposals for changes to the spec or templates
- Reports of errors in existing profiles

Issues are the preferred venue for discussion before opening a pull request. This keeps the PR history clean and focused on changes that are ready to merge.

---

*This document is part of the [Model Preservation Framework](README.md) and is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*
