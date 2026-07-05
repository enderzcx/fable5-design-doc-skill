# Fable5 Design Prompt Quality Rules

## Public-Safe Default

Assume the skill may be published. Do not bake in private paths, private repository names, personal workflow preferences, customer data, credentials, or organization-specific policy. Put those in the generated prompt document only when the user explicitly asks for a private prompt pack.

## The Grill Gate Is Mandatory

Run a grill-me-style clarification interview before writing the prompt document. The point is not to approve every detail; it is to prevent the prompt from drifting on hard boundaries.

The interview should establish:

- what Fable5 is designing;
- who the design serves;
- what success means;
- what Fable5 owns;
- what Fable5 must not change silently;
- what evidence proves the eventual design can be executed.

## Fable5 Owns Design Judgment

The prompt should delegate real design choices to Fable5. It should constrain mission, boundaries, evidence, and stop conditions. It should not pre-design the product unless the user explicitly supplied those decisions.

Use this split:

- **Confirmed boundary**: the user accepted it; Fable5 must obey it.
- **Fable5-owned choice**: the user delegated it; Fable5 decides and explains.
- **Ask condition**: Fable5 must stop before changing it.

## Prompt Document Beats Long Chat Prompt

The final output should be a durable prompt document plus a short launch prompt. Avoid handing the user a giant chat prompt that is likely to exceed input limits.

## Verification Is Part Of The Prompt

Every generated prompt document should require Fable5 to produce a verifiable design document, not just inspiration. The prompt should demand evidence such as acceptance criteria, review surfaces, screenshots, fixtures, smoke tests, checklists, or other task-appropriate validation.

## Design-Only Boundary

Unless the user explicitly asks otherwise, Fable5 should design and plan. It should not implement code, mutate production state, publish releases, spend money, change accounts, or perform irreversible writes.
