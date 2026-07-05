# Fable5 Design Doc Skill

## Description / 描述

**English:**
Fable5 Design Doc Skill is a public-safe prompt packaging skill. It helps you create a reusable prompt document and a short launch prompt for Fable5, or another AI design agent, to produce a design document. The skill includes a mandatory clarification gate, a quality checker, and reusable templates. It is designed for open-source use and does not encode private paths, projects, credentials, or personal preferences.

**中文：**
Fable5 Design Doc Skill 是一个公共安全的提示词打包技能。它帮助你为 Fable5，或其他 AI 设计代理，创建可复用的提示文档和简短启动提示，用来产出设计文档。该技能包含强制澄清门、质量检查器和可复用模板。它面向开源使用，不包含私有路径、项目、凭据或个人偏好。

## When To Use / 适用场景

**English:**
Use this skill when:

- You want Fable5 to design a product, feature, architecture, UX, workflow, or system.
- The output should be a durable prompt document that Fable5 can read later.
- The task has enough ambiguity that a prompt could run off course without clarification.
- You need a short launch prompt that points Fable5 to the full prompt document.

**中文：**
在以下情况下使用此技能：

- 你希望 Fable5 设计产品、功能、架构、用户体验、工作流或系统。
- 输出应该是一份可复用的提示文档，供 Fable5 后续读取。
- 任务存在足够模糊性，如果不先澄清，提示词可能会跑偏。
- 你需要一段简短启动提示，让 Fable5 去读取完整提示文档。

## When Not To Use / 不适用场景

**English:**
Do not use this skill when:

- You want implementation code instead of a prompt pack.
- You need a normal PRD, SPEC, or one-off copywriting task.
- You are debugging, reviewing, or doing work that does not require a reusable design prompt.
- The request is already fully specified and needs no clarification.

**中文：**
在以下情况下不要使用此技能：

- 你需要的是实现代码，而不是提示词包。
- 你需要普通 PRD、SPEC 或一次性文案。
- 你在调试、审查，或处理不需要可复用设计提示词的任务。
- 请求已经完全明确，不需要澄清。

## Installation / 安装

**English:**
Copy or symlink the skill folder into your agent's skills directory:

```bash
cp -r fable5-design-doc ~/.claude/skills/fable5-design-doc
```

If your agent uses another skills directory, copy the `fable5-design-doc/` folder there.

**中文：**
将技能文件夹复制或符号链接到你的代理技能目录：

```bash
cp -r fable5-design-doc ~/.claude/skills/fable5-design-doc
```

如果你的代理使用其他技能目录，请将 `fable5-design-doc/` 文件夹复制到对应位置。

## Usage Example / 使用示例

**English:**
Ask your agent to use the skill:

```text
Use fable5-design-doc. I want Fable5 to design the onboarding UX for my desktop app. Create a prompt document and a short launch prompt. Grill me first so the prompt does not drift.
```

The skill will:

1. Run a grill-me-style clarification interview.
2. Separate confirmed user boundaries from Fable5-owned decisions.
3. Create a prompt document from `templates/fable5-design-prompt.md`.
4. Create a short launch prompt from `templates/launch-prompt.md`.
5. Run `scripts/check_fable5_design_prompt.py` to validate the generated prompt document.

**中文：**
向你的代理发出请求：

```text
Use fable5-design-doc. I want Fable5 to design the onboarding UX for my desktop app. Create a prompt document and a short launch prompt. Grill me first so the prompt does not drift.
```

该技能将：

1. 运行 grill-me 风格的澄清访谈。
2. 将用户确认的边界与 Fable5 拥有的决策分开。
3. 使用 `templates/fable5-design-prompt.md` 创建提示文档。
4. 使用 `templates/launch-prompt.md` 创建简短启动提示。
5. 运行 `scripts/check_fable5_design_prompt.py` 验证生成的提示文档。

## Workflow / 工作流

**English:**

1. **Classify** - Confirm the request matches the "When To Use" criteria.
2. **Run The Grill Gate** - Conduct a clarification interview, one question at a time, with recommended answers.
3. **Separate Boundaries** - Write down only confirmed user decisions. Delegate unresolved details to Fable5.
4. **Create The Prompt Pack** - Use `templates/fable5-design-prompt.md` and `templates/launch-prompt.md`.
5. **Validate** - Run the checker script and fix missing sections or unresolved placeholders.
6. **Output** - Return the prompt document path, short launch prompt, checker result, and unresolved assumptions.

**中文：**

1. **分类** - 确认请求符合“适用场景”。
2. **运行 Grill 门** - 进行澄清访谈，一次一个问题，并附带推荐答案。
3. **分离边界** - 只记录用户确认的决策。未解决的细节交给 Fable5。
4. **创建提示词包** - 使用 `templates/fable5-design-prompt.md` 和 `templates/launch-prompt.md`。
5. **验证** - 运行检查器脚本，修复缺失章节或未替换占位符。
6. **输出** - 返回提示文档路径、简短启动提示、检查器结果和未解决假设。

## File Structure / 文件结构

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

**English:**

- `SKILL.md` - Skill definition and workflow.
- `agents/openai.yaml` - Agent UI metadata, when supported.
- `evals/trigger_cases.json` - Routing examples for maintainers.
- `references/quality-rules.md` - Public-safe quality rules.
- `scripts/check_fable5_design_prompt.py` - Validates generated prompt documents.
- `templates/fable5-design-prompt.md` - Template for the full prompt document.
- `templates/launch-prompt.md` - Template for the short launch prompt.

**中文：**

- `SKILL.md` - 技能定义和工作流。
- `agents/openai.yaml` - 代理 UI 元数据，在支持时使用。
- `evals/trigger_cases.json` - 给维护者的路由示例。
- `references/quality-rules.md` - 公共安全质量规则。
- `scripts/check_fable5_design_prompt.py` - 验证生成的提示文档。
- `templates/fable5-design-prompt.md` - 完整提示文档模板。
- `templates/launch-prompt.md` - 简短启动提示模板。

## Validation / 验证

**English:**
After generating a prompt document, run the checker:

```bash
python3 fable5-design-doc/scripts/check_fable5_design_prompt.py path/to/prompt-doc.md
```

The checker fails when required sections are missing or template placeholders remain unresolved. Fix every issue before using the prompt.

**中文：**
生成提示文档后，运行检查器：

```bash
python3 fable5-design-doc/scripts/check_fable5_design_prompt.py path/to/prompt-doc.md
```

当必需章节缺失或模板占位符未替换时，检查器会失败。使用提示词前请修复所有问题。

## Public Safety Boundary / 公共安全边界

**English:**
This skill is public-safe by default. It does not encode:

- Private paths, repository names, or file locations.
- Personal workflow preferences or credentials.
- Organization-specific rules or customer data.
- Any information that would compromise privacy or security.

Generated prompt documents are also public-safe unless the user explicitly requests a private prompt pack.

**中文：**
此技能默认公共安全。它不包含：

- 私有路径、仓库名称或文件位置。
- 个人工作流偏好或凭据。
- 组织特定规则或客户数据。
- 任何会损害隐私或安全的信息。

除非用户明确要求私有提示词包，否则生成的提示文档也应保持公共安全。

## License / 许可证

MIT
