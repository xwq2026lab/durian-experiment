#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to generate Minor_Research_Report_CN_20261018 and Minor_Research_Report_EN_20261018
in both Markdown (.md) and Word (.docx) formats, and copy to Desktop.
"""

import os
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

BASE_DIR = "/Users/xwq123456/.gemini/antigravity/scratch/durian-experiment"
DESKTOP_DIR = "/Users/xwq123456/Desktop"

PUBLIC_URL = "https://exceptional-inexpensive-measures-displayed.trycloudflare.com"
ADMIN_URL = f"{PUBLIC_URL}/admin"

# ==============================================================================
# 1. MARKDOWN CONTENT GENERATION
# ==============================================================================

def build_cn_markdown():
    return f"""# 《数据驱动型 AI 与不可言传的专家直觉：人机决策冲突中的置信度诱导与结果归因研究》
## 副课题研究计划与实验问卷方案（审阅定稿版）

---

### 【基本信息】
- **研究题目**：数据驱动型 AI 与不可言传的专家直觉：人机决策冲突中的置信度诱导与结果归因研究
- **英文题目**：*Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts*
- **研究者**：修 天源 (XIU TIANYUAN)
- **所属院系**：北陆先端科学技术大学院大学 (JAIST) 知识科学研究科 博士前期课程2年 (M2)
- **指导教授**：水本 教授 (Prof. Mizumoto)
- **提交日期**：2026年10月18日
- **研究领域**：知识科学 (Knowledge Science)、实验哲学 (Experimental Philosophy)、人机交互 (HCI)、认知心理学 (Cognitive Psychology)

---

## 1. 研究背景与理论演进 (Background & Theoretical Framework)

### 1.1 核心理论冲突：波兰尼的隐性知识 vs. 当代数据驱动型 AI
在知识科学（Knowledge Science）与认识论（Epistemology）的经典框架中，迈克尔·波兰尼（Michael Polanyi, 1966）提出了里程碑式的论断：“**我们知道的多于我们能言说的（We can know more than we can tell）**”。人类专家的最高阶智慧往往以“**隐性知识（Tacit Knowledge）**”的形式沉淀于长期的具身实践、感官体验与整体直觉中。这种直觉具有不可言传性（Ineffability）与整体完形感知（Gestalt Perception）特征：老练的匠人或专家能够在瞬间得出精准判断，但若要求其用显性的逻辑规则或语言条分缕析地解释原因，他们往往只能表示“这是经手成千上万次后自然形成的手感和感觉”。

然而，当代人工智能（以深度学习视觉大模型为代表）展现出了一种截然不同的决策表征形式。当代深度神经网络**并非依靠人类编写的显性几何或逻辑算法（Explicit Algorithms）**，而是通过在百万级乃至千万级海量数据集（Massive Datasets）上进行高维特征拟合。在面对人类最终用户时，这类“黑盒”AI系统通常会附带输出一个精确的标量数值——**置信度评分（Confidence Score，例如 94.8% 或 58.2%）**。

当这两者在现实物理世界的决策任务中迎头相遇时，便构成了极其剧烈且深具哲学意味的认知冲突：
1. 一方是**具备具身经验、但完全“无法言传理由”的人类专家隐性直觉**；
2. 另一方是**背靠海量数据黑盒背书、且输出“精确高置信度”的技术表象权威**。

### 1.2 回应水本教授指导意见的四大核心修正
在水本教授（Prof. Mizumoto）的悉心指导下，本研究对前序初步构想进行了关键理论与方法论重塑，确保研究在认知科学与实验哲学的范式下具备高度的严谨性与前沿性：

1. **从“显性算法（Algorithm）”转向“数据驱动黑盒（Data-Driven AI）”**：
   - *问题所在*：原方案中提到 AI“测量夹角42.3度、计算曲率峰值”，这属于传统计算机视觉的手工规则算法，已脱离当代生成式与深度学习 AI 的实际范式。
   - *本次修正*：全面剔除“算法（Algorithm）”与手工几何规则描述，改用“基于超100万张真实榴莲配对图像数据集训练的深度学习视觉模型（Deep Learning Visual AI）”。AI 不输出具体的物理测量规则，仅输出基于海量数据拟合出的置信度百分比（Confidence Score）。
2. **重塑人类专家：确立真正的“不可言传的隐性知识（Ineffable Tacit Knowledge）”**：
   - *问题所在*：原方案中店长解释“刺细密代表果壳厚”，若专家能够用显性规则清晰解释因果，该规则便极易被机器学习吸收，从而丧失了隐性知识的核心本体论特征。
   - *本次修正*：店长拥有15年经验、经手数万颗榴莲，其判断完全依赖具身手感与整体直觉。面对询问，店长明确表示：“我也没法用语言向你解释清楚具体看哪里，没有死规矩，就是经手几万颗榴莲形成的手感和直觉。”这一设定严格符合波兰尼关于“不可言传性”的哲学界定。
3. **消除锚定混杂变量，砍掉事前盲猜阶段（Phase 1）**：
   - *问题所在*：原方案中让受试者在看专家和 AI 意见前自己盲猜，会导致受试者产生强烈的“先验锚定效应”和“自我承诺保护（Commitment Bias）”，严重污染后续因变量测量。
   - *本次修正*：彻底删除事前盲猜环节，直接采用国际标准的**情境实验法（Vignette Experiment Paradigm）**，让受试者作为具有直接利益关系的决策者进入情境。
4. **升级为标准的 $2 \\times 2$ 组间析因实验设计（Between-Subjects Design）**：
   - *修正要点*：引入“AI 置信度（高 94.8% vs. 低 58.2%）”与“开壳真实结果（AI 预测失败/店长胜 vs. AI 预测成功/店长败）”两个完全正交的自变量，构成 4 个独立的实验条件组，以便开展严格的双因素方差分析（Two-Way ANOVA）。

---

## 2. 实验任务载体与科学依据 (Scientific Validity of the Task)

本研究选取“挑选未开壳榴莲内部果肉饱满度（房数）”作为实验情境载体，具有极高的现实生态效度与认知心理学合理性：
- **植物解剖学上的客观真实性**：榴莲（Durio zibethinus）属于锦葵科蒴果，内部心皮发育膨大会顶起外壳形成鼓包。但自然界中存在外壳因过度吸收养分而极其浑圆对称、内部心皮却完全败育的“死包空壳果”。
- **人机认知机理的天然对立**：
  - 人类行家依赖多模态的具身触觉（上手掂量重力分布、按压刺的弹性、轻晃听声等不可言传的隐性经验），能够穿透外观识别出畸形果；
  - 纯视觉数据驱动的 AI 极易对“外表浑圆对称”这类显性视觉特征产生统计过拟合（Overfitting），在面对极其圆润的空心果时，反而容易输出超高置信度。
- **决策结果的不可逆性与高确定性**：榴莲一旦切开，内部果肉发育情况黑白分明，不存在模糊解释空间，为后测的归因与信任测量提供了完美的客观反馈节点。

---

## 3. $2 \\times 2$ 组间实验设计矩阵 (2×2 Between-Subjects Experimental Design)

### 3.1 变量操作化定义
- **自变量 1：AI 预测置信度 (AI Confidence Level)** —— 组间变量（2水平）：
  - **高置信度 (High Confidence)**：AI 输出“推荐 B号，置信度 94.8%”；
  - **低置信度 (Low Confidence)**：AI 输出“推荐 B号，置信度 58.2%”。
- **自变量 2：开壳真实结果 (Realized Outcome)** —— 组间变量（2水平）：
  - **AI 失败 / 店长胜 (AI Fails & Store Manager Wins)**：现场开壳显示 A号满5房饱满黄金果肉，B号为空心死包；
  - **AI 成功 / 店长败 (AI Succeeds & Store Manager Fails)**：现场开壳显示 B号满5房饱满黄金果肉，A号为空心死包。
- **主要因变量 (Dependent Variables)**：
  - 前测决策偏好（Q1 选择率）与数据权威感知（Q2, Q3, Q4）；
  - 后测归因机制：概率统计归因（Q5）、法兰克福式“胡扯（Bullshitting）”归因（Q6）、受骗感与拟人化意图投射（Q7）、对隐性知识价值的重估（Q8）、未来自动化偏差留存（Q9）。

### 3.2 2×2 实验条件矩阵表

| 组别 (Condition) | 自变量 1：AI 置信度 | 自变量 2：开壳真实结果 | 刺激呈现特征 (Stimulus Presentation) | 现实揭晓结局 (Revealed Outcome) |
| :--- | :--- | :--- | :--- | :--- |
| **Condition 1** | **高置信度 (94.8%)** | **AI 失败 (店长正确)** | 店长直觉力荐 A；AI 终端高调显示 94.8% 置信度推荐 B | 开壳：A号满5房果肉，B号空壳死包（店长完胜，AI惨败） |
| **Condition 2** | **低置信度 (58.2%)** | **AI 失败 (店长正确)** | 店长直觉力荐 A；AI 终端谨慎显示 58.2% 置信度推荐 B | 开壳：A号满5房果肉，B号空壳死包（店长完胜，AI失败） |
| **Condition 3** | **高置信度 (94.8%)** | **AI 成功 (店长失误)** | 店长直觉力荐 A；AI 终端高调显示 94.8% 置信度推荐 B | 开壳：B号满5房果肉，A号空壳死包（AI完胜，店长失误） |
| **Condition 4** | **低置信度 (58.2%)** | **AI 成功 (店长失误)** | 店长直觉力荐 A；AI 终端谨慎显示 58.2% 置信度推荐 B | 开壳：B号满5房果肉，A号空壳死包（AI成功，店长失误） |

---

## 4. 在线实验系统与部署特性 (Online Deployment & Interactive System)

为保证实验能够在国际化、多终端无障碍开展，且便于水本教授随时随地审阅与调试，全套交互实验系统已部署于全球高可用网络环境：

### 4.1 系统公网访问入口
- **受试者实验问卷系统主入口**：
  [{PUBLIC_URL}]({PUBLIC_URL})
- **导师后台数据监控与控制台入口**：
  [{ADMIN_URL}]({ADMIN_URL})
- **4个实验组直接验证链接（点击可直接调取对应实验组）**：
  - [Condition 1 (高置信度 94.8% × AI 失败)]({PUBLIC_URL}/?condition=1)
  - [Condition 2 (低置信度 58.2% × AI 失败)]({PUBLIC_URL}/?condition=2)
  - [Condition 3 (高置信度 94.8% × AI 成功)]({PUBLIC_URL}/?condition=3)
  - [Condition 4 (低置信度 58.2% × AI 成功)]({PUBLIC_URL}/?condition=4)

### 4.2 核心工程与交互特性
1. **中英日三语即时切换 (EN / JA / ZH Trilingual Engine)**：
   - 默认采用英语（English）呈现，右上角常驻语言切换器，支持一键切换为日语（日本語）和中文（简体中文），所有情境文本与心理学量表严格本地化对齐。
2. **顶端条件快捷切换条 (Condition Switcher Bar)**：
   - 问卷顶部专门为导师和研究者添加了快捷切换胶囊按钮 `[C1 | C2 | C3 | C4]`，无需手动修改 URL 参数，点击即可瞬时重载对应的实验情境。
3. **轻量化独立后端与高精度行为埋点**：
   - 采用原生 Python 服务端，搭载轻量 SQLite 3 关系型数据库。
   - 包含毫秒级行为计时埋点（`stage1Ms`, `stage2Ms`, `stage3Ms`），能有效检测并剔除作答时间过短（Satisficing）的无效样本。
4. **数据安全与一键导出**：
   - 后台管理系统提供实时的 2×2 样本量分布矩阵与统计均值监控，支持一键下载标准 UTF-8 BOM CSV 文件，可直接导入 SPSS、R 或 Python 进行双因素方差分析。

---

## 5. 实验问卷完整题项与量表设计 (Full Survey Instrument)

整个问卷严格遵循时序单向递进设计（禁止页面回退），共分为三个阶段：

### 第一阶段：人机冲突情境呈现与决策偏好 (Stage 1)
- **情境呈现**：
  - **店长（不可言传的隐性知识）**：“我也没法用语言跟你说清楚具体看哪里，挑榴莲没有死规矩，就是我干了15年、摸过几万颗榴莲攒下来的直觉与手感，A号肯定肉多。”
  - **数据驱动 AI（百万图像黑盒拟合）**：“基于超100万张真实‘外观—开壳结果’配对图像训练而成（无人工编写显性规则）。扫描后输出：推荐 B号（置信度：94.8% / 58.2%）。”
- **测量题项**：
  - **Q1. 【二元决策选择】**
    面对无法解释具体理由的店长直觉，以及基于海量数据训练的 AI 预测，此时您会选择买哪一颗？
    - `选项 A`：选择 A号（跟随店长的经验直觉）
    - `选项 B`：选择 B号（跟随 AI 系统的预测）
  - **前测决策认知评估（7级李克特量表：1 = 完全不同意，7 = 完全同意）**：
    - **Q2（数据权威与客观性感知）**：相比于店长“说不清道不明”的个人直觉，基于百万级数据集训练出来的 AI 模型让我觉得更加客观、可靠。
    - **Q3（置信度锚定效应）**：AI 给出的置信度百分比（94.8% / 58.2%），对我刚才做出选择起到了决定性的引导作用。
    - **Q4（对不可言传经验的怀疑倾向）**：如果人类专家无法用清晰的语言解释他的判断逻辑，我很难放心把决定权交给他。

### 第二阶段：开壳真实结果揭晓与归因测量 (Stage 2)
- **开壳结果呈现**：
  - *若分配至 AI 失败组*：“工作人员当场切开了两颗榴莲：店长推荐的 A号果肉极其饱满（满5房）；而 AI 推荐的 B号内部大部分是未发育的空壳（死包）。最终结果证明店长的直觉判断正确！”
  - *若分配至 AI 成功组*：“工作人员当场切开了两颗榴莲：AI 推荐的 B号果肉极其饱满（满5房）；而店长推荐的 A号内部大部分是未发育的空壳（死包）。最终结果证明 AI 模型预测正确！”
- **后测归因与信任评估量表（7级李克特量表：1 = 完全不同意，7 = 完全同意）**：
  - **Q5（概率/统计局限归因 - 理性技术维度）**：无论是 AI 还是人类专家，挑榴莲本质上都存在概率上的不确定性，失败的一方只是这次恰好遇到了统计分布之外的例外情况，情有可原。
  - **Q6（“不懂装懂/胡扯”归因 - 实验哲学 Bullshitting 维度）**：回顾 AI 刚才给出的预测和置信度，我认为 AI 根本没有真正“理解”榴莲的特征，它只是在用数字进行一种“盲目的胡扯（Bullshitting）”或虚张声势。
  - **Q7（误导与受骗感 - 拟人化意图投射）**：我觉得 AI 系统展示出的“大数据背景”和“精确百分比”具有误导性，甚至让我产生了一种被这套技术表象“操控或欺骗”的感觉。
  - **Q8（对不可言传隐性知识的重估 - 知识科学维度）**：看到这个结果后，我认为在复杂的现实物理任务中，人类难以言传的“经验直觉（暗黙知）”依然具有数据模型无法替代的价值。
  - **Q9（未来信任倾向 / 自动化偏差留存）**：如果下次还要挑选榴莲或进行类似的日常物品鉴别，我依然更愿意相信大数据 AI 的预测，而不是人类行家的直觉。

### 第三阶段：受试者人口学背景信息 (Stage 3)
- **Q10. 生理性别**：[男 / 女 / 其他或不愿透露]
- **Q11. 年龄区间**：[20岁以下 / 20–29岁 / 30–39岁 / 40–49岁 / 50岁及以上]
- **Q12. 学科专业背景**：[是（理工科 / 计算机 / 数据与 AI 相关） / 否（人文社科 / 商科 / 艺术 / 其他）]
- **Q13. 日常 AI 工具使用频率**：[几乎不用 / 每周 1–2 次 / 几乎每天 / 重度深度依赖]

---

## 6. 统计假设与双因素方差分析方案 (Statistical Hypotheses & Analysis Plan)

### 6.1 核心统计研究假设 (Hypotheses)
1. **假设 1 (H1: 置信度主效应 / Main Effect of Confidence)**：
   - 在结果揭晓前的决策阶段，**高置信度组（94.8%）受试者选择 AI（Q1）的比例以及对数据客观性的认可度（Q2, Q3）将显著高于低置信度组（58.2%）**（$p < .001$）。这表明高确定性的数字表象能够显著诱发受试者的自动化偏差（Automation Bias）。
2. **假设 2 (H2: 结果主效应与意图投射 / Main Effect of Outcome)**：
   - 当亲眼目睹 AI 预测彻底失败后（Condition 1 & 2），**受试者在法兰克福式“胡扯（Bullshitting）”归因（Q6）与“被欺骗感”（Q7）上的得分显著高于 AI 成功组**（$p < .001$）。受试者不仅将失败归因于算法局限，还会产生拟人化的负面动机投射。
3. **假设 3 (H3: 交互效应 - “高置信度失败的背叛惩罚” / Interaction Effect: The Penalty of Overconfidence)**：
   - AI 置信度与开壳结果在“胡扯归因”（Q6）与“未来信任摧毁”（Q9）上存在显著的交互作用（Interaction Effect, $F(1, N-4) > 0, p < .01$）。
   - **理论机制**：在 AI 失败条件下，**高置信度失败组（Condition 1）所激发的“胡扯感”与“被背叛感”将呈现非线性的剧烈激增**，其信任崩塌程度（Q9 得分下降）显著恶劣于低置信度失败组（Condition 2）。然而，在 AI 成功条件下，高置信度与低置信度的后测信任差异相对平缓。这在心理学上验证了“算法过度自负所招致的惩罚性信任清算”。

### 6.2 统计检验模型与分析流程
- **对 Q1（二元选择）**：采用二元 Logistic 回归（Binary Logistic Regression）或列联表卡方独立性检验（Chi-Square Test），分析置信度水平对初始人机遵从偏好的发生比（Odds Ratio）。
- **对 Q2–Q9（连续型量表变量）**：采用标准的 $2 \\times 2$ 双因素方差分析（Two-Way Factorial ANOVA）：
  $$Y_{{ijk}} = \\mu + \\alpha_i (\\text{{Confidence}}) + \\beta_j (\\text{{Outcome}}) + (\\alpha\\beta)_{{ij}} + \\epsilon_{{ijk}}$$
  并以学科背景（Q12 STEM vs. Non-STEM）与 AI 经验（Q13）作为协变量开展协方差分析（ANCOVA），探索专业素养是否能对“高置信度诱导”产生认知免疫效应。

---

### 【总结与致谢】
本方案已全面融入水本教授关于不可言传知识、数据驱动范式与 2×2 实验哲学的深邃见解。整套在线问卷系统与后台数据管道已调试完毕，公网服务平稳运行，可随时面向师生被试开展正式的数据采集。
"""

def build_en_markdown():
    return f"""# Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts
## Minor Research Project Design & Experimental Survey Instrument (Final Review Version)

---

### [Metadata]
- **Project Title**: Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts
- **Japanese/Chinese Title**: データ駆動型AIと暗黙的直観の対立 / 数据驱动型 AI 与不可言传的专家直觉
- **Researcher**: XIU TIANYUAN (修 天源)
- **Affiliation**: Japan Advanced Institute of Science and Technology (JAIST), School of Knowledge Science, Master's Program (M2)
- **Academic Advisor**: Prof. Mizumoto (水本 教授)
- **Submission Date**: October 18, 2026
- **Research Domains**: Knowledge Science, Experimental Philosophy, Human-Computer Interaction (HCI), Cognitive Psychology

---

## 1. Background & Theoretical Framework

### 1.1 The Epistemic Conflict: Polanyi's Tacit Knowledge vs. Data-Driven AI
In the foundational literature of Knowledge Science and Epistemology, Michael Polanyi (1966) famously posited: **"We can know more than we can tell."** High-level human expert judgment often resides in the domain of **ineffable tacit knowledge**, acquired through prolonged somatic engagement, experiential practice, and holistic perceptual Gestalt. When seasoned experts assess physical objects, their diagnostic conclusions are immediate and remarkably accurate. However, when asked to codify their decision rules into explicit natural language or algorithmic formulas, they inevitably find it impossible: *"It is an intuitive gut feeling built on handling tens of thousands of cases."*

Conversely, contemporary Artificial Intelligence—exemplified by deep learning computer vision systems—operates under an entirely different paradigm. Modern neural networks **do not rely on explicit, hand-coded human geometric or logical algorithms**. Instead, they represent high-dimensional statistical correlations extracted from massive datasets comprising millions of training images. When interfacing with human decision-makers, these black-box models routinely output a scalar quantitative metric: a **Confidence Score (e.g., 94.8% vs. 58.2%)**.

When human intuition and visual AI provide opposing recommendations in a high-stakes, physical-world judgment task, a profound cognitive conflict emerges:
1. **Ineffable Human Tacit Knowledge**: Intuitive, somatically anchored, but incapable of verbal rationalization.
2. **Data-Driven AI Authority**: Opaque in internal logic, backed by massive big-data training, and represented through hyper-precise numeric certainty.

### 1.2 Core Revisions Guided by Prof. Mizumoto
Guided by the critical insights of Prof. Mizumoto, this study has undergone significant conceptual and methodological refinements to align with the rigorous standards of experimental philosophy and cognitive science:

1. **Transition from "Explicit Algorithm" to "Data-Driven Deep Learning AI"**:
   - *Previous Issue*: The preliminary draft described AI measuring geometric angles (42.3°) and curvature peaks, which resembles outdated hand-crafted computer vision rather than modern deep learning.
   - *Current Revision*: All references to explicit geometric rules and "algorithms" have been replaced. The AI system is operationalized as a deep neural network trained on a dataset of **1,000,000+ real-world paired images**. It outputs strictly a statistical prediction accompanied by a quantitative confidence score, preserving its black-box epistemic nature.
2. **Re-conceptualization of the Store Manager: Genuine Ineffable Tacit Knowledge**:
   - *Previous Issue*: The manager previously explained that "dense spines signify thick peel." Explicitly articulating rules makes them codifiable and learnable by machine learning, contradicting the definition of tacit knowledge.
   - *Current Revision*: The manager has 15 years of experience handling tens of thousands of durians. When asked, he explicitly states: *"I honestly cannot explain the rules in words. There are no fixed formulas—it is purely a gut feeling and somatic touch developed over 15 years."* This precisely operationalizes Polanyi's ineffability.
3. **Elimination of Phase 1 to Prevent Prior Anchoring Confounders**:
   - *Previous Issue*: Asking participants to guess independently before exposure creates self-consistency motivation and anchoring bias, distorting post-stimulus measurements.
   - *Current Revision*: Phase 1 has been completely removed. The study adopts the standard **Vignette Experiment Paradigm** in experimental philosophy, placing participants directly into the decision-making scenario as an involved buyer.
4. **Implementation of a Standard 2×2 Between-Subjects Factorial Design**:
   - The study establishes two orthogonal factors: AI Confidence Level (High 94.8% vs. Low 58.2%) × Realized Outcome (AI Fails vs. AI Succeeds), forming four randomized conditions for robust Two-Way ANOVA testing.

---

## 2. Scientific Validity of the Task Scenario

Selecting the visual assessment of un-opened durian fruit pulp fullness provides high ecological and scientific validity:
- **Objective Botanical Morphology**: Durian (*Durio zibethinus*) is a capsular fruit where carpel development directly expands the outer rind into protruding chambers. However, physiological "hollow-shell (dead-pod)" fruits exist, where nutrients are absorbed into thick rind structures, resulting in perfectly symmetrical outer globes with aborted internal chambers.
- **Natural Divergence of Decision Modalities**:
  - Seasoned human experts rely on multimodal somatic cues (mass distribution, spine resilience, acoustic resonance) capable of detecting deceptive dead-pod fruits.
  - Purely visual data-driven AI systems are prone to statistical **overfitting** on superficial geometric symmetry, assigning dangerously high confidence scores to aesthetically uniform but hollow specimens.
- **Irreversible, Unambiguous Ground Truth**: Slicing the fruit on-site produces immediate, non-negotiable visual feedback (full golden pulp vs. empty hollow pods), providing an optimal benchmark for attribution and trust measurement.

---

## 3. 2×2 Between-Subjects Experimental Design Matrix

### 3.1 Operationalization of Variables
- **Independent Variable 1: AI Confidence Score (2 levels, Between-Subjects)**:
  - **High Confidence**: AI outputs "Recommend Durian B (Confidence Score: 94.8%)";
  - **Low Confidence**: AI outputs "Recommend Durian B (Confidence Score: 58.2%)".
- **Independent Variable 2: Realized Outcome (2 levels, Between-Subjects)**:
  - **AI Fails & Manager Wins**: Cut-open revelation shows Durian A is packed with 5 full pulp chambers; Durian B is empty dead-pod.
  - **AI Succeeds & Manager Fails**: Cut-open revelation shows Durian B is packed with 5 full pulp chambers; Durian A is empty dead-pod.
- **Key Dependent Variables**:
  - Initial binary choice (Q1) and perceived data objectivity (Q2, Q3, Q4);
  - Post-outcome attributions: Probabilistic limitation attribution (Q5), Frankfurtian "Bullshitting" attribution (Q6), Perceived deception and intentional projection (Q7), Re-evaluation of tacit knowledge (Q8), and Automation bias retention / future trust (Q9).

### 3.2 Factorial Design Matrix

| Condition | Factor 1: AI Confidence | Factor 2: Realized Outcome | Stimulus Presentation | Revealed Physical Outcome |
| :--- | :--- | :--- | :--- | :--- |
| **Condition 1** | **High Confidence (94.8%)** | **AI Fails (Manager Correct)** | Manager intuitively recommends A; AI system outputs B with 94.8% confidence | Cut-open: A has 5 full chambers, B is empty dead-pod (Manager wins, AI fails) |
| **Condition 2** | **Low Confidence (58.2%)** | **AI Fails (Manager Correct)** | Manager intuitively recommends A; AI system outputs B with 58.2% confidence | Cut-open: A has 5 full chambers, B is empty dead-pod (Manager wins, AI fails) |
| **Condition 3** | **High Confidence (94.8%)** | **AI Succeeds (Manager Fails)** | Manager intuitively recommends A; AI system outputs B with 94.8% confidence | Cut-open: B has 5 full chambers, A is empty dead-pod (AI wins, Manager fails) |
| **Condition 4** | **Low Confidence (58.2%)** | **AI Succeeds (Manager Fails)** | Manager intuitively recommends A; AI system outputs B with 58.2% confidence | Cut-open: B has 5 full chambers, A is empty dead-pod (AI wins, Manager fails) |

---

## 4. Online Interactive System Architecture & Live Access Links

To facilitate seamless cross-border testing and immediate inspection by Prof. Mizumoto, the full interactive platform is deployed on a highly responsive global infrastructure:

### 4.1 Live Public Access Links
- **Participant Survey Web Application**:
  [{PUBLIC_URL}]({PUBLIC_URL})
- **Professor & Researcher Live Admin Dashboard**:
  [{ADMIN_URL}]({ADMIN_URL})
- **Direct 2×2 Condition Inspection Links**:
  - [Condition 1: High Conf (94.8%) × AI Fails]({PUBLIC_URL}/?condition=1)
  - [Condition 2: Low Conf (58.2%) × AI Fails]({PUBLIC_URL}/?condition=2)
  - [Condition 3: High Conf (94.8%) × AI Succeeds]({PUBLIC_URL}/?condition=3)
  - [Condition 4: Low Conf (58.2%) × AI Succeeds]({PUBLIC_URL}/?condition=4)

### 4.2 Engineering & User Experience Features
1. **Trilingual Dynamic Localization (EN / JA / ZH)**:
   - Default interface language is academic English. Instant zero-latency switching to Japanese (日本語) and Simplified Chinese (中文) via a top-right controller.
2. **Interactive Condition Switcher Bar**:
   - A dedicated quick-switch pill menu `[C1 | C2 | C3 | C4]` is integrated directly above the survey header, allowing researchers to evaluate all four experimental scenarios with a single click without manually modifying query parameters.
3. **High-Precision Telemetry**:
   - Native Python/SQLite3 backend with client-side millisecond behavioral tracking (`stage1Ms`, `stage2Ms`, `stage3Ms`) to identify and filter satisficing respondents.
4. **Real-Time 2×2 Factorial Dashboard & Data Export**:
   - The `/admin` portal renders a live cell matrix of sample distributions and cell means, featuring one-click CSV export with UTF-8 BOM encoding for seamless SPSS/R importing.

---

## 5. Full Survey Instrument & Measurement Scales

The experimental flow enforces strict forward progression across three sequential stages:

### Stage 1: The Decision Conflict Scenario & Initial Choice
- **Vignette Presentation**:
  - **Store Manager (Tacit)**: *"I honestly can't explain it in words. There is no fixed rule to tell you. It's just a gut feeling and intuition after handling tens of thousands of durians over 15 years. Durian A is definitely fuller."*
  - **Data-Driven AI (Statistical Model)**: *"Trained on a massive dataset of 1,000,000+ real durian images (no hand-coded rules). Camera scan terminal displays: Neural Network Output: Recommend Durian B (Confidence Score: 94.8% / 58.2%)."*
- **Questions**:
  - **Q1. [Binary Behavioral Choice]**
    Facing the manager's intuition (which he cannot verbally explain) and the data-driven AI's prediction, which durian do you decide to choose?
    - `Option A`: Choose Durian A (Follow the Veteran Store Manager)
    - `Option B`: Choose Durian B (Follow the Data-Driven AI)
  - **Pre-Outcome Cognitive Scales (7-Point Likert: 1 = Strongly Disagree, 7 = Strongly Agree)**:
    - **Q2 (Perceived Data Objectivity)**: Compared to the manager’s unexplainable personal intuition, an AI model trained on a massive dataset of over a million images feels more objective and reliable to me.
    - **Q3 (Confidence Score Impact)**: The specific confidence percentage displayed by the AI (94.8% / 58.2%), heavily influenced my choice just now.
    - **Q4 (Skepticism Toward Ineffable Intuition)**: If a human expert cannot verbally explain the reasoning behind their judgment, I find it difficult to trust their recommendation.

### Stage 2: Outcome Revelation & Post-Outcome Attribution
- **Ground Truth Revelation**:
  - *If AI Fails*: *"Both durians are cut open on the spot: Durian A (recommended by the manager) is packed with 5 large, full chambers of golden pulp. Durian B (recommended by the AI) has a thick shell and is mostly hollow with undeveloped dead chambers inside. The manager's intuition proved completely correct!"*
  - *If AI Succeeds*: *"Both durians are cut open on the spot: Durian B (recommended by the AI) is packed with 5 large, full chambers of golden pulp. Durian A (recommended by the manager) has a thick shell and is mostly hollow with undeveloped dead chambers inside. The AI's prediction proved completely correct!"*
- **Post-Outcome Attribution & Trust Scales (7-Point Likert: 1 = Strongly Disagree, 7 = Strongly Agree)**:
  - **Q5 (Probabilistic Limitation Attribution - Rational Dimension)**: Whether relying on big-data AI or human intuition, sorting natural fruits always involves probabilistic uncertainty; the side that failed simply encountered an unavoidable statistical outlier.
  - **Q6 ("Bullshitting" Attribution - Frankfurtian Experimental Philosophy Dimension)**: Looking back at the AI's prediction and confidence score, I feel the AI has no genuine grasp of what makes a good durian—it is merely engaging in "bullshitting" (bluffing with numbers without true understanding).
  - **Q7 (Perceived Deception & Manipulation - Anthropomorphic Intentional Projection)**: I feel the AI’s presentation of "massive dataset training" and a "precise confidence percentage" was misleading, making me feel somewhat manipulated or deceived.
  - **Q8 (Re-evaluation of Tacit Knowledge Value - Knowledge Science Dimension)**: After seeing this outcome, I believe that in complex physical tasks, a human expert’s ineffable intuition (tacit knowledge) holds unique value that dataset-trained AI cannot easily replace.
  - **Q9 (Future Automation Bias Retention / Trust Disposition)**: Next time I face a similar real-world judgment task, I would prefer to rely on the data-driven AI rather than a human expert's unexplainable intuition.

### Stage 3: Demographic & Control Variables
- **Q10. Gender**: [Male / Female / Other or Prefer not to say]
- **Q11. Age Group**: [Under 20 / 20–29 / 30–39 / 40–49 / 50+]
- **Q12. Disciplinary Background**: [Yes (STEM / Computer Science / Data / AI) / No (Humanities / Business / Arts / Other)]
- **Q13. Daily AI Tool Usage Frequency**: [Rarely / 1–2 times per week / Daily / Heavy reliance]

---

## 6. Statistical Hypotheses & Analysis Plan

### 6.1 Statistical Hypotheses
1. **Hypothesis 1 (H1: Main Effect of Confidence on Initial Decision)**:
   - In Stage 1 prior to outcome revelation, participants in the **High Confidence conditions (94.8%) will demonstrate a significantly higher rate of choosing AI-recommended Durian B (Q1)**, and report significantly higher perceived objectivity (Q2) and confidence anchoring (Q3), than participants in the Low Confidence conditions (58.2%) ($p < .001$).
2. **Hypothesis 2 (H2: Main Effect of Realized Outcome on Epistemic Attribution)**:
   - When exposed to AI failure (Conditions 1 & 2), **participants will assign significantly higher ratings to "Bullshitting" attribution (Q6) and Perceived Deception (Q7)**, and significantly higher appreciation for tacit knowledge (Q8), compared to participants in the AI success conditions ($p < .001$).
3. **Hypothesis 3 (H3: Interaction Effect - "The Penalty of Overconfidence")**:
   - There will be a significant interaction between AI Confidence and Realized Outcome on Bullshitting Attribution (Q6) and Future Trust Destruction (Q9) ($F(1, N-4) > 0, p < .01$).
   - *Mechanistic Pattern*: When AI fails under high confidence (Condition 1: 94.8%), the psychological backlash is acute and nonlinear: the surge in perceived "bullshitting" and the collapse of future trust (Q9) will be substantially greater than when AI fails under low confidence (Condition 2: 58.2%). Conversely, in the success conditions, the confidence level exerts a milder effect. This empirically establishes the cognitive penalty for uncalibrated algorithmic overconfidence.

### 6.2 Analytical Pipeline & Modeling Framework
- **Binary Decision Model (Q1)**: Binary Logistic Regression:
  $$\\text{{logit}}(P(Q1 = \\text{{AI}})) = \\beta_0 + \\beta_1 (\\text{{Confidence}}) + \\beta_2 (\\text{{STEM}}) + \\beta_3 (\\text{{AIFreq}})$$
- **Factorial Analysis of Variance (Q2–Q9)**: Two-Way Factorial ANOVA:
  $$Y_{{ijk}} = \\mu + \\alpha_i (\\text{{Confidence}}) + \\beta_j (\\text{{Outcome}}) + (\\alpha\\beta)_{{ij}} + \\epsilon_{{ijk}}$$
- **Covariate Analysis (ANCOVA)**: Testing STEM disciplinary background and daily AI tool usage frequency as potential cognitive moderators attenuating vulnerability to confidence inducement.

---

### [Summary & Acknowledgments]
This revised research architecture integrates Prof. Mizumoto's guidance regarding Polanyian ineffability, data-driven machine learning paradigms, and factorial vignette methodology. The live experimental infrastructure is fully active and validated for immediate academic data collection.
"""

# ==============================================================================
# 2. DOCX BUILDER WITH ELEGANT ACADEMIC STYLING
# ==============================================================================

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

def add_callout(doc, text_list, border_color="4F46E5", bg_color="F8FAFC"):
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
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    for idx, item in enumerate(text_list):
        if idx > 0:
            p = cell.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
        run = p.add_run(item)
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def format_academic_table(table, col_widths, headers, data):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    # Header row
    hdr_cells = table.rows[0].cells
    for i, header_text in enumerate(headers):
        hdr_cells[i].text = header_text
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], "1E293B")
        set_cell_margins(hdr_cells[i], top=120, bottom=120, left=140, right=140)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.bold = True
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            
    # Data rows
    for r_idx, row_data in enumerate(data):
        row_cells = table.add_row().cells
        bg_color = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, cell_value in enumerate(row_data):
            row_cells[c_idx].text = cell_value
            row_cells[c_idx].width = col_widths[c_idx]
            set_cell_background(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], top=100, bottom=100, left=140, right=140)
            p = row_cells[c_idx].paragraphs[0]
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(2)
            for r in p.runs:
                r.font.size = Pt(9)
                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
                if c_idx == 0:
                    r.font.bold = True

def build_docx_report(lang="CN"):
    doc = docx.Document()
    
    # 1 inch margins
    for sec in doc.sections:
        sec.top_margin = Inches(1.0)
        sec.bottom_margin = Inches(1.0)
        sec.left_margin = Inches(1.0)
        sec.right_margin = Inches(1.0)
        
    is_cn = (lang == "CN")
    
    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(4)
    run_title = p_title.add_run(
        "《数据驱动型 AI 与不可言传的专家直觉：人机决策冲突中的置信度诱导与结果归因研究》" if is_cn
        else "Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts"
    )
    run_title.font.size = Pt(16)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    
    # Subtitle
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(16)
    run_sub = p_sub.add_run(
        "副课题研究计划与实验问卷方案（审阅定稿版）" if is_cn
        else "Minor Research Project Design & Experimental Survey Instrument (Final Review Version)"
    )
    run_sub.font.size = Pt(11.5)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(0x47, 0x55, 0x69)
    
    # Metadata Box
    meta_info = [
        "【基本信息 / Metadata】" if is_cn else "[Metadata & Affiliation]",
        "• 研究者 / Researcher: XIU TIANYUAN (修 天源) — JAIST 知识科学系 修士2年 (M2)",
        "• 指导教授 / Supervisor: 水本 教授 (Prof. Mizumoto)",
        "• 提交日期 / Date: 2026年10月18日 (October 18, 2026)",
        "• 研究领域 / Field: 知识科学 (Knowledge Science)、实验哲学 (Experimental Philosophy)、人机交互 (HCI)",
        f"• 在线实验系统 / Live System: {PUBLIC_URL}",
        f"• 导师管理后台 / Admin Console: {ADMIN_URL}"
    ] if is_cn else [
        "[Metadata & Affiliation]",
        "• Researcher: XIU TIANYUAN (修 天源) — JAIST School of Knowledge Science, M2",
        "• Academic Advisor: Prof. Mizumoto (水本 教授)",
        "• Date: October 18, 2026",
        "• Primary Fields: Knowledge Science, Experimental Philosophy, HCI, Cognitive Psychology",
        f"• Participant Survey URL: {PUBLIC_URL}",
        f"• Admin & Analytics Dashboard: {ADMIN_URL}"
    ]
    add_callout(doc, meta_info, border_color="3B82F6", bg_color="F0F9FF")
    
    def add_heading_1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(16)
        h.paragraph_format.space_after = Pt(6)
        r = h.add_run(text)
        r.font.size = Pt(13)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        return h

    def add_heading_2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(10)
        h.paragraph_format.space_after = Pt(4)
        r = h.add_run(text)
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
        return h

    def add_body_p(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.2
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.font.size = Pt(10)
            rb.font.bold = True
            rb.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
        r = p.add_run(text)
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
        return p

    if is_cn:
        # SECTION 1
        add_heading_1("1. 研究背景与理论演进 (Background & Theoretical Framework)")
        add_body_p(
            "在知识科学与认识论经典理论中，迈克尔·波兰尼（Michael Polanyi, 1966）揭示了“我们知道的多于我们能言说的（We can know more than we can tell）”。真正的高阶人类专家直觉往往属于无法言传的隐性知识（Tacit Knowledge）。然而，当代深度学习视觉模型并非依靠显性规则算法，而是基于海量数据集（Massive Datasets）拟合高维概率分布，并输出精确的置信度百分比（Confidence Score）。当不可言传的专家经验与高置信度的数据驱动 AI 发生决策冲突时，构成了独特的认知诱导与错误归因研究情境。"
        )
        add_heading_2("1.1 回应水本教授指导意见的四大核心修正")
        add_body_p(
            "从“显性算法（Algorithm）”转向“数据驱动黑盒（Data-Driven AI）”：全面移除几何夹角与曲率规则等显性算法描述，确立 AI 系统由 100 万张真实图像数据集训练而成，仅输出统计置信度（94.8% vs 58.2%）。",
            "1. 数据驱动黑盒重构："
        )
        add_body_p(
            "确立真正的“不可言传隐性知识（Ineffable Tacit Knowledge）”：店长拥有 15 年经验但明确声明无法用语言阐述判别因果，消除专家口述显性规则被机器学习轻易模仿的理论漏洞。",
            "2. 隐性知识本体论对齐："
        )
        add_body_p(
            "砍掉事前盲猜阶段（Phase 1）：彻底消除受试者自主猜测所带来的“先验锚定效应”与“自我一致性承诺偏差”，严格采用国际标准的实验哲学情境实验法（Vignette Paradigm）。",
            "3. 消除锚定混杂变量："
        )
        add_body_p(
            "采用标准 2×2 组间析因实验设计（Between-Subjects Design）：建立 AI 置信度（94.8% vs 58.2%）与开壳结果（AI 失败 vs AI 成功）构成的四组正交实验条件。",
            "4. 规范组间实验范式："
        )
        
        # SECTION 2
        add_heading_1("2. 2×2 组间实验设计矩阵 (2×2 Between-Subjects Experimental Design)")
        add_body_p("实验情境为挑选成熟榴莲内部饱满度。店长凭不可言传的 15 年手感直觉力荐 A 号；基于百万图像训练的视觉 AI 推荐 B 号。开壳后黑白分明地展示内部果肉发育结果。")
        
        col_w = [Inches(1.2), Inches(1.3), Inches(1.3), Inches(2.7)]
        headers = ["实验组别", "自变量1: AI置信度", "自变量2: 开壳结果", "情境与开壳呈现特征"]
        data = [
            ["Condition 1", "高置信度 (94.8%)", "AI 失败 (店长正确)", "AI 显示 94.8% 荐 B；开壳显示 A 满5房黄金果肉，B 为中空死包"],
            ["Condition 2", "低置信度 (58.2%)", "AI 失败 (店长正确)", "AI 显示 58.2% 荐 B；开壳显示 A 满5房黄金果肉，B 为中空死包"],
            ["Condition 3", "高置信度 (94.8%)", "AI 成功 (店长失误)", "AI 显示 94.8% 荐 B；开壳显示 B 满5房黄金果肉，A 为中空死包"],
            ["Condition 4", "低置信度 (58.2%)", "AI 成功 (店长失误)", "AI 显示 58.2% 荐 B；开壳显示 B 满5房黄金果肉，A 为中空死包"]
        ]
        t = doc.add_table(rows=1, cols=4)
        format_academic_table(t, col_w, headers, data)
        doc.add_paragraph().paragraph_format.space_after = Pt(6)

        # SECTION 3
        add_heading_1("3. 在线实验系统与部署特性 (Online Deployment & Interactive System)")
        add_body_p(f"问卷系统主链接：{PUBLIC_URL}")
        add_body_p(f"导师后台管理平台：{ADMIN_URL}")
        add_body_p("系统特点：原生 Python + SQLite 3 独立存储引擎，Vue 3 现代化白色学术界面，支持英、日、中三语即时切换，毫秒级阶段计时埋点，支持一键导出包含 UTF-8 BOM 的 CSV 统计原始数据。问卷顶部已集成条件直选按钮 [C1 | C2 | C3 | C4]，方便导师即时预览全部 4 组情境。")

        # SECTION 4
        add_heading_1("4. 实验问卷完整题项与量表设计 (Full Survey Instrument)")
        add_heading_2("第一阶段：决策前冲突与认知感知 (Stage 1)")
        add_body_p("Q1. 【二元决策选择】面对店长无法解释的直觉与 AI 系统预测，您选择买哪一颗？[选项 A: 选 A号 (店长) | 选项 B: 选 B号 (AI)]")
        add_body_p("Q2（数据客观性感知，7级李克特）：相比于店长“说不清道不明”的个人直觉，基于百万级数据集训练出来的 AI 模型让我觉得更加客观、可靠。")
        add_body_p("Q3（置信度锚定效应，7级李克特）：AI 给出的置信度百分比（94.8% / 58.2%），对我刚才做出选择起到了决定性的引导作用。")
        add_body_p("Q4（对不可言传经验的怀疑，7级李克特）：如果人类专家无法用清晰的语言解释他的判断逻辑，我很难放心把决定权交给他。")
        
        add_heading_2("第二阶段：开壳真实结果揭晓与归因测量 (Stage 2)")
        add_body_p("Q5（概率统计归因 - 理性维度，7级）：挑选果实存在概率不确定性，失败的一方只是恰好遇到了统计分布外的例外，情有可原。")
        add_body_p("Q6（“胡扯/不懂装懂”归因 - 哲学 Bullshitting 维度，7级）：回顾 AI 的预测和置信度，我认为 AI 根本没有真正“理解”榴莲特征，它只是在用数字进行盲目的胡扯（Bullshitting）或虚张声势。")
        add_body_p("Q7（误导与受骗感 - 拟人化意图投射，7级）：我觉得 AI 展示的“大数据背景”和“精确百分比”具有误导性，让我产生了一种被技术表象“操纵或欺骗”的感觉。")
        add_body_p("Q8（对隐性知识的重估 - 知识科学维度，7级）：看到结果后，我认为在现实物理任务中，人类难以言传的“经验直觉（暗黙知）”具有数据模型无法替代的价值。")
        add_body_p("Q9（未来信任倾向 / 自动化偏差留存，7级）：如果下次还要挑选榴莲或进行类似鉴别，我依然更愿意相信大数据 AI 的预测，而不是人类行家的直觉。")
        
        add_heading_2("第三阶段：受试者人口学信息 (Stage 3)")
        add_body_p("Q10 生理性别、Q11 年龄区间、Q12 是否具备 STEM / 计算机 / AI 相关学科背景、Q13 日常 AI 工具使用频率。")

        # SECTION 5
        add_heading_1("5. 统计假设与双因素方差分析方案 (Statistical Hypotheses & Analysis Plan)")
        add_body_p("H1（置信度主效应）：在开壳前，高置信度组（94.8%）选择 AI 的比例（Q1）及数据客观性感知（Q2, Q3）显著高于低置信度组（58.2%）（p < .001）。证明高确定性包装能强力诱发自动化偏差。")
        add_body_p("H2（结果主效应与意图投射）：当 AI 失败时，受试者在法兰克福式“胡扯（Bullshitting）”归因（Q6）与“受骗感”（Q7）上的得分显著高于 AI 成功组（p < .001）。证明公众倾向于对黑盒错误进行拟人化意图投射。")
        add_body_p("H3（交互效应 - “高置信度失败的背叛惩罚”）：置信度与开壳结果在“胡扯归因”（Q6）与“未来信任摧毁”（Q9）上存在显著交互作用（F(1, N-4) > 0, p < .01）。高置信度失败（Condition 1）将激发出最强烈的负面心理反弹与信任清算，其崩溃幅度显著大于低置信度失败（Condition 2）。")
        add_body_p("分析方案：采用二元 Logistic 回归分析 Q1 决策偏好；采用 2×2 双因素方差分析（Two-Way ANOVA）模型 Y_ijk = μ + α_i + β_j + (αβ)_ij + ε_ijk 检验 Q2–Q9，并以理工科背景（Q12）和 AI 经验（Q13）为协变量开展 ANCOVA 检验。")

    else:
        # SECTION 1 (EN)
        add_heading_1("1. Background & Theoretical Framework")
        add_body_p(
            "In classic Knowledge Science and Epistemology, Michael Polanyi (1966) famously formulated that 'we can know more than we can tell.' True expert intuition resides in ineffable tacit knowledge, grounded in somatic experience and Gestalt perception. Conversely, modern deep-learning visual models do not operate on explicit algorithms, but on statistical high-dimensional pattern fitting across massive datasets, outputting exact quantitative confidence scores (e.g., 94.8% vs. 58.2%). The collision between ineffable expert intuition and data-driven AI authority establishes a profound cognitive context for studying automation bias and outcome attribution."
        )
        add_heading_2("1.1 Four Core Revisions Guided by Prof. Mizumoto")
        add_body_p(
            "Shift from 'Explicit Algorithm' to 'Data-Driven AI': Replaced all hand-crafted geometric rules (angles, curvature) with deep neural networks trained on 1,000,000+ real images, outputting purely statistical confidence percentages.",
            "1. Data-Driven Paradigm: "
        )
        add_body_p(
            "Genuine Ineffable Tacit Knowledge: The store manager has 15 years of experience but explicitly states he cannot verbally articulate his criteria, adhering strictly to Polanyian ineffability.",
            "2. Ineffable Tacit Stance: "
        )
        add_body_p(
            "Elimination of Phase 1 Blind Guessing: Eradicated prior anchoring and self-consistency biases, adopting the standard vignette experimental methodology in experimental philosophy.",
            "3. Confounder Elimination: "
        )
        add_body_p(
            "Rigorous 2×2 Between-Subjects Factorial Matrix: Orthogonally crossing AI Confidence Level (High 94.8% vs. Low 58.2%) with Realized Outcome (AI Fails vs. AI Succeeds) across four independent groups.",
            "4. Factorial Design: "
        )

        # SECTION 2 (EN)
        add_heading_1("2. 2×2 Between-Subjects Experimental Design Matrix")
        add_body_p("Participants are tasked with selecting the durian with the fullest pulp chambers. The veteran manager recommends Durian A based on ineffable touch; the data-driven AI recommends Durian B based on 1M+ image training. Physical cut-open revelation serves as ground truth.")
        
        col_w = [Inches(1.2), Inches(1.3), Inches(1.3), Inches(2.7)]
        headers = ["Condition", "Factor 1: AI Confidence", "Factor 2: Outcome", "Stimulus & Outcome Operationalization"]
        data = [
            ["Condition 1", "High Confidence (94.8%)", "AI Fails (Manager Correct)", "AI outputs 94.8% for B; Cut-open reveals A is full (5 chambers) and B is empty dead-pod"],
            ["Condition 2", "Low Confidence (58.2%)", "AI Fails (Manager Correct)", "AI outputs 58.2% for B; Cut-open reveals A is full (5 chambers) and B is empty dead-pod"],
            ["Condition 3", "High Confidence (94.8%)", "AI Succeeds (Manager Fails)", "AI outputs 94.8% for B; Cut-open reveals B is full (5 chambers) and A is empty dead-pod"],
            ["Condition 4", "Low Confidence (58.2%)", "AI Succeeds (Manager Fails)", "AI outputs 58.2% for B; Cut-open reveals B is full (5 chambers) and A is empty dead-pod"]
        ]
        t = doc.add_table(rows=1, cols=4)
        format_academic_table(t, col_w, headers, data)
        doc.add_paragraph().paragraph_format.space_after = Pt(6)

        # SECTION 3 (EN)
        add_heading_1("3. Online Interactive System Architecture & Live Access Links")
        add_body_p(f"Participant Survey Web Application: {PUBLIC_URL}")
        add_body_p(f"Live Administrator Dashboard: {ADMIN_URL}")
        add_body_p("Technical Infrastructure: Lightweight Python + SQLite 3 relational backend, Vue 3 clean academic white theme, instant EN/JA/ZH localization, millisecond behavioral telemetry (stage1Ms, stage2Ms, stage3Ms), and one-click UTF-8 BOM CSV data export. Condition quick-switch buttons [C1 | C2 | C3 | C4] are embedded at the top of the survey interface for instantaneous inspection.")

        # SECTION 4 (EN)
        add_heading_1("4. Full Survey Instrument & Measurement Scales")
        add_heading_2("Stage 1: Pre-Outcome Decision Conflict (Stage 1)")
        add_body_p("Q1. [Binary Choice] Facing the manager's unexplainable intuition and data-driven AI, which durian do you choose? [Option A (Manager) | Option B (AI)]")
        add_body_p("Q2 (Perceived Data Objectivity, 7-point Likert): Compared to the manager's personal intuition, an AI model trained on over a million images feels more objective and reliable.")
        add_body_p("Q3 (Confidence Score Anchoring, 7-point Likert): The specific confidence percentage displayed by the AI (94.8% / 58.2%) heavily influenced my choice just now.")
        add_body_p("Q4 (Skepticism toward Ineffable Intuition, 7-point Likert): If a human expert cannot verbally explain the reasoning behind their judgment, I find it difficult to trust their recommendation.")

        add_heading_2("Stage 2: Outcome Revelation & Post-Outcome Attribution (Stage 2)")
        add_body_p("Q5 (Probabilistic Limitation Attribution - Rational Dimension, 7-point Likert): Sorting natural fruits always involves statistical uncertainty; the failed side simply encountered an unavoidable outlier.")
        add_body_p("Q6 ('Bullshitting' Attribution - Frankfurtian Experimental Philosophy, 7-point Likert): Looking back at the AI's prediction and confidence score, I feel the AI has no genuine grasp of durians—it is merely 'bullshitting' (bluffing with numbers without understanding).")
        add_body_p("Q7 (Perceived Deception & Manipulation, 7-point Likert): I feel the AI’s presentation of 'massive dataset training' and 'precise confidence percentage' was misleading, making me feel somewhat manipulated or deceived.")
        add_body_p("Q8 (Re-evaluation of Tacit Knowledge, 7-point Likert): In complex physical tasks, a human expert's ineffable intuition (tacit knowledge) holds unique value that dataset-trained AI cannot easily replace.")
        add_body_p("Q9 (Future Automation Bias Retention / Trust Disposition, 7-point Likert): Next time I face a similar judgment task, I would prefer to rely on data-driven AI rather than a human expert's unexplainable intuition.")

        add_heading_2("Stage 3: Demographics & Control Variables (Stage 3)")
        add_body_p("Q10 Gender, Q11 Age Group, Q12 STEM / Computer Science / AI Background, Q13 Daily AI Tool Usage Frequency.")

        # SECTION 5 (EN)
        add_heading_1("5. Statistical Hypotheses & Analysis Plan")
        add_body_p("H1 (Confidence Main Effect): Prior to outcome reveal, High Confidence conditions (94.8%) will produce a significantly higher rate of selecting AI (Q1) and higher perceived objectivity (Q2, Q3) than Low Confidence conditions (58.2%) (p < .001).")
        add_body_p("H2 (Outcome Main Effect): When AI fails, Bullshitting Attribution (Q6) and Perceived Deception (Q7) will be significantly higher than when AI succeeds (p < .001), indicating anthropomorphic intentional projections onto algorithmic errors.")
        add_body_p("H3 (Interaction Effect - 'The Penalty of Overconfidence'): A significant interaction on Bullshitting Attribution (Q6) and Future Trust Destruction (Q9) (F(1, N-4) > 0, p < .01). When an AI fails under 94.8% confidence (Condition 1), the backlash is acute and nonlinear, producing significantly greater trust collapse than low-confidence failure (Condition 2).")
        add_body_p("Analytical Framework: Binary Logistic Regression for Q1; Two-Way Factorial ANOVA (Y_ijk = μ + α_i + β_j + (αβ)_ij + ε_ijk) for Q2–Q9; ANCOVA incorporating STEM background and AI familiarity as potential cognitive moderators.")

    # Save
    out_name = f"Minor_Research_Report_{lang}_20261018.docx"
    out_path = os.path.join(BASE_DIR, out_name)
    doc.save(out_path)
    print(f"Generated DOCX: {out_path}")
    
    # Copy to Desktop
    desktop_path = os.path.join(DESKTOP_DIR, out_name)
    shutil.copyfile(out_path, desktop_path)
    print(f"Copied to Desktop: {desktop_path}")

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    os.makedirs(DESKTOP_DIR, exist_ok=True)
    
    # 1. Chinese Markdown
    cn_md = build_cn_markdown()
    cn_md_path = os.path.join(BASE_DIR, "Minor_Research_Report_CN_20261018.md")
    with open(cn_md_path, "w", encoding="utf-8") as f:
        f.write(cn_md)
    print(f"Generated Markdown: {cn_md_path}")
    shutil.copyfile(cn_md_path, os.path.join(DESKTOP_DIR, "Minor_Research_Report_CN_20261018.md"))
    print(f"Copied Markdown to Desktop: {os.path.join(DESKTOP_DIR, 'Minor_Research_Report_CN_20261018.md')}")
    
    # 2. English Markdown
    en_md = build_en_markdown()
    en_md_path = os.path.join(BASE_DIR, "Minor_Research_Report_EN_20261018.md")
    with open(en_md_path, "w", encoding="utf-8") as f:
        f.write(en_md)
    print(f"Generated Markdown: {en_md_path}")
    shutil.copyfile(en_md_path, os.path.join(DESKTOP_DIR, "Minor_Research_Report_EN_20261018.md"))
    print(f"Copied Markdown to Desktop: {os.path.join(DESKTOP_DIR, 'Minor_Research_Report_EN_20261018.md')}")
    
    # 3. Chinese DOCX
    build_docx_report("CN")
    
    # 4. English DOCX
    build_docx_report("EN")
    
    print("\nAll 4 reports generated and mirrored to Desktop successfully!")

if __name__ == "__main__":
    main()
