# Fable5 Design Doc Skill

Create a prompt pack for Fable5 design work:

- a durable prompt document Fable5 can read;
- a short launch prompt that points Fable5 at that document;
- a grill-me-style clarification gate so the prompt does not drift;
- a checker that catches missing required prompt sections.

This skill is public-safe by default. It does not encode private paths, private projects, personal workflow preferences, credentials, or organization-specific rules.

## Install

Copy or symlink the skill folder into your agent's skills directory:

```bash
cp -r fable5-design-doc ~/.claude/skills/fable5-design-doc
```

If your agent uses another skills directory, copy the `fable5-design-doc/` folder there.

## Use

Ask for a Fable5 design prompt pack:

```text
Use fable5-design-doc. I want Fable5 to design the onboarding UX for my desktop app. Create a prompt document and a short launch prompt. Grill me first so the prompt does not drift.
```

The skill will:

1. run a grill-me-style clarification interview;
2. separate confirmed user boundaries from Fable5-owned decisions;
3. create a prompt document from `templates/fable5-design-prompt.md`;
4. create a short launch prompt from `templates/launch-prompt.md`;
5. run `scripts/check_fable5_design_prompt.py`.

## Validate A Generated Prompt

```bash
python3 fable5-design-doc/scripts/check_fable5_design_prompt.py path/to/prompt-doc.md
```

The checker fails when required sections are missing or template placeholders remain unresolved.

## Package

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

## License

MIT
