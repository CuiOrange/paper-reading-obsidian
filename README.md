# Paper Reading Obsidian

将指定论文收录到 Zotero 的适当分类，通过 ZotLit 创建 Obsidian 文献笔记，再生成有原文定位、公式推导和带注释代码的中文精读内容。

## 安装

仓库根目录就是技能目录。发布到 GitHub 后，支持技能安装器的客户端可直接接收仓库链接。也可把完整目录复制到客户端的技能目录；例如 Codex 的 `~/.codex/skills/paper-reading-obsidian`，或 Claude Code 的 `~/.claude/skills/paper-reading-obsidian`。目录中应直接包含 `SKILL.md`。

本地维护时可创建符号链接，避免两份文件漂移：

```bash
ln -s /absolute/path/to/paper-reading-obsidian ~/.codex/skills/paper-reading-obsidian
```

目标已存在时先检查，不覆盖原技能。安装后在下一轮对话查看是否已发现技能；未发现时重新开启会话。

## 依赖和能力

- Obsidian 桌面版、Zotero，以及 ZotLit 插件。
- 模板资源按已检查的 ZotLit 2.1.4 文件式 Liquid 接口编写；其他版本先检查其实际模板或 profile 格式。
- 自动收录需要实际可用的 Zotero 写入接口或 UI 操作能力；ZotLit 创建笔记也需要可调用的真实操作。技能本身不会提供这些连接。
- 检查脚本只需要 Python 3.10+ 标准库；全文提取按环境选用 PyMuPDF、现有转换器或 PDF 工具。
- 已安装 `anti-defensive-writing`、`shuorenhua` 时读取并遵循；没有时使用包内的基本写作规范。

安装技能不会替换现有模板、启用 CSS、修改主题或改动文库。首次配置时确定目标文库、vault、模板位置、论文笔记目录、分类映射和待分类位置，再验证一次真实的创建及更新流程。

## 使用

```text
使用 $paper-reading-obsidian 收录并精读这篇论文：https://arxiv.org/abs/...

继续完善这篇论文的笔记，重点补全损失函数与作者代码的对应关系。

只解释笔记中的定理 2，保留我的其他内容。
```

默认写中文。Obsidian 文件中的公式使用 `$...$` 和 `$$...$$`；聊天中的公式遵循用户指令。论文主线、完整证明和代码分层组织，长内容可折叠。作者论断、补充推导和个人思考分别标明。

## 目录

- `SKILL.md`：流程入口与关键约束。
- `references/setup.md`：环境发现、接口和模板安装。
- `references/reading-guide.md`：精读、数学、实验和代码讲解。
- `references/writing-guide.md`：清晰表达与两个写作技能的调用规则。
- `references/note-contract.md`：笔记身份、内容区域、恢复状态与展示规范。
- `assets/zotlit/`：可选 Liquid 模板；安装到 vault 前适配并预览。
- `assets/paper-note.css`：仅作用于 `paper-reading` 类的可选样式。
- `scripts/validate_note.py`：只读结构检查，不能判断论文理解是否正确。

## 检查笔记

```bash
python3 scripts/validate_note.py /absolute/path/to/note.md --vault /absolute/path/to/vault
```

脚本检查区域标记、必要身份、围栏闭合、模板残留及本地嵌入目标。它不完整解析 YAML/LaTeX，不模拟 ZotLit，也不代替 Obsidian 渲染和原文核验。

## 发布

此目录可以作为独立 Git 仓库发布。提交提示词、模板与检查器即可，个人路径配置、凭据、论文 PDF 和私人笔记不进入技能仓库。Zotero/ZotLit 的实际接口因环境而异，应分别记录已经验证和仍待接通的能力。

精读设计参考 [cswjl/paper-explainer](https://github.com/cswjl/paper-explainer)。本项目将其完整覆盖、减少重复、保留核验依据等思路改为 Zotero + Obsidian 流程；不包含其 XeLaTeX 模板或执行脚本。出处与许可见 `THIRD_PARTY_NOTICES.md`。
