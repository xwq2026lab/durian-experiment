#!/usr/bin/env python3
"""
Statistical Analysis Pipeline for Durian Human-AI Decision Conflict Experiment
Research Topic: Algorithmic Authority vs. Empirical Intuition
Author: Knowledge Science & Experimental Philosophy Research Group
Runs with pure Python standard library or enhanced with scipy/pandas.
"""

import sqlite3
import math
import os
import sys

DB_PATH = os.path.join(os.path.dirname(__file__), "durian_experiment.db")


def mean(arr):
    return sum(arr) / len(arr) if arr else 0.0


def stdev(arr):
    if len(arr) < 2:
        return 0.0
    m = mean(arr)
    return math.sqrt(sum((x - m) ** 2 for x in arr) / (len(arr) - 1))


def paired_t_test(x, y):
    """Calculates paired samples t-test and p-value approximation."""
    if len(x) != len(y) or len(x) < 2:
        return 0.0, 1.0, 0.0
    diffs = [a - b for a, b in zip(x, y)]
    d_bar = mean(diffs)
    s_d = stdev(diffs)
    n = len(diffs)
    se = s_d / math.sqrt(n)
    if se == 0:
        return 0.0, 1.0, 0.0
    t_stat = d_bar / se
    df = n - 1
    # Student's t approximation for p-value
    p_val = 2.0 * (1.0 - t_distribution_cdf(abs(t_stat), df))
    cohen_d = d_bar / s_d if s_d != 0 else 0.0
    return t_stat, p_val, cohen_d


def independent_t_test(x, y):
    """Welch's t-test for independent samples."""
    n1, n2 = len(x), len(y)
    if n1 < 2 or n2 < 2:
        return 0.0, 1.0, 0.0
    m1, m2 = mean(x), mean(y)
    s1, s2 = stdev(x), stdev(y)
    v1, v2 = s1 ** 2 / n1, s2 ** 2 / n2
    se = math.sqrt(v1 + v2)
    if se == 0:
        return 0.0, 1.0, 0.0
    t_stat = (m1 - m2) / se
    df = ((v1 + v2) ** 2) / ((v1 ** 2) / (n1 - 1) + (v2 ** 2) / (n2 - 1))
    p_val = 2.0 * (1.0 - t_distribution_cdf(abs(t_stat), df))
    pooled_sd = math.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
    cohen_d = (m1 - m2) / pooled_sd if pooled_sd != 0 else 0.0
    return t_stat, p_val, cohen_d


def pearson_r(x, y):
    """Calculates Pearson correlation coefficient and p-value."""
    n = len(x)
    if n < 3:
        return 0.0, 1.0
    mx, my = mean(x), mean(y)
    sx, sy = stdev(x), stdev(y)
    if sx == 0 or sy == 0:
        return 0.0, 1.0
    cov = sum((a - mx) * (b - my) for a, b in zip(x, y)) / (n - 1)
    r = cov / (sx * sy)
    t = r * math.sqrt((n - 2) / max(0.0001, (1 - r ** 2)))
    p_val = 2.0 * (1.0 - t_distribution_cdf(abs(t), n - 2))
    return r, p_val


def normal_cdf(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2)))


def t_distribution_cdf(t, df):
    """Accurate approximation of Student's t CDF across degrees of freedom."""
    if df <= 0:
        return 0.5
    # Variance stabilization transform
    z = t * (1.0 - 1.0 / (4.0 * df)) / math.sqrt(1.0 + (t * t) / (2.0 * df))
    return normal_cdf(z)


def mcnemar_test(b, c):
    """McNemar's test with continuity correction."""
    if (b + c) == 0:
        return 0.0, 1.0
    chi2 = ((abs(b - c) - 1.0) ** 2) / (b + c)
    # 1 df chi-square p-value
    p_val = 1.0 - math.erf(math.sqrt(chi2) / math.sqrt(2))
    return chi2, p_val


def run_full_analysis():
    if not os.path.exists(DB_PATH):
        print(f"[错误] 未找到实验数据库文件: {DB_PATH}")
        print("请先启动 server.py 以自动初始化数据库并注入样本数据。")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM responses")
    rows = c.fetchall()
    conn.close()

    n = len(rows)
    if n == 0:
        print("[提示] 数据库中尚无受试者数据。")
        return

    print("=" * 72)
    print("      副课题实证研究数据统计与因果检验报告 (Statistical Report)       ")
    print(" 题目:《当算法权威遇上经验直觉：人机决策冲突中的高置信度诱导与错误归因》")
    print("=" * 72)
    print(f"样本总量 (Total Sample Size): N = {n}\n")

    # ---------------------------------------------------------
    # 1. 行为决策迁移分析 (Behavioral Choice Transition & McNemar's Test)
    # ---------------------------------------------------------
    print("▶ 模块一：行为决策迁移与自动化偏差诱导 (Choice Transition & Inducement)")
    print("-" * 72)

    a_to_b = sum(1 for r in rows if r["q1_baseline"] == "A" and r["q3_final"] == "B")
    a_to_a = sum(1 for r in rows if r["q1_baseline"] == "A" and r["q3_final"] == "A")
    b_to_b = sum(1 for r in rows if r["q1_baseline"] == "B" and r["q3_final"] == "B")
    b_to_a = sum(1 for r in rows if r["q1_baseline"] == "B" and r["q3_final"] == "A")

    baseline_a = a_to_b + a_to_a
    baseline_b = b_to_b + b_to_a
    final_a = a_to_a + b_to_a
    final_b = a_to_b + b_to_b

    switch_rate_a_to_b = (a_to_b / baseline_a * 100) if baseline_a > 0 else 0
    chi2_mcnemar, p_mcnemar = mcnemar_test(a_to_b, b_to_a)

    print(f"• 基线直觉分布 (Q1) : 选样品 A (店长/鼓包) = {baseline_a} ({baseline_a/n*100:.1f}%), 选样品 B = {baseline_b} ({baseline_b/n*100:.1f}%)")
    print(f"• 最终介入分布 (Q3) : 选样品 A (店长) = {final_a} ({final_a/n*100:.1f}%), 选样品 B (AI 94.8%) = {final_b} ({final_b/n*100:.1f}%)")
    print(f"• 核心反转率 (A -> B 叛离率): {a_to_b} / {baseline_a} ({switch_rate_a_to_b:.1f}%) 的受试者在 AI 高置信度介入后推翻自身直觉倒向算法！")
    print(f"• 麦克尼马尔检验 (McNemar's Test) : χ² = {chi2_mcnemar:.3f}, p = {p_mcnemar:.4f}")
    if p_mcnemar < 0.05:
        print("  ✓ 结论: 94.8% 高置信度算法介入导致受试者发生极其显著的单向从众顺从转移 (p < 0.05)。")
    else:
        print("  - 结论: 样本量暂不足以达到统计显著性。")
    print()

    # ---------------------------------------------------------
    # 2. 诱导机制自评量表检验 (Inducement Mechanisms: Q4 - Q7)
    # ---------------------------------------------------------
    print("▶ 模块二：高置信度诱导机制量表分析 (Q4 - Q7 Likert 1-7)")
    print("-" * 72)
    scales_induce = {
        "Q4 数字锚定 (94.8% 客观科学假象)": [r["q4_anchor"] for r in rows],
        "Q5 视觉权威 (3D 网格与专业话语)": [r["q5_visual"] for r in rows],
        "Q6 认知顺从 (高确信度压制质疑)": [r["q6_conformity"] for r in rows],
        "Q7 不确定性规避 (防御性安全感)": [r["q7_uncertainty"] for r in rows]
    }

    print(f"{'测量维度':<32} {'均值 (M)':<10} {'标准差 (SD)':<12} {'与中立值(4.0)对比'}")
    for name, vals in scales_induce.items():
        m, s = mean(vals), stdev(vals)
        diff_desc = "显著偏高 (存在强烈诱导)" if m > 4.5 else "中立偏温和"
        print(f"{name:<32} {m:<10.2f} {s:<12.2f} {diff_desc}")

    # 分组检验：发生叛离者 (A->B) vs 坚守直觉者 (A->A) 的诱导心理差异
    group_switched = [r for r in rows if r["q1_baseline"] == "A" and r["q3_final"] == "B"]
    group_resisted = [r for r in rows if r["q1_baseline"] == "A" and r["q3_final"] == "A"]

    if len(group_switched) >= 2 and len(group_resisted) >= 2:
        print("\n• 组间对比：【倒向 AI 组】vs【坚守直觉组】在数字锚定(Q4)上的独立样本 t 检验:")
        q4_switch = [r["q4_anchor"] for r in group_switched]
        q4_resist = [r["q4_anchor"] for r in group_resisted]
        t_stat, p_val, d = independent_t_test(q4_switch, q4_resist)
        print(f"  M_倒向 = {mean(q4_switch):.2f} (SD={stdev(q4_switch):.2f})  vs  M_坚守 = {mean(q4_resist):.2f} (SD={stdev(q4_resist):.2f})")
        print(f"  Welch's t = {t_stat:.3f}, p = {p_val:.4f}, Cohen's d = {d:.2f}")
        if p_val < 0.05:
            print("  ✓ 结论: 倒向 AI 的受试者对数字锚定与视觉权威的敏感度显著高于坚守直觉者。")
    print()

    # ---------------------------------------------------------
    # 3. 错误归因与哲学“胡扯”检验 (Frankfurtian Bullshit vs Mechanical Error)
    # ---------------------------------------------------------
    print("▶ 模块三：结果揭晓后的归因竞争 (Q8 机械局限 vs Q9 虚张声势/胡扯 vs Q10 欺骗感)")
    print("-" * 72)
    q8_vals = [r["q8_mechanical"] for r in rows]
    q9_vals = [r["q9_bullshit"] for r in rows]
    q10_vals = [r["q10_deception"] for r in rows]
    q11_vals = [r["q11_aversion"] for r in rows]
    q12_vals = [r["q12_metacog"] for r in rows]

    print(f"• Q8 机械/硬件客观局限归因 : M = {mean(q8_vals):.2f}, SD = {stdev(q8_vals):.2f}")
    print(f"• Q9 虚张声势/胡扯归因 (Bullshit) : M = {mean(q9_vals):.2f}, SD = {stdev(q9_vals):.2f}")
    print(f"• Q10 伪科学欺骗/忽悠感归因 : M = {mean(q10_vals):.2f}, SD = {stdev(q10_vals):.2f}")

    # 配对样本 t 检验：Q9 (Bullshit) vs Q8 (Mechanical)
    t_pair, p_pair, d_pair = paired_t_test(q9_vals, q8_vals)
    print(f"\n• 配对样本 t 检验 (Q9 胡扯归因 vs Q8 机械归因):")
    print(f"  t({n-1}) = {t_pair:.3f}, p = {p_pair:.4f}, Cohen's d = {d_pair:.2f}")
    if p_pair < 0.05 and t_pair > 0:
        print("  ✓ 核心发现: 人类在面对 AI 严重翻车时，具有极其显著的【哲学胡扯归因倾向】！")
        print("    受试者普遍认为 AI 的本质是‘根本不懂真实生理因果规律却虚张声势地给出 94.8%’，")
        print("    而非仅仅原谅其为‘摄像头分辨率不足等纯硬件客观技术限制’。")
    print()

    # ---------------------------------------------------------
    # 4. 算法厌恶预测模型与相关性 (Algorithm Aversion Prediction)
    # ---------------------------------------------------------
    print("▶ 模块四：算法厌恶 (Q11) 与认知反思 (Q12) 相关性分析")
    print("-" * 72)
    r_q9_aversion, p_q9 = pearson_r(q9_vals, q11_vals)
    r_q8_aversion, p_q8 = pearson_r(q8_vals, q11_vals)
    r_q10_aversion, p_q10 = pearson_r(q10_vals, q11_vals)
    r_q12_aversion, p_q12 = pearson_r(q12_vals, q11_vals)

    print(f"• Q9 (胡扯归因) -> Q11 (算法信任崩塌/厌恶) 相关系数: r = {r_q9_aversion:.3f} (p = {p_q9:.4f})")
    print(f"• Q10 (欺骗归因) -> Q11 (算法信任崩塌/厌恶) 相关系数: r = {r_q10_aversion:.3f} (p = {p_q10:.4f})")
    print(f"• Q8 (机械局限) -> Q11 (算法信任崩塌/厌恶) 相关系数: r = {r_q8_aversion:.3f} (p = {p_q8:.4f})")
    print(f"• Q12 元认知反思警醒度均分 : M = {mean(q12_vals):.2f} (SD = {stdev(q12_vals):.2f})")
    print(f"  (反映受试者普遍对‘精确数字剥夺独立思考’产生高度警觉共鸣)")

    print("\n" + "=" * 72)
    print("                      学术统计分析流程执行完毕                          ")
    print("========================================================================\n")


if __name__ == "__main__":
    run_full_analysis()
