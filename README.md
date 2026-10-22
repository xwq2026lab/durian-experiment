# 人机决策冲突中的“高置信度诱导”与错误归因研究
## 实验问卷系统与学术实证分析套件 (Durian Experiment Lab)

> **研究题目**：
> - **中文**：《当算法权威遇上经验直觉：人机决策冲突中的“高置信度诱导”与错误归因研究》
> - **日文**：『アルゴリズムの権威と経験的直観の対立：人間とAIの判断競合における「高確信度誘導」とエラー帰属に関する研究』
> - **英文**：*Algorithmic Authority vs. Empirical Intuition: High-Confidence Inducement and Error Attribution in Human-AI Decision Conflicts*
> 
> **学科背景**：知识科学（Knowledge Science）、实验哲学（Experimental Philosophy）、人机交互（HCI）

---

## 目录结构与模块说明

```
durian-experiment/
├── index.html               # 交互式 Web 实验问卷（Tailwind CSS + Vue 3 + 动效 + 防回退逻辑）
├── server.py                # Python 原生零依赖后端（内置 SQLite、实时管理看板、CSV导出、REST API）
├── analysis.py              # 学术统计分析脚本（McNemar 检验、独立/配对 t 检验、相关分析、效应量 d）
├── google_forms_script.js   # Google Forms Apps Script 自动化批量建卷代码
├── qualtrics_import.txt     # Qualtrics 官方高级文本格式（一键全题库导入）
├── durian_experiment.db     # SQLite 实验数据库（自动持久化保存应答与反应耗时）
└── README.md                # 本研究技术文档与操作指南
```

---

## 核心研究范式与理论框架

1. **知识科学视角（Knowledge Science）**：
   - **默会知识（Tacit Knowledge）**：老果农基于触觉、心皮放射暗纹与果刺粗疏间距的隐性经验。
   - **形式化模型过拟合（Formal Overfitting）**：视觉 AI 基于表面轮廓三维对称性算法，陷入典型的局部形态学过拟合，忽视植物心皮发育顶起外壳的生物学因果。
2. **实验哲学视角（Experimental Philosophy）**：
   - **法兰克福“胡扯/虚张声势”归因（Frankfurt's Bullshit）**：AI 在根本不具备真实因果理解的情况下打出 94.8% 超高确信度，这种对真假漠不关心的修辞欺诈在受试者眼中构成“虚张声势（Bullshitting）”。
3. **人机交互与认知心理学（HCI & Cognitive Science）**：
   - **自动化偏差（Automation Bias）** 与 **数字锚定（Numerical Anchoring）**：94.8% 精确数字与 3D 点云权威如何剥夺受试者对常识直觉的信任。
   - **算法厌恶（Algorithm Aversion）**：当具有极高声称置信度的系统遭遇灾难性翻车时，人类信任发生不可逆坍塌。

---

## 快速使用指南

### 1. 启动本地全功能实验服务器
无需安装任何三方 Python 依赖（纯标准库实现）：
```bash
python3 server.py
```
终端将输出访问端口与地址：
* **受试者实验问卷前台**：[http://localhost:8080/](http://localhost:8080/)
* **研究员实时数据管理看板**：[http://localhost:8080/admin](http://localhost:8080/admin)
* **实时完整 CSV 下载接口**：[http://localhost:8080/api/export.csv](http://localhost:8080/api/export.csv)
* **聚合统计 JSON 接口**：[http://localhost:8080/api/stats](http://localhost:8080/api/stats)

### 2. 执行统计推断与学术报告
在终端直接运行：
```bash
python3 analysis.py
```
系统将自动输出学术级检验结果：
- **McNemar $\chi^2$ 检验**：量化 AI 94.8% 置信度是否导致统计显著的立场叛离（A $\rightarrow$ B 顺从）。
- **Welch's $t$ 检验与 Cohen's $d$**：对比“顺从算法组”与“坚守直觉组”在数字锚定（Q4）上的差异。
- **配对样本 $t$ 检验**：对比【Q9 哲学胡扯归因】vs【Q8 机械硬件归因】的竞争性假设。
- **Pearson $r$ 相关矩阵**：分析归因态度与算法厌恶（Q11）的关联。

### 3. 第三方平台问卷一键导入
* **Google Forms**：
  打开 [Google Apps Script](https://script.google.com/)，将 `google_forms_script.js` 贴入并点击“运行”，自动生成包含分页逻辑、7 点量表矩阵的正式 Google 表单。
* **Qualtrics**：
  在 Qualtrics 创建空白项目，选择“工具 (Tools) -> 导入/导出 (Import/Export) -> 从文本导入 (Import Survey from TXT)”，选择 `qualtrics_import.txt` 即可 3 秒内完成导入。
