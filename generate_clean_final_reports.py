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

PUBLIC_URL = "https://durian-experiment.vercel.app"
ADMIN_URL = f"{PUBLIC_URL}/admin"

# ==============================================================================
# 1. STANDALONE ACADEMIC MARKDOWN CONTENT (CN & EN)
# ==============================================================================

def get_cn_markdown():
    return f"""# 人类直觉 vs. 人工直觉：当两个“不可言传的黑盒”发生决策冲突时的认识论双标与错误归因研究
## 副课题研究计划与实验问卷设计方案

---

### 基本信息
- **研究题目**：人类直觉 vs. 人工直觉：当两个“不可言传的黑盒”发生决策冲突时的认识论双标与错误归因研究
- **英文题目**：*Human Intuition vs. Artificial Intuition: Epistemic Asymmetry and Error Attribution When Two "Ineffable Black Boxes" Conflict*
- **研究者**：修 天源 (XIU TIANYUAN)，北陆先端科学技术大学院大学 (JAIST) 知识科学研究科 博士前期课程二年级 (M2)
- **指导教授**：水本 教授 (Prof. Mizumoto)
- **日期**：2026年11月3日
- **研究领域**：知识科学 (Knowledge Science)、实验哲学 (Experimental Philosophy)、人机交互 (HCI)、认知心理学 (Cognitive Psychology)

---

## 1. 研究背景与核心理论框架 (Background & Theoretical Framework)

### 1.1 两种“不可言传的直觉黑盒”：波兰尼隐性知识与深度学习亚符号表征的认识论同构
在知识科学（Knowledge Science）与认识论（Epistemology）的经典传统中，迈克尔·波兰尼（Michael Polanyi, 1966）提出了著名的隐性知识（Tacit Knowledge）命题：“我们知道的多于我们能言说的（We can know more than we can tell）”。在复杂的现实物理判别任务（如农产品品质甄别、临床触诊、器物鉴定）中，资深人类行家依靠长期具身实践积累的整体完形感知（Gestalt Perception）做出精准判断，但往往无法用显性的语言规则向他人解释自己的判断依据。

然而，随着当代人工智能从早期的“显性符号规则系统（Rule-Based Expert Systems）”演进为“端到端深度学习神经网络（End-to-End Deep Learning）”，一个深刻的认识论现象浮出水面：**当代深度学习 AI 与人类专家在“无法用语言直接解释判断过程”这一点上具有高度的认识论同构性（Epistemic Isomorphism）**。深度学习模型并不依赖人工编写的显性特征规则，而是通过多层神经网络的高维亚符号权重（Sub-symbolic Weights）直接输出预测概率。在给出判断的瞬间，人类专家与深度学习 AI 本质上都是**“不可言传的黑盒（Ineffable Black Boxes）”**——从广义认识论而言，二者的判断都是**“直觉性的（Intuitive）”**（即“人类具身直觉 Human Intuition” vs. “人工统计直觉 Artificial Intuition”），尽管 AI 在事后（Post-hoc）或许可以通过显著图或特征归因算法尝试提取显性特征。

### 1.2 严格对称的基准控制：有限破坏性采样样本量、历史总体准确率与个案把握度
为了纯粹地检验人类决策者对“人类直觉”与“AI 直觉”是否存在认识论上的双重标准（Epistemic Double Standards），必须在实验设计中消除信息量与能力不对等带来的混杂偏误（Confounding Bias）：
1. **受物理核验制约的同等有限训练样本量（~3,000 颗开壳品尝样本）**：在诸如未开壳榴莲品质甄别等物理任务中，无论人类还是 AI，仅凭肉眼或摄像头“观察外观”虽然可以接触上万颗果实，但要获得“内部果肉是否饱满、口感是否甘甜”的真实标签（Ground Truth），必须经历**切开果壳并实际品尝的破坏性核验（Destructive Verification）**。因此，真正具有结果反馈的有效训练样本在现实中必然是有限的。本研究严格设定资深店长与深度学习 AI 均是从**约 3,000 颗真正切开并品尝过果肉的榴莲样本**中习得各自的直觉表征。
2. **完全相同的历史总体准确率（85% Overall Accuracy）**：双方在过往标准化盲测中的历史总体准确率完全一致，均为 **85%**（即平均每判断 100 颗榴莲，双方各有 85 颗判断正确、15 颗失误）。
3. **完全匹配的个案把握度（Matched Case-Specific Confidence: 90% vs. 90% 或 60% vs. 60%）**：在面对当前具体的两颗榴莲（A 号与 B 号）时，店长对推荐 A 号的主观把握度与 AI 对推荐 B 号的模型置信度严格对齐——在“双高把握度”条件下双方均为 **90% 笃定**，在“双低把握度”条件下双方均为 **60% 吃不准（临界犹豫状态）**。

### 1.3 核心研究问题 (Research Questions)
当训练样本规模（~3,000 例破坏性核验样本）、历史总体准确率（85%）以及当前个案把握度（90% 或 60%）被完全拉平，且人类行家与深度学习 AI 同样无法用语言解释各自的判断依据时，本研究旨在探究以下三个核心科学问题：
- **RQ1（事前选择偏好与不可解释性的认识论双标）**：当“人类直觉”与“AI 直觉”在完全对称的客观基准上发生正面冲突时，决策者更倾向于相信哪一方（Q1）？面对同样“说不出理由”的黑盒状态，人们是否对其中一方抱有更高的“客观性偏见”（Q2），并在“要求必须用语言解释理由”上展现出显著的认识论双重标准（Q4）？
- **RQ2（事后错误归因的不对称性与法兰克福式“胡扯”投射）**：当现场切开榴莲、客观真相揭晓（必有一方判断正确、另一方彻底失败）后，人们对“失败的 AI”与“失败的人类店长”是否采取截然不同的归因逻辑？具体而言，当 AI 的直觉失败时，人们是否比面对人类店长犯同样错误时，更严苛地指责其“毫无真正理解、仅在用数字进行哈里·法兰克福（Frankfurt, 2005）意义上的盲目胡扯（Bullshitting）”（Q6）与“过度自信误导”（Q7），而非理性地归因于 85% 准确率下不可避免的概率例外（Q5）？
- **RQ3（高把握度失败的反噬效应与事后显性特征提取的补偿价值）**：当失败发生在 90% 高把握度条件下时，其引发的信任崩塌是否显著强于 60% 低把握度条件下的失败（过分自信惩罚效应）？此外，鉴于深度学习虽然在判断瞬间同为直觉黑盒，但具备**事后提取并标出显性视觉特征（Post-hoc Feature Extraction）**的技术潜力，这种“事后特征提取能力”在多大程度上能够挽回或提升决策者对 AI 直觉的信任（Q8、Q9）？

---

## 2. $2 \\times 2$ 组间析因实验设计 ($2 \\times 2$ Between-Subjects Experimental Design)

### 2.1 自变量与因变量定义
本研究采用 **$2 \\times 2$ 组间析因实验设计（Between-Subjects Factorial Design）**，正交操纵两个核心自变量：
- **自变量 1：双方的当前个案把握度 / 置信度水平（Matched Case Confidence Level，组间 2 水平）**
  - **双方高把握度（Both High Confidence: 90%）**：店长表示自己有约 **90%** 的把握确定 A 号更好；AI 终端同样显示推荐 B 号的个案置信度为 **90%**。
  - **双方低把握度（Both Low Confidence: 60%）**：店长表示这两颗处于临界状态、自己只有约 **60%** 的把握略倾向于 A 号；AI 终端同样显示推荐 B 号的个案置信度仅为 **60%**。
- **自变量 2：现场开壳真实结果 / 失败主体（Realized Outcome / Who Failed，组间 2 水平）**
  - **AI 失败 / 店长正确（AI Fails / Manager Correct）**：切开验证显示店长推荐的 A 号满 5 房饱满黄金果肉，AI 推荐的 B 号为空壳死包果（此时后续归因题项针对**失败的 AI 系统**）。
  - **店长失败 / AI 正确（Manager Fails / AI Correct）**：切开验证显示 AI 推荐的 B 号满 5 房饱满黄金果肉，店长推荐的 A 号为空壳死包果（此时后续归因题项完全对称地针对**失败的资深店长**）。

### 2.2 $2 \\times 2$ 实验条件分组矩阵

| 实验组别 | 自变量 1：双方个案把握度 | 自变量 2：开壳真实结果（失败方） | 阶段一：对称冲突刺激呈现（双方均基于 ~3,000 例开壳品尝样本，历史总体准确率均为 85%） | 阶段二：现场切开验证结果与对称归因对象 |
| :--- | :--- | :--- | :--- | :--- |
| **Condition 1** | **双方高把握度 (90% vs. 90%)** | **AI 失败 (店长正确)** | 店长凭直觉以 **90%** 把握推荐 A；AI 凭神经网络直觉以 **90%** 置信度推荐 B | A号满5房果肉，B号空壳死包。对称测量受试者对**失败的 AI 系统**（在 90% 把握下失误）的归因 |
| **Condition 2** | **双方低把握度 (60% vs. 60%)** | **AI 失败 (店长正确)** | 店长凭直觉以 **60%** 把握略倾向 A；AI 凭神经网络直觉以 **60%** 置信度略倾向 B | A号满5房果肉，B号空壳死包。对称测量受试者对**失败的 AI 系统**（在 60% 把握下失误）的归因 |
| **Condition 3** | **双方高把握度 (90% vs. 90%)** | **店长失败 (AI 正确)** | 店长凭直觉以 **90%** 把握推荐 A；AI 凭神经网络直觉以 **90%** 置信度推荐 B | B号满5房果肉，A号空壳死包。对称测量受试者对**失败的资深店长**（在 90% 把握下失误）的归因 |
| **Condition 4** | **双方低把握度 (60% vs. 60%)** | **店长失败 (AI 正确)** | 店长凭直觉以 **60%** 把握略倾向 A；AI 凭神经网络直觉以 **60%** 置信度略倾向 B | B号满5房果肉，A号空壳死包。对称测量受试者对**失败的资深店长**（在 60% 把握下失误）的归因 |

---

## 3. 实验问卷完整题项与量表设计 (Complete Survey Instrument)

实验系统采用严格的单向分阶段递进控制（受试者进入阶段二知晓开壳结果后，无法返回阶段一修改初始选择与前测评价）。

### 第一阶段：两种“直觉黑盒”的正面冲突与前测认知评估 (Stage 1)

> **【阶段一：实验情境呈现】**  
> 假设您正在水果店挑选未开壳的榴莲，面前有两颗价格相同的榴莲（**A 号** 与 **B 号**）。为了挑出内部果肉最饱满甘甜的一颗，您同时咨询了店里的**资深人类店长**和店内配置的**深度学习视觉 AI 系统**。  
> *(背景说明：因为只有真正切开并品尝过，才能确知榴莲内部的果肉饱满度与口感，所以无论是这位店长还是这套 AI，其有效训练经验都是有限的——**双方各自都是从大约 3,000 颗真正切开并品尝过的榴莲样本中学习总结出来的**。在过往的标准化盲测中，**店长与 AI 的历史总体准确率完全相同，均为 85%**。同时，店长（依靠人类隐性直觉）与深度学习 AI（依靠多层神经网络黑盒）**都无法用语言解释自己具体的判断规则**——从某种意义上说，二者的判断都是“直觉性的”。)*  
> 面对眼前的 A 号与 B 号，双方给出了完全相反的建议：
>
> - **👨‍🌾 资深店长的直觉判断 ——【推荐 A 号】**  
>   *训练经验：约 3,000 颗切开品尝过的榴莲 | 历史总体准确率：85%*  
>   - **[Condition 1 & 3 高把握度 90%]** 店长说：*“老实说我也没法用语言向你解释具体规则。但凭我切开品尝过约 3,000 颗榴莲攒下的直觉，我对这颗非常有把握——我有大约 **90% 的把握**确定 A 号更好（我的历史总体准确率是 85%）。”*  
>   - **[Condition 2 & 4 低把握度 60%]** 店长说：*“老实说我也没法用语言向你解释具体规则。凭我切开品尝过约 3,000 颗榴莲的直觉，今天这两颗非常接近、很难拿准——我只有大约 **60% 的把握**略微倾向于 A 号（我的历史总体准确率是 85%）。”*
>
> - **🤖 深度学习 AI 系统的直觉判断 ——【推荐 B 号】**  
>   *训练数据：约 3,000 颗切开品尝过的榴莲配对数据 | 历史总体准确率：85%*  
>   - **[Condition 1 & 3 高把握度 90%]** 终端显示：*“历史总体准确率：85% | 当前预测：推荐 B 号（当前个案把握度 / 置信度：**90%**）—— 注：深度神经网络基于高维黑盒特征直接输出直觉概率，无法提供显性的语言解释。”*  
>   - **[Condition 2 & 4 低把握度 60%]** 终端显示：*“历史总体准确率：85% | 当前预测：推荐 B 号（当前个案把握度 / 置信度：**60%**）—— 注：深度神经网络基于高维黑盒特征直接输出直觉概率，无法提供显性的语言解释。”*

#### 1. 行为决策题项
- **Q1.【二元决策选择】** 当“人类店长的直觉”与“深度学习 AI 的直觉”在相同训练样本量（~3,000 颗）、相同总体准确率（85%）以及相同当前把握度（90% 或 60%）下给出相反建议，且双方都无法用语言解释理由时，您决定选择哪一颗？
  - [ ] **选择 A 号**（跟随资深人类店长的直觉）
  - [ ] **选择 B 号**（跟随深度学习 AI 的直觉）

#### 2. 事前认知与认识论双标评估量表（7级李克特量表：1 = 完全不同意，4 = 中立，7 = 完全同意）
- **Q2（两种“直觉”之间的客观性感知）**：即便人类店长和深度学习 AI 拥有完全相同的训练样本量（~3,000 颗）和相同的总体准确率（85%），且同样无法用语言解释理由，我仍然觉得 AI 的“统计直觉”比人类的“具身直觉”更加客观可靠。
- **Q3（当前个案把握度的决策影响）**：双方在当前这颗榴莲上展示出的具体把握度水平（本次均为 **90%** [或 **60%**]），对我刚才的权衡与选择产生了很大影响。
- **Q4（对“无法用语言解释”的认识论双标）**：相比于人类专家“只可意会、说不出理由”的直觉，我更难以容忍一个“同样说不出任何显性规则与理由”的黑盒 AI 系统。

---

### 第二阶段：真实结果揭晓与对称式错误归因量表 (Stage 2)

> **【阶段二：现场开壳验证结果呈现】**
> - **Condition 1 & Condition 2（AI 失败 / 店长正确 — 归因对象 `{{failedAgent}}` = “AI 系统”）**：  
>   *工作人员当场切开了两颗榴莲：**店长推荐的 A 号果肉极其饱满甘甜（满 5 房黄金果肉）；而 AI 推荐的 B 号果壳极厚，内部大部分是未发育的空壳（死包）。最终结果证明：店长的直觉判断完全正确，而 AI 系统的直觉预测失败了！***
> - **Condition 3 & Condition 4（店长失败 / AI 正确 — 归因对象 `{{failedAgent}}` = “人类店长”）**：  
>   *工作人员当场切开了两颗榴莲：**AI 推荐的 B 号果肉极其饱满甘甜（满 5 房黄金果肉）；而店长推荐的 A 号果壳极厚，内部大部分是未发育的空壳（死包）。最终结果证明：AI 系统的直觉预测完全正确，而人类店长的直觉判断失败了！***

#### 事后归因、法兰克福式“胡扯”投射与事后特征提取量表（7级李克特量表：1 = 完全不同意，4 = 中立，7 = 完全同意）
*(注：Q5–Q7 采用严格的对称测量设计——在 Condition 1 & 2 中 `{{failedAgent}}` 自动填入“**AI 系统**”，在 Condition 3 & 4 中自动填入“**人类店长**”，以直接对比受试者对人机双方犯同等错误时的归因双标)*：
- **Q5（概率局限归因 — 理性容错维度）**：既然双方历史总体准确率都是 85%，挑选天然水果本就存在不可避免的概率风险；这次判断失败的**【AI 系统 / 人类店长】**只是恰好遇到了那 15% 的统计例外情况，完全情有可原。
- **Q6（法兰克福式“胡扯 / 不懂装懂”归因 — 实验哲学维度）**：看到这次失败的结果，再回想刚才**【AI 系统 / 人类店长】**无法解释理由却给出 **90% [或 60%]** 把握度的样子，我觉得**【AI 系统 / 人类店长】**其实并没有真正理解这颗榴莲的品质，只是在“虚张声势 / 盲目胡扯（Bullshitting）”。
- **Q7（过度自信与误导感归因 — 责任谴责维度）**：我认为这次失败的**【AI 系统 / 人类店长】**在无法用语言解释具体依据的情况下，依然表现出 **90% [或 60%]** 的把握度，这种做法具有误导性，令我感到失望。
- **Q8（事后显性特征提取的价值 — 可解释 AI 维度）**：虽然人类与深度学习 AI 在做判断的瞬间都依赖“直觉”，但如果 AI 能在事后提取并标出显性的视觉特征（例如标出果刺间距或果壳轮廓的高亮热力图），我对 AI 建议的信任度将会显著超越无法解释理由的人类专家。
- **Q9（未来信任倾向变化 — 远期决策偏好）**：经历了这次开壳验证后，下次面对具有相同历史准确率（85%）但同样无法用语言解释理由的“人类直觉”与“AI 直觉”，我会更倾向于依赖深度学习 AI 而不是人类专家。

---

### 第三阶段：受试者人口学与控制变量 (Stage 3)

- **Q10. 性别**：[ 男 / 女 / 其他或不愿透露 ]
- **Q11. 具体年龄（周岁）**：[ 数字填空题：填写具体整数周岁，如 `24`（限定 16–99 岁连续数值变量） ]
- **Q12. 学科专业背景**：[ 是（理工科 STEM / 计算机 / 数据科学 / AI 相关专业） / 否（人文社科 / 商科 / 艺术 / 其他非理工专业） ]
- **Q13. 日常使用 AI 工具（如 ChatGPT、Claude 等）的频率**：[ 几乎不用 / 每周 1–2 次 / 几乎每天使用 / 重度深度依赖 ]

---

## 4. 统计假设、预期结果与样本量计算 (Hypotheses, Expected Results & Power Analysis)

### 4.1 核心统计假设
- **假设 1（H1：事前认识论双标与个案把握度效应）**：在结果揭晓前的阶段一，尽管店长与 AI 拥有完全相同的训练样本量（~3,000 例）与总体准确率（85%），受试者在面对“无法用语言解释理由”时仍将表现出显著的认识论双标（Q4 均值显著高于中立值 4.0，$p < .001$）；同时，双高把握度组（90% vs. 90%，C1 & C3）在把握度影响权重（Q3）上将显著高于双低把握度组（60% vs. 60%，C2 & C4）。
- **假设 2（H2：失败主体的不对称归因主效应 — “对 AI 错误的严苛惩罚”）**：在阶段二结果揭晓后，比较“AI 失败组（C1 & C2）”与“店长失败组（C3 & C4）”对各自失败主体的归因得分：当 AI 预测失败时，受试者对失败 AI 的法兰克福式“胡扯（Bullshitting）”归因（Q6）与“误导失望感”（Q7）将显著高于人类店长犯同等错误时受到的指责（$p < .001$），而在理性概率豁免（Q5）上的得分将显著低于店长失败组。
- **假设 3（H3：个案把握度 $\\times$ 失败主体的二阶交互效应与事后特征提取补偿）**：个案把握度（90% vs. 60%）与失败主体（AI 失败 vs. 店长失败）在 Q6、Q7 及 Q9 上存在显著二阶交互作用（$p < .01$）。“90% 高把握度下的失败”比“60% 低把握度下的失败”引发显著更强的信任反噬，且该惩罚斜率在 AI 失败时（C1 vs. C2）显著陡峭于店长失败时（C3 vs. C4）。此外，Q8 将呈现显著正向得分（$> 5.0$），证明“事后提取并标出显性特征”对修复 AI 直觉信任的关键作用。

### 4.2 预期结果与先验样本量计算 (Expected Results & A Priori Power Analysis)
基于上述假设，设定各阶段核心指标的大致预期表现（7 级李克特量表，1–7 分，假定组内标准差 $SD \\approx 1.15$）：
1. **阶段一预期表现**：在完全对称基线下，预计约 **55%–60%** 受试者选择人类直觉（A号），**40%–45%** 选择 AI 直觉（B号）；认识论双标量表（Q4）预期均值约为 **$M = 5.10, SD = 1.20$**（显著高于中立值 $4.0$，单样本效应量 Cohen's $d \\approx 0.92$）。
2. **阶段二核心因变量（以 Q6 法兰克福式“胡扯”归因为代表）的 $2 \\times 2$ 预期单元均值**：

| 实验条件组 | 自变量 1：把握度 | 自变量 2：失败主体 | 预期均值 ($M$) | 预期标准差 ($SD$) | 实质效应预期 |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Condition 1** | 高把握度 (90%) | AI 系统失败 | **5.60** | 1.15 | 强烈认识论反噬：高把握翻车的黑盒 AI 被高度归因为“盲目胡扯” |
| **Condition 2** | 低把握度 (60%) | AI 系统失败 | **3.80** | 1.15 | 当 AI 事先表明仅 60% 临界把握时，指责显著缓和（$\\Delta_{{\\text{{AI}}}} = +1.80$） |
| **Condition 3** | 高把握度 (90%) | 人类店长失败 | **3.60** | 1.15 | 对人类行家经验失手的容忍度较高 |
| **Condition 4** | 低把握度 (60%) | 人类店长失败 | **3.40** | 1.15 | 被高度豁免为正常的 15% 统计例外（$\\Delta_{{\\text{{Human}}}} = +0.20$） |

3. **基于预期均值的样本量推算（$\\alpha = 0.05$，统计检验力 $1 - \\beta = 0.80$，$2 \\times 2$ 固定效应方差分析，$df_1 = 1$）**：
   - **失败主体主效应**（$\\mu_{{\\text{{AI}}}} = 4.70$ vs. $\\mu_{{\\text{{Human}}}} = 3.50$，主效应偏差 $|\\beta| = 0.60$）：效应量 Cohen's $f = 0.60 / 1.15 = \\mathbf{{0.52}}$，最低仅需 **$N = 32$ 人**（每组 8 人）；
   - **把握度主效应**（$\\mu_{{90\\%}} = 4.60$ vs. $\\mu_{{60\\%}} = 3.60$，主效应偏差 $|\\alpha| = 0.50$）：效应量 Cohen's $f = 0.50 / 1.15 = \\mathbf{{0.43}}$，最低仅需 **$N = 45$ 人**（每组 12 人）；
   - **二阶交互效应**（$|\\gamma| = |(5.60 - 3.80) - (3.60 - 3.40)| / 4 = 0.40$）：交互效应量 **Cohen's $f = 0.40 / 1.15 = \\mathbf{{0.35}}$**。在 $\\alpha = 0.05, 1 - \\beta = 0.80$ 标准下，检验该交互效应所需的最低有效总样本量为 **$N = 68$ 人（即每组 $n = 17$ 人）**。
   - 计入约 15% 的注意力筛查与无效卷缓冲，单一语种样本池的目标招募人数定为 **$N = 80$ 人（每组 $n = 20$ 人）**。

### 4.3 目标受试者群体与跨文化范围界定 (Target Participants & Cultural Scope)
- **基准方案（单一文化同质样本控制）**：为避免语言与文化差异在 $2 \\times 2$ 组间设计中引入额外混杂方差，本研究基准方案聚焦单一母语群体（例如招募 **$N = 68\\text{{–}}80$ 名日语母语成年受试者**，正式发放时将问卷显示界面锁定为日文 `?lang=ja&locklang=1`；若由研究者个人渠道独立招募，亦可同理锁定为单一中文界面招募 $N = 68\\text{{–}}80$ 名中文母语者）。审阅链接内置的英、日、中文切换供学术指导与审阅使用。
- **可选跨文化扩展假说（若同步采集多语种样本）**：若研究同时采集日本与中文母语受试者（每语种各 $N = 68\\text{{–}}80$ 人），可进一步检验探索性文化差异假说（H4）：受传统“职人（職人 / *Shokunin*）”具身技艺传统的影响，日本受试者在面对不可言传的判断时，是否比处于高频算法推荐消费环境中的中国受试者对“人类直觉”表现出更高的偏好与失误宽容度。

### 4.4 统计检验模型
1. **二项检验与二元 Logistic 回归（Q1）**：控制连续年龄（Q11）、理工科背景（Q12）与日常 AI 频率（Q13）：
   $$\\text{{logit}}(P(\\text{{Choice}} = \\text{{AI}})) = \\beta_0 + \\beta_1 \\cdot \\text{{ConfidenceLevel}} + \\beta_2 \\cdot \\text{{Age}} + \\beta_3 \\cdot \\text{{STEM}} + \\beta_4 \\cdot \\text{{AIFreq}}$$
2. **$2 \\times 2$ 组间双因素方差分析与协方差分析（ANOVA / ANCOVA，Q2–Q9）**：
   $$Y_{{ijk}} = \\mu + \\alpha_i (\\text{{Confidence}}_i) + \\beta_j (\\text{{FailedAgent}}_j) + (\\alpha\\beta)_{{ij}} (\\text{{Confidence}}_i \\times \\text{{FailedAgent}}_j) + \\epsilon_{{ijk}}$$

---

## 5. 在线实验系统架构与单盲访问链接 (Online Experimental System & Blinded Access Links)

在线实验平台严格区分**“受试者正式单盲入口”**与**“导师审阅预览模式”**：在正式受试者入口中，**顶部的条件切换栏与组别标签已被完全隐藏**，系统静默执行随机分配并锁定会话（防止刷新串组）；仅在携带 `?preview=1` 参数的审阅链接中才展示四组切换栏。

- **受试者正式单盲问卷入口（已隐藏所有条件切换标签）**：[{PUBLIC_URL}]({PUBLIC_URL})
  - 单一语言锁定被试入口（显示界面锁定为日文，隐藏语言切换与条件栏）：[{PUBLIC_URL}/?lang=ja&locklang=1]({PUBLIC_URL}/?lang=ja&locklang=1)
- **研究者与导师管理后台（实时统计与 CSV 导出）**：[{ADMIN_URL}]({ADMIN_URL})
- **导师审阅专用预览链接（带 `?preview=1` 条件切换栏，仅供审阅）**：
  - Condition 1 (双方 90% 高把握 × AI 失败/店长正确)：[{PUBLIC_URL}/?condition=1&preview=1]({PUBLIC_URL}/?condition=1&preview=1)
  - Condition 2 (双方 60% 低把握 × AI 失败/店长正确)：[{PUBLIC_URL}/?condition=2&preview=1]({PUBLIC_URL}/?condition=2&preview=1)
  - Condition 3 (双方 90% 高把握 × 店长失败/AI正确)：[{PUBLIC_URL}/?condition=3&preview=1]({PUBLIC_URL}/?condition=3&preview=1)
  - Condition 4 (双方 60% 低把握 × 店长失败/AI正确)：[{PUBLIC_URL}/?condition=4&preview=1]({PUBLIC_URL}/?condition=4&preview=1)
"""


def get_en_markdown():
    return f"""# Human Intuition vs. Artificial Intuition: Epistemic Asymmetry and Error Attribution When Two "Ineffable Black Boxes" Conflict
## Minor Research Project Proposal & Experimental Survey Design

---

### Project Metadata
- **Research Title**: *Human Intuition vs. Artificial Intuition: Epistemic Asymmetry and Error Attribution When Two "Ineffable Black Boxes" Conflict*
- **Researcher**: Tianyuan Xiu, Master's Program (M2), School of Knowledge Science, Japan Advanced Institute of Science and Technology (JAIST)
- **Academic Advisor**: Prof. Masaharu Mizumoto
- **Date**: November 3, 2026
- **Research Domains**: Knowledge Science, Experimental Philosophy, Human-Computer Interaction (HCI), Cognitive Psychology

---

## 1. Background & Theoretical Framework

### 1.1 Two Kinds of "Ineffable Black Boxes": Epistemic Isomorphism Between Human Tacit Knowledge and Deep Learning Intuition
In the foundational literature of Knowledge Science and Epistemology, Michael Polanyi (1966) famously characterized human **Tacit Knowledge** with the maxim: *"We can know more than we can tell."* In complex physical diagnostic tasks—such as agricultural quality sorting, clinical palpation, or artisan appraisal—seasoned human practitioners rely on holistic Gestalt perception honed through embodied experience to make accurate judgments, yet they are fundamentally incapable of articulating their decision rules in explicit words.

Crucially, as contemporary artificial intelligence has evolved from early rule-based symbolic expert systems to **end-to-end Deep Learning neural networks**, a profound epistemological parallel has emerged: **both human experts and contemporary deep-learning AI systems are equally incapable of explaining their holistic judgments in words at the moment of decision**. Rather than executing explicit logical rules, deep neural networks map high-dimensional inputs to probability outputs across millions of sub-symbolic weights. In a fundamental epistemological sense, both judgments are **"intuitive"** (*Human Embodied Intuition* vs. *Artificial Statistical Intuition*), even though an AI system might subsequently attempt to extract and highlight explicit features *post-hoc*.

### 1.2 Strictly Controlled Baseline Symmetry: Bounded Ground-Truth Training Data, Overall Accuracy, and Matched Case Confidence
To rigorously isolate how human decision-makers evaluate and attribute errors to **Human Intuition** versus **Artificial Intuition**, an experimental design must eliminate confounding asymmetries in training data realism, baseline accuracy, and certainty levels:
1. **Bounded Ground-Truth Training Data (~3,000 Opened & Taste-Tested Durians)**: In physical diagnostic tasks such as evaluating un-opened durians, although both humans and cameras can casually *look* at tens of thousands of fruits on shelves, verifying the actual internal ground truth (whether the pulp chambers are full and sweet) requires **destructive testing—cutting the fruit open and tasting it**. Consequently, the true labeled training set is inherently limited in reality for both humans and AI. In this study, both the veteran store manager and the deep-learning AI are explicitly defined as having learned from the **same finite ground-truth sample of approximately 3,000 durians actually cut open and taste-tested**.
2. **Identical Historical Overall Accuracy (85% Overall Accuracy)**: In prior standardized blind evaluations, both the veteran store manager and the deep-learning AI achieved the exact same **85% overall accuracy** (succeeding in 85 out of 100 cases and failing in 15).
3. **Matched Case-Specific Confidence (90% vs. 90% in High; 60% vs. 60% in Low)**: When evaluating the specific pair of durians (Durian A vs. Durian B) in the vignette, both agents express matched case-specific confidence in their respective recommendations—either **both are 90% confident** (High Confidence conditions) or **both are only 60% confident / borderline** (Low Confidence conditions).

### 1.3 Core Research Questions
By holding training data size (~3,000 destructively verified cases), overall accuracy (85%), and case-specific confidence (90% vs. 90%, or 60% vs. 60%) strictly equal across two agents that are equally incapable of verbal explanation, this study investigates three core research questions:
- **RQ1 (Pre-Outcome Choice & Epistemic Double Standard Toward Unexplainability)**: When *Human Intuition* and *Artificial Intuition* directly conflict under strictly equalized competence and confidence, which intuition do decision-makers trust (Q1)? Do people perceive statistical AI intuition as inherently more "objective" than human embodied intuition (Q2), or do they exhibit an **Epistemic Double Standard**—tolerating ineffability in a human expert while penalizing the exact same lack of verbal explanation in a black-box AI (Q4)?
- **RQ2 (Asymmetric Post-Outcome Error Attribution & Frankfurtian "Bullshitting")**: Once the fruits are cut open on-site and one intuition fails while the other succeeds, do observers attribute the error symmetrically to the 15% probabilistic base rate (Q5), or do they exhibit **Asymmetric Epistemic Blame**? Specifically, when the AI fails (Conditions 1 & 2), are participants significantly more likely to accuse the failed AI of lacking true understanding and engaging in Frankfurtian *"bullshitting"* (Frankfurt, 2005) (Q6) and misleading overconfidence (Q7) than they are to accuse the failed human manager when he makes the exact same mistake (Conditions 3 & 4)?
- **RQ3 (The Penalty of Overconfidence & Value of Post-Hoc Explicit Feature Extraction)**: Does failing at 90% confidence trigger a disproportionately harsher epistemic backlash than failing at 60% confidence, and is this *Penalty of Overconfidence* steeper against AI than against humans? Furthermore, addressing the unique technological capability of AI to extract explicit visual features *afterward* (e.g., post-hoc saliency heatmaps of spine spacing), to what extent does post-hoc feature extraction restore trust in AI intuition (Q8, Q9)?

---

## 2. $2 \\times 2$ Between-Subjects Experimental Design

### 2.1 Independent and Dependent Variables
The study employs a **$2 \\times 2$ between-subjects factorial design** manipulating two orthogonal independent variables:
- **Factor 1: Matched Case-Specific Confidence Level (Between-Subjects, 2 Levels)**
  - **Both High Confidence (90% vs. 90%)**: Both the veteran store manager (recommending Durian A) and the deep-learning AI (recommending Durian B) express **90% confidence** in their respective judgments for this specific pair.
  - **Both Low Confidence (60% vs. 60%)**: Both the veteran store manager (recommending Durian A) and the deep-learning AI (recommending Durian B) find this pair borderline and express only **60% confidence** in their respective judgments.
- **Factor 2: Realized Physical Outcome / Who Failed (Between-Subjects, 2 Levels)**
  - **AI Fails / Manager Correct (Conditions 1 & 2)**: On-site slicing reveals Durian A (Manager's choice) is packed with 5 full golden chambers of sweet pulp, whereas Durian B (AI's choice) is a hollow dead-pod fruit. Stage 2 attribution items symmetrically evaluate **the failed AI system**.
  - **Manager Fails / AI Correct (Conditions 3 & 4)**: On-site slicing reveals Durian B (AI's choice) is packed with 5 full golden chambers of sweet pulp, whereas Durian A (Manager's choice) is a hollow dead-pod fruit. Stage 2 attribution items symmetrically evaluate **the failed store manager**.

### 2.2 $2 \\times 2$ Factorial Condition Matrix

| Condition | Factor 1: Matched Case Confidence | Factor 2: Realized Outcome (Who Failed) | Stage 1: Symmetric Conflict Stimulus (Both trained on ~3,000 opened & tasted durians; Both have 85% Overall Accuracy) | Stage 2: On-Site Cut-Open Outcome & Symmetric Target of Attribution (`{{failedAgent}}`) |
| :--- | :--- | :--- | :--- | :--- |
| **Condition 1** | **Both High Confidence (90% vs. 90%)** | **AI Fails (Manager Correct)** | Manager intuitively recommends A (**90%** sure); AI intuitively recommends B (**90%** confidence) | Durian A is full; Durian B is hollow. Stage 2 measures error attribution toward **the failed AI system** (which failed at 90% confidence) |
| **Condition 2** | **Both Low Confidence (60% vs. 60%)** | **AI Fails (Manager Correct)** | Manager intuitively leans toward A (**60%** sure); AI intuitively leans toward B (**60%** confidence) | Durian A is full; Durian B is hollow. Stage 2 measures error attribution toward **the failed AI system** (which failed at 60% confidence) |
| **Condition 3** | **Both High Confidence (90% vs. 90%)** | **Manager Fails (AI Correct)** | Manager intuitively recommends A (**90%** sure); AI intuitively recommends B (**90%** confidence) | Durian B is full; Durian A is hollow. Stage 2 measures error attribution toward **the failed store manager** (who failed at 90% confidence) |
| **Condition 4** | **Both Low Confidence (60% vs. 60%)** | **Manager Fails (AI Correct)** | Manager intuitively leans toward A (**60%** sure); AI intuitively leans toward B (**60%** confidence) | Durian B is full; Durian A is hollow. Stage 2 measures error attribution toward **the failed store manager** (who failed at 60% confidence) |

---

## 3. Complete Survey Instrument & Measurement Scales

The online survey enforces strict forward-only progression across three sequential stages to prevent post-outcome hindsight contamination of Stage 1 responses.

### Stage 1: The Symmetric Intuition Conflict & Pre-Outcome Evaluation

> **[Stage 1 Scenario Vignette]**  
> Imagine you are at a fruit market choosing between two un-opened durians (**Durian A** and **Durian B**) of the same price. You want the one with the fullest, sweetest pulp inside, so you consult both a **veteran store manager** and a **deep-learning visual AI system**.  
> *(Background: Because verifying a durian's internal pulp and taste requires actually cutting it open, training data is naturally limited for both humans and AI. **Both the store manager and the AI learned from approximately 3,000 durians that were actually cut open and taste-tested.** In prior standardized blind tests, **both achieved the exact same overall accuracy of 85%**. Furthermore, both the human expert and the deep-learning AI make **"intuitive" judgments** that **cannot be explained in words**.)*  
> For this specific pair of durians, they give opposite recommendations:
>
> - **👨‍🌾 Veteran Store Manager's Intuition — [Recommends Durian A]**  
>   *Experience: ~3,000 opened & taste-tested durians | Overall Accuracy: 85%*  
>   - **[Conditions 1 & 3 — High Confidence (90%)]**: *"I honestly can't explain the rules in words. Based on my intuition from cutting open and tasting around 3,000 durians, I feel very confident about this case—I'm about **90% sure** Durian A is the better one (my overall accuracy is 85%)."*  
>   - **[Conditions 2 & 4 — Low Confidence (60%)]**: *"I honestly can't explain the rules in words. Based on my intuition from cutting open and tasting around 3,000 durians, this pair is a borderline call—I'm only about **60% sure** and slightly leaning toward Durian A (my overall accuracy is 85%)."*
>
> - **🤖 Deep Learning Visual AI's Intuition — [Recommends Durian B]**  
>   *Training Data: ~3,000 opened & taste-tested durians | Overall Accuracy: 85%*  
>   - **[Conditions 1 & 3 — High Confidence (90%)]**: *"Overall Historical Accuracy: 85% | Current Prediction: Recommend Durian B (Case Confidence: **90%**) — Note: Deep neural network black-box intuition; cannot provide verbal explanation."*  
>   - **[Conditions 2 & 4 — Low Confidence (60%)]**: *"Overall Historical Accuracy: 85% | Current Prediction: Recommend Durian B (Case Confidence: **60%**) — Note: Deep neural network black-box intuition; cannot provide verbal explanation."*

#### 1. Behavioral Decision Item
- **Q1. [Binary Choice]** When human intuition and AI intuition conflict under the exact same training experience (~3,000 cases), the same overall accuracy (85%), and the same confidence level (90% or 60%)—and neither can explain its judgment in words—which durian do you choose?
  - [ ] **Choose Durian A** (Follow the Veteran Store Manager's Intuition)
  - [ ] **Choose Durian B** (Follow the Deep Learning AI's Intuition)

#### 2. Pre-Outcome Cognitive & Epistemic Evaluation Scales (7-Point Likert: 1 = Strongly Disagree, 4 = Neutral, 7 = Strongly Agree)
- **Q2 (Perceived Objectivity Between Two "Intuitions")**: Even though both learned from ~3,000 opened durians, share an 85% overall accuracy, and cannot explain their rules in words, the AI's statistical "intuition" still feels more objective and reliable to me than the human's bodily "intuition."
- **Q3 (Impact of Case-Specific Confidence Level)**: The specific confidence level expressed by both sides for this pair (**90%** [or **60%**]) strongly influenced how I weighed my decision just now.
- **Q4 (Epistemic Double Standard Toward Unexplainability)**: I find it much harder to tolerate an AI system that "cannot explain its reasoning in words" than to tolerate a human expert who "cannot explain their intuition in words."

---

### Stage 2: Outcome Revelation & Symmetric Post-Outcome Attribution Scales

> **[On-Site Cut-Open Verification Results]**
> - **Conditions 1 & 2 (AI Fails / Store Manager Correct — Target `{{failedAgent}}` = `"the AI system"`)**:  
>   *Both durians are cut open on the spot: **Durian A (recommended by the manager) is packed with 5 large, full chambers of sweet golden pulp. Durian B (recommended by the AI) has a thick shell and is mostly hollow with undeveloped dead chambers inside. The store manager's intuition proved right, and the AI's prediction failed!***
> - **Conditions 3 & 4 (Store Manager Fails / AI Correct — Target `{{failedAgent}}` = `"the store manager"`)**:  
>   *Both durians are cut open on the spot: **Durian B (recommended by the AI) is packed with 5 large, full chambers of sweet golden pulp. Durian A (recommended by the manager) has a thick shell and is mostly hollow with undeveloped dead chambers inside. The AI's prediction proved right, and the store manager's intuition failed!***

#### Symmetric Post-Outcome Attribution, "Bullshitting," and Post-Hoc Feature Extraction Scales (7-Point Likert: 1 = Strongly Disagree, 4 = Neutral, 7 = Strongly Agree)
*(Note: Items Q5–Q7 dynamically insert `{{failedAgent}}` = **"the AI system"** in Conditions 1 & 2, and **"the store manager"** in Conditions 3 & 4, enabling a direct symmetric test of human vs. AI error attribution)*:
- **Q5 (Probabilistic Forgiveness — Normal Statistical Outlier)**: Since both have an 85% overall accuracy, judging natural fruit always carries a 15% chance of error; the fact that **[the AI system / the store manager]** failed this time is simply an unavoidable statistical outlier and completely understandable.
- **Q6 ("Bullshitting" / Fake Understanding Attribution — Experimental Philosophy Dimension)**: Seeing this failure, and looking back at how **[the AI system / the store manager]** expressed **90% [or 60%]** confidence without being able to explain why in words, I feel **[the AI system / the store manager]** had no genuine grasp of this case and was merely "bluffing / bullshitting."
- **Q7 (Perceived Overconfidence & Misleadingness — Blame Dimension)**: I feel that expressing **90% [or 60%]** confidence without being able to provide any verbal explanation was misleading on the part of **[the AI system / the store manager]**, making this failure frustrating.
- **Q8 (Value of Post-Hoc Explicit Feature Extraction — Explainable AI Dimension)**: Although both humans and deep-learning AI make "intuitive" judgments that cannot be explained in words at first, if the AI could afterward extract and highlight explicit visual features (e.g., pointing out specific spine angles or shell contours), I would trust the AI much more than an unexplainable human expert.
- **Q9 (Future Trust Preference Between Two Intuitions)**: After witnessing this outcome, next time I face a similar task where a human expert and a deep-learning AI have the same overall accuracy (85%) and neither can explain their judgment in words, I would prefer to rely on the AI rather than the human expert.

---

### Stage 3: Demographic & Control Variables

- **Q10. Gender**: [ Male / Female / Other or Prefer not to say ]
- **Q11. Age (in years)**: [ Exact numeric input: specific integer age in years, e.g., `24` (continuous variable, valid range 16–99) ]
- **Q12. Academic Background**: [ Yes (STEM / Computer Science / Data Science / AI) / No (Humanities / Social Sciences / Business / Arts / Other) ]
- **Q13. Daily AI Tool Usage Frequency (e.g., ChatGPT, Claude)**: [ Rarely / 1–2 times per week / Daily / Heavy reliance ]

---

## 4. Hypotheses, Expected Results, Sample Size Calculation & Analysis Plan

### 4.1 Primary Statistical Hypotheses
- **Hypothesis 1 (H1: Pre-Outcome Epistemic Double Standard Toward Unexplainability)**: In Stage 1 prior to outcome revelation, despite identical training data (~3,000 cases) and overall accuracy (85%), participants will exhibit a significant epistemic double standard in Q4 (mean score significantly above neutral $4.0$, $p < .001$), demanding explicit verbal explanations more strictly from black-box AI than from human tacit intuition. Meanwhile, matched high confidence (90% vs. 90%, Conditions 1 & 3) will yield significantly higher perceived confidence impact (Q3) than matched low confidence (60% vs. 60%, Conditions 2 & 4).
- **Hypothesis 2 (H2: Main Effect of Failed Agent — Asymmetric Epistemic Blame Against AI)**: In Stage 2, comparing attribution toward the failed AI (Conditions 1 & 2) versus the failed human manager (Conditions 3 & 4), participants will assign significantly higher Frankfurtian *"bullshitting"* attribution (Q6) and perceived misleadingness (Q7), and significantly lower probabilistic forgiveness (Q5), to **the failed AI system** than to **the failed human manager** for the exact same diagnostic failure ($p < .001$).
- **Hypothesis 3 (H3: Confidence $\\times$ Failed Agent Interaction & Post-Hoc Feature Extraction)**: There will be a significant two-way interaction between Case Confidence (90% vs. 60%) and Failed Agent (AI Fails vs. Manager Fails) on Q6, Q7, and Q9 ($p < .01$). Failing after expressing 90% confidence will provoke a much harsher backlash than failing after expressing 60% confidence, and this *Penalty of Overconfidence* will be disproportionately steeper when the AI fails (C1 vs. C2) than when the human manager fails (C3 vs. C4). Furthermore, Q8 will show strong positive agreement ($> 5.0$), demonstrating that **post-hoc explicit feature extraction** is a key mechanism for overcoming distrust of AI intuition.

### 4.2 Expected Results & A Priori Sample Size Calculation (Power Analysis)
Based on Hypotheses H1–H3, we specify the rough quantitative expectations on the 7-point Likert scales (1 = Strongly Disagree, 4 = Neutral, 7 = Strongly Agree, assuming a typical within-cell standard deviation of $SD \\approx 1.15$):
1. **Stage 1 Expectations**: Under strictly symmetric baselines, approximately **55%–60%** of participants are expected to favor Human Intuition (Durian A) vs. **40%–45%** for AI Intuition (Durian B), while Q4 (Epistemic Double Standard on Unexplainability) is expected to average **$M = 5.10, SD = 1.20$** (significantly above the midpoint $4.0$, one-sample Cohen's $d \\approx 0.92$).
2. **Stage 2 Expected $2 \\times 2$ Cell Means (illustrated on the primary outcome Q6: Frankfurtian "Bullshitting" Attribution)**:

| Condition | Factor 1: Confidence | Factor 2: Failed Agent | Expected Mean ($M$) | Expected $SD$ | Substantive Interpretation |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Condition 1** | High (90%) | AI System Fails | **5.60** | 1.15 | Severe backlash: 90%-confident failed black-box AI judged as "bullshitting" |
| **Condition 2** | Low (60%) | AI System Fails | **3.80** | 1.15 | Attenuated blame when AI expressed borderline 60% confidence ($\\Delta_{{\\text{{AI}}}} = +1.80$) |
| **Condition 3** | High (90%) | Manager Fails | **3.60** | 1.15 | Greater leniency toward human veteran intuition failing at 90% confidence |
| **Condition 4** | Low (60%) | Manager Fails | **3.40** | 1.15 | Excused as normal 15% statistical outlier ($\\Delta_{{\\text{{Human}}}} = +0.20$) |

3. **Required Sample Size Calculation ($\\alpha = 0.05$, Power $1 - \\beta = 0.80$, $2 \\times 2$ Fixed-Effects ANOVA, $df_1 = 1$)**:
   - **Main Effect of Failed Agent** ($\\mu_{{\\text{{AI}}}} = 4.70$ vs. $\\mu_{{\\text{{Human}}}} = 3.50$, effect $|\\beta| = 0.60$): Cohen's $f = 0.60 / 1.15 = \\mathbf{{0.52}}$ $\\rightarrow$ minimum required **$N = 32$** ($n = 8$ per condition).
   - **Main Effect of Confidence** ($\\mu_{{90\\%}} = 4.60$ vs. $\\mu_{{60\\%}} = 3.60$, effect $|\\alpha| = 0.50$): Cohen's $f = 0.50 / 1.15 = \\mathbf{{0.43}}$ $\\rightarrow$ minimum required **$N = 45$** ($n = 12$ per condition).
   - **Two-Way Interaction Effect** ($|\\gamma| = |(5.60 - 3.80) - (3.60 - 3.40)| / 4 = 0.40$): **Cohen's $f = 0.40 / 1.15 = \\mathbf{{0.35}}$** $\\rightarrow$ minimum required **$N = 68$** (**$n = 17$ per condition**) to achieve $80\\%$ statistical power at $\\alpha = 0.05$.
   - Including a ~15% buffer for quality screening, the **target sample size is $N = 80$ participants ($n = 20$ per condition)** within a single homogeneous participant pool.

### 4.3 Target Participant Pool & Cultural Scope
- **Primary Baseline Design (Single Homogeneous Group)**: To avoid linguistic and cultural confounding within the $2 \\times 2$ design, the baseline study targets a single homogeneous language group (**$N = 68\\text{{–}}80$ adult participants**, e.g., native Japanese speakers with the survey display locked to Japanese via `?lang=ja&locklang=1`, or equivalently a single homogeneous group of native Chinese speakers if self-recruited). The English, Japanese, and Chinese language switcher on the general link was built primarily to facilitate academic review.
- **Optional Cross-Cultural Extension (If Multi-Language Samples Are Collected)**: If both Japanese and Chinese participant groups are collected ($N = 68\\text{{–}}80$ per group), an exploratory cultural hypothesis (H4) can be tested: whether Japanese participants show greater deference and forgiveness toward unexplainable human intuition (consistent with cultural respect for *shokunin* craftsmanship) compared to Chinese participants who are more accustomed to everyday AI recommendations in consumer platforms.

### 4.4 Statistical Modeling Pipeline
1. **Binomial & Logistic Regression (Q1)** controlling for continuous Age (Q11), STEM background (Q12), and AI usage frequency (Q13):
   $$\\text{{logit}}(P(\\text{{Choice}} = \\text{{AI}})) = \\beta_0 + \\beta_1 \\cdot \\text{{ConfidenceLevel}} + \\beta_2 \\cdot \\text{{Age}} + \\beta_3 \\cdot \\text{{STEM}} + \\beta_4 \\cdot \\text{{AIFreq}}$$
2. **Two-Way Factorial ANOVA & ANCOVA (Q2–Q9)**:
   $$Y_{{ijk}} = \\mu + \\alpha_i (\\text{{Confidence}}_i) + \\beta_j (\\text{{FailedAgent}}_j) + (\\alpha\\beta)_{{ij}} (\\text{{Confidence}}_i \\times \\text{{FailedAgent}}_j) + \\epsilon_{{ijk}}$$

---

## 5. Online Experimental System & Blinded Access Links

The online platform strictly separates the **Blinded Participant Entry** from the **Supervisor Preview Mode**: on the actual participant URL, **all condition-switching tabs and condition labels are completely hidden**, and random assignment is locked per browser session so participants cannot view other conditions. Condition-switching tabs appear exclusively when `?preview=1` is appended by the researcher.

- **Blinded Participant Survey Entry (Condition tabs strictly hidden)**: [{PUBLIC_URL}]({PUBLIC_URL})
  - Single-Language Locked Participant Entry (Display locked to Japanese): [{PUBLIC_URL}/?lang=ja&locklang=1]({PUBLIC_URL}/?lang=ja&locklang=1)
- **Researcher & Supervisor Admin Portal**: [{ADMIN_URL}]({ADMIN_URL})
- **Supervisor Preview Links (With `?preview=1` condition switcher for inspection only)**:
  - Condition 1 (Both 90% Confident × AI Fails / Manager Wins): [{PUBLIC_URL}/?condition=1&preview=1]({PUBLIC_URL}/?condition=1&preview=1)
  - Condition 2 (Both 60% Confident × AI Fails / Manager Wins): [{PUBLIC_URL}/?condition=2&preview=1]({PUBLIC_URL}/?condition=2&preview=1)
  - Condition 3 (Both 90% Confident × Manager Fails / AI Wins): [{PUBLIC_URL}/?condition=3&preview=1]({PUBLIC_URL}/?condition=3&preview=1)
  - Condition 4 (Both 60% Confident × Manager Fails / AI Wins): [{PUBLIC_URL}/?condition=4&preview=1]({PUBLIC_URL}/?condition=4&preview=1)
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
    add_title("人类直觉 vs. 人工直觉：当两个“不可言传的黑盒”发生决策冲突时的认识论双标与错误归因研究")
    add_subtitle("副课题研究计划与实验问卷设计方案")
    
    meta_info = [
        "【研究基本信息】",
        "• 中文题目：人类直觉 vs. 人工直觉：当两个“不可言传的黑盒”发生决策冲突时的认识论双标与错误归因研究",
        "• 英文题目：Human Intuition vs. Artificial Intuition: Epistemic Asymmetry and Error Attribution When Two 'Ineffable Black Boxes' Conflict",
        "• 研究者：修 天源 (XIU TIANYUAN) — 北陆先端科学技术大学院大学 (JAIST) 知识科学研究科 博士前期课程二年级 (M2)",
        "• 指导教授：水本 教授 (Prof. Mizumoto)",
        "• 提交日期：2026年11月3日",
        "• 研究领域：知识科学 (Knowledge Science)、实验哲学 (Experimental Philosophy)、人机交互 (HCI)、认知心理学 (Cognitive Psychology)"
    ]
    add_callout(doc, meta_info, is_cn=True, border_color="1E293B", bg_color="F8FAFC")

    # --- SECTION 1 ---
    add_h1("1. 研究背景与核心理论框架 (Background & Theoretical Framework)")
    
    add_h2("1.1 两种“不可言传的直觉黑盒”：人类隐性知识与深度学习亚符号表征的认识论同构")
    add_body(
        "在知识科学（Knowledge Science）与认识论（Epistemology）传统中，迈克尔·波兰尼（Michael Polanyi, 1966）提出了著名的隐性知识（Tacit Knowledge）命题：“我们知道的多于我们能言说的（We can know more than we can tell）”。在复杂的物理鉴别任务中，资深人类行家依靠长期具身实践所沉淀的完形感知（Gestalt Perception）做出精准判断，但往往无法用显性的语言规则向他人解释其判断依据。"
    )
    add_body(
        "与此同时，当代人工智能已从早期的“显性符号规则系统”演进为“端到端深度学习神经网络（Deep Learning）”。一个关键的认识论事实在于：当代深度学习 AI 与人类行家在“无法用语言直接解释判断过程”这一点上具有高度的认识论同构性（Epistemic Isomorphism）。深度神经网络不依赖人工编写的显性规则，而是通过高维亚符号权重直接输出概率。在做出判断的瞬间，人类专家与深度学习 AI 同样是“不可言传的黑盒”——从广义认识论看，二者的判断都是“直觉性的（Intuitive）”（即“人类具身直觉 Human Intuition” vs. “人工统计直觉 Artificial Intuition”），尽管 AI 在事后（Post-hoc）或许可以通过特征提取算法尝试提取显性特征。"
    )

    add_h2("1.2 严格对称的基准控制：有限破坏性核验样本量、历史总体准确率与个案把握度")
    add_body(
        "为纯粹检验人类决策者对“人类直觉”与“AI 直觉”是否存在认识论双重标准（Epistemic Double Standards），本研究在实验刺激设计上实施了三项严格的对称控制："
    )
    add_body(
        "在未开壳榴莲品质甄别等物理任务中，无论人类还是摄像头，仅“观察外观”虽可接触数万颗果实，但要确知内部果肉饱满度与口感的真实结果（Ground Truth），必须经历切开果壳并实际品尝的破坏性核验（Destructive Verification）。因此，真正带真实标签的训练数据在现实中必然是有限的。本研究设定店长与 AI 均是从约 3,000 颗真正切开并品尝过果肉的榴莲样本中习得各自的直觉。",
        "1. 受物理核验制约的同等有限训练样本量（~3,000 颗开壳品尝样本）："
    )
    add_body(
        "店长与深度学习 AI 在过往标准化盲测中的历史总体准确率完全相同，均为 85%（即平均每判断 100 颗榴莲，双方各有 85 颗正确、15 颗失误）。",
        "2. 完全相同的历史总体准确率（85% Overall Accuracy）："
    )
    add_body(
        "在面对当前具体的两颗榴莲（A 号与 B 号）时，店长对推荐 A 号的把握度与 AI 对推荐 B 号的置信度严格对齐——在“双高把握度”条件下双方均为 90% 笃定，在“双低把握度”条件下双方均为 60% 吃不准（临界犹豫状态）。",
        "3. 完全匹配的个案把握度（90% vs. 90% 或 60% vs. 60%）："
    )

    add_h2("1.3 核心研究问题 (Research Questions)")
    add_body(
        "当训练样本量（~3,000 例）、历史总体准确率（85%）和当前个案把握度（90% 或 60%）完全相等，且双方都无法用语言解释判断规则时，决策者更倾向于相信哪一种“直觉”（Q1）？人们是否在“要求必须能用语言解释理由”上对人类直觉与 AI 直觉采取双重标准（Q2、Q4）？",
        "• RQ1（事前选择偏好与不可解释性的认识论双标）："
    )
    add_body(
        "当现场开壳验证揭晓、其中一方失败而另一方成功时，受试者对“失败的 AI 系统”与“失败的人类店长”是否采取不对称的归因逻辑？当 AI 直觉失败时，人们是否比面对人类店长犯同等错误时，更严苛地指责其“毫无真正理解、仅在用数字进行哈里·法兰克福（Frankfurt, 2005）意义上的盲目胡扯（Bullshitting）”（Q6）与“过度自信误导”（Q7），而非理性归因于 85% 准确率下的 15% 概率例外（Q5）？",
        "• RQ2（事后错误归因的不对称性与法兰克福式“胡扯”投射）："
    )
    add_body(
        "90% 高把握度下的失败是否比 60% 低把握度下的失败引发更强烈的信任反噬（过分自信惩罚效应）？此外，鉴于深度学习具备事后提取并标出显性视觉特征（Post-hoc Feature Extraction）的潜力，这种事后特征提取能力能在多大程度上弥补人们对 AI 直觉的信任赤字（Q8、Q9）？",
        "• RQ3（高把握度失败的反噬效应与事后显性特征提取的补偿价值）："
    )

    # --- SECTION 2 ---
    add_h1("2. 2×2 组间析因实验设计 (2×2 Between-Subjects Experimental Design)")
    add_body(
        "本研究采用 2×2 组间析因设计（Between-Subjects Factorial Design），正交操纵两个核心自变量：自变量 1 为双方当前个案把握度（双高把握度 90% vs. 90% 对比 双低把握度 60% vs. 60%）；自变量 2 为现场开壳真实结果/失败主体（AI 失败/店长正确 对比 店长失败/AI 正确）。受试者随机均等分配至以下 4 个实验条件组："
    )
    
    col_w = [Inches(1.05), Inches(1.35), Inches(1.35), Inches(2.75)]
    headers = ["实验组别", "自变量 1：双方个案把握度", "自变量 2：开壳结果（失败方）", "对称实验刺激呈现与阶段二对称归因对象"]
    data = [
        ["Condition 1", "双方高把握度 (90% vs. 90%)", "AI 失败 (店长正确)", "双方均基于~3,000例样本、总体准确率均为85%。店长以90%把握推荐A；AI以90%置信度推荐B。开壳：A满5房，B空壳。阶段二测量对【失败的AI系统】的归因"],
        ["Condition 2", "双方低把握度 (60% vs. 60%)", "AI 失败 (店长正确)", "双方均基于~3,000例样本、总体准确率均为85%。店长以60%把握略倾向A；AI以60%置信度略倾向B。开壳：A满5房，B空壳。阶段二测量对【失败的AI系统】的归因"],
        ["Condition 3", "双方高把握度 (90% vs. 90%)", "店长失败 (AI 正确)", "双方均基于~3,000例样本、总体准确率均为85%。店长以90%把握推荐A；AI以90%置信度推荐B。开壳：B满5房，A空壳。阶段二测量对【失败的资深店长】的归因"],
        ["Condition 4", "双方低把握度 (60% vs. 60%)", "店长失败 (AI 正确)", "双方均基于~3,000例样本、总体准确率均为85%。店长以60%把握略倾向A；AI以60%置信度略倾向B。开壳：B满5房，A空壳。阶段二测量对【失败的资深店长】的归因"]
    ]
    t = doc.add_table(rows=1, cols=4)
    format_academic_table(t, col_w, headers, data, is_cn=True)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # --- SECTION 3 ---
    add_h1("3. 实验问卷完整题项与量表设计 (Complete Survey Instrument)")
    add_body("在线问卷采用严格的单向递进式分阶段控制（禁止回退修改前序作答），分为以下三个阶段：")

    add_h2("第一阶段：两种“直觉黑盒”的正面冲突与前测认知评估 (Stage 1)")
    vignette_stage1 = [
        "【阶段一：对称冲突情境呈现】",
        "假设您正在水果店挑选未开壳的榴莲，面前有两颗价格相同的榴莲（A 号 与 B 号）。为了挑出内部果肉最饱满甘甜的一颗，您同时咨询了店里的资深人类店长和店内配置的深度学习视觉 AI 系统。",
        "（背景说明：因为只有真正切开并品尝过，才能确知榴莲内部的果肉饱满度与口感，所以无论是这位店长还是这套 AI，其有效训练经验都是有限的——双方各自都是从大约 3,000 颗真正切开并品尝过的榴莲样本中学习总结出来的。在过往的标准化盲测中，店长与 AI 的历史总体准确率完全相同，均为 85%。同时，店长与深度学习 AI 都无法用语言解释自己具体的判断规则——从某种意义上说，二者的判断都是“直觉性的”。）",
        "• 资深店长的直觉判断（推荐 A 号 | ~3,000颗开壳品尝经验 | 历史总体准确率 85%）：“老实说我也没法用语言向你解释具体规则。凭我切开品尝过约 3,000 颗榴莲攒下的直觉，我对这颗非常有把握——我有大约 90% 的把握确定 A 号更好 [或 Condition 2/4：今天这两颗非常接近、很难拿准——我只有大约 60% 的把握略微倾向于 A 号]（我的历史总体准确率是 85%）。”",
        "• 深度学习 AI 的直觉判断（推荐 B 号 | ~3,000颗开壳品尝训练数据 | 历史总体准确率 85%）：“历史总体准确率：85% | 当前预测：推荐 B 号（当前个案把握度 / 置信度：90% [或 Condition 2/4：60%]）—— 注：深度神经网络基于高维黑盒特征直接输出直觉概率，无法提供显性的语言解释。”"
    ]
    add_callout(doc, vignette_stage1, is_cn=True, border_color="3B82F6", bg_color="F0F9FF")

    add_body("当“人类店长的直觉”与“深度学习 AI 的直觉”在相同训练样本量（~3,000 颗）、相同总体准确率（85%）以及相同当前把握度（90% 或 60%）下给出相反建议，且双方都无法用语言解释理由时，您决定选择哪一颗？\n   [ 选项 A ]：选择 A 号（跟随资深人类店长的直觉）\n   [ 选项 B ]：选择 B 号（跟随深度学习 AI 的直觉）", "Q1.【二元决策选择】")
    add_body("即便人类店长和深度学习 AI 拥有完全相同的训练样本量（~3,000 颗）和相同的总体准确率（85%），且同样无法用语言解释理由，我仍然觉得 AI 的“统计直觉”比人类的“具身直觉”更加客观可靠。（7级李克特量表：1 = 完全不同意，7 = 完全同意）", "Q2（两种“直觉”之间的客观性感知）：")
    add_body("双方在当前这颗榴莲上展示出的具体把握度水平（本次均为 90% / 60%），对我刚才的权衡与选择产生了很大影响。（7级李克特量表：1 = 完全不同意，7 = 完全同意）", "Q3（当前个案把握度的决策影响）：")
    add_body("相比于人类专家“只可意会、说不出理由”的直觉，我更难以容忍一个“同样说不出任何显性规则与理由”的黑盒 AI 系统。（7级李克特量表：1 = 完全不同意，7 = 完全同意）", "Q4（对“无法用语言解释”的认识论双标）：")

    add_h2("第二阶段：真实结果揭晓与对称式错误归因量表 (Stage 2)")
    vignette_stage2 = [
        "【阶段二：现场开壳验证结果呈现】",
        "• Condition 1 & 2（AI 失败 / 店长正确 — 归因对象为“AI 系统”）：工作人员当场切开了两颗榴莲：店长推荐的 A 号果肉极其饱满甘甜（满 5 房黄金果肉）；而 AI 推荐的 B 号果壳极厚，内部大部分是未发育的空壳（死包）。最终结果证明：店长的直觉判断完全正确，而 AI 系统的直觉预测失败了！",
        "• Condition 3 & 4（店长失败 / AI 正确 — 归因对象为“人类店长”）：工作人员当场切开了两颗榴莲：AI 推荐的 B 号果肉极其饱满甘甜（满 5 房黄金果肉）；而店长推荐的 A 号果壳极厚，内部大部分是未发育的空壳（死包）。最终结果证明：AI 系统的直觉预测完全正确，而人类店长的直觉判断失败了！"
    ]
    add_callout(doc, vignette_stage2, is_cn=True, border_color="10B981", bg_color="F0FDF4")

    add_body("既然双方历史总体准确率都是 85%，挑选天然水果本就存在不可避免的概率风险；这次判断失败的【AI 系统 / 人类店长】只是恰好遇到了那 15% 的统计例外情况，完全情有可原。（1 = 完全不同意，7 = 完全同意）", "Q5（概率局限归因 — 理性容错维度）：")
    add_body("看到这次失败的结果，再回想刚才【AI 系统 / 人类店长】无法解释理由却给出 90% [或 60%] 把握度的样子，我觉得【AI 系统 / 人类店长】其实并没有真正理解这颗榴莲的品质，只是在“虚张声势 / 盲目胡扯（Bullshitting）”。（1 = 完全不同意，7 = 完全同意）", "Q6（法兰克福式“胡扯 / 不懂装懂”归因 — 实验哲学维度）：")
    add_body("我认为这次失败的【AI 系统 / 人类店长】在无法用语言解释具体依据的情况下，依然表现出 90% [或 60%] 的把握度，这种做法具有误导性，令我感到失望。（1 = 完全不同意，7 = 完全同意）", "Q7（过度自信与误导感归因 — 责任谴责维度）：")
    add_body("虽然人类与深度学习 AI 在做判断的瞬间都依赖“直觉”，但如果 AI 能在事后提取并标出显性的视觉特征（例如标出果刺间距或果壳轮廓的高亮热力图），我对 AI 建议的信任度将会显著超越无法解释理由的人类专家。（1 = 完全不同意，7 = 完全同意）", "Q8（事后显性特征提取的价值 — 可解释 AI 维度）：")
    add_body("经历了这次开壳验证后，下次面对具有相同历史准确率（85%）但同样无法用语言解释理由的“人类直觉”与“AI 直觉”，我会更倾向于依赖深度学习 AI 而不是人类专家。（1 = 完全不同意，7 = 完全同意）", "Q9（未来信任倾向变化 — 远期决策偏好）：")

    add_h2("第三阶段：受试者人口学与控制变量 (Stage 3)")
    add_body("• Q10. 性别：[ 男 / 女 / 其他或不愿透露 ]\n"
             "• Q11. 具体年龄（周岁）：[ 数字输入框：填写具体整数周岁，如 24（连续数值变量，16–99岁） ]\n"
             "• Q12. 学科专业背景：[ 是（理工科 STEM / 计算机 / 数据科学 / AI 相关专业） / 否（人文社科 / 商科 / 艺术 / 其他非理工专业） ]\n"
             "• Q13. 日常使用 AI 工具（如 ChatGPT、Claude 等）的频率：[ 几乎不用 / 每周 1–2 次 / 几乎每天使用 / 重度深度依赖 ]")

    # --- SECTION 4 ---
    add_h1("4. 统计假设、预期结果与样本量计算 (Hypotheses, Expected Results & Power Analysis)")
    add_h2("4.1 核心统计假设")
    add_body(
        "在阶段一结果揭晓前，尽管店长与 AI 拥有完全相同的训练样本量（~3,000 例）与总体准确率（85%），受试者在面对“无法用语言解释理由”时仍将表现出显著的认识论双标（Q4 均值显著高于中立值 4.0，p < .001）；同时，双高把握度组（90% vs. 90%，C1 & C3）在把握度影响权重（Q3）上将显著高于双低把握度组（60% vs. 60%，C2 & C4）。",
        "• 假设 1（H1：事前认识论双标与个案把握度效应）："
    )
    add_body(
        "在阶段二结果揭晓后，比较“AI 失败组（C1 & C2）”与“店长失败组（C3 & C4）”对各自失败主体的归因得分：当 AI 预测失败时，受试者对失败 AI 的法兰克福式“胡扯（Bullshitting）”归因（Q6）与“误导失望感”（Q7）将显著高于人类店长犯同等错误时受到的指责（p < .001），而在理性概率豁免（Q5）上的得分将显著低于店长失败组。",
        "• 假设 2（H2：失败主体的不对称归因主效应 — “对 AI 错误的严苛惩罚”）："
    )
    add_body(
        "个案把握度（90% vs. 60%）与失败主体（AI 失败 vs. 店长失败）在 Q6、Q7 及 Q9 上存在显著二阶交互作用（p < .01）。“90% 高把握度下的失败”比“60% 低把握度下的失败”引发显著更强的反噬，且该惩罚斜率在 AI 失败时（C1 vs. C2）显著陡峭于店长失败时（C3 vs. C4）。此外，Q8 将呈现显著高分（> 5.0），证实“事后显性特征提取”对修复 AI 直觉信任的关键作用。",
        "• 假设 3（H3：把握度 × 失败主体交互效应与事后特征提取补偿）："
    )

    add_h2("4.2 预期结果与先验样本量计算 (Expected Results & Sample Size Calculation)")
    add_body(
        "在阶段一对称基线下，预计约 55%–60% 受试者选择人类直觉（A号），40%–45% 选择 AI 直觉（B号）；Q4（认识论双标）预期均值约为 M = 5.10, SD = 1.20（显著高于中立值 4.0，Cohen's d ≈ 0.92）。阶段二核心因变量（以 Q6 法兰克福式“胡扯”归因为代表，7级量表，假定组内标准差 SD ≈ 1.15）的四组预期均值如下表所示："
    )
    exp_w_cn = [Inches(1.1), Inches(1.15), Inches(1.25), Inches(0.85), Inches(2.15)]
    exp_h_cn = ["实验条件组", "把握度水平", "失败主体", "预期均值 (SD)", "实质效应预期"]
    exp_d_cn = [
        ["Condition 1", "高把握 (90%)", "AI 系统失败", "5.60 (1.15)", "强烈认识论反噬：高把握翻车黑盒 AI 被高度归因为胡扯"],
        ["Condition 2", "低把握 (60%)", "AI 系统失败", "3.80 (1.15)", "AI 事先表明仅 60% 临界把握，指责显著缓和 (Δ_AI = +1.80)"],
        ["Condition 3", "高把握 (90%)", "人类店长失败", "3.60 (1.15)", "对人类资深行家直觉失误的容忍度显著更高"],
        ["Condition 4", "低把握 (60%)", "人类店长失败", "3.40 (1.15)", "被豁免为正常的 15% 概率例外 (Δ_Human = +0.20)"]
    ]
    t_exp_cn = doc.add_table(rows=1, cols=5)
    format_academic_table(t_exp_cn, exp_w_cn, exp_h_cn, exp_d_cn, is_cn=True)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_body(
        "基于上述预期均值进行 2×2 固定效应方差分析（α = 0.05，统计检验力 1 - β = 0.80，分子自由度 df_1 = 1）的先验样本量推算：（1）失败主体主效应（4.70 vs. 3.50，Cohen's f = 0.60 / 1.15 = 0.52）最低仅需 N = 32 人；（2）把握度主效应（4.60 vs. 3.60，Cohen's f = 0.50 / 1.15 = 0.43）最低仅需 N = 45 人；（3）二阶交互效应（|γ| = |(5.60 - 3.80) - (3.60 - 3.40)| / 4 = 0.40，Cohen's f = 0.40 / 1.15 = 0.35）所需的最低有效总样本量为 N = 68 人（每组 n = 17 人）。计入约 15% 的注意力与质量筛查缓冲，单一语种样本池的目标招募样本量设定为 N = 80 人（每组 n = 20 人）。",
        "• 样本量功效推算结论："
    )

    add_h2("4.3 目标受试者群体、文化范围与统计检验模型")
    add_body(
        "为避免跨语言与文化背景在 2×2 设计中引入混杂干扰，本研究基准方案聚焦单一母语同质受试者群体（N = 68–80 人，例如日语母语成年受试者，正式发放时将问卷显示界面锁定为日文 ?lang=ja&locklang=1；若由研究者个人渠道独立招募，亦可同理锁定为单一中文界面招募中文母语者；审阅页内置的多语言切换主要用于学术指导审阅）。若后续同步采集日本与中国两组受试者（每语种各 N = 68–80 人），则可进一步检验探索性跨文化假说（H4）：探讨日本受试者（受传统“职人”经验尊重影响）是否比高频接触算法消费推荐的中国受试者对人类直觉展现更高的偏好与失误宽容度。",
        "• 目标受试者与文化范围："
    )
    add_body(
        "采用卡方检验与二元 Logistic 回归分析 Q1 决策选择；采用 2×2 组间双因素方差分析（Two-Way Factorial ANOVA: Y_ijk = μ + α_i + β_j + (αβ)_ij + ε_ijk）检验 Q2–Q9 的主效应与交互效应，并将连续年龄（Q11）、理工科背景（Q12）与 AI 使用频率（Q13）纳入协方差分析（ANCOVA）。",
        "• 统计检验模型："
    )

    # --- SECTION 5 ---
    add_h1("5. 在线实验系统架构与单盲访问链接 (Online Experimental System & Blinded Links)")
    add_body(
        "在线实验系统严格实施“受试者单盲入口”与“导师审阅预览模式”分离：在受试者正式入口中，顶部的条件切换栏与组别标签已被完全移除，系统静默执行随机分配并锁定浏览器会话；仅在附带 ?preview=1 参数的导师审阅链接中才展示四组切换栏："
    )
    add_body(f"• 受试者正式单盲问卷入口（已隐藏所有条件切换标签）：{PUBLIC_URL}\n"
             f"• 单一语言锁定被试入口（显示界面锁定为日文）：{PUBLIC_URL}/?lang=ja&locklang=1\n"
             f"• 研究者与导师管理后台：{ADMIN_URL}\n"
             f"• 导师审阅预览 C1 (双方 90% × AI 失败)：{PUBLIC_URL}/?condition=1&preview=1\n"
             f"• 导师审阅预览 C2 (双方 60% × AI 失败)：{PUBLIC_URL}/?condition=2&preview=1\n"
             f"• 导师审阅预览 C3 (双方 90% × 店长失败)：{PUBLIC_URL}/?condition=3&preview=1\n"
             f"• 导师审阅预览 C4 (双方 60% × 店长失败)：{PUBLIC_URL}/?condition=4&preview=1")

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
    add_title("Human Intuition vs. Artificial Intuition: Epistemic Asymmetry and Error Attribution When Two 'Ineffable Black Boxes' Conflict")
    add_subtitle("Minor Research Project Proposal & Experimental Survey Design")
    
    meta_info = [
        "[Project Metadata]",
        "• Research Title: Human Intuition vs. Artificial Intuition: Epistemic Asymmetry and Error Attribution When Two 'Ineffable Black Boxes' Conflict",
        "• Researcher: Tianyuan Xiu — Master's Program (M2), School of Knowledge Science, JAIST",
        "• Academic Advisor: Prof. Masaharu Mizumoto",
        "• Date: November 3, 2026",
        "• Research Domains: Knowledge Science, Experimental Philosophy, Human-Computer Interaction (HCI), Cognitive Psychology"
    ]
    add_callout(doc, meta_info, is_cn=False, border_color="1E293B", bg_color="F8FAFC")

    # --- SECTION 1 ---
    add_h1("1. Background & Theoretical Framework")
    
    add_h2("1.1 Two Kinds of 'Ineffable Black Boxes': Human Tacit Knowledge and Deep Learning Intuition")
    add_body(
        "In the foundational literature of Knowledge Science and Epistemology, Michael Polanyi (1966) characterized human Tacit Knowledge with the maxim: 'We can know more than we can tell.' In complex physical diagnostic tasks, seasoned human practitioners rely on holistic Gestalt perception honed through embodied experience to make accurate judgments, yet they are fundamentally incapable of articulating their decision rules in explicit words."
    )
    add_body(
        "Crucially, as contemporary artificial intelligence has evolved from rule-based symbolic expert systems to end-to-end Deep Learning neural networks, a profound epistemological isomorphism has emerged: both human experts and contemporary deep-learning AI systems are equally incapable of explaining their holistic judgments in words at the moment of decision. Rather than executing explicit verbal rules, deep neural networks map high-dimensional inputs to probability outputs across millions of sub-symbolic weights. In a fundamental epistemological sense, both judgments are 'intuitive' (Human Embodied Intuition vs. Artificial Statistical Intuition), even though an AI system might subsequently attempt to extract and identify explicit features post-hoc."
    )

    add_h2("1.2 Strictly Controlled Baseline Symmetry: Bounded Training Data, Overall Accuracy, and Matched Confidence")
    add_body(
        "To rigorously isolate how human decision-makers evaluate and attribute errors to Human Intuition versus Artificial Intuition, this study enforces three strict baseline controls:"
    )
    add_body(
        "In physical diagnostic tasks such as evaluating un-opened durians, although both humans and cameras can casually look at tens of thousands of fruits, verifying the actual internal ground truth (pulp fullness and taste) requires destructive testing—cutting the fruit open and tasting it. Thus, labeled ground-truth training data are inherently bounded for both. Both the store manager and the deep-learning AI are explicitly defined as having learned from approximately 3,000 durians actually cut open and taste-tested.",
        "1. Bounded Ground-Truth Training Data (~3,000 Opened & Taste-Tested Durians): "
    )
    add_body(
        "In prior standardized blind evaluations, both the veteran store manager and the deep-learning AI achieved the exact same 85% overall accuracy.",
        "2. Identical Historical Overall Accuracy (85% Overall Accuracy): "
    )
    add_body(
        "When evaluating the specific pair of durians (Durian A vs. Durian B), both agents express matched case-specific confidence—either both are 90% confident (High Confidence conditions) or both are only 60% confident / borderline (Low Confidence conditions).",
        "3. Matched Case-Specific Confidence (90% vs. 90% in High; 60% vs. 60% in Low): "
    )

    add_h2("1.3 Core Research Questions")
    add_body(
        "When Human Intuition and Artificial Intuition conflict under identical training sample size (~3,000 cases), identical overall accuracy (85%), and matched case-specific confidence (90% or 60%)—and neither can explain its reasoning in words—which intuition do decision-makers trust (Q1), and do they exhibit an Epistemic Double Standard toward unexplainability (Q2, Q4)?",
        "• RQ1 (Pre-Outcome Choice & Epistemic Double Standard Toward Unexplainability): "
    )
    add_body(
        "Once on-site verification reveals that one intuition failed while the other succeeded, do observers attribute the error symmetrically to the 15% statistical outlier rate (Q5), or do they exhibit Asymmetric Epistemic Blame—accusing a failed AI of lacking true understanding and engaging in Frankfurtian 'bullshitting' (Frankfurt, 2005) (Q6) and misleading overconfidence (Q7) far more harshly than a failed human expert making the exact same mistake?",
        "• RQ2 (Asymmetric Post-Outcome Error Attribution & Frankfurtian 'Bullshitting'): "
    )
    add_body(
        "Does failing at 90% confidence provoke a disproportionately harsher backlash than failing at 60% confidence ('The Penalty of Overconfidence'), and to what extent can post-hoc explicit feature extraction by AI restore user trust (Q8, Q9)?",
        "• RQ3 (The Penalty of Overconfidence & Value of Post-Hoc Feature Extraction): "
    )

    # --- SECTION 2 ---
    add_h1("2. 2×2 Between-Subjects Experimental Design")
    add_body(
        "The experiment employs a 2×2 between-subjects factorial design manipulating two orthogonal independent variables: Factor 1 is Matched Case-Specific Confidence (Both High 90% vs. Both Low 60%); Factor 2 is Realized Outcome / Who Failed (AI Fails/Manager Correct vs. Manager Fails/AI Correct). Participants are randomly assigned with equal probability to one of the four conditions:"
    )
    
    col_w = [Inches(1.05), Inches(1.35), Inches(1.35), Inches(2.75)]
    headers = ["Condition", "Factor 1: Matched Confidence", "Factor 2: Outcome (Who Failed)", "Symmetric Stimulus Presentation & Stage 2 Attribution Target"]
    data = [
        ["Condition 1", "Both High (90% vs. 90%)", "AI Fails (Manager Correct)", "Both trained on ~3,000 cases; both 85% overall accuracy. Manager 90% sure on A; AI 90% confident on B. Cut-open: A is full, B is hollow. Stage 2 evaluates the failed AI system"],
        ["Condition 2", "Both Low (60% vs. 60%)", "AI Fails (Manager Correct)", "Both trained on ~3,000 cases; both 85% overall accuracy. Manager 60% leaning A; AI 60% leaning B. Cut-open: A is full, B is hollow. Stage 2 evaluates the failed AI system"],
        ["Condition 3", "Both High (90% vs. 90%)", "Manager Fails (AI Correct)", "Both trained on ~3,000 cases; both 85% overall accuracy. Manager 90% sure on A; AI 90% confident on B. Cut-open: B is full, A is hollow. Stage 2 evaluates the failed store manager"],
        ["Condition 4", "Both Low (60% vs. 60%)", "Manager Fails (AI Correct)", "Both trained on ~3,000 cases; both 85% overall accuracy. Manager 60% leaning A; AI 60% leaning B. Cut-open: B is full, A is hollow. Stage 2 evaluates the failed store manager"]
    ]
    t = doc.add_table(rows=1, cols=4)
    format_academic_table(t, col_w, headers, data, is_cn=False)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # --- SECTION 3 ---
    add_h1("3. Complete Survey Instrument & Measurement Scales")
    add_body("The online questionnaire enforces strict forward-only progression across three sequential stages:")

    add_h2("Stage 1: The Symmetric Intuition Conflict & Pre-Outcome Evaluation")
    vignette_stage1 = [
        "[Stage 1: Symmetric Conflict Vignette Presentation]",
        "Imagine you are at a fruit market choosing between two un-opened durians (Durian A and Durian B) of the same price. You want the one with the fullest, sweetest pulp inside, so you consult both a veteran store manager and a deep-learning visual AI system.",
        "(Background: Because verifying a durian's internal pulp and taste requires actually cutting it open, training data is naturally limited for both humans and AI. Both the store manager and the AI learned from approximately 3,000 durians that were actually cut open and taste-tested. In prior standardized blind tests, both achieved the exact same overall accuracy of 85%. Furthermore, both the human expert and the deep-learning AI make 'intuitive' judgments that cannot be explained in words.)",
        "• Veteran Store Manager's Intuition (Recommends Durian A | ~3,000 opened & tasted durians | Overall Accuracy: 85%): \"I honestly can't explain the rules in words. Based on my intuition from cutting open and tasting around 3,000 durians, I feel very confident about this case—I'm about 90% sure Durian A is the better one [or Conditions 2 & 4: this pair is a borderline call—I'm only about 60% sure and slightly leaning toward Durian A] (my overall accuracy is 85%).\"",
        "• Deep Learning Visual AI's Intuition (Recommends Durian B | ~3,000 opened & tasted durians | Overall Accuracy: 85%): \"Overall Historical Accuracy: 85% | Current Prediction: Recommend Durian B (Case Confidence: 90% [or Conditions 2 & 4: 60%]) — Note: Deep neural network black-box intuition; cannot provide verbal explanation.\""
    ]
    add_callout(doc, vignette_stage1, is_cn=False, border_color="3B82F6", bg_color="F0F9FF")

    add_body("When human intuition and AI intuition conflict under the exact same training experience (~3,000 cases), the same overall accuracy (85%), and the same confidence level (90% or 60%)—and neither can explain its judgment in words—which durian do you choose?\n   [ Option A ]: Choose Durian A (Follow the Veteran Store Manager's Intuition)\n   [ Option B ]: Choose Durian B (Follow the Deep Learning AI's Intuition)", "Q1. [Binary Choice] ")
    add_body("Even though both learned from ~3,000 opened durians, share an 85% overall accuracy, and cannot explain their rules in words, the AI's statistical 'intuition' still feels more objective and reliable to me than the human's bodily 'intuition.' (7-Point Likert: 1 = Strongly Disagree, 7 = Strongly Agree)", "Q2 (Perceived Objectivity Between Two 'Intuitions'): ")
    add_body("The specific confidence level expressed by both sides for this pair (90% / 60%) strongly influenced how I weighed my decision just now. (7-Point Likert: 1 = Strongly Disagree, 7 = Strongly Agree)", "Q3 (Impact of Case-Specific Confidence Level): ")
    add_body("I find it much harder to tolerate an AI system that 'cannot explain its reasoning in words' than to tolerate a human expert who 'cannot explain their intuition in words.' (7-Point Likert: 1 = Strongly Disagree, 7 = Strongly Agree)", "Q4 (Epistemic Double Standard Toward Unexplainability): ")

    add_h2("Stage 2: Outcome Revelation & Symmetric Post-Outcome Attribution Scales")
    vignette_stage2 = [
        "[Stage 2: On-Site Cut-Open Verification Results]",
        "• Conditions 1 & 2 (AI Fails / Manager Correct — Target = 'the AI system'): Both durians are cut open on the spot: Durian A (recommended by the manager) is packed with 5 large, full chambers of sweet golden pulp. Durian B (recommended by the AI) has a thick shell and is mostly hollow with undeveloped dead chambers inside. The store manager's intuition proved right, and the AI's prediction failed!",
        "• Conditions 3 & 4 (Manager Fails / AI Correct — Target = 'the store manager'): Both durians are cut open on the spot: Durian B (recommended by the AI) is packed with 5 large, full chambers of sweet golden pulp. Durian A (recommended by the manager) has a thick shell and is mostly hollow with undeveloped dead chambers inside. The AI's prediction proved right, and the store manager's intuition failed!"
    ]
    add_callout(doc, vignette_stage2, is_cn=False, border_color="10B981", bg_color="F0FDF4")

    add_body("Since both have an 85% overall accuracy, judging natural fruit always carries a 15% chance of error; the fact that [the AI system / the store manager] failed this time is simply an unavoidable statistical outlier and completely understandable. (1 = Strongly Disagree, 7 = Strongly Agree)", "Q5 (Probabilistic Forgiveness — Normal Statistical Outlier): ")
    add_body("Seeing this failure, and looking back at how [the AI system / the store manager] expressed 90% [or 60%] confidence without being able to explain why in words, I feel [the AI system / the store manager] had no genuine grasp of this case and was merely 'bluffing / bullshitting.' (1 = Strongly Disagree, 7 = Strongly Agree)", "Q6 ('Bullshitting' / Fake Understanding Attribution — Experimental Philosophy Dimension): ")
    add_body("I feel that expressing 90% [or 60%] confidence without being able to provide any verbal explanation was misleading on the part of [the AI system / the store manager], making this failure frustrating. (1 = Strongly Disagree, 7 = Strongly Agree)", "Q7 (Perceived Overconfidence & Misleadingness — Blame Dimension): ")
    add_body("Although both humans and deep-learning AI make 'intuitive' judgments that cannot be explained in words at first, if the AI could afterward extract and highlight explicit visual features (e.g., pointing out specific spine angles or shell contours), I would trust the AI much more than an unexplainable human expert. (1 = Strongly Disagree, 7 = Strongly Agree)", "Q8 (Value of Post-Hoc Explicit Feature Extraction — Explainable AI Dimension): ")
    add_body("After witnessing this outcome, next time I face a similar task where a human expert and a deep-learning AI have the same overall accuracy (85%) and neither can explain their judgment in words, I would prefer to rely on the AI rather than the human expert. (1 = Strongly Disagree, 7 = Strongly Agree)", "Q9 (Future Trust Preference Between Two Intuitions): ")

    add_h2("Stage 3: Demographic & Control Variables")
    add_body("• Q10. Gender: [ Male / Female / Other or Prefer not to say ]\n"
             "• Q11. Age (in years): [ Exact numeric input: specific integer age in years, e.g., 24 (continuous variable, valid range 16–99) ]\n"
             "• Q12. Academic Background: [ Yes (STEM / Computer Science / Data Science / AI) / No (Humanities / Social Sciences / Business / Arts / Other) ]\n"
             "• Q13. Daily AI Tool Usage Frequency (e.g., ChatGPT, Claude): [ Rarely / 1–2 times per week / Daily / Heavy reliance ]")

    # --- SECTION 4 ---
    add_h1("4. Hypotheses, Expected Results, Sample Size Calculation & Analysis Plan")
    add_h2("4.1 Primary Statistical Hypotheses")
    add_body(
        "In Stage 1 prior to outcome revelation, despite identical training data (~3,000 cases) and overall accuracy (85%), participants will exhibit a significant epistemic double standard in Q4 (mean score > 4.0, p < .001), demanding explicit verbal explanations more strictly from black-box AI than from human tacit intuition; meanwhile, matched high confidence (90% vs. 90%, C1 & C3) will yield significantly higher perceived confidence impact (Q3) than matched low confidence (60% vs. 60%, C2 & C4).",
        "• Hypothesis 1 (H1: Pre-Outcome Epistemic Double Standard Toward Unexplainability): "
    )
    add_body(
        "In Stage 2, comparing attribution toward the failed AI (Conditions 1 & 2) versus the failed store manager (Conditions 3 & 4), participants will assign significantly higher Frankfurtian 'bullshitting' attribution (Q6) and perceived misleadingness (Q7), and significantly lower probabilistic forgiveness (Q5), to the failed AI system than to the failed human manager for the exact same diagnostic error (p < .001).",
        "• Hypothesis 2 (H2: Main Effect of Failed Agent — Asymmetric Epistemic Blame Against AI): "
    )
    add_body(
        "There will be a significant two-way interaction between Case Confidence (90% vs. 60%) and Failed Agent (AI Fails vs. Manager Fails) on Q6, Q7, and Q9 (p < .01). Failing at 90% confidence will provoke a much harsher backlash than failing at 60% confidence, and this Penalty of Overconfidence will be steeper against AI (C1 vs. C2) than against the human expert (C3 vs. C4). Moreover, Q8 will show strong agreement (> 5.0), confirming the value of post-hoc explicit feature extraction.",
        "• Hypothesis 3 (H3: Confidence × Failed Agent Interaction & Post-Hoc Feature Extraction): "
    )

    add_h2("4.2 Expected Results & A Priori Sample Size Calculation (Power Analysis)")
    add_body(
        "In Stage 1, under strictly matched baselines, approximately 55%–60% of participants are expected to choose Human Intuition (Durian A) vs. 40%–45% for AI Intuition (Durian B), while Q4 (Epistemic Double Standard on Unexplainability) is expected around M = 5.10, SD = 1.20 (significantly above the neutral midpoint 4.0, one-sample Cohen's d ≈ 0.92). For Stage 2, assuming a standard within-cell SD ≈ 1.15 on the 7-point Likert scales, the rough expected 2×2 cell means (illustrated on the primary outcome Q6: Frankfurtian 'Bullshitting' Attribution) are:"
    )
    exp_w_en = [Inches(1.1), Inches(1.15), Inches(1.25), Inches(0.85), Inches(2.15)]
    exp_h_en = ["Condition", "Confidence", "Failed Agent", "Expected M (SD)", "Substantive Expectation"]
    exp_d_en = [
        ["Condition 1", "High (90%)", "AI System Fails", "5.60 (1.15)", "Severe backlash: 90%-confident failed black-box AI judged as 'bullshitting'"],
        ["Condition 2", "Low (60%)", "AI System Fails", "3.80 (1.15)", "Attenuated blame when AI expressed borderline 60% confidence (Δ_AI = +1.80)"],
        ["Condition 3", "High (90%)", "Manager Fails", "3.60 (1.15)", "Greater leniency toward human veteran intuition failing at 90% confidence"],
        ["Condition 4", "Low (60%)", "Manager Fails", "3.40 (1.15)", "Excused as normal 15% statistical outlier (Δ_Human = +0.20)"]
    ]
    t_exp_en = doc.add_table(rows=1, cols=5)
    format_academic_table(t_exp_en, exp_w_en, exp_h_en, exp_d_en, is_cn=False)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_body(
        "Conducting an a priori power analysis for a 2×2 fixed-effects ANOVA (α = 0.05, statistical power 1 - β = 0.80, numerator df_1 = 1) based on these expected means yields: (1) Main Effect of Failed Agent (4.70 vs. 3.50, Cohen's f = 0.60 / 1.15 = 0.52) requires minimum N = 32 (n = 8 per cell); (2) Main Effect of Confidence (4.60 vs. 3.60, Cohen's f = 0.50 / 1.15 = 0.43) requires minimum N = 45 (n = 12 per cell); (3) Two-Way Interaction Effect (|γ| = |(5.60 - 3.80) - (3.60 - 3.40)| / 4 = 0.40, Cohen's f = 0.40 / 1.15 = 0.35) requires a minimum total sample size of N = 68 participants (n = 17 per condition). Allowing a ~15% buffer for quality screening, the target sample size is N = 80 participants (n = 20 per condition) within a single homogeneous participant pool.",
        "• Required Sample Size Calculation: "
    )

    add_h2("4.3 Target Participant Pool, Cultural Scope & Statistical Models")
    add_body(
        "To avoid cross-cultural confounding within the 2×2 design, the baseline plan focuses on a single homogeneous language group (N = 68–80 adult participants, e.g., native Japanese speakers with the survey display locked to Japanese via ?lang=ja&locklang=1, or equivalently native Chinese speakers if self-recruited; the English/Japanese/Chinese toggle on the general link was built primarily for supervision review). Optionally, if both Japanese and Chinese participant groups are collected (N = 68–80 per group), an exploratory cultural hypothesis (H4) can be tested: whether Japanese participants show greater trust and forgiveness toward human tacit intuition (consistent with cultural respect for shokunin craftsmanship) compared to Chinese participants accustomed to everyday AI consumer recommendations.",
        "• Target Participants & Cultural Scope: "
    )
    add_body(
        "Chi-square test and Binary Logistic Regression for Q1; 2×2 Between-Subjects Factorial ANOVA (Y_ijk = μ + α_i + β_j + (αβ)_ij + ε_ijk) for Q2–Q9; Bonferroni-corrected simple main effects and ANCOVA controlling for continuous Age (Q11), STEM background (Q12), and AI usage frequency (Q13).",
        "• Statistical Modeling Pipeline: "
    )

    # --- SECTION 5 ---
    add_h1("5. Online Experimental System & Blinded Access Links")
    add_body(
        "The online experimental system strictly separates the Blinded Participant Entry from the Supervisor Preview Mode: on the actual participant URL, all condition-switching tabs and condition labels are completely hidden, and random assignment is locked per browser session so participants cannot see other conditions. Condition-switching tabs appear exclusively when ?preview=1 is appended for researcher inspection:"
    )
    add_body(f"• Blinded Participant Survey Entry (Condition tabs strictly hidden): {PUBLIC_URL}\n"
             f"• Single-Language Locked Participant Entry (Display locked to Japanese): {PUBLIC_URL}/?lang=ja&locklang=1\n"
             f"• Researcher & Supervisor Admin Portal: {ADMIN_URL}\n"
             f"• Supervisor Preview C1 (Both 90% Confident × AI Fails): {PUBLIC_URL}/?condition=1&preview=1\n"
             f"• Supervisor Preview C2 (Both 60% Confident × AI Fails): {PUBLIC_URL}/?condition=2&preview=1\n"
             f"• Supervisor Preview C3 (Both 90% Confident × Manager Fails): {PUBLIC_URL}/?condition=3&preview=1\n"
             f"• Supervisor Preview C4 (Both 60% Confident × Manager Fails): {PUBLIC_URL}/?condition=4&preview=1")

    out_name = "Minor_Research_Report_EN_20261018.docx"
    p_base = os.path.join(BASE_DIR, out_name)
    p_desk = os.path.join(DESKTOP_SUBDIR, out_name)
    p_desk_clear = os.path.join(DESKTOP_SUBDIR, "Minor_Research_Proposal_ENGLISH_XiuTianyuan.docx")
    doc.save(p_base)
    shutil.copyfile(p_base, p_desk)
    shutil.copyfile(p_base, p_desk_clear)
    print(f"Saved standalone EN DOCX: {p_desk} and {p_desk_clear}")


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
