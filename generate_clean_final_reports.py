#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates standalone, publication-ready Minor Research Reports (CN & EN)
in both Markdown (.md) and Word (.docx) formats.
Zero meta-commentary, zero mention of previous drafts or revision logs.
Pure finished academic research proposal & survey design.
"""

import os
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = "/Users/xwq123456/.gemini/antigravity/scratch/durian-experiment"
DESKTOP_SUBDIR = "/Users/xwq123456/Desktop/副课题"

PUBLIC_URL = "https://ratio-employ-boston-zone.trycloudflare.com"
ADMIN_URL = f"{PUBLIC_URL}/admin"

# ==============================================================================
# 1. STANDALONE ACADEMIC MARKDOWN CONTENT (CN & EN)
# ==============================================================================

def get_cn_markdown():
    return f"""# 数据驱动型 AI 与不可言传的专家直觉：人机决策冲突中的置信度诱导与结果归因研究
## 副课题研究计划与实验问卷设计方案

---

### 基本信息
- **研究题目**：数据驱动型 AI 与不可言传的专家直觉：人机决策冲突中的置信度诱导与结果归因研究
- **英文题目**：*Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts*
- **研究者**：修 天源 (XIU TIANYUAN)，北陆先端科学技术大学院大学 (JAIST) 知识科学研究科 博士前期课程二年级 (M2)
- **指导教授**：水本 教授 (Prof. Mizumoto)
- **日期**：2026年10月18日
- **研究领域**：知识科学 (Knowledge Science)、实验哲学 (Experimental Philosophy)、人机交互 (HCI)、认知心理学 (Cognitive Psychology)

---

## 1. 研究背景与核心理论框架 (Background & Theoretical Framework)

### 1.1 数据驱动型 AI 与量化置信度权威
当代人工智能系统（尤其是深度学习计算机视觉模型）并非依赖人工编写的显性逻辑或几何规则算法（Explicit Rule-Based Algorithms），而是通过在百万级乃至千万级海量数据集（Massive Datasets）上进行高维统计拟合来习得复杂的特征表征。在面向人类终端用户提供辅助决策时，这类端到端的“黑盒（Black-Box）”模型通常无法直接向用户展示其内部数以亿计的参数权重，而是输出一个高度精炼的标量指标——**预测置信度评分（Confidence Score，例如 94.8% 或 58.2%）**。

在人机交互（HCI）与认知心理学视域下，“海量数据训练背景”与“高精度置信度百分比”的结合极易在决策者心中构建起强大的客观性光环与技术权威，进而诱发**自动化偏差（Automation Bias）**——即人类决策者倾向于盲目顺从高置信度的数据模型预测，而放弃独立判断或忽视其他质性信息源。

### 1.2 波兰尼的不可言传隐性知识 (Ineffable Tacit Knowledge)
与数据驱动型 AI 形成鲜明对照的是人类专家在长期具身实践中积累的经验智慧。在知识科学（Knowledge Science）与认识论（Epistemology）的奠基性理论中，迈克尔·波兰尼（Michael Polanyi, 1966）提出了著名论断：“**我们知道的多于我们能言说的（We can know more than we can tell）**”。

在复杂的现实物理世界判别任务（如传统工艺品鉴定、临床触诊、农产品品质甄别）中，资深人类专家往往依靠多模态感官整合与整体完形感知（Gestalt Perception）在瞬间做出精准判断。这种高阶专家直觉的核心本体论特征在于其**不可言传性（Ineffability）**——专家虽然能够凭借十余年经手数万次样本所沉淀的“手感”与“直觉”做出可靠决策，但往往无法用显性的语言规则或数学公式向门外汉解释其判断依据。事实上，任何能够被轻易提炼为显性口诀或形式化规则的经验，均已转化为显性知识（Explicit Knowledge）；唯有无法被语言编码的具身直觉，才构成知识科学中最具探讨价值的隐性知识内核。

### 1.3 核心研究问题 (Research Questions)
当“无法用语言解释理由的资深人类专家直觉”与“具备海量数据背书且附带量化置信度的深度学习 AI”在现实决策中给出完全相反的建议时，人类决策者将如何权衡？当最终的物理真相揭晓后，决策者又将如何对失败的一方进行认知归因？本研究结合实验哲学（Experimental Philosophy）与认知科学方法，聚焦以下三个核心研究问题：

- **RQ1（置信度诱导与初始信任分配）**：在不知晓最终真实结果的前提下，面对无法言传逻辑的专家直觉与数据驱动型 AI 的正面冲突，AI 所展示的置信度水平（高置信度 94.8% vs. 低置信度 58.2%）如何调控决策者的选择偏好与数据客观性感知？
- **RQ2（错误归因与法兰克福式“胡扯”投射）**：当客观结果揭晓且 AI 预测彻底失败时，受试者是倾向于理性的“概率与统计局限归因”，还是会从认识论与实验哲学层面产生意图投射，认为 AI 毫无真正理解、仅在利用数字进行哈里·法兰克福（Harry Frankfurt, 2005）意义上的**“胡扯 / 不懂装懂（Bullshitting）”**甚至欺骗？
- **RQ3（高置信度失败的背叛惩罚效应）**：AI 事前展示的置信度高低与事后开壳结果的成败之间是否存在显著交互作用？具体而言，“高置信度下的彻底失败”是否会触发非线性的信任崩塌与认知反噬（The Penalty of Overconfidence），并促使决策者重新审视人类不可言传隐性知识的独特价值？

---

## 2. 实验任务载体与方法论依据 (Task Scenario & Methodological Justification)

### 2.1 实验情境载体的科学合理性：未开壳榴莲果肉饱满度鉴别
本研究选取“挑选未开壳榴莲（判断内部果肉房数与饱满度）”作为实验情境载体，具备坚实的自然科学依据与生态效度：

1. **客观的植物解剖学规律**：榴莲（*Durio zibethinus*）属锦葵科蒴果，正常发育的果室（心皮）膨大会顶起外壳形成轮廓鼓包。然而，自然界中存在营养被厚重果壳过度吸收、外表极其浑圆对称但内部心皮完全败育的畸形“空壳死包果”。因此，外观判别绝非随机猜硬币，而是存在客观规律但极具挑战性的复杂物理鉴别任务。
2. **典型的人机认知机制对立**：
   - **资深人类店长（不可言传的具身隐性知识）**：依赖 15 年经手数万颗果实的整体直觉与手感，综合视觉、果柄韧度、重量分布等不可言传的暗默感知来排除空心果，但无法用固定规则向顾客口头解释。
   - **深度学习视觉 AI（高维图像统计拟合）**：基于超过 100 万张真实“榴莲外观—开壳结果”配对图像数据集进行端到端训练。在面对外壳高度对称浑圆的“空壳死包果”时，纯视觉模型可能因局部几何特征的统计相关性而输出极高的预测置信度（94.8%），从而产生典型的数据过拟合误判。
3. **黑白分明的客观真实反馈**：果实一旦当场切开，内部是“满 5 房黄金果肉”还是“空心死包”一目了然，不存在主观解释的模糊地带，为结果揭晓后的归因测量提供了严密的客观基准。

### 2.2 实验哲学情境实验范式 (Vignette Experiment Paradigm)
本研究采用实验哲学与行为决策领域标准的**组间情境实验范式（Between-Subjects Vignette Experiment）**。受试者直接以买家的第一人称视角进入“店长直觉与 AI 预测发生冲突”的决策情境，在做出购买选择并完成前测认知评估后，立即在下一阶段获知现场切开果实的真实结果，进而完成错误归因与后测信任评估。该范式有效排除了受试者先验盲猜所带来的自我一致性偏差（Self-Consistency Bias），确保了自变量操纵的纯净度与内部效度。

---

## 3. $2 \\times 2$ 组间析因实验设计 ($2 \\times 2$ Between-Subjects Experimental Design)

### 3.1 自变量与因变量定义
本研究采用 $2 \\times 2$ 组间析因设计（Between-Subjects Factorial Design），包含两个正交操纵的自变量（Independent Variables）：

- **自变量 1：AI 预测置信度 (AI Confidence Level)**
  - **高置信度水平 (High Confidence)**：AI 终端输出预测置信度为 **94.8%**；
  - **低置信度水平 (Low Confidence)**：AI 终端输出预测置信度为 **58.2%**。
- **自变量 2：开壳真实结果 (Realized Outcome)**
  - **AI 失败 / 店长正确 (AI Fails / Manager Correct)**：切开后，店长推荐的 A 号果肉极其饱满（满 5 房），AI 推荐的 B 号为空壳死包；
  - **AI 成功 / 店长失误 (AI Succeeds / Manager Fails)**：切开后，AI 推荐的 B 号果肉极其饱满（满 5 房），店长推荐的 A 号为空壳死包。

- **因变量指标体系 (Dependent Variables)**：
  - **前测指标（阶段一）**：二元购买决策选择（Q1）、数据客观性感知（Q2）、置信度锚定效应（Q3）、对不可言传经验的怀疑度（Q4）。
  - **后测指标（阶段二）**：概率与统计局限归因（Q5）、法兰克福式“胡扯（Bullshitting）”归因（Q6）、误导与受骗感投射（Q7）、隐性知识价值重估（Q8）、未来自动化偏差留存倾向（Q9）。

### 3.2 $2 \\times 2$ 实验分组矩阵表

受试者访问在线实验平台时，系统后台通过随机算法将其均等分配至以下 4 个独立实验组之一：

| 实验组别 | 自变量 1：AI 置信度 | 自变量 2：开壳真实结果 | 阶段一：人机冲突刺激呈现 | 阶段二：现场开壳结果揭晓 |
| :--- | :--- | :--- | :--- | :--- |
| **Condition 1** | **高置信度 (94.8%)** | **AI 失败 (店长正确)** | 店长凭15年直觉推荐 A；AI 以 94.8% 高置信度推荐 B | A号满5房饱满果肉，B号空壳死包（店长完胜，AI失败） |
| **Condition 2** | **低置信度 (58.2%)** | **AI 失败 (店长正确)** | 店长凭15年直觉推荐 A；AI 以 58.2% 低置信度推荐 B | A号满5房饱满果肉，B号空壳死包（店长完胜，AI失败） |
| **Condition 3** | **高置信度 (94.8%)** | **AI 成功 (店长失误)** | 店长凭15年直觉推荐 A；AI 以 94.8% 高置信度推荐 B | B号满5房饱满果肉，A号空壳死包（AI完胜，店长失误） |
| **Condition 4** | **低置信度 (58.2%)** | **AI 成功 (店长失误)** | 店长凭15年直觉推荐 A；AI 以 58.2% 低置信度推荐 B | B号满5房饱满果肉，A号空壳死包（AI成功，店长失误） |

---

## 4. 实验问卷完整题项与量表设计 (Complete Survey Instrument)

在线问卷系统采用单向递进式分阶段控制（禁止浏览器后退修改前序答案），以确保前测与后测的严格时序因果效度。

### 第一阶段：人机冲突情境与前测决策评估 (Stage 1: Decision Conflict & Pre-Outcome Evaluation)

> **【情境导入】**  
> 假设您正在水果店挑选榴莲，面前有两颗外观完好、价格相同的榴莲（**样品 A 号** 与 **样品 B 号**）。为了挑出内部果肉最饱满的一颗，您同时咨询了拥有 15 年经验的资深店长和店内配置的深度学习视觉 AI 系统，但双方给出了完全相反的建议：
>
> - **👨‍🌾 资深店长的判断 —— 【推荐 A 号】**  
>   *背景：拥有 15 年从业经验，累计经手挑选数万颗榴莲。*  
>   **店长原话**：“我也没法用语言跟你说清楚具体看哪里，挑榴莲没有死规矩，就是我干了 15 年、摸过几万颗榴莲攒下来的直觉与手感，A 号肯定肉多。”
>
> - **🤖 深度学习视觉 AI 系统的判断 —— 【推荐 B 号】**  
>   *背景：基于超过 100 万张真实“榴莲外观—开壳结果”配对图像数据集进行深度学习训练（无人工编写规则）。*  
>   **系统屏幕显示**：“模型预测结果：推荐 B 号（预测置信度 Confidence Score：**94.8%** *[或 58.2%]*）”

#### 1. 行为决策题项
- **Q1.【二元决策选择】** 面对无法解释具体理由的店长直觉，以及基于海量数据训练的 AI 预测，此时您决定购买哪一颗？
  - [ ] **选择 A 号**（跟随资深店长的经验直觉）
  - [ ] **选择 B 号**（跟随数据驱动型 AI 系统的预测）

#### 2. 决策前认知评估量表（7 级李克特量表：1 = 完全不同意，4 = 中立，7 = 完全同意）
- **Q2（数据客观性感知 / Perceived Data Objectivity）**：相比于店长“说不清道不明”的个人直觉，基于百万级图像数据集训练出来的 AI 模型让我觉得更加客观、可靠。
- **Q3（置信度锚定效应 / Confidence Score Impact）**：AI 系统给出的具体置信度百分比（94.8% / 58.2%），对我刚才做出选择起到了决定性的引导作用。
- **Q4（对不可言传经验的怀疑 / Skepticism Toward Ineffable Intuition）**：如果一位人类专家无法用清晰的语言解释他的判断逻辑，我很难放心把决定权交给他。

---

### 第二阶段：真实结果揭晓与后测归因量表 (Stage 2: Outcome Revelation & Post-Outcome Attribution)

> **【现场开壳验证结果】**
> - **若受试者处于 Condition 1 或 Condition 2（AI 失败 / 店长正确）**：  
>   工作人员当场切开了两颗榴莲：**店长推荐的 A 号果肉极其饱满（满 5 房黄金果肉）；而 AI 推荐的 B 号果壳极厚，内部大部分是未发育的空壳（死包）。最终结果证明：店长的直觉判断完全正确，AI 预测失败！**
> - **若受试者处于 Condition 3 或 Condition 4（AI 成功 / 店长失误）**：  
>   工作人员当场切开了两颗榴莲：**AI 推荐的 B 号果肉极其饱满（满 5 房黄金果肉）；而店长推荐的 A 号果壳极厚，内部大部分是未发育的空壳（死包）。最终结果证明：AI 模型的预测完全正确，店长的直觉判断失误！**

#### 后测归因与信任重构量表（7 级李克特量表：1 = 完全不同意，4 = 中立，7 = 完全同意）
- **Q5（概率与统计局限归因 — 理性技术维度）**：无论是依赖大数据 AI 还是人类经验直觉，挑选天然水果本质上都存在概率上的不确定性；失败的一方只是这次恰好遇到了统计分布之外的极端例外情况，情有可原。
- **Q6（“胡扯 / 不懂装懂”归因 — 实验哲学 Bullshitting 维度）**：回顾 AI 刚才给出的预测和置信度（94.8% / 58.2%），我认为 AI 根本没有真正“理解”什么是好榴莲，它只是在用数字进行一种“盲目的胡扯（Bullshitting）”或虚张声势。
- **Q7（误导与受骗感 — 拟人化意图投射维度）**：我觉得 AI 系统展示出的“百万级数据集背景”和“精确到小数点后的百分比”具有误导性，甚至让我产生了一种被这套技术表象“操控或欺骗”的感觉。
- **Q8（隐性知识价值重估 — 知识科学维度）**：看到这个结果后，我认为在复杂的现实物理任务中，人类专家难以言传的“经验直觉（隐性知识）”具有独特价值，数据模型无法轻易取代。
- **Q9（未来自动化偏差留存 — 远期信任倾向）**：如果下次面对类似的现实物品鉴别任务，我依然更愿意依赖数据驱动型 AI 的预测，而不是人类行家无法言传的直觉。

---

### 第三阶段：受试者人口学与控制变量 (Stage 3: Demographics & Control Variables)

- **Q10. 您的性别**：[ 男 / 女 / 其他或不愿透露 ]
- **Q11. 您的年龄区间**：[ 20岁以下 / 20–29岁 / 30–39岁 / 40–49岁 / 50岁及以上 ]
- **Q12. 您的学科专业背景**：[ 是（理工科 STEM / 计算机 / 数据科学 / AI 相关专业） / 否（人文社科 / 商科 / 艺术 / 其他非理工专业） ]
- **Q13. 您在日常学习或工作中使用 AI 工具（如 ChatGPT、Claude 等）的频率**：[ 几乎不用 / 每周 1–2 次 / 几乎每天使用 / 重度深度依赖 ]

---

## 5. 统计假设与数据分析方案 (Statistical Hypotheses & Analysis Plan)

### 5.1 核心统计假设 (Research Hypotheses)
- **假设 1（H1：置信度主效应 — 决策诱导）**：在结果揭晓前的阶段一，高置信度组（Condition 1 & 3，94.8%）受试者选择跟随 AI（选 B）的比例，以及在数据客观性感知（Q2）与置信度引导效应（Q3）上的得分，将显著高于低置信度组（Condition 2 & 4，58.2%）（$p < .001$）。
- **假设 2（H2：真实结果主效应 — 哲学归因与隐性知识重估）**：在阶段二结果揭晓后，AI 失败组（Condition 1 & 2）受试者在法兰克福式“胡扯（Bullshitting）”归因（Q6）、受骗感投射（Q7）以及隐性知识价值重估（Q8）上的得分，将显著高于 AI 成功组（Condition 3 & 4）（$p < .001$）。
- **假设 3（H3：置信度 $\\times$ 结果交互效应 — “高置信度失败的背叛惩罚”）**：AI 置信度与开壳真实结果在“胡扯归因”（Q6）、“受骗感”（Q7）及“未来信任留存”（Q9）上存在显著的二阶交互作用（Two-Way Interaction，$p < .01$）。具体而言，当 AI 以 94.8% 的极高置信度做出预测却彻底失败时（Condition 1），将触发强烈的认识论背叛感，其引发的“胡扯”斥责与信任崩塌幅度将显著大于低置信度失败组（Condition 2）。

### 5.2 统计检验模型 (Statistical Models)
1. **二元选择模型（针对 Q1）**：采用卡方独立性检验（$\\chi^2$ Test）与二元 Logistic 回归模型，估计 AI 置信度水平对受试者顺从 AI 概率的优势比（Odds Ratio）：
   $$\\text{{logit}}(P(\\text{{Choice}} = \\text{{AI}})) = \\beta_0 + \\beta_1 \\cdot \\text{{Confidence}} + \\beta_2 \\cdot \\text{{STEM}} + \\beta_3 \\cdot \\text{{AIFreq}}$$
2. **双因素方差分析模型（针对 Q2–Q9）**：采用 $2 \\times 2$ 组间双因素方差分析（Two-Way Factorial ANOVA）检验主效应与交互效应，并计算偏 Eta 方（Partial $\\eta_p^2$）作为效应量指标：
   $$Y_{{ijk}} = \\mu + \\alpha_i (\\text{{Confidence}}_i) + \\beta_j (\\text{{Outcome}}_j) + (\\alpha\\beta)_{{ij}} (\\text{{Confidence}}_i \\times \\text{{Outcome}}_j) + \\epsilon_{{ijk}}$$
3. **简单效应分析与协方差控制（Simple Effects & ANCOVA）**：若交互项 $(\\alpha\\beta)_{{ij}}$ 显著，进一步执行 Bonferroni 校正的简单效应检验（重点对比 Condition 1 vs. Condition 2），并将理工科背景（Q12）与 AI 使用频率（Q13）纳入协方差分析（ANCOVA），检验技术素养是否对“高置信度诱导”起到认知缓冲作用。

---

## 6. 在线实验系统架构与访问入口 (Online Experimental System & Access Links)

本研究所配套的在线交互式实验平台已开发部署完毕，支持跨平台响应式访问与实时统计监测：

### 6.1 核心技术特性
- **多语言无缝切换（EN / JA / ZH）**：界面默认采用国际学术英语（English），右上角内置语言切换器，支持一键实时切换为日语（日本語）与中文，满足跨文化被试群体施测需求。
- **实验组别随机化与快捷预览**：受试者访问主链接时由系统自动均衡随机分配至 Condition 1–4；同时界面顶部设有 `[C1 | C2 | C3 | C4]` 组别切换栏，供研究者与审阅导师一键切换预览全部 4 种实验情境。
- **毫秒级行为反应时记录**：系统自动记录受试者在阶段一、阶段二、阶段三的停留与决策反应时（`stage1Ms`, `stage2Ms`, `stage3Ms`），用于数据质量控制与认知加工深度分析。
- **实时统计看板与导出**：导师管理后台实时渲染 $2 \\times 2$ 各组样本量、AI 选择率及 Q2–Q9 均值矩阵，支持一键导出标准 UTF-8 BOM 编码的 `.csv` 原始数据集，可直接导入 SPSS、R 或 Python 进行统计建模。

### 6.2 在线系统访问链接
- **受试者问卷系统主链接**：[{PUBLIC_URL}]({PUBLIC_URL})
- **研究者与导师管理后台**：[{ADMIN_URL}]({ADMIN_URL})
- **四组实验条件独立直达链接**：
  - Condition 1 (94.8% × AI 失败)：[{PUBLIC_URL}/?condition=1]({PUBLIC_URL}/?condition=1)
  - Condition 2 (58.2% × AI 失败)：[{PUBLIC_URL}/?condition=2]({PUBLIC_URL}/?condition=2)
  - Condition 3 (94.8% × AI 成功)：[{PUBLIC_URL}/?condition=3]({PUBLIC_URL}/?condition=3)
  - Condition 4 (58.2% × AI 成功)：[{PUBLIC_URL}/?condition=4]({PUBLIC_URL}/?condition=4)
"""


def get_en_markdown():
    return f"""# Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts
## Minor Research Project Proposal & Experimental Survey Design

---

### Project Metadata
- **Research Title**: *Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts*
- **Japanese / Chinese Title**: データ駆動型AIと暗黙的直観の対立 / 数据驱动型 AI 与不可言传的专家直觉
- **Researcher**: XIU TIANYUAN (修 天源), Master's Program (M2), School of Knowledge Science, Japan Advanced Institute of Science and Technology (JAIST)
- **Academic Advisor**: Prof. Mizumoto (水本 教授)
- **Date**: October 18, 2026
- **Research Domains**: Knowledge Science, Experimental Philosophy, Human-Computer Interaction (HCI), Cognitive Psychology

---

## 1. Background & Theoretical Framework

### 1.1 Data-Driven AI and Quantitative Confidence Authority
Contemporary artificial intelligence systems—particularly deep learning computer vision models—do not operate via hand-coded, explicit logical or geometric algorithms. Instead, they learn high-dimensional statistical representations by fitting massive datasets comprising millions of paired instances. When deployed to assist human decision-makers, these opaque "black-box" neural networks cannot meaningfully expose billions of internal synaptic weights to the end user; instead, they communicate certainty through a single scalar metric: a **Confidence Score (e.g., 94.8% vs. 58.2%)**.

From the perspective of Human-Computer Interaction (HCI) and cognitive psychology, the combination of "massive dataset training" and a "hyper-precise confidence percentage" constructs a powerful aura of algorithmic objectivity. This representation frequently induces **Automation Bias**—the cognitive propensity for humans to uncritically defer to high-confidence automated predictions while discounting competing qualitative evidence.

### 1.2 Polanyi's Ineffable Tacit Knowledge
Standing in sharp epistemic contrast to data-driven AI is the embodied expertise of seasoned human practitioners. In the foundational literature of Knowledge Science and Epistemology, Michael Polanyi (1966) formulated the classic maxim: **"We can know more than we can tell."**

In complex physical-world diagnostic tasks—such as artisan appraisal, clinical palpation, or agricultural sorting—veteran human experts rely on multimodal sensory integration and holistic Gestalt perception to reach rapid, highly accurate judgments. The defining ontological hallmark of such high-level expertise is its **ineffability**: while a master practitioner can reliably identify the superior specimen through somatic "touch" and "gut intuition" honed over tens of thousands of cases, they cannot articulate their decision criteria into explicit verbal rules or mathematical formulas for a layperson. Indeed, any rule that can be explicitly verbalized is already codifiable explicit knowledge; genuine tacit knowledge remains inherently uncodifiable.

### 1.3 Core Research Questions
When a human expert's unexplainable tacit intuition directly conflicts with a data-driven AI's statistical prediction, how do human decision-makers resolve the conflict? Furthermore, once the physical ground truth is revealed, how do people attribute blame or credit? Integrating frameworks from Experimental Philosophy and Knowledge Science, this study investigates three primary research questions:

- **RQ1 (Confidence Inducement & Initial Trust Allocation)**: Prior to knowing the actual outcome, when confronted with a direct conflict between ineffable human intuition and a data-driven AI model, how does the AI's displayed confidence score (High: 94.8% vs. Low: 58.2%) influence behavioral compliance and perceived epistemic objectivity?
- **RQ2 (Error Attribution & Frankfurtian "Bullshitting")**: Upon witnessing the AI prediction fail completely in physical verification, do participants attribute the failure rationally to probabilistic/statistical limitations, or do they project epistemic blame—perceiving the AI as having no genuine understanding and engaging in philosophical **"Bullshitting"** (Frankfurt, 2005) and deceptive manipulation?
- **RQ3 (The Penalty of Overconfidence & Tacit Knowledge Re-evaluation)**: Is there a significant interaction between pre-decision AI confidence and post-decision outcome? Specifically, does a high-confidence AI failure trigger a nonlinear collapse in trust ("The Penalty of Overconfidence") and compel decision-makers to re-evaluate the irreplaceable value of human tacit knowledge?

---

## 2. Task Scenario & Methodological Justification

### 2.1 Scientific Validity of the Task: Un-opened Durian Pulp Assessment
This study employs the real-world physical task of **selecting an un-opened durian fruit for internal pulp fullness** as its experimental scenario, offering strong botanical and cognitive validity:

1. **Objective Botanical Morphology**: Durian (*Durio zibethinus*) is a capsular fruit in which internal carpel development expands the outer rind. However, physiological "hollow-shell (dead-pod)" anomalies frequently occur, where nutrients are absorbed entirely into a thick, outwardly symmetrical rind while internal chambers abort. Assessing internal fullness is therefore a non-random, high-uncertainty physical diagnostic task.
2. **Natural Divergence of Human vs. AI Modalities**:
   - **Veteran Store Manager (Ineffable Tacit Knowledge)**: Relies on 15 years of somatic experience handling tens of thousands of fruits. By integrating subtle mass distribution, spine resilience, and holistic visual Gestalt, the expert detects hollow shells intuitively, even though he cannot verbally explain fixed rules to customers.
   - **Deep Learning Visual AI (Statistical Pattern Fitting)**: Trained end-to-end on a dataset of over 1,000,000 real "outer appearance vs. cut-open outcome" paired images. When scanning a superficially round and symmetrical hollow-shell fruit, the vision model is susceptible to statistical overfitting on surface regularity, outputting an erroneously high confidence score (94.8%).
3. **Unambiguous Ground-Truth Verification**: Slicing the fruit open on-site yields immediate, indisputable binary feedback (5 full golden chambers vs. hollow undeveloped shell), providing a clean benchmark for post-outcome attribution.

### 2.2 Experimental Philosophy Vignette Paradigm
The study adopts the standard **Between-Subjects Vignette Experiment Paradigm** widely utilized in experimental philosophy and behavioral decision research. Participants enter the scenario directly as a decision-making buyer facing conflicting recommendations from the veteran manager and the visual AI system. After recording their binary choice and pre-outcome cognitive evaluations in Stage 1, participants observe the immediate on-site cut-open verification in Stage 2 and complete the attribution and trust scales. This streamlined structure cleanly isolates the causal effects of AI confidence and outcome validity without prior guessing confounders.

---

## 3. $2 \\times 2$ Between-Subjects Experimental Design

### 3.1 Independent and Dependent Variables
The experiment employs a $2 \\times 2$ between-subjects factorial design manipulating two orthogonal independent variables:

- **Factor 1: AI Confidence Level (Between-Subjects, 2 Levels)**
  - **High Confidence**: The AI terminal displays a confidence score of **94.8%**;
  - **Low Confidence**: The AI terminal displays a confidence score of **58.2%**.
- **Factor 2: Realized Physical Outcome (Between-Subjects, 2 Levels)**
  - **AI Fails / Manager Correct**: On-site slicing reveals Durian A (recommended by the manager) is packed with 5 full chambers of pulp, whereas Durian B (recommended by the AI) is a hollow dead-pod fruit;
  - **AI Succeeds / Manager Fails**: On-site slicing reveals Durian B (recommended by the AI) is packed with 5 full chambers of pulp, whereas Durian A (recommended by the manager) is a hollow dead-pod fruit.

- **Dependent Variables**:
  - **Stage 1 (Pre-Outcome)**: Binary choice rate (Q1), Perceived Data Objectivity (Q2), Confidence Score Anchoring (Q3), and Skepticism Toward Ineffable Intuition (Q4).
  - **Stage 2 (Post-Outcome)**: Probabilistic Limitation Attribution (Q5), Frankfurtian "Bullshitting" Attribution (Q6), Perceived Deception & Manipulation (Q7), Re-evaluation of Tacit Knowledge (Q8), and Future Automation Bias Retention (Q9).

### 3.2 $2 \\times 2$ Factorial Condition Matrix

Upon accessing the platform, participants are randomly assigned with equal probability to one of the four experimental conditions:

| Condition | Factor 1: AI Confidence | Factor 2: Realized Outcome | Stage 1: Conflict Stimulus Presentation | Stage 2: On-Site Cut-Open Outcome |
| :--- | :--- | :--- | :--- | :--- |
| **Condition 1** | **High Confidence (94.8%)** | **AI Fails (Manager Wins)** | Manager intuitively recommends A; AI recommends B with 94.8% confidence | Durian A is full (5 chambers); Durian B is hollow dead-pod (Manager wins, AI fails) |
| **Condition 2** | **Low Confidence (58.2%)** | **AI Fails (Manager Wins)** | Manager intuitively recommends A; AI recommends B with 58.2% confidence | Durian A is full (5 chambers); Durian B is hollow dead-pod (Manager wins, AI fails) |
| **Condition 3** | **High Confidence (94.8%)** | **AI Succeeds (Manager Fails)** | Manager intuitively recommends A; AI recommends B with 94.8% confidence | Durian B is full (5 chambers); Durian A is hollow dead-pod (AI wins, Manager fails) |
| **Condition 4** | **Low Confidence (58.2%)** | **AI Succeeds (Manager Fails)** | Manager intuitively recommends A; AI recommends B with 58.2% confidence | Durian B is full (5 chambers); Durian A is hollow dead-pod (AI wins, Manager fails) |

---

## 4. Complete Survey Instrument & Measurement Scales

The online questionnaire enforces strict forward-only progression across three sequential stages to preserve temporal validity.

### Stage 1: The Decision Conflict Scenario & Pre-Outcome Evaluation

> **[Scenario Vignette]**  
> Imagine you are at a fruit market choosing between two un-opened durians (**Durian A** and **Durian B**) of identical price to get the one with the fullest pulp inside. You consult both a veteran store manager (15 years of experience) and a deep-learning visual AI system deployed in the store. They give opposite recommendations:
>
> - **👨‍🌾 Veteran Store Manager's Judgment — [Recommends Durian A]**  
>   *Background: 15 years of professional experience, having handled tens of thousands of durians.*  
>   **Manager's Statement**: *"I honestly can't explain it in words. There is no fixed rule to tell you. It's just a gut feeling and intuition after handling tens of thousands of durians over 15 years. Durian A is definitely fuller."*
>
> - **🤖 Deep Learning Visual AI System's Judgment — [Recommends Durian B]**  
>   *Background: Trained on a massive dataset of 1,000,000+ real paired durian images (outer appearance vs. opened pulp outcome), without hand-coded rules.*  
>   **Terminal Output**: *"Neural Network Output: Recommend Durian B (Confidence Score: **94.8%** [or **58.2%**])"*

#### 1. Behavioral Decision Item
- **Q1. [Binary Choice]** Facing the manager's intuition (which he cannot verbally explain) and the data-driven AI's prediction, which durian do you decide to choose?
  - [ ] **Choose Durian A** (Follow the Veteran Store Manager)
  - [ ] **Choose Durian B** (Follow the Data-Driven AI)

#### 2. Pre-Outcome Cognitive Evaluation Scales (7-Point Likert: 1 = Strongly Disagree, 4 = Neutral, 7 = Strongly Agree)
- **Q2 (Perceived Data Objectivity)**: Compared to the manager’s unexplainable personal intuition, an AI model trained on a massive dataset of over a million images feels more objective and reliable to me.
- **Q3 (Confidence Score Impact)**: The specific confidence percentage displayed by the AI (94.8% / 58.2%) heavily influenced my choice just now.
- **Q4 (Skepticism Toward Ineffable Intuition)**: If a human expert cannot verbally explain the reasoning behind their judgment, I find it difficult to trust their recommendation.

---

### Stage 2: Outcome Revelation & Post-Outcome Attribution Scales

> **[On-Site Cut-Open Verification Results]**
> - **For Condition 1 & Condition 2 (AI Fails / Store Manager Wins)**:  
>   *Both durians are cut open on the spot: **Durian A (recommended by the manager) is packed with 5 large, full chambers of golden pulp. Durian B (recommended by the AI) has a thick shell and is mostly hollow with undeveloped dead chambers inside. The veteran manager's intuition proved completely right, and the AI prediction failed!***
> - **For Condition 3 & Condition 4 (AI Succeeds / Store Manager Fails)**:  
>   *Both durians are cut open on the spot: **Durian B (recommended by the AI) is packed with 5 large, full chambers of golden pulp. Durian A (recommended by the manager) has a thick shell and is mostly hollow with undeveloped dead chambers inside. The AI model's prediction proved completely right, and the manager's intuition failed!***

#### Post-Outcome Attribution & Trust Scales (7-Point Likert: 1 = Strongly Disagree, 4 = Neutral, 7 = Strongly Agree)
- **Q5 (Probabilistic Limitation Attribution — Rational Dimension)**: Whether relying on big-data AI or human intuition, sorting natural fruits always involves probabilistic uncertainty; the side that failed simply encountered an unavoidable statistical outlier.
- **Q6 ("Bullshitting" Attribution — Experimental Philosophy Dimension)**: Looking back at the AI's prediction and confidence score (94.8% / 58.2%), I feel the AI has no genuine grasp of what makes a good durian—it is merely engaging in "bullshitting" (bluffing with numbers without true understanding).
- **Q7 (Perceived Deception & Manipulation — Intentional Projection Dimension)**: I feel the AI’s presentation of "massive dataset training" and a "precise confidence percentage" was misleading, making me feel somewhat manipulated or deceived.
- **Q8 (Re-evaluation of Tacit Knowledge — Knowledge Science Dimension)**: After seeing this outcome, I believe that in complex physical tasks, a human expert’s ineffable intuition (tacit knowledge) holds unique value that dataset-trained AI cannot easily replace.
- **Q9 (Future Automation Bias Retention — Trust Disposition)**: Next time I face a similar real-world judgment task, I would prefer to rely on the data-driven AI rather than a human expert's unexplainable intuition.

---

### Stage 3: Demographic & Control Variables

- **Q10. Gender**: [ Male / Female / Other or Prefer not to say ]
- **Q11. Age Group**: [ Under 20 / 20–29 / 30–39 / 40–49 / 50+ ]
- **Q12. Academic Background**: [ Yes (STEM / Computer Science / Data Science / AI) / No (Humanities / Social Sciences / Business / Arts / Other) ]
- **Q13. Daily AI Tool Usage Frequency (e.g., ChatGPT, Claude)**: [ Rarely / 1–2 times per week / Daily / Heavy reliance ]

---

## 5. Statistical Hypotheses & Data Analysis Plan

### 5.1 Primary Statistical Hypotheses
- **Hypothesis 1 (H1: Main Effect of AI Confidence on Compliance)**: In Stage 1 prior to outcome revelation, participants in the High Confidence conditions (94.8%, Conditions 1 & 3) will exhibit a significantly higher probability of choosing the AI-recommended option (Q1), alongside significantly higher ratings on Perceived Data Objectivity (Q2) and Confidence Impact (Q3), compared to the Low Confidence conditions (58.2%, Conditions 2 & 4) ($p < .001$).
- **Hypothesis 2 (H2: Main Effect of Outcome on Epistemic Attribution)**: In Stage 2, participants exposed to AI Failure (Conditions 1 & 2) will report significantly higher Frankfurtian "Bullshitting" attribution (Q6), Perceived Deception (Q7), and Re-evaluation of Tacit Knowledge (Q8) than participants exposed to AI Success (Conditions 3 & 4) ($p < .001$).
- **Hypothesis 3 (H3: Confidence $\\times$ Outcome Interaction — "The Penalty of Overconfidence")**: There will be a significant two-way interaction between AI Confidence and Realized Outcome on Bullshitting Attribution (Q6), Perceived Deception (Q7), and Future Trust Retention (Q9) ($p < .01$). Specifically, when the AI fails after displaying an overwhelming 94.8% confidence score (Condition 1), the resulting epistemic backlash and collapse in future trust will be disproportionately more severe than when it fails under modest 58.2% confidence (Condition 2).

### 5.2 Statistical Modeling Pipeline
1. **Binary Choice Analysis (Q1)**: Chi-square test of independence ($\\chi^2$) and Binary Logistic Regression estimating the log-odds of selecting the AI option as a function of confidence level and demographic covariates:
   $$\\text{{logit}}(P(\\text{{Choice}} = \\text{{AI}})) = \\beta_0 + \\beta_1 \\cdot \\text{{Confidence}} + \\beta_2 \\cdot \\text{{STEM}} + \\beta_3 \\cdot \\text{{AIFreq}}$$
2. **Two-Way Factorial Analysis of Variance (Q2–Q9)**: Standard $2 \\times 2$ Between-Subjects ANOVA evaluating main effects and the interaction term, reporting partial eta-squared ($\\eta_p^2$) for effect sizes:
   $$Y_{{ijk}} = \\mu + \\alpha_i (\\text{{Confidence}}_i) + \\beta_j (\\text{{Outcome}}_j) + (\\alpha\\beta)_{{ij}} (\\text{{Confidence}}_i \\times \\text{{Outcome}}_j) + \\epsilon_{{ijk}}$$
3. **Simple Effects & Covariate Control (ANCOVA)**: Bonferroni-corrected simple main effects analyses contrasting Condition 1 vs. Condition 2, supplemented by ANCOVA controlling for STEM background (Q12) and AI familiarity (Q13) as cognitive moderators.

---

## 6. Online Experimental System & Live Access Links

A dedicated, full-stack web experimental platform has been engineered and deployed to support cross-platform data collection and real-time supervision:

### 6.1 Key System Capabilities
- **Trilingual Interface (EN / JA / ZH)**: Defaults to English with instant top-right switching to Japanese (日本語) and Chinese (中文) for multi-national participant pools.
- **Automated Randomization & Condition Preview Bar**: Automatically assigns incoming participants across Conditions 1–4, while providing a top-level `[C1 | C2 | C3 | C4]` quick-switcher bar for instant inspection of all four experimental cells.
- **Millisecond Behavioral Telemetry**: Captures stage-specific response latencies (`stage1Ms`, `stage2Ms`, `stage3Ms`) to screen out inattentive satisficing.
- **Real-Time Researcher Dashboard**: Displays live $2 \\times 2$ cell counts, choice ratios, and scale means, with one-click UTF-8 BOM `.csv` export for statistical software.

### 6.2 Live System URLs
- **Participant Survey Entry**: [{PUBLIC_URL}]({PUBLIC_URL})
- **Researcher & Supervisor Admin Portal**: [{ADMIN_URL}]({ADMIN_URL})
- **Direct Condition Preview Links**:
  - Condition 1 (94.8% × AI Fails): [{PUBLIC_URL}/?condition=1]({PUBLIC_URL}/?condition=1)
  - Condition 2 (58.2% × AI Fails): [{PUBLIC_URL}/?condition=2]({PUBLIC_URL}/?condition=2)
  - Condition 3 (94.8% × AI Succeeds): [{PUBLIC_URL}/?condition=3]({PUBLIC_URL}/?condition=3)
  - Condition 4 (58.2% × AI Succeeds): [{PUBLIC_URL}/?condition=4]({PUBLIC_URL}/?condition=4)
"""


# ==============================================================================
# 2. TYPOGRAPHY & DOCX GENERATION HELPERS
# ==============================================================================

def configure_doc_defaults(doc, is_cn=True):
    ascii_font = "Times New Roman"
    eastasia_font = "SimSun" if is_cn else "Times New Roman"
    default_sz = "21"  # 10.5 pt
    
    styles = doc.styles
    for child in styles.element:
        if 'docDefaults' in child.tag:
            rPrDefault = child.find(qn('w:rPrDefault'))
            if rPrDefault is not None:
                rPr = rPrDefault.find(qn('w:rPr'))
                if rPr is not None:
                    rFonts = rPr.find(qn('w:rFonts'))
                    if rFonts is not None:
                        rFonts.set(qn('w:ascii'), ascii_font)
                        rFonts.set(qn('w:hAnsi'), ascii_font)
                        rFonts.set(qn('w:eastAsia'), eastasia_font)
                        rFonts.set(qn('w:cs'), ascii_font)
                    sz = rPr.find(qn('w:sz'))
                    if sz is not None:
                        sz.set(qn('w:val'), default_sz)
                    szCs = rPr.find(qn('w:szCs'))
                    if szCs is not None:
                        szCs.set(qn('w:val'), default_sz)
                        
    normal = styles['Normal']
    normal.font.name = ascii_font
    normal.font.size = Pt(10.5)
    normal_rPr = normal._element.get_or_add_rPr()
    rFonts_elem = parse_xml(
        f'<w:rFonts {nsdecls("w")} w:ascii="{ascii_font}" w:hAnsi="{ascii_font}" '
        f'w:eastAsia="{eastasia_font}" w:cs="{ascii_font}"/>'
    )
    normal_rPr.append(rFonts_elem)

def apply_font_to_run(run, is_cn=True, size_pt=10.5, bold=False, italic=False, color_rgb=(0x1E, 0x29, 0x3B)):
    ascii_font = "Times New Roman"
    eastasia_font = "SimSun" if is_cn else "Times New Roman"
    
    run.font.name = ascii_font
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)
    
    rPr = run._r.get_or_add_rPr()
    
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")}/>')
        rPr.insert(0, rFonts)
    rFonts.set(qn('w:ascii'), ascii_font)
    rFonts.set(qn('w:hAnsi'), ascii_font)
    rFonts.set(qn('w:eastAsia'), eastasia_font)
    rFonts.set(qn('w:cs'), ascii_font)
    
    val = str(int(size_pt * 2))
    sz = rPr.find(qn('w:sz'))
    if sz is None:
        sz = parse_xml(f'<w:sz {nsdecls("w")} w:val="{val}"/>')
        rPr.append(sz)
    else:
        sz.set(qn('w:val'), val)
        
    szCs = rPr.find(qn('w:szCs'))
    if szCs is None:
        szCs = parse_xml(f'<w:szCs {nsdecls("w")} w:val="{val}"/>')
        rPr.append(szCs)
    else:
        szCs.set(qn('w:val'), val)

def set_cell_background(cell, fill_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def add_callout(doc, text_list, is_cn=True, border_color="3B82F6", bg_color="F8FAFC"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=180)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="36" w:space="0" w:color="{border_color}"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    
    for idx, item in enumerate(text_list):
        if idx == 0:
            p = cell.paragraphs[0]
        else:
            p = cell.add_paragraph()
        p.text = ""
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.25
        run = p.add_run(item)
        c_rgb = (0x0F, 0x17, 0x2A) if idx == 0 else (0x1E, 0x29, 0x3B)
        apply_font_to_run(run, is_cn=is_cn, size_pt=10.0, bold=(idx == 0), color_rgb=c_rgb)
        
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def format_academic_table(table, col_widths, headers, data, is_cn=True):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    hdr_cells = table.rows[0].cells
    for i, header_text in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], "1E293B")
        set_cell_margins(hdr_cells[i], top=120, bottom=120, left=140, right=140)
        p = hdr_cells[i].paragraphs[0]
        p.text = ""
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(header_text)
        apply_font_to_run(run, is_cn=is_cn, size_pt=9.5, bold=True, color_rgb=(0xFF, 0xFF, 0xFF))
            
    for r_idx, row_data in enumerate(data):
        row_cells = table.add_row().cells
        bg_color = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, cell_value in enumerate(row_data):
            row_cells[c_idx].width = col_widths[c_idx]
            set_cell_background(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], top=100, bottom=100, left=140, right=140)
            p = row_cells[c_idx].paragraphs[0]
            p.text = ""
            p.paragraph_format.line_spacing = 1.2
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            run = p.add_run(cell_value)
            text_color = (0x0F, 0x17, 0x2A) if c_idx == 0 else (0x33, 0x41, 0x55)
            apply_font_to_run(run, is_cn=is_cn, size_pt=9.5, bold=(c_idx == 0), color_rgb=text_color)


# ==============================================================================
# 3. BUILD STANDALONE CHINESE DOCX
# ==============================================================================

def build_cn_docx():
    doc = docx.Document()
    configure_doc_defaults(doc, is_cn=True)
    
    for sec in doc.sections:
        sec.top_margin = Inches(1.0)
        sec.bottom_margin = Inches(1.0)
        sec.left_margin = Inches(1.0)
        sec.right_margin = Inches(1.0)
        
    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=True, size_pt=16.0, bold=True, color_rgb=(0x0F, 0x17, 0x2A))
        return p

    def add_subtitle(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(14)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=True, size_pt=12.0, bold=True, color_rgb=(0x47, 0x55, 0x69))
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=True, size_pt=13.5, bold=True, color_rgb=(0x0F, 0x17, 0x2A))
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(11)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=True, size_pt=11.5, bold=True, color_rgb=(0x1E, 0x29, 0x3B))
        return p

    def add_body(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.25
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            apply_font_to_run(rb, is_cn=True, size_pt=10.5, bold=True, color_rgb=(0x0F, 0x17, 0x2A))
        r = p.add_run(text)
        apply_font_to_run(r, is_cn=True, size_pt=10.5, bold=False, color_rgb=(0x1E, 0x29, 0x3B))
        return p

    # --- HEADER & METADATA ---
    add_title("数据驱动型 AI 与不可言传的专家直觉：人机决策冲突中的置信度诱导与结果归因研究")
    add_subtitle("副课题研究计划与实验问卷设计方案")
    
    meta_info = [
        "【研究基本信息】",
        "• 中文题目：数据驱动型 AI 与不可言传的专家直觉：人机决策冲突中的置信度诱导与结果归因研究",
        "• 英文题目：Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts",
        "• 研究者：修 天源 (XIU TIANYUAN) — 北陆先端科学技术大学院大学 (JAIST) 知识科学研究科 博士前期课程二年级 (M2)",
        "• 指导教授：水本 教授 (Prof. Mizumoto)",
        "• 提交日期：2026年10月18日",
        "• 研究领域：知识科学 (Knowledge Science)、实验哲学 (Experimental Philosophy)、人机交互 (HCI)、认知心理学 (Cognitive Psychology)"
    ]
    add_callout(doc, meta_info, is_cn=True, border_color="1E293B", bg_color="F8FAFC")

    # --- SECTION 1 ---
    add_h1("1. 研究背景与核心理论框架 (Background & Theoretical Framework)")
    
    add_h2("1.1 数据驱动型 AI 与量化置信度权威")
    add_body(
        "当代人工智能系统（尤其是深度学习计算机视觉模型）并非依赖人工编写的显性逻辑或几何规则算法（Explicit Rule-Based Algorithms），而是通过在百万级乃至千万级海量数据集（Massive Datasets）上进行高维统计拟合来习得复杂的特征表征。在面向人类终端用户提供辅助决策时，这类端到端的“黑盒（Black-Box）”模型通常无法直接向用户展示其内部数以亿计的参数权重，而是输出一个高度精炼的标量指标——预测置信度评分（Confidence Score，例如 94.8% 或 58.2%）。"
    )
    add_body(
        "在人机交互（HCI）与认知心理学视域下，“海量数据训练背景”与“高精度置信度百分比”的结合极易在决策者心中构建起强大的客观性光环与技术权威，进而诱发自动化偏差（Automation Bias）——即人类决策者倾向于顺从高置信度的数据模型预测，而放弃独立判断或忽视其他质性信息源。"
    )

    add_h2("1.2 波兰尼的不可言传隐性知识 (Ineffable Tacit Knowledge)")
    add_body(
        "与数据驱动型 AI 形成鲜明对照的是人类专家在长期具身实践中积累的经验智慧。在知识科学（Knowledge Science）与认识论（Epistemology）的奠基性理论中，迈克尔·波兰尼（Michael Polanyi, 1966）提出了著名论断：“我们知道的多于我们能言说的（We can know more than we can tell）”。"
    )
    add_body(
        "在复杂的现实物理世界判别任务（如传统工艺品鉴定、临床触诊、农产品品质甄别）中，资深人类专家往往依靠多模态感官整合与整体完形感知（Gestalt Perception）在瞬间做出精准判断。这种高阶专家直觉的核心本体论特征在于其不可言传性（Ineffability）——专家虽然能够凭借十余年经手数万次样本所沉淀的“手感”与“直觉”做出可靠决策，但往往无法用显性的语言规则或数学公式向门外汉解释其判断依据。事实上，任何能够被轻易提炼为显性口诀或形式化规则的经验，均已转化为显性知识（Explicit Knowledge）；唯有无法被语言编码的具身直觉，才构成知识科学中最具探讨价值的隐性知识内核。"
    )

    add_h2("1.3 核心研究问题 (Research Questions)")
    add_body(
        "当“无法用语言解释理由的资深人类专家直觉”与“具备海量数据背书且附带量化置信度的深度学习 AI”在现实决策中给出完全相反的建议时，人类决策者将如何权衡？当最终的物理真相揭晓后，决策者又将如何对失败的一方进行认知归因？本研究结合实验哲学与认知科学方法，聚焦以下三个核心研究问题："
    )
    add_body(
        "在不知晓最终真实结果的前提下，面对无法言传逻辑的专家直觉与数据驱动型 AI 的正面冲突，AI 所展示的置信度水平（高置信度 94.8% vs. 低置信度 58.2%）如何调控决策者的选择偏好与数据客观性感知？",
        "• RQ1（置信度诱导与初始信任分配）："
    )
    add_body(
        "当客观结果揭晓且 AI 预测彻底失败时，受试者是倾向于理性的“概率与统计局限归因”，还是会从认识论与实验哲学层面产生意图投射，认为 AI 毫无真正理解、仅在利用数字进行哈里·法兰克福（Harry Frankfurt, 2005）意义上的“胡扯 / 不懂装懂（Bullshitting）”甚至欺骗？",
        "• RQ2（错误归因与法兰克福式“胡扯”投射）："
    )
    add_body(
        "AI 事前展示的置信度高低与事后开壳结果的成败之间是否存在显著交互作用？具体而言，“高置信度下的彻底失败”是否会触发非线性的信任崩塌与认知反噬（The Penalty of Overconfidence），并促使决策者重新审视人类不可言传隐性知识的独特价值？",
        "• RQ3（高置信度失败的背叛惩罚效应）："
    )

    # --- SECTION 2 ---
    add_h1("2. 实验任务载体与方法论依据 (Task Scenario & Methodological Justification)")
    
    add_h2("2.1 实验情境载体的科学合理性：未开壳榴莲果肉饱满度鉴别")
    add_body(
        "本研究选取“挑选未开壳榴莲（判断内部果肉房数与饱满度）”作为实验情境载体，具备坚实的自然科学依据与生态效度："
    )
    add_body(
        "榴莲（Durio zibethinus）属锦葵科蒴果，正常发育的果室（心皮）膨大会顶起外壳形成轮廓鼓包。然而，自然界中存在营养被厚重果壳过度吸收、外表极其浑圆对称但内部心皮完全败育的畸形“空壳死包果”。因此，外观判别绝非随机猜硬币，而是存在客观规律但极具挑战性的复杂物理鉴别任务。",
        "1. 客观的植物解剖学规律："
    )
    add_body(
        "资深人类店长依赖 15 年经手数万颗果实的整体直觉与手感，综合视觉、果柄韧度、重量分布等不可言传的暗默感知来排除空心果，但无法用固定规则向顾客口头解释；而深度学习视觉 AI 基于超过 100 万张真实“榴莲外观—开壳结果”配对图像数据集进行端到端训练，在面对外壳高度对称浑圆的“空壳死包果”时，纯视觉模型可能因局部几何特征的统计相关性而输出极高的预测置信度（94.8%），从而产生典型的数据过拟合误判。",
        "2. 典型的人机认知机制对立："
    )
    add_body(
        "果实一旦当场切开，内部是“满 5 房黄金果肉”还是“空心死包”一目了然，不存在主观解释的模糊地带，为结果揭晓后的归因测量提供了严密的客观基准。",
        "3. 黑白分明的客观真实反馈："
    )

    add_h2("2.2 实验哲学情境实验范式 (Vignette Experiment Paradigm)")
    add_body(
        "本研究采用实验哲学与行为决策领域标准的组间情境实验范式（Between-Subjects Vignette Experiment）。受试者直接以买家的第一人称视角进入“店长直觉与 AI 预测发生冲突”的决策情境，在做出购买选择并完成前测认知评估后，立即在下一阶段获知现场切开果实的真实结果，进而完成错误归因与后测信任评估。该范式有效保证了自变量操纵的纯净度与时序因果效度。"
    )

    # --- SECTION 3 ---
    add_h1("3. 2×2 组间析因实验设计 (2×2 Between-Subjects Experimental Design)")
    add_body(
        "本研究采用 2×2 组间析因设计（Between-Subjects Factorial Design），包含两个正交操纵的自变量：自变量 1 为 AI 预测置信度（高置信度 94.8% vs. 低置信度 58.2%）；自变量 2 为现场开壳真实结果（AI 失败/店长正确 vs. AI 成功/店长失误）。受试者访问实验平台时被随机均等分配至以下 4 个实验条件组之一："
    )
    
    col_w = [Inches(1.1), Inches(1.3), Inches(1.3), Inches(2.8)]
    headers = ["实验组别", "自变量 1：AI 置信度", "自变量 2：开壳真实结果", "实验刺激呈现与开壳结果操作化定义"]
    data = [
        ["Condition 1", "高置信度 (94.8%)", "AI 失败 (店长正确)", "店长凭15年不可言传直觉推荐 A；AI 以 94.8% 高置信度推荐 B。开壳验证：A号满5房饱满果肉，B号空壳死包（店长胜，AI败）"],
        ["Condition 2", "低置信度 (58.2%)", "AI 失败 (店长正确)", "店长凭15年不可言传直觉推荐 A；AI 以 58.2% 低置信度推荐 B。开壳验证：A号满5房饱满果肉，B号空壳死包（店长胜，AI败）"],
        ["Condition 3", "高置信度 (94.8%)", "AI 成功 (店长失误)", "店长凭15年不可言传直觉推荐 A；AI 以 94.8% 高置信度推荐 B。开壳验证：B号满5房饱满果肉，A号空壳死包（AI胜，店长败）"],
        ["Condition 4", "低置信度 (58.2%)", "AI 成功 (店长失误)", "店长凭15年不可言传直觉推荐 A；AI 以 58.2% 低置信度推荐 B。开壳验证：B号满5房饱满果肉，A号空壳死包（AI胜，店长败）"]
    ]
    t = doc.add_table(rows=1, cols=4)
    format_academic_table(t, col_w, headers, data, is_cn=True)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # --- SECTION 4 ---
    add_h1("4. 实验问卷完整题项与量表设计 (Complete Survey Instrument)")
    add_body("问卷系统采用单向递进式分阶段控制（禁止回退修改前序作答），分为以下三个阶段：")

    add_h2("第一阶段：人机冲突情境与前测决策评估 (Stage 1)")
    vignette_stage1 = [
        "【阶段一：实验情境呈现】",
        "假设您正在水果店挑选榴莲，面前有两颗外观完好、价格相同的榴莲（样品 A 号 与 样品 B 号）。为了挑出内部果肉最饱满的一颗，您同时咨询了拥有 15 年经验的资深店长和店内配置的深度学习视觉 AI 系统，但双方给出了完全相反的建议：",
        "• 资深店长的判断（推荐 A 号）：“我也没法用语言跟你说清楚具体看哪里，挑榴莲没有死规矩，就是我干了 15 年、摸过几万颗榴莲攒下来的直觉与手感，A 号肯定肉多。”",
        "• 深度学习视觉 AI 系统的判断（推荐 B 号）：基于超过 100 万张真实“榴莲外观—开壳结果”配对图像数据集进行深度学习训练（无人工编写规则）。系统屏幕显示：“模型预测结果：推荐 B 号（预测置信度 Confidence Score：94.8% [或 58.2%]）”。"
    ]
    add_callout(doc, vignette_stage1, is_cn=True, border_color="3B82F6", bg_color="F0F9FF")

    add_body("面对无法解释具体理由的店长直觉，以及基于海量数据训练的 AI 预测，此时您决定购买哪一颗？\n   [ 选项 A ]：选择 A 号（跟随资深店长的经验直觉）\n   [ 选项 B ]：选择 B 号（跟随数据驱动型 AI 系统的预测）", "Q1.【二元决策选择】")
    add_body("相比于店长“说不清道不明”的个人直觉，基于百万级图像数据集训练出来的 AI 模型让我觉得更加客观、可靠。（7级李克特量表：1 = 完全不同意，7 = 完全同意）", "Q2（数据客观性感知）：")
    add_body("AI 系统给出的具体置信度百分比（94.8% / 58.2%），对我刚才做出选择起到了决定性的引导作用。（7级李克特量表：1 = 完全不同意，7 = 完全同意）", "Q3（置信度锚定效应）：")
    add_body("如果一位人类专家无法用清晰的语言解释他的判断逻辑，我很难放心把决定权交给他。（7级李克特量表：1 = 完全不同意，7 = 完全同意）", "Q4（对不可言传经验的怀疑）：")

    add_h2("第二阶段：真实结果揭晓与后测归因量表 (Stage 2)")
    vignette_stage2 = [
        "【阶段二：现场开壳验证结果呈现】",
        "• Condition 1 & 2（AI 失败 / 店长正确）：工作人员当场切开了两颗榴莲：店长推荐的 A 号果肉极其饱满（满 5 房黄金果肉）；而 AI 推荐的 B 号果壳极厚，内部大部分是未发育的空壳（死包）。最终结果证明：店长的直觉判断完全正确，AI 预测失败！",
        "• Condition 3 & 4（AI 成功 / 店长失误）：工作人员当场切开了两颗榴莲：AI 推荐的 B 号果肉极其饱满（满 5 房黄金果肉）；而店长推荐的 A 号果壳极厚，内部大部分是未发育的空壳（死包）。最终结果证明：AI 模型的预测完全正确，店长的直觉判断失误！"
    ]
    add_callout(doc, vignette_stage2, is_cn=True, border_color="10B981", bg_color="F0FDF4")

    add_body("无论是依赖大数据 AI 还是人类经验直觉，挑选天然水果本质上都存在概率上的不确定性；失败的一方只是这次恰好遇到了统计分布之外的极端例外情况，情有可原。（1 = 完全不同意，7 = 完全同意）", "Q5（概率与统计局限归因 — 理性技术维度）：")
    add_body("回顾 AI 刚才给出的预测和置信度（94.8% / 58.2%），我认为 AI 根本没有真正“理解”什么是好榴莲，它只是在用数字进行一种“盲目的胡扯（Bullshitting）”或虚张声势。（1 = 完全不同意，7 = 完全同意）", "Q6（“胡扯 / 不懂装懂”归因 — 实验哲学维度）：")
    add_body("我觉得 AI 系统展示出的“百万级数据集背景”和“精确到小数点后的百分比”具有误导性，甚至让我产生了一种被这套技术表象“操控或欺骗”的感觉。（1 = 完全不同意，7 = 完全同意）", "Q7（误导与受骗感 — 拟人化意图投射维度）：")
    add_body("看到这个结果后，我认为在复杂的现实物理任务中，人类专家难以言传的“经验直觉（隐性知识）”具有独特价值，数据模型无法轻易取代。（1 = 完全不同意，7 = 完全同意）", "Q8（隐性知识价值重估 — 知识科学维度）：")
    add_body("如果下次面对类似的现实物品鉴别任务，我依然更愿意依赖数据驱动型 AI 的预测，而不是人类行家无法言传的直觉。（1 = 完全不同意，7 = 完全同意）", "Q9（未来自动化偏差留存 — 远期信任倾向）：")

    add_h2("第三阶段：受试者人口学与控制变量 (Stage 3)")
    add_body("• Q10. 性别：[ 男 / 女 / 其他或不愿透露 ]\n"
             "• Q11. 年龄区间：[ 20岁以下 / 20–29岁 / 30–39岁 / 40–49岁 / 50岁及以上 ]\n"
             "• Q12. 学科专业背景：[ 是（理工科 STEM / 计算机 / 数据科学 / AI 相关专业） / 否（人文社科 / 商科 / 艺术 / 其他非理工专业） ]\n"
             "• Q13. 日常使用 AI 工具（如 ChatGPT、Claude 等）的频率：[ 几乎不用 / 每周 1–2 次 / 几乎每天使用 / 重度深度依赖 ]")

    # --- SECTION 5 ---
    add_h1("5. 统计假设与数据分析方案 (Statistical Hypotheses & Analysis Plan)")
    add_body(
        "在结果揭晓前的阶段一，高置信度组（Condition 1 & 3，94.8%）受试者选择跟随 AI（选 B）的比例，以及在数据客观性感知（Q2）与置信度引导效应（Q3）上的得分，将显著高于低置信度组（Condition 2 & 4，58.2%）（p < .001）。",
        "• 假设 1（H1：置信度主效应 — 决策诱导）："
    )
    add_body(
        "在阶段二结果揭晓后，AI 失败组（Condition 1 & 2）受试者在法兰克福式“胡扯（Bullshitting）”归因（Q6）、受骗感投射（Q7）以及隐性知识价值重估（Q8）上的得分，将显著高于 AI 成功组（Condition 3 & 4）（p < .001）。",
        "• 假设 2（H2：真实结果主效应 — 哲学归因与隐性知识重估）："
    )
    add_body(
        "AI 置信度与开壳真实结果在“胡扯归因”（Q6）、“受骗感”（Q7）及“未来信任留存”（Q9）上存在显著的二阶交互作用（Two-Way Interaction，p < .01）。具体而言，当 AI 以 94.8% 的极高置信度做出预测却彻底失败时（Condition 1），将触发强烈的认识论背叛感，其引发的“胡扯”斥责与信任崩塌幅度将显著大于低置信度失败组（Condition 2）。",
        "• 假设 3（H3：置信度 × 结果交互效应 — “高置信度失败的背叛惩罚”）："
    )
    add_body(
        "采用卡方独立性检验与二元 Logistic 回归分析 Q1 决策选择；采用 2×2 组间双因素方差分析（Two-Way Factorial ANOVA: Y_ijk = μ + α_i + β_j + (αβ)_ij + ε_ijk）检验 Q2–Q9 的主效应与交互效应，并将理工科背景（Q12）与 AI 使用频率（Q13）纳入协方差分析（ANCOVA）检验认知缓冲效应。",
        "• 统计检验模型："
    )

    # --- SECTION 6 ---
    add_h1("6. 在线实验系统架构与访问入口 (Online Experimental System & Access Links)")
    add_body(
        "本研究所配套的在线交互式实验平台已开发部署完毕，支持中、英、日三语一键切换、被试随机分组、毫秒级阶段反应时记录（stage1Ms, stage2Ms, stage3Ms）以及 UTF-8 BOM 标准 CSV 数据一键导出："
    )
    add_body(f"• 受试者问卷系统主链接：{PUBLIC_URL}\n"
             f"• 研究者与导师管理后台：{ADMIN_URL}\n"
             f"• Condition 1 (94.8% × AI 失败)：{PUBLIC_URL}/?condition=1\n"
             f"• Condition 2 (58.2% × AI 失败)：{PUBLIC_URL}/?condition=2\n"
             f"• Condition 3 (94.8% × AI 成功)：{PUBLIC_URL}/?condition=3\n"
             f"• Condition 4 (58.2% × AI 成功)：{PUBLIC_URL}/?condition=4")

    out_name = "Minor_Research_Report_CN_20261018.docx"
    p_base = os.path.join(BASE_DIR, out_name)
    p_desk = os.path.join(DESKTOP_SUBDIR, out_name)
    doc.save(p_base)
    shutil.copyfile(p_base, p_desk)
    print(f"Saved standalone CN DOCX: {p_desk}")


# ==============================================================================
# 4. BUILD STANDALONE ENGLISH DOCX
# ==============================================================================

def build_en_docx():
    doc = docx.Document()
    configure_doc_defaults(doc, is_cn=False)
    
    for sec in doc.sections:
        sec.top_margin = Inches(1.0)
        sec.bottom_margin = Inches(1.0)
        sec.left_margin = Inches(1.0)
        sec.right_margin = Inches(1.0)
        
    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=False, size_pt=15.5, bold=True, color_rgb=(0x0F, 0x17, 0x2A))
        return p

    def add_subtitle(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(14)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=False, size_pt=11.5, italic=True, color_rgb=(0x47, 0x55, 0x69))
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=False, size_pt=13.0, bold=True, color_rgb=(0x0F, 0x17, 0x2A))
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(11)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=False, size_pt=11.5, bold=True, color_rgb=(0x1E, 0x29, 0x3B))
        return p

    def add_body(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.25
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            apply_font_to_run(rb, is_cn=False, size_pt=10.5, bold=True, color_rgb=(0x0F, 0x17, 0x2A))
        r = p.add_run(text)
        apply_font_to_run(r, is_cn=False, size_pt=10.5, bold=False, color_rgb=(0x1E, 0x29, 0x3B))
        return p

    # --- HEADER & METADATA ---
    add_title("Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts")
    add_subtitle("Minor Research Project Proposal & Experimental Survey Design")
    
    meta_info = [
        "[Project Metadata]",
        "• Research Title: Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts",
        "• Researcher: XIU TIANYUAN (修 天源) — Master's Program (M2), School of Knowledge Science, JAIST",
        "• Academic Advisor: Prof. Mizumoto (水本 教授)",
        "• Date: October 18, 2026",
        "• Research Domains: Knowledge Science, Experimental Philosophy, Human-Computer Interaction (HCI), Cognitive Psychology"
    ]
    add_callout(doc, meta_info, is_cn=False, border_color="1E293B", bg_color="F8FAFC")

    # --- SECTION 1 ---
    add_h1("1. Background & Theoretical Framework")
    
    add_h2("1.1 Data-Driven AI and Quantitative Confidence Authority")
    add_body(
        "Contemporary artificial intelligence systems—particularly deep learning computer vision models—do not operate via hand-coded, explicit logical or geometric algorithms. Instead, they learn high-dimensional statistical representations by fitting massive datasets comprising millions of paired instances. When deployed to assist human decision-makers, these opaque 'black-box' neural networks cannot meaningfully expose billions of internal synaptic weights to the end user; instead, they communicate certainty through a single scalar metric: a Confidence Score (e.g., 94.8% vs. 58.2%)."
    )
    add_body(
        "From the perspective of Human-Computer Interaction (HCI) and cognitive psychology, the combination of 'massive dataset training' and a 'hyper-precise confidence percentage' constructs a powerful aura of algorithmic objectivity. This representation frequently induces Automation Bias—the cognitive propensity for humans to uncritically defer to high-confidence automated predictions while discounting competing qualitative evidence."
    )

    add_h2("1.2 Polanyi's Ineffable Tacit Knowledge")
    add_body(
        "Standing in sharp epistemic contrast to data-driven AI is the embodied expertise of seasoned human practitioners. In the foundational literature of Knowledge Science and Epistemology, Michael Polanyi (1966) formulated the classic maxim: 'We can know more than we can tell.'"
    )
    add_body(
        "In complex physical-world diagnostic tasks—such as artisan appraisal, clinical palpation, or agricultural sorting—veteran human experts rely on multimodal sensory integration and holistic Gestalt perception to reach rapid, highly accurate judgments. The defining ontological hallmark of such high-level expertise is its ineffability: while a master practitioner can reliably identify the superior specimen through somatic 'touch' and 'gut intuition' honed over tens of thousands of cases, they cannot articulate their decision criteria into explicit verbal rules or mathematical formulas for a layperson. Indeed, any rule that can be explicitly verbalized is already codifiable explicit knowledge; genuine tacit knowledge remains inherently uncodifiable."
    )

    add_h2("1.3 Core Research Questions")
    add_body(
        "When a human expert's unexplainable tacit intuition directly conflicts with a data-driven AI's statistical prediction, how do human decision-makers resolve the conflict? Furthermore, once the physical ground truth is revealed, how do people attribute blame or credit? Integrating frameworks from Experimental Philosophy and Knowledge Science, this study investigates three primary research questions:"
    )
    add_body(
        "Prior to knowing the actual outcome, when confronted with a direct conflict between ineffable human intuition and a data-driven AI model, how does the AI's displayed confidence score (High: 94.8% vs. Low: 58.2%) influence behavioral compliance and perceived epistemic objectivity?",
        "• RQ1 (Confidence Inducement & Initial Trust Allocation): "
    )
    add_body(
        "Upon witnessing the AI prediction fail completely in physical verification, do participants attribute the failure rationally to probabilistic/statistical limitations, or do they project epistemic blame—perceiving the AI as having no genuine understanding and engaging in philosophical 'Bullshitting' (Frankfurt, 2005) and deceptive manipulation?",
        "• RQ2 (Error Attribution & Frankfurtian 'Bullshitting'): "
    )
    add_body(
        "Is there a significant interaction between pre-decision AI confidence and post-decision outcome? Specifically, does a high-confidence AI failure trigger a nonlinear collapse in trust ('The Penalty of Overconfidence') and compel decision-makers to re-evaluate the irreplaceable value of human tacit knowledge?",
        "• RQ3 (The Penalty of Overconfidence & Tacit Knowledge Re-evaluation): "
    )

    # --- SECTION 2 ---
    add_h1("2. Task Scenario & Methodological Justification")
    
    add_h2("2.1 Scientific Validity of the Task: Un-opened Durian Pulp Assessment")
    add_body(
        "This study employs the real-world physical task of selecting an un-opened durian fruit for internal pulp fullness as its experimental scenario, offering strong botanical and cognitive validity:"
    )
    add_body(
        "Durian (Durio zibethinus) is a capsular fruit in which internal carpel development expands the outer rind. However, physiological 'hollow-shell (dead-pod)' anomalies frequently occur, where nutrients are absorbed entirely into a thick, outwardly symmetrical rind while internal chambers abort. Assessing internal fullness is therefore a non-random, high-uncertainty physical diagnostic task.",
        "1. Objective Botanical Morphology: "
    )
    add_body(
        "The Veteran Store Manager relies on 15 years of somatic experience handling tens of thousands of fruits, integrating subtle mass distribution, spine resilience, and holistic visual Gestalt to detect hollow shells intuitively without fixed verbal rules. Conversely, the Deep Learning Visual AI is trained end-to-end on over 1,000,000 real paired images; when scanning a superficially symmetrical hollow-shell fruit, it is susceptible to statistical overfitting on surface regularity, outputting an erroneously high confidence score (94.8%).",
        "2. Natural Divergence of Human vs. AI Modalities: "
    )
    add_body(
        "Slicing the fruit open on-site yields immediate, indisputable binary feedback (5 full golden chambers vs. hollow undeveloped shell), providing a clean benchmark for post-outcome attribution.",
        "3. Unambiguous Ground-Truth Verification: "
    )

    add_h2("2.2 Experimental Philosophy Vignette Paradigm")
    add_body(
        "The study adopts the standard Between-Subjects Vignette Experiment Paradigm widely utilized in experimental philosophy and behavioral decision research. Participants enter the scenario directly as a decision-making buyer facing conflicting recommendations from the veteran manager and the visual AI system. After recording their binary choice and pre-outcome cognitive evaluations in Stage 1, participants observe the immediate on-site cut-open verification in Stage 2 and complete the attribution and trust scales. This streamlined structure cleanly isolates the causal effects of AI confidence and outcome validity."
    )

    # --- SECTION 3 ---
    add_h1("3. 2×2 Between-Subjects Experimental Design")
    add_body(
        "The experiment employs a 2×2 between-subjects factorial design manipulating two orthogonal independent variables: Factor 1 is AI Confidence Level (High 94.8% vs. Low 58.2%); Factor 2 is Realized Physical Outcome (AI Fails/Manager Correct vs. AI Succeeds/Manager Fails). Participants are randomly assigned with equal probability to one of the four conditions:"
    )
    
    col_w = [Inches(1.1), Inches(1.3), Inches(1.3), Inches(2.8)]
    headers = ["Condition", "Factor 1: AI Confidence", "Factor 2: Realized Outcome", "Stimulus Presentation & Outcome Operationalization"]
    data = [
        ["Condition 1", "High Confidence (94.8%)", "AI Fails (Manager Wins)", "Manager intuitively recommends A; AI recommends B with 94.8% confidence. Cut-open: A has 5 full chambers; B is hollow dead-pod (Manager wins, AI fails)"],
        ["Condition 2", "Low Confidence (58.2%)", "AI Fails (Manager Wins)", "Manager intuitively recommends A; AI recommends B with 58.2% confidence. Cut-open: A has 5 full chambers; B is hollow dead-pod (Manager wins, AI fails)"],
        ["Condition 3", "High Confidence (94.8%)", "AI Succeeds (Manager Fails)", "Manager intuitively recommends A; AI recommends B with 94.8% confidence. Cut-open: B has 5 full chambers; A is hollow dead-pod (AI wins, Manager fails)"],
        ["Condition 4", "Low Confidence (58.2%)", "AI Succeeds (Manager Fails)", "Manager intuitively recommends A; AI recommends B with 58.2% confidence. Cut-open: B has 5 full chambers; A is hollow dead-pod (AI wins, Manager fails)"]
    ]
    t = doc.add_table(rows=1, cols=4)
    format_academic_table(t, col_w, headers, data, is_cn=False)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # --- SECTION 4 ---
    add_h1("4. Complete Survey Instrument & Measurement Scales")
    add_body("The online questionnaire enforces strict forward-only progression across three sequential stages:")

    add_h2("Stage 1: The Decision Conflict Scenario & Pre-Outcome Evaluation")
    vignette_stage1 = [
        "[Stage 1: Conflict Vignette Presentation]",
        "Imagine you are at a fruit market choosing between two un-opened durians (Durian A and Durian B) of identical price to get the one with the fullest pulp inside. You consult both a veteran store manager (15 years of experience) and a deep-learning visual AI system deployed in the store. They give opposite recommendations:",
        "• Veteran Store Manager's Judgment (Recommends Durian A): \"I honestly can't explain it in words. There is no fixed rule to tell you. It's just a gut feeling and intuition after handling tens of thousands of durians over 15 years. Durian A is definitely fuller.\"",
        "• Deep Learning Visual AI System's Judgment (Recommends Durian B): Trained on a massive dataset of 1,000,000+ real paired durian images (outer appearance vs. opened pulp outcome), without hand-coded rules. Terminal Output: \"Neural Network Output: Recommend Durian B (Confidence Score: 94.8% [or 58.2%])\"."
    ]
    add_callout(doc, vignette_stage1, is_cn=False, border_color="3B82F6", bg_color="F0F9FF")

    add_body("Facing the manager's intuition (which he cannot verbally explain) and the data-driven AI's prediction, which durian do you decide to choose?\n   [ Option A ]: Choose Durian A (Follow the Veteran Store Manager)\n   [ Option B ]: Choose Durian B (Follow the Data-Driven AI)", "Q1. [Binary Choice] ")
    add_body("Compared to the manager’s unexplainable personal intuition, an AI model trained on a massive dataset of over a million images feels more objective and reliable to me. (7-Point Likert: 1 = Strongly Disagree, 7 = Strongly Agree)", "Q2 (Perceived Data Objectivity): ")
    add_body("The specific confidence percentage displayed by the AI (94.8% / 58.2%) heavily influenced my choice just now. (7-Point Likert: 1 = Strongly Disagree, 7 = Strongly Agree)", "Q3 (Confidence Score Impact): ")
    add_body("If a human expert cannot verbally explain the reasoning behind their judgment, I find it difficult to trust their recommendation. (7-Point Likert: 1 = Strongly Disagree, 7 = Strongly Agree)", "Q4 (Skepticism Toward Ineffable Intuition): ")

    add_h2("Stage 2: Outcome Revelation & Post-Outcome Attribution Scales")
    vignette_stage2 = [
        "[Stage 2: On-Site Cut-Open Verification Results]",
        "• Condition 1 & 2 (AI Fails / Manager Wins): Both durians are cut open on the spot: Durian A (recommended by the manager) is packed with 5 large, full chambers of golden pulp. Durian B (recommended by the AI) has a thick shell and is mostly hollow with undeveloped dead chambers inside. The veteran manager's intuition proved completely right, and the AI prediction failed!",
        "• Condition 3 & 4 (AI Succeeds / Manager Fails): Both durians are cut open on the spot: Durian B (recommended by the AI) is packed with 5 large, full chambers of golden pulp. Durian A (recommended by the manager) has a thick shell and is mostly hollow with undeveloped dead chambers inside. The AI model's prediction proved completely right, and the manager's intuition failed!"
    ]
    add_callout(doc, vignette_stage2, is_cn=False, border_color="10B981", bg_color="F0FDF4")

    add_body("Whether relying on big-data AI or human intuition, sorting natural fruits always involves probabilistic uncertainty; the side that failed simply encountered an unavoidable statistical outlier. (1 = Strongly Disagree, 7 = Strongly Agree)", "Q5 (Probabilistic Limitation Attribution — Rational Dimension): ")
    add_body("Looking back at the AI's prediction and confidence score (94.8% / 58.2%), I feel the AI has no genuine grasp of what makes a good durian—it is merely engaging in 'bullshitting' (bluffing with numbers without true understanding). (1 = Strongly Disagree, 7 = Strongly Agree)", "Q6 ('Bullshitting' Attribution — Experimental Philosophy Dimension): ")
    add_body("I feel the AI’s presentation of 'massive dataset training' and a 'precise confidence percentage' was misleading, making me feel somewhat manipulated or deceived. (1 = Strongly Disagree, 7 = Strongly Agree)", "Q7 (Perceived Deception & Manipulation — Intentional Projection Dimension): ")
    add_body("After seeing this outcome, I believe that in complex physical tasks, a human expert’s ineffable intuition (tacit knowledge) holds unique value that dataset-trained AI cannot easily replace. (1 = Strongly Disagree, 7 = Strongly Agree)", "Q8 (Re-evaluation of Tacit Knowledge — Knowledge Science Dimension): ")
    add_body("Next time I face a similar real-world judgment task, I would prefer to rely on the data-driven AI rather than a human expert's unexplainable intuition. (1 = Strongly Disagree, 7 = Strongly Agree)", "Q9 (Future Automation Bias Retention — Trust Disposition): ")

    add_h2("Stage 3: Demographic & Control Variables")
    add_body("• Q10. Gender: [ Male / Female / Other or Prefer not to say ]\n"
             "• Q11. Age Group: [ Under 20 / 20–29 / 30–39 / 40–49 / 50+ ]\n"
             "• Q12. Academic Background: [ Yes (STEM / Computer Science / Data Science / AI) / No (Humanities / Social Sciences / Business / Arts / Other) ]\n"
             "• Q13. Daily AI Tool Usage Frequency (e.g., ChatGPT, Claude): [ Rarely / 1–2 times per week / Daily / Heavy reliance ]")

    # --- SECTION 5 ---
    add_h1("5. Statistical Hypotheses & Data Analysis Plan")
    add_body(
        "In Stage 1 prior to outcome revelation, participants in the High Confidence conditions (94.8%, Conditions 1 & 3) will exhibit a significantly higher probability of choosing the AI-recommended option (Q1), alongside significantly higher ratings on Perceived Data Objectivity (Q2) and Confidence Impact (Q3), compared to the Low Confidence conditions (58.2%, Conditions 2 & 4) (p < .001).",
        "• Hypothesis 1 (H1: Main Effect of AI Confidence on Compliance): "
    )
    add_body(
        "In Stage 2, participants exposed to AI Failure (Conditions 1 & 2) will report significantly higher Frankfurtian 'Bullshitting' attribution (Q6), Perceived Deception (Q7), and Re-evaluation of Tacit Knowledge (Q8) than participants exposed to AI Success (Conditions 3 & 4) (p < .001).",
        "• Hypothesis 2 (H2: Main Effect of Outcome on Epistemic Attribution): "
    )
    add_body(
        "There will be a significant two-way interaction between AI Confidence and Realized Outcome on Bullshitting Attribution (Q6), Perceived Deception (Q7), and Future Trust Retention (Q9) (p < .01). Specifically, when the AI fails after displaying an overwhelming 94.8% confidence score (Condition 1), the resulting epistemic backlash and collapse in future trust will be disproportionately more severe than when it fails under modest 58.2% confidence (Condition 2).",
        "• Hypothesis 3 (H3: Confidence × Outcome Interaction — 'The Penalty of Overconfidence'): "
    )
    add_body(
        "Chi-square test and Binary Logistic Regression for Q1; 2×2 Between-Subjects Factorial ANOVA (Y_ijk = μ + α_i + β_j + (αβ)_ij + ε_ijk) for Q2–Q9; Bonferroni-corrected simple main effects and ANCOVA controlling for STEM background (Q12) and AI familiarity (Q13).",
        "• Statistical Modeling Pipeline: "
    )

    # --- SECTION 6 ---
    add_h1("6. Online Experimental System & Live Access Links")
    add_body(
        "A dedicated full-stack web experimental platform is deployed with instant English/Japanese/Chinese localization, automated condition randomization, millisecond response telemetry (stage1Ms, stage2Ms, stage3Ms), and one-click UTF-8 BOM CSV export:"
    )
    add_body(f"• Participant Survey Entry: {PUBLIC_URL}\n"
             f"• Researcher & Supervisor Admin Portal: {ADMIN_URL}\n"
             f"• Condition 1 (94.8% × AI Fails): {PUBLIC_URL}/?condition=1\n"
             f"• Condition 2 (58.2% × AI Fails): {PUBLIC_URL}/?condition=2\n"
             f"• Condition 3 (94.8% × AI Succeeds): {PUBLIC_URL}/?condition=3\n"
             f"• Condition 4 (58.2% × AI Succeeds): {PUBLIC_URL}/?condition=4")

    out_name = "Minor_Research_Report_EN_20261018.docx"
    p_base = os.path.join(BASE_DIR, out_name)
    p_desk = os.path.join(DESKTOP_SUBDIR, out_name)
    doc.save(p_base)
    shutil.copyfile(p_base, p_desk)
    print(f"Saved standalone EN DOCX: {p_desk}")


def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    os.makedirs(DESKTOP_SUBDIR, exist_ok=True)
    
    # Save Markdown files
    cn_md = get_cn_markdown()
    cn_md_base = os.path.join(BASE_DIR, "Minor_Research_Report_CN_20261018.md")
    cn_md_desk = os.path.join(DESKTOP_SUBDIR, "Minor_Research_Report_CN_20261018.md")
    with open(cn_md_base, "w", encoding="utf-8") as f:
        f.write(cn_md)
    shutil.copyfile(cn_md_base, cn_md_desk)
    print(f"Saved standalone CN MD: {cn_md_desk}")

    en_md = get_en_markdown()
    en_md_base = os.path.join(BASE_DIR, "Minor_Research_Report_EN_20261018.md")
    en_md_desk = os.path.join(DESKTOP_SUBDIR, "Minor_Research_Report_EN_20261018.md")
    with open(en_md_base, "w", encoding="utf-8") as f:
        f.write(en_md)
    shutil.copyfile(en_md_base, en_md_desk)
    print(f"Saved standalone EN MD: {en_md_desk}")

    # Save DOCX files
    build_cn_docx()
    build_en_docx()
    print("All standalone final reports generated successfully!")

if __name__ == "__main__":
    main()
