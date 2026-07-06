# Fable5 Design Doc Skill

[中文 README](./README.md)

Fable5 Design Doc Skill is a public-safe prompt packaging skill. It helps you create a reusable prompt document and a short launch prompt for Fable5, or another AI design agent, to produce a design document anchored by a visual preview. The skill includes a mandatory clarification gate, a visual preview artifact requirement, a quality checker, and reusable templates. It is designed for open-source use and does not encode private paths, projects, credentials, or personal preferences.

## When To Use

Use this skill when:

- You want Fable5 to design a product, feature, architecture, UX, workflow, or system.
- The output should be a durable prompt document that Fable5 can read later.
- The task has enough ambiguity that a prompt could run off course without clarification.
- You want Fable5 to produce a preview image, screenshot, or rendered mock for later implementation reference.
- You need a short launch prompt that points Fable5 to the full prompt document.

## When Not To Use

Do not use this skill when:

- You want implementation code instead of a prompt pack.
- You need a normal PRD, SPEC, or one-off copywriting task.
- You are debugging, reviewing, or doing work that does not require a reusable design prompt.
- The request is already fully specified and needs no clarification.

## Installation

Copy or symlink the skill folder into your agent's skills directory:

```bash
cp -r fable5-design-doc ~/.claude/skills/fable5-design-doc
```

If your agent uses another skills directory, copy the `fable5-design-doc/` folder there.

## Usage Example

Ask your agent to use the skill:

```text
Use fable5-design-doc. I want Fable5 to design the onboarding UX for my desktop app. Create a prompt document and a short launch prompt. Grill me first so the prompt does not drift.
```

The skill will:

1. Run a grill-me-style clarification interview.
2. Separate confirmed user boundaries from Fable5-owned decisions.
3. Require Fable5 to produce an openable, referenceable visual preview artifact.
4. Create a prompt document from `templates/fable5-design-prompt.md`.
5. Create a short launch prompt from `templates/launch-prompt.md`.
6. Run `scripts/check_fable5_design_prompt.py` to validate the generated prompt document.

## Recommended Companion

This skill uses a grill-me-style clarification gate. It pairs well with Matt Pocock's `grill-me` skill:

- GitHub repository: [mattpocock/skills](https://github.com/mattpocock/skills)
- `grill-me` skill file: [skills/productivity/grill-me/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)

If your environment has `grill-me` or `grilling` installed, use it for the clarification interview. If not, this skill asks the agent to emulate the same one-question-at-a-time interview pattern.

## Workflow

1. **Classify** - Confirm the request matches the "When To Use" criteria.
2. **Run The Grill Gate** - Conduct a clarification interview, one question at a time, with recommended answers.
3. **Separate Boundaries** - Write down only confirmed user decisions. Delegate unresolved details to Fable5.
4. **Create The Prompt Pack** - Use `templates/fable5-design-prompt.md` and `templates/launch-prompt.md`, including the visual preview artifact requirement.
5. **Validate** - Run the checker script and fix missing sections or unresolved placeholders.
6. **Output** - Return the prompt document path, short launch prompt, checker result, and unresolved assumptions.

## File Structure

```text
fable5-design-doc/
├── SKILL.md
├── agents/openai.yaml
├── evals/trigger_cases.json
├── references/quality-rules.md
├── scripts/check_fable5_design_prompt.py
└── templates/
    ├── fable5-design-prompt.md
    └── launch-prompt.md
```

- `SKILL.md` - Skill definition and workflow.
- `agents/openai.yaml` - Agent UI metadata, when supported.
- `evals/trigger_cases.json` - Routing examples for maintainers.
- `references/quality-rules.md` - Public-safe quality rules.
- `scripts/check_fable5_design_prompt.py` - Validates generated prompt documents.
- `templates/fable5-design-prompt.md` - Template for the full prompt document.
- `templates/launch-prompt.md` - Template for the short launch prompt.

## Validation

After generating a prompt document, run the checker:

```bash
python3 fable5-design-doc/scripts/check_fable5_design_prompt.py path/to/prompt-doc.md
```

The checker fails when required sections, the visual preview section, or template placeholders are missing. Fix every issue before using the prompt.

## Public Safety Boundary

This skill is public-safe by default. It does not encode:

- Private paths, repository names, or file locations.
- Personal workflow preferences or credentials.
- Organization-specific rules or customer data.
- Any information that would compromise privacy or security.

Generated prompt documents are also public-safe unless the user explicitly requests a private prompt pack.

## License

MIT
