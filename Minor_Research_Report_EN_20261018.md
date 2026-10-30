# Human Intuition vs. Artificial Intuition: Epistemic Asymmetry and Error Attribution When Two "Ineffable Black Boxes" Conflict
## Minor Research Project Proposal & Experimental Survey Design

---

### Project Metadata
- **Research Title**: *Human Intuition vs. Artificial Intuition: Epistemic Asymmetry and Error Attribution When Two "Ineffable Black Boxes" Conflict*
- **Researcher**: Tianyuan Xiu, Master's Program (M2), School of Knowledge Science, Japan Advanced Institute of Science and Technology (JAIST)
- **Academic Advisor**: Prof. Masaharu Mizumoto
- **Date**: October 30, 2026
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

## 2. $2 \times 2$ Between-Subjects Experimental Design

### 2.1 Independent and Dependent Variables
The study employs a **$2 \times 2$ between-subjects factorial design** manipulating two orthogonal independent variables:
- **Factor 1: Matched Case-Specific Confidence Level (Between-Subjects, 2 Levels)**
  - **Both High Confidence (90% vs. 90%)**: Both the veteran store manager (recommending Durian A) and the deep-learning AI (recommending Durian B) express **90% confidence** in their respective judgments for this specific pair.
  - **Both Low Confidence (60% vs. 60%)**: Both the veteran store manager (recommending Durian A) and the deep-learning AI (recommending Durian B) find this pair borderline and express only **60% confidence** in their respective judgments.
- **Factor 2: Realized Physical Outcome / Who Failed (Between-Subjects, 2 Levels)**
  - **AI Fails / Manager Correct (Conditions 1 & 2)**: On-site slicing reveals Durian A (Manager's choice) is packed with 5 full golden chambers of sweet pulp, whereas Durian B (AI's choice) is a hollow dead-pod fruit. Stage 2 attribution items symmetrically evaluate **the failed AI system**.
  - **Manager Fails / AI Correct (Conditions 3 & 4)**: On-site slicing reveals Durian B (AI's choice) is packed with 5 full golden chambers of sweet pulp, whereas Durian A (Manager's choice) is a hollow dead-pod fruit. Stage 2 attribution items symmetrically evaluate **the failed store manager**.

### 2.2 $2 \times 2$ Factorial Condition Matrix

| Condition | Factor 1: Matched Case Confidence | Factor 2: Realized Outcome (Who Failed) | Stage 1: Symmetric Conflict Stimulus (Both trained on ~3,000 opened & tasted durians; Both have 85% Overall Accuracy) | Stage 2: On-Site Cut-Open Outcome & Symmetric Target of Attribution (`{failedAgent}`) |
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
> - **Conditions 1 & 2 (AI Fails / Store Manager Correct — Target `{failedAgent}` = `"the AI system"`)**:  
>   *Both durians are cut open on the spot: **Durian A (recommended by the manager) is packed with 5 large, full chambers of sweet golden pulp. Durian B (recommended by the AI) has a thick shell and is mostly hollow with undeveloped dead chambers inside. The store manager's intuition proved right, and the AI's prediction failed!***
> - **Conditions 3 & 4 (Store Manager Fails / AI Correct — Target `{failedAgent}` = `"the store manager"`)**:  
>   *Both durians are cut open on the spot: **Durian B (recommended by the AI) is packed with 5 large, full chambers of sweet golden pulp. Durian A (recommended by the manager) has a thick shell and is mostly hollow with undeveloped dead chambers inside. The AI's prediction proved right, and the store manager's intuition failed!***

#### Symmetric Post-Outcome Attribution, "Bullshitting," and Post-Hoc Feature Extraction Scales (7-Point Likert: 1 = Strongly Disagree, 4 = Neutral, 7 = Strongly Agree)
*(Note: Items Q5–Q7 dynamically insert `{failedAgent}` = **"the AI system"** in Conditions 1 & 2, and **"the store manager"** in Conditions 3 & 4, enabling a direct symmetric test of human vs. AI error attribution)*:
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
- **Hypothesis 3 (H3: Confidence $\times$ Failed Agent Interaction & Post-Hoc Feature Extraction)**: There will be a significant two-way interaction between Case Confidence (90% vs. 60%) and Failed Agent (AI Fails vs. Manager Fails) on Q6, Q7, and Q9 ($p < .01$). Failing after expressing 90% confidence will provoke a much harsher backlash than failing after expressing 60% confidence, and this *Penalty of Overconfidence* will be disproportionately steeper when the AI fails (C1 vs. C2) than when the human manager fails (C3 vs. C4). Furthermore, Q8 will show strong positive agreement ($> 5.0$), demonstrating that **post-hoc explicit feature extraction** is a key mechanism for overcoming distrust of AI intuition.

### 4.2 Expected Results & A Priori Sample Size Calculation (Power Analysis)
Based on Hypotheses H1–H3, we specify the rough quantitative expectations on the 7-point Likert scales (1 = Strongly Disagree, 4 = Neutral, 7 = Strongly Agree, assuming a typical within-cell standard deviation of $SD \approx 1.15$):
1. **Stage 1 Expectations**: Under strictly symmetric baselines, approximately **55%–60%** of participants are expected to favor Human Intuition (Durian A) vs. **40%–45%** for AI Intuition (Durian B), while Q4 (Epistemic Double Standard on Unexplainability) is expected to average **$M = 5.10, SD = 1.20$** (significantly above the midpoint $4.0$, one-sample Cohen's $d \approx 0.92$).
2. **Stage 2 Expected $2 \times 2$ Cell Means (illustrated on the primary outcome Q6: Frankfurtian "Bullshitting" Attribution)**:

| Condition | Factor 1: Confidence | Factor 2: Failed Agent | Expected Mean ($M$) | Expected $SD$ | Substantive Interpretation |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Condition 1** | High (90%) | AI System Fails | **5.60** | 1.15 | Severe backlash: 90%-confident failed black-box AI judged as "bullshitting" |
| **Condition 2** | Low (60%) | AI System Fails | **3.80** | 1.15 | Attenuated blame when AI expressed borderline 60% uncertainty ($\Delta_{\text{AI}} = +1.80$) |
| **Condition 3** | High (90%) | Manager Fails | **3.60** | 1.15 | Greater leniency toward human veteran intuition failing at 90% confidence |
| **Condition 4** | Low (60%) | Manager Fails | **3.40** | 1.15 | Excused as normal 15% statistical outlier ($\Delta_{\text{Human}} = +0.20$) |

3. **Required Sample Size Calculation ($\alpha = 0.05$, Power $1 - \beta = 0.80$, $2 \times 2$ Fixed-Effects ANOVA, $df_1 = 1$)**:
   - **Main Effect of Failed Agent** ($\mu_{\text{AI}} = 4.70$ vs. $\mu_{\text{Human}} = 3.50$, effect $|\beta| = 0.60$): Cohen's $f = 0.60 / 1.15 = \mathbf{0.52}$ $\rightarrow$ minimum required **$N = 32$** ($n = 8$ per condition).
   - **Main Effect of Confidence** ($\mu_{90\%} = 4.60$ vs. $\mu_{60\%} = 3.60$, effect $|\alpha| = 0.50$): Cohen's $f = 0.50 / 1.15 = \mathbf{0.43}$ $\rightarrow$ minimum required **$N = 45$** ($n = 12$ per condition).
   - **Two-Way Interaction Effect** ($|\gamma| = |(5.60 - 3.80) - (3.60 - 3.40)| / 4 = 0.40$): **Cohen's $f = 0.40 / 1.15 = \mathbf{0.35}$** $\rightarrow$ minimum required **$N = 68$** (**$n = 17$ per condition**) to achieve $80\%$ statistical power at $\alpha = 0.05$.
   - Including a ~15% buffer for quality screening, the **target sample size is $N = 80$ participants ($n = 20$ per condition)** within a single homogeneous participant pool.

### 4.3 Target Participant Pool & Cultural Scope
- **Primary Baseline Design (Single Homogeneous Cultural Group)**: To avoid linguistic and cultural confounding within the $2 \times 2$ design, the baseline study recruits a single culturally homogeneous participant group (**$N = 68\text{–}80$ adult native speakers of one language**, e.g., native Chinese speakers, with the survey interface locked to that language). The multilingual toggle (English / Japanese / Chinese) is maintained on the review interface solely for academic supervision.
- **Optional Cross-Cultural Extension (If Multi-Language Crowdsourcing Panels Are Utilized)**: Should crowdsourcing panels be deployed across both Japanese and Chinese speakers ($N = 68\text{–}80$ per cultural group), an exploratory cultural hypothesis (H4) can be tested: whether Japanese participants exhibit greater deference and error-forgiveness toward ineffable human intuition—reflecting the cultural valuation of embodied *shokunin* craftsmanship and tacit knowledge—compared to Chinese participants accustomed to pervasive algorithmic consumer recommendation ecosystems.

### 4.4 Statistical Modeling Pipeline
1. **Binomial & Logistic Regression (Q1)** controlling for continuous Age (Q11), STEM background (Q12), and AI usage frequency (Q13):
   $$\text{logit}(P(\text{Choice} = \text{AI})) = \beta_0 + \beta_1 \cdot \text{ConfidenceLevel} + \beta_2 \cdot \text{Age} + \beta_3 \cdot \text{STEM} + \beta_4 \cdot \text{AIFreq}$$
2. **Two-Way Factorial ANOVA & ANCOVA (Q2–Q9)**:
   $$Y_{ijk} = \mu + \alpha_i (\text{Confidence}_i) + \beta_j (\text{FailedAgent}_j) + (\alpha\beta)_{ij} (\text{Confidence}_i \times \text{FailedAgent}_j) + \epsilon_{ijk}$$

---

## 5. Online Experimental System & Blinded Access Links

The online platform strictly separates the **Blinded Participant Entry** from the **Supervisor Preview Mode**: on the actual participant URL, **all condition-switching tabs and condition labels are completely hidden**, and random assignment is locked per browser session so participants cannot view other conditions. Condition-switching tabs appear exclusively when `?preview=1` is appended by the researcher.

- **Blinded Participant Survey Entry (Condition tabs strictly hidden)**: [https://durian-experiment.vercel.app](https://durian-experiment.vercel.app)
  - Single-Language Locked Participant Entry (e.g., Chinese-locked): [https://durian-experiment.vercel.app/?lang=zh&locklang=1](https://durian-experiment.vercel.app/?lang=zh&locklang=1)
- **Researcher & Supervisor Admin Portal**: [https://durian-experiment.vercel.app/admin](https://durian-experiment.vercel.app/admin)
- **Supervisor Preview Links (With `?preview=1` condition switcher for inspection only)**:
  - Condition 1 (Both 90% Confident × AI Fails / Manager Wins): [https://durian-experiment.vercel.app/?condition=1&preview=1](https://durian-experiment.vercel.app/?condition=1&preview=1)
  - Condition 2 (Both 60% Confident × AI Fails / Manager Wins): [https://durian-experiment.vercel.app/?condition=2&preview=1](https://durian-experiment.vercel.app/?condition=2&preview=1)
  - Condition 3 (Both 90% Confident × Manager Fails / AI Wins): [https://durian-experiment.vercel.app/?condition=3&preview=1](https://durian-experiment.vercel.app/?condition=3&preview=1)
  - Condition 4 (Both 60% Confident × Manager Fails / AI Wins): [https://durian-experiment.vercel.app/?condition=4&preview=1](https://durian-experiment.vercel.app/?condition=4&preview=1)
