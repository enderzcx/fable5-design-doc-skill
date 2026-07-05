---
name: fable5-design-doc
description: Create a public-safe Fable5 design-document prompt pack. Use when the user wants Fable5 to design a product, feature, architecture, UX, workflow, or system and needs a reusable prompt document plus a short launch prompt. Requires a grill-me-style clarification interview before writing. Not for implementing code, writing the final design yourself, ordinary PRDs, debugging, reviews, or one-off copywriting.
---

# Fable5 Design Doc

Use this skill to turn a rough request into a prompt pack for Fable5:

1. a durable prompt document that Fable5 can read;
2. a short launch prompt that points Fable5 at that document.

The skill owns prompt packaging, clarification, and quality gates. It does not own the final design judgment. Fable5 owns the design.

## Workflow

### 1. Classify

Use this skill only when all are true:

- The user wants Fable5 to create a design document or design plan.
- The output should be a prompt document Fable5 can read later.
- The task has enough ambiguity that a prompt could run off course without clarification.

If the user wants a normal PRD/SPEC, use the planning skill for that environment. If the user wants implementation, do not use this skill.

### 2. Run The Grill Gate

Before writing the prompt document, run a grill-me-style interview.

If a `grill-me` or `grilling` skill is available, use it. If not, emulate it:

- Ask one question at a time.
- Give your recommended answer with each question.
- Wait for the user's answer before continuing.
- Stop asking about details the user explicitly delegates to Fable5.
- Keep grilling only until the hard boundaries are clear.

Clarify these minimum boundaries:

- Design target: what Fable5 is designing.
- Primary audience or user.
- Desired outcome and success criteria.
- What Fable5 decides autonomously.
- What Fable5 must ask the user before changing.
- Non-goals and forbidden actions.
- Required source material.
- Required evidence or validation.
- Where to write the prompt document.

### 3. Separate User Boundaries From Fable5 Freedom

Write down only the decisions the user actually confirmed.

Do not turn your own recommended answers into hard requirements unless the user accepted them. For unresolved details, say Fable5 owns the decision.

### 4. Create The Prompt Pack

Use `templates/fable5-design-prompt.md` as the document shape and `templates/launch-prompt.md` as the short launch prompt shape.

The prompt document must include:

- role and task;
- design target;
- confirmed boundaries;
- Fable5 decision authority;
- source-reading instructions;
- optional collaborator/model delegation;
- required final document structure;
- validation and evidence requirements;
- stop/ask conditions;
- strict non-goals.

The short launch prompt must be 1-3 sentences and must point to the prompt document path or URL.

### 5. Validate

Run the checker on the generated prompt document:

```bash
python3 fable5-design-doc/scripts/check_fable5_design_prompt.py <prompt-doc.md>
```

Fix missing sections before finalizing.

## Output Contract

Return:

- the prompt document path;
- the short launch prompt;
- the checker result;
- any unresolved assumptions Fable5 must decide or ask about.

Do not include private paths, private project names, personal preferences, credentials, or organization-specific rules unless the user explicitly wants a private prompt pack.

## Resources

- `references/quality-rules.md`: public-safe quality rules.
- `templates/fable5-design-prompt.md`: prompt document template.
- `templates/launch-prompt.md`: short launch prompt template.
- `scripts/check_fable5_design_prompt.py`: required-section checker.
- `evals/trigger_cases.json`: routing examples for maintainers.
