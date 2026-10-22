#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full Academic Report Generator with Perfect Typography (No Mixed Font Sizes).
Configures OpenXML rFonts (ascii, hAnsi, eastAsia, cs) and exact sz/szCs.
Outputs full academic documents with all chapters, instruments, and tables.
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
DESKTOP_DIR = "/Users/xwq123456/Desktop/副课题"

PUBLIC_URL = "https://exceptional-inexpensive-measures-displayed.trycloudflare.com"
ADMIN_URL = f"{PUBLIC_URL}/admin"

# ==============================================================================
# TYPOGRAPHY HELPER FUNCTIONS
# ==============================================================================

def configure_doc_defaults(doc, is_cn=True):
    """Ensure document defaults have consistent font families and sizes."""
    ascii_font = "Times New Roman"
    eastasia_font = "SimSun" if is_cn else "Times New Roman"
    default_sz = "21"  # 10.5 pt (Standard 五号)
    
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
                        
    # Normal style configuration
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
    """Apply strict, uniform font properties to every single run to eliminate size discrepancy."""
    ascii_font = "Times New Roman"
    eastasia_font = "SimSun" if is_cn else "Times New Roman"
    
    run.font.name = ascii_font
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)
    
    rPr = run._r.get_or_add_rPr()
    
    # 1. Ensure rFonts is completely specified
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")}/>')
        rPr.insert(0, rFonts)
    rFonts.set(qn('w:ascii'), ascii_font)
    rFonts.set(qn('w:hAnsi'), ascii_font)
    rFonts.set(qn('w:eastAsia'), eastasia_font)
    rFonts.set(qn('w:cs'), ascii_font)
    
    # 2. Strict half-point sizes for both Latin and Asian/Complex scripts
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
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.25
        run = p.add_run(item)
        apply_font_to_run(run, is_cn=is_cn, size_pt=10.0, bold=(idx == 0), color_rgb=(0x1E, 0x29, 0x3B))
        
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def format_academic_table(table, col_widths, headers, data, is_cn=True):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    # Header row
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
            
    # Data rows
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
            apply_font_to_run(run, is_cn=is_cn, size_pt=9.0, bold=(c_idx == 0), color_rgb=text_color)

# ==============================================================================
# BUILD EXHAUSTIVE CHINESE WORD REPORT
# ==============================================================================

def build_full_cn_docx():
    doc = docx.Document()
    configure_doc_defaults(doc, is_cn=True)
    
    # 1 inch margins
    for sec in doc.sections:
        sec.top_margin = Inches(1.0)
        sec.bottom_margin = Inches(1.0)
        sec.left_margin = Inches(1.0)
        sec.right_margin = Inches(1.0)
        
    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=True, size_pt=16.0, bold=True, color_rgb=(0x0F, 0x17, 0x2A))
        return p

    def add_subtitle(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(14)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=True, size_pt=11.5, italic=True, color_rgb=(0x47, 0x55, 0x69))
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=True, size_pt=13.0, bold=True, color_rgb=(0x0F, 0x17, 0x2A))
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
        apply_font_to_run(r, is_cn=True, size_pt=10.5, bold=False, color_rgb=(0x33, 0x41, 0x55))
        return p

    # --- COVER / METADATA ---
    add_title("《数据驱动型 AI 与不可言传的专家直觉：人机决策冲突中的置信度诱导与结果归因研究》")
    add_subtitle("副课题研究计划与实验问卷方案（审阅定稿版）")
    
    meta_info = [
        "【基本信息 / Metadata】",
        "• 研究题目：数据驱动型 AI 与不可言传的专家直觉：人机决策冲突中的置信度诱导与结果归因研究",
        "• 英文题目：Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts",
        "• 研究者：修 天源 (XIU TIANYUAN) — 北陆先端科学技术大学院大学 (JAIST) 知识科学研究科 博士前期课程2年 (M2)",
        "• 指导教授：水本 教授 (Prof. Mizumoto)",
        "• 提交日期：2026年10月18日",
        "• 研究领域：知识科学 (Knowledge Science)、实验哲学 (Experimental Philosophy)、人机交互 (HCI)、认知心理学 (Cognitive Psychology)",
        f"• 在线实验系统公网入口：{PUBLIC_URL}",
        f"• 导师后台控制台入口：{ADMIN_URL}"
    ]
    add_callout(doc, meta_info, is_cn=True, border_color="3B82F6", bg_color="F0F9FF")

    # --- CHAPTER 1 ---
    add_h1("1. 研究背景与理论演进 (Background & Theoretical Framework)")
    add_body(
        "在知识科学（Knowledge Science）与认识论（Epistemology）的经典理论体系中，迈克尔·波兰尼（Michael Polanyi, 1966）揭示了一个核心命题：“我们知道的多于我们能言说的（We can know more than we can tell）”。人类专家的最高阶智慧往往以“隐性知识（Tacit Knowledge）”的形式沉淀于长期的具身实践、感官体验与整体直觉中。老练的匠人或专家能够在瞬间得出精准判断，但若要求其用显性的逻辑规则或语言条分缕析地解释原因，他们往往只能表示“这是经手成千上万次后自然形成的手感和感觉”。"
    )
    add_body(
        "然而，当代以深度神经网络为代表的人工智能系统展现出了一种截然不同的决策表征形式。当代深度学习系统并非依赖人工编写的显性规则算法（Explicit Algorithms），而是基于海量数据集（Massive Datasets，如百万级配对图像）进行高维统计拟合。在面向人类用户输出决策时，这类“黑盒”模型通常伴随一个精确的标量数值——置信度评分（Confidence Score，如 94.8% 或 58.2%）。当不可言传的专家经验与高置信度的数据驱动 AI 迎头相遇时，便构成了极具现实意义的认知冲突情境。"
    )

    add_h2("1.1 回应水本教授指导意见的四大核心修正")
    add_body(
        "全面移除几何夹角（42.3°）与曲率峰值等显性算法描述。当代深度神经网络并不依赖手工几何规则，因此确立 AI 决策完全由“100万张真实榴莲外观—开壳结果配对图像数据集”训练而成，仅输出统计置信度百分比，符合数据驱动黑盒的本质。",
        "1. 从“显性算法（Algorithm）”转向“数据驱动黑盒（Data-Driven AI）”："
    )
    add_body(
        "原方案中店长解释“刺细密代表壳厚”，容易被误认为显性知识并被 AI 吸收。现全面重构为：店长拥有 15 年从业经验、经手数万颗榴莲，明确表示“挑榴莲没有死规矩，全凭手感与直觉，无法用语言解释清楚”。这严格符合波兰尼关于“不可言传性”的哲学界定。",
        "2. 确立真正的“不可言传隐性知识（Ineffable Tacit Knowledge）”："
    )
    add_body(
        "彻底砍掉受试者事前自主盲猜阶段（原 Phase 1），消除自主猜测所带来的“先验锚定效应”与“自我一致性承诺偏差”，严格采用国际标准的实验哲学情境实验法（Vignette Paradigm）。",
        "3. 消除锚定混杂变量，砍掉事前盲猜阶段（Phase 1）："
    )
    add_body(
        "引入 AI 置信度（高 94.8% vs. 低 58.2%）与开壳真实结果（AI 失败/店长胜 vs. AI 成功/店长败）两个完全正交的自变量，构成 4 组独立的实验条件，为后续开展严格的双因素方差分析（Two-Way ANOVA）提供坚实的数据结构。",
        "4. 升级为标准的 2×2 组间析因实验设计（Between-Subjects Factorial Design）："
    )

    # --- CHAPTER 2 ---
    add_h1("2. 实验任务载体与科学依据 (Scientific Validity of the Task Scenario)")
    add_body(
        "本研究选取“挑选未开壳榴莲内部果肉饱满度（房数）”作为实验情境载体，具有严密的科学合理性与现实生态效度："
    )
    add_body(
        "榴莲（Durio zibethinus）属于锦葵科蒴果，内部心皮发育膨大会顶起果壳形成鼓包。但植物生理中普遍存在“死包空心果”：外壳因吸收过多养分而极其浑圆对称，内部心皮却完全败育。因此，挑选果实具有客观解剖学规律，绝非随机猜运气。",
        "• 植物形态学与解剖学客观依据："
    )
    add_body(
        "资深店长依赖多模态具身触觉（上手掂量重力分布、轻捏刺的弹性弹性与轻晃听声等不可言传的隐性经验），能够识别出死包果；而基于图像数据训练的 AI 极易对“外表浑圆对称”这类几何特征产生统计过拟合（Overfitting），在面对极其浑圆的空心死包果时反而容易输出超高置信度（94.8%）。",
        "• 人机认知机制的天然对立："
    )
    add_body(
        "榴莲切开后，内部饱满果肉与空心死壳黑白分明，不存在模糊解释空间，为后测的归因与信任测量提供了完美的客观反馈节点。",
        "• 真实反馈的非对称性与高确定性："
    )

    # --- CHAPTER 3 ---
    add_h1("3. 2×2 组间实验设计矩阵 (2×2 Between-Subjects Factorial Design)")
    add_body(
        "实验建立两个完全正交的自变量：自变量 1 为 AI 预测置信度（高 94.8% vs. 低 58.2%）；自变量 2 为现场开壳真实结果（AI 失败/店长胜 vs. AI 成功/店长败）。受试者进入系统后被完全随机分配至 4 种实验条件之一："
    )
    
    col_w = [Inches(1.1), Inches(1.3), Inches(1.3), Inches(2.8)]
    headers = ["组别 (Condition)", "自变量1: AI置信度", "自变量2: 开壳真实结果", "刺激呈现与现实开壳特征"]
    data = [
        ["Condition 1", "高置信度 (94.8%)", "AI 失败 (店长正确)", "店长凭不可言传经验力荐 A；AI 显示 94.8% 置信度力荐 B；开壳显示 A 满5房黄金果肉，B 为中空死包（店长完胜，AI惨败）"],
        ["Condition 2", "低置信度 (58.2%)", "AI 失败 (店长正确)", "店长凭不可言传经验力荐 A；AI 显示 58.2% 置信度谨慎荐 B；开壳显示 A 满5房黄金果肉，B 为中空死包（店长完胜，AI失败）"],
        ["Condition 3", "高置信度 (94.8%)", "AI 成功 (店长失误)", "店长凭不可言传经验力荐 A；AI 显示 94.8% 置信度力荐 B；开壳显示 B 满5房黄金果肉，A 为中空死包（AI完胜，店长失误）"],
        ["Condition 4", "低置信度 (58.2%)", "AI 成功 (店长失误)", "店长凭不可言传经验力荐 A；AI 显示 58.2% 置信度谨慎荐 B；开壳显示 B 满5房黄金果肉，A 为中空死包（AI成功，店长失误）"]
    ]
    t = doc.add_table(rows=1, cols=4)
    format_academic_table(t, col_w, headers, data, is_cn=True)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # --- CHAPTER 4 ---
    add_h1("4. 在线实验系统与部署特性 (Online Deployment & Interactive System)")
    add_body(f"受试者问卷系统主入口：{PUBLIC_URL}")
    add_body(f"导师后台管理平台入口：{ADMIN_URL}")
    add_body(
        "系统核心工程特性：\n"
        "1. 中英日三语动态切换：默认英语呈现，右上角支持随时一键切换为日语与中文。\n"
        "2. 条件快速预览切换条：问卷顶端集成 [C1 | C2 | C3 | C4] 胶囊切换按钮，供导师与研究人员即时预览全部 4 个组别的实验交互。\n"
        "3. 高精度行为埋点：记录 stage1Ms, stage2Ms, stage3Ms 毫秒级阅读与决策时长，自动筛除无效样本。\n"
        "4. 独立存储与导出：搭载 SQLite 3 关系型数据库，后台支持实时 2×2 样本矩阵图表与 UTF-8 BOM CSV 一键下载。"
    )

    # --- CHAPTER 5 ---
    add_h1("5. 实验问卷完整题项与量表设计 (Full Survey Instrument)")
    add_h2("第一部分：人机冲突情境与决策偏好 (Stage 1)")
    add_body("情境展示：展示 A、B 两颗榴莲。店长直言：“我也没法用语言跟你说清楚具体看哪里，挑榴莲没有死规矩，就是我干了15年、摸过几万颗榴莲攒下来的直觉与手感，A号肯定肉多。” AI 终端显示：“基于超100万张真实开壳图像训练。模型预测结果：推荐 B号（预测置信度：94.8% / 58.2%）”。")
    add_body("Q1. 【二元决策选择】面对店长无法解释的直觉与 AI 系统预测，此时您会选择买哪一颗？\n   • 选项 A：选择 A号（跟随店长的经验直觉）\n   • 选项 B：选择 B号（跟随 AI 系统的预测）")
    add_body("决策前认知评估量表（7级李克特量表：1 = 完全不同意，7 = 完全同意）：\n"
             "• Q2（数据权威与客观性感知）：相比于店长“说不清道不明”的个人直觉，基于百万级数据集训练出来的 AI 模型让我觉得更加客观、可靠。\n"
             "• Q3（置信度锚定效应）：AI 给出的置信度百分比（94.8% / 58.2%），对我刚才做出选择起到了决定性的引导作用。\n"
             "• Q4（对不可言传经验的怀疑倾向）：如果人类专家无法用清晰的语言解释他的判断逻辑，我很难放心把决定权交给他。")

    add_h2("第二部分：开壳真实结果揭晓与归因测量 (Stage 2)")
    add_body("开壳真实结果揭晓：工作人员当场切开两颗榴莲。依据分组条件，展示 A号满5房黄金果肉/B号空壳死包（AI失败），或展示 B号满5房黄金果肉/A号空壳死包（AI成功）。")
    add_body("后测归因与信任评估量表（7级李克特量表：1 = 完全不同意，7 = 完全同意）：\n"
             "• Q5（概率/统计局限归因 - 理性技术维度）：无论是 AI 还是人类专家，挑榴莲本质上都存在概率上的不确定性，失败的一方只是这次恰好遇到了统计分布之外的例外情况，情有可原。\n"
             "• Q6（“不懂装懂/胡扯”归因 - 实验哲学 Bullshitting 维度）：回顾 AI 刚才给出的预测和置信度，我认为 AI 根本没有真正“理解”榴莲的特征，它只是在用数字进行一种“盲目的胡扯（Bullshitting）”或虚张声势。\n"
             "• Q7（误导与受骗感 - 拟人化意图投射）：我觉得 AI 系统展示出的“大数据背景”和“精确百分比”具有误导性，甚至让我产生了一种被这套技术表象“操控或欺骗”的感觉。\n"
             "• Q8（对不可言传隐性知识的重估 - 知识科学维度）：看到这个结果后，我认为在复杂的现实物理任务中，人类难以言传的“经验直觉（暗黙知）”依然具有数据模型无法替代的价值。\n"
             "• Q9（未来信任倾向 / 自动化偏差留存）：如果下次还要挑选榴莲或进行类似的日常物品鉴别，我依然更愿意相信大数据 AI 的预测，而不是人类行家的直觉。")

    add_h2("第三部分：受试者人口学背景信息 (Stage 3)")
    add_body("• Q10. 生理性别：[男 / 女 / 其他或不愿透露]\n"
             "• Q11. 年龄区间：[20岁以下 / 20–29岁 / 30–39岁 / 40–49岁 / 50岁及以上]\n"
             "• Q12. 学科专业背景：[是（理工科 / 计算机 / 数据与 AI 相关） / 否（人文社科 / 商科 / 艺术 / 其他）]\n"
             "• Q13. 日常 AI 工具使用频率：[几乎不用 / 每周 1–2 次 / 几乎每天 / 重度深度依赖]")

    # --- CHAPTER 6 ---
    add_h1("6. 统计假设与双因素方差分析方案 (Statistical Hypotheses & Analysis Plan)")
    add_body(
        "在开壳前决策阶段，高置信度组（94.8%）受试者选择 AI（Q1）的比例以及对数据客观性的认可度（Q2, Q3）将显著高于低置信度组（58.2%）（p < .001）。这表明高确定性的数字包装能够显著强化自动化偏差（Automation Bias）。",
        "• 假设 1 (H1: 置信度主效应 / Main Effect of Confidence)："
    )
    add_body(
        "当目睹 AI 预测彻底失败后（Condition 1 & 2），受试者在法兰克福式“胡扯（Bullshitting）”归因（Q6）与“被欺骗感”（Q7）上的得分显著高于 AI 成功组（p < .001）。受试者不仅将失败归因于算法缺陷，还会产生拟人化的负面动机投射。",
        "• 假设 2 (H2: 结果主效应与意图投射 / Main Effect of Outcome)："
    )
    add_body(
        "AI 置信度与开壳结果在“胡扯归因”（Q6）与“未来信任摧毁”（Q9）上存在显著交互作用（F(1, N-4) > 0, p < .01）。在 AI 失败条件下，高置信度失败（Condition 1）将激发最强烈的负面心理反弹，其信任崩塌程度显著大于低置信度失败（Condition 2），验证“算法过度自负所招致的惩罚性信任清算”。",
        "• 假设 3 (H3: 交互效应 - “高置信度失败的背叛惩罚” / Penalty of Overconfidence)："
    )
    add_body(
        "统计检验方案：采用二元 Logistic 回归分析 Q1 初始决策；对 Q2–Q9 采用标准的 2×2 双因素方差分析模型：\n"
        "Y_ijk = μ + α_i (Confidence) + β_j (Outcome) + (αβ)_ij + ε_ijk\n"
        "并以理工科背景（Q12）和 AI 使用频率（Q13）作为协变量开展 ANCOVA 检验，探索专业知识是否能够成为对抗“过度自信诱导”的认知防护缓冲带。"
    )

    out_name = "Minor_Research_Report_CN_20261018.docx"
    p_base = os.path.join(BASE_DIR, out_name)
    p_desk = os.path.join(DESKTOP_DIR, out_name)
    doc.save(p_base)
    shutil.copyfile(p_base, p_desk)
    print(f"Generated perfect CN DOCX: {p_desk}")

# ==============================================================================
# BUILD EXHAUSTIVE ENGLISH WORD REPORT
# ==============================================================================

def build_full_en_docx():
    doc = docx.Document()
    configure_doc_defaults(doc, is_cn=False)
    
    # 1 inch margins
    for sec in doc.sections:
        sec.top_margin = Inches(1.0)
        sec.bottom_margin = Inches(1.0)
        sec.left_margin = Inches(1.0)
        sec.right_margin = Inches(1.0)
        
    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=False, size_pt=15.0, bold=True, color_rgb=(0x0F, 0x17, 0x2A))
        return p

    def add_subtitle(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(14)
        run = p.add_run(text)
        apply_font_to_run(run, is_cn=False, size_pt=11.0, italic=True, color_rgb=(0x47, 0x55, 0x69))
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
        apply_font_to_run(r, is_cn=False, size_pt=10.5, bold=False, color_rgb=(0x33, 0x41, 0x55))
        return p

    # --- COVER / METADATA ---
    add_title("Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts")
    add_subtitle("Minor Research Project Design & Experimental Survey Instrument (Final Review Version)")
    
    meta_info = [
        "[Metadata & Affiliation]",
        "• Project Title: Data-Driven AI vs. Ineffable Expert Intuition: Confidence Inducement and Outcome Attribution in Human-AI Decision Conflicts",
        "• Researcher: XIU TIANYUAN (修 天源) — JAIST School of Knowledge Science, Master's Program (M2)",
        "• Academic Advisor: Prof. Mizumoto (水本 教授)",
        "• Submission Date: October 18, 2026",
        "• Research Domains: Knowledge Science, Experimental Philosophy, Human-Computer Interaction (HCI), Cognitive Psychology",
        f"• Participant Survey URL: {PUBLIC_URL}",
        f"• Admin & Analytics Dashboard: {ADMIN_URL}"
    ]
    add_callout(doc, meta_info, is_cn=False, border_color="3B82F6", bg_color="F0F9FF")

    # --- CHAPTER 1 ---
    add_h1("1. Background & Theoretical Framework")
    add_body(
        "In the foundational literature of Knowledge Science and Epistemology, Michael Polanyi (1966) famously posited: 'We can know more than we can tell.' High-level human expert judgment often resides in the domain of ineffable tacit knowledge, acquired through prolonged somatic engagement, experiential practice, and holistic perceptual Gestalt. When seasoned experts assess physical objects, their diagnostic conclusions are immediate and remarkably accurate. However, when asked to codify their decision rules into explicit natural language or algorithmic formulas, they inevitably find it impossible: 'It is an intuitive gut feeling built on handling tens of thousands of cases.'"
    )
    add_body(
        "Conversely, contemporary Artificial Intelligence—exemplified by deep learning computer vision systems—operates under an entirely different paradigm. Modern neural networks do not rely on explicit, hand-coded human geometric or logical algorithms. Instead, they represent high-dimensional statistical correlations extracted from massive datasets comprising millions of training images. When interfacing with human decision-makers, these black-box models routinely output a scalar quantitative metric: a Confidence Score (e.g., 94.8% vs. 58.2%). The collision between ineffable expert intuition and data-driven AI authority establishes a profound cognitive context for studying automation bias and outcome attribution."
    )

    add_h2("1.1 Core Revisions Guided by Prof. Mizumoto")
    add_body(
        "All references to explicit geometric rules (angles, curvature) have been eradicated. The AI system is operationalized as a deep neural network trained on a dataset of 1,000,000+ real-world paired images. It outputs strictly a statistical prediction accompanied by a quantitative confidence score, preserving its black-box epistemic nature.",
        "1. Shift from 'Explicit Algorithm' to 'Data-Driven AI': "
    )
    add_body(
        "The manager has 15 years of experience handling tens of thousands of durians. When asked, he explicitly states: 'I honestly cannot explain the rules in words. There are no fixed formulas—it is purely a gut feeling and somatic touch developed over 15 years.' This precisely operationalizes Polanyi's ineffability.",
        "2. Re-conceptualization of Store Manager (Genuine Ineffable Tacit Knowledge): "
    )
    add_body(
        "Asking participants to guess independently before exposure creates self-consistency motivation and anchoring bias, distorting post-stimulus measurements. Phase 1 has been completely removed. The study adopts the standard Vignette Experiment Paradigm in experimental philosophy.",
        "3. Elimination of Phase 1 Blind Guessing: "
    )
    add_body(
        "The study establishes two orthogonal factors: AI Confidence Level (High 94.8% vs. Low 58.2%) × Realized Outcome (AI Fails vs. AI Succeeds), forming four randomized conditions for robust Two-Way ANOVA testing.",
        "4. Standard 2×2 Between-Subjects Factorial Matrix: "
    )

    # --- CHAPTER 2 ---
    add_h1("2. Scientific Validity of the Task Scenario")
    add_body(
        "Selecting the visual assessment of un-opened durian fruit pulp fullness provides high ecological and scientific validity:"
    )
    add_body(
        "Durian (Durio zibethinus) is a capsular fruit where carpel development directly expands the outer rind into protruding chambers. However, physiological 'hollow-shell (dead-pod)' fruits exist, where nutrients are absorbed into thick rind structures, resulting in perfectly symmetrical outer globes with aborted internal chambers.",
        "• Objective Botanical Morphology: "
    )
    add_body(
        "Seasoned human experts rely on multimodal somatic cues (mass distribution, spine resilience, acoustic resonance) capable of detecting deceptive dead-pod fruits. Conversely, purely visual data-driven AI systems are prone to statistical overfitting on superficial geometric symmetry, assigning dangerously high confidence scores (94.8%) to aesthetically uniform but hollow specimens.",
        "• Natural Divergence of Decision Modalities: "
    )
    add_body(
        "Slicing the fruit on-site produces immediate, non-negotiable visual feedback (full golden pulp vs. empty hollow pods), providing an optimal benchmark for attribution and trust measurement.",
        "• Irreversible, Unambiguous Ground Truth: "
    )

    # --- CHAPTER 3 ---
    add_h1("3. 2×2 Between-Subjects Experimental Design Matrix")
    add_body(
        "The factorial matrix orthogonally crosses Factor 1 (AI Confidence Level: High 94.8% vs. Low 58.2%) with Factor 2 (Realized Outcome: AI Fails vs. AI Succeeds). Participants are randomly assigned to one of four experimental conditions upon loading the survey:"
    )
    
    col_w = [Inches(1.1), Inches(1.3), Inches(1.3), Inches(2.8)]
    headers = ["Condition", "Factor 1: AI Confidence", "Factor 2: Realized Outcome", "Stimulus & Outcome Operationalization"]
    data = [
        ["Condition 1", "High Confidence (94.8%)", "AI Fails (Manager Correct)", "Manager recommends A via tacit intuition; AI outputs 94.8% confidence for B; Cut-open reveals A is full (5 chambers) and B is empty dead-pod (Manager wins, AI fails)"],
        ["Condition 2", "Low Confidence (58.2%)", "AI Fails (Manager Correct)", "Manager recommends A via tacit intuition; AI outputs 58.2% confidence for B; Cut-open reveals A is full (5 chambers) and B is empty dead-pod (Manager wins, AI fails)"],
        ["Condition 3", "High Confidence (94.8%)", "AI Succeeds (Manager Fails)", "Manager recommends A via tacit intuition; AI outputs 94.8% confidence for B; Cut-open reveals B is full (5 chambers) and A is empty dead-pod (AI wins, Manager fails)"],
        ["Condition 4", "Low Confidence (58.2%)", "AI Succeeds (Manager Fails)", "Manager recommends A via tacit intuition; AI outputs 58.2% confidence for B; Cut-open reveals B is full (5 chambers) and A is empty dead-pod (AI wins, Manager fails)"]
    ]
    t = doc.add_table(rows=1, cols=4)
    format_academic_table(t, col_w, headers, data, is_cn=False)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # --- CHAPTER 4 ---
    add_h1("4. Online Interactive System Architecture & Live Access Links")
    add_body(f"Participant Survey Web Application: {PUBLIC_URL}")
    add_body(f"Supervisor Analytics Dashboard: {ADMIN_URL}")
    add_body(
        "Technical Highlights:\n"
        "1. Instant Trilingual Localization: English default with zero-latency toggling to Japanese (日本語) and Simplified Chinese (中文).\n"
        "2. Embedded Condition Switcher Bar: Top-level [C1 | C2 | C3 | C4] pill buttons allow Prof. Mizumoto to immediately preview all four scenarios with one click.\n"
        "3. High-Precision Telemetry: Millisecond behavioral tracking (stage1Ms, stage2Ms, stage3Ms) to detect satisficing respondents.\n"
        "4. Relational Data Pipeline: SQLite 3 engine supporting real-time factorial cell monitoring and one-click UTF-8 BOM CSV export for SPSS and R."
    )

    # --- CHAPTER 5 ---
    add_h1("5. Full Survey Instrument & Measurement Scales")
    add_h2("Stage 1: The Decision Conflict Scenario & Initial Choice (Stage 1)")
    add_body("Vignette Stimulus: Store manager asserts: 'I honestly can't explain it in words. There is no fixed rule to tell you. It's just a gut feeling and intuition after handling tens of thousands of durians over 15 years. Durian A is definitely fuller.' Visual AI terminal displays: 'Trained on 1,000,000+ real durian images. Recommend Durian B (Confidence Score: 94.8% / 58.2%).'")
    add_body("Q1. [Binary Behavioral Choice] Facing the manager's intuition (which he cannot verbally explain) and the data-driven AI's prediction, which durian do you decide to choose?\n   • Option A: Choose Durian A (Follow the Veteran Store Manager)\n   • Option B: Choose Durian B (Follow the Data-Driven AI)")
    add_body("Pre-Outcome Cognitive Scales (7-Point Likert: 1 = Strongly Disagree, 7 = Strongly Agree):\n"
             "• Q2 (Perceived Data Objectivity): Compared to the manager’s unexplainable personal intuition, an AI model trained on a massive dataset of over a million images feels more objective and reliable to me.\n"
             "• Q3 (Confidence Score Impact): The specific confidence percentage displayed by the AI (94.8% / 58.2%), heavily influenced my choice just now.\n"
             "• Q4 (Skepticism Toward Ineffable Intuition): If a human expert cannot verbally explain the reasoning behind their judgment, I find it difficult to trust their recommendation.")

    add_h2("Stage 2: Outcome Revelation & Post-Outcome Attribution (Stage 2)")
    add_body("Ground Truth Revelation: Both fruits are sliced open on-site, revealing either full golden pulp in A and hollow dead pods in B (AI Failure), or full golden pulp in B and hollow dead pods in A (AI Success).")
    add_body("Post-Outcome Attribution & Trust Scales (7-Point Likert: 1 = Strongly Disagree, 7 = Strongly Agree):\n"
             "• Q5 (Probabilistic Limitation Attribution - Rational Dimension): Whether relying on big-data AI or human intuition, sorting natural fruits always involves probabilistic uncertainty; the side that failed simply encountered an unavoidable statistical outlier.\n"
             "• Q6 ('Bullshitting' Attribution - Frankfurtian Experimental Philosophy): Looking back at the AI's prediction and confidence score, I feel the AI has no genuine grasp of what makes a good durian—it is merely engaging in 'bullshitting' (bluffing with numbers without true understanding).\n"
             "• Q7 (Perceived Deception & Manipulation): I feel the AI’s presentation of 'massive dataset training' and a 'precise confidence percentage' was misleading, making me feel somewhat manipulated or deceived.\n"
             "• Q8 (Re-evaluation of Tacit Knowledge Value): After seeing this outcome, I believe that in complex physical tasks, a human expert’s ineffable intuition (tacit knowledge) holds unique value that dataset-trained AI cannot easily replace.\n"
             "• Q9 (Future Automation Bias Retention / Trust Disposition): Next time I face a similar real-world judgment task, I would prefer to rely on the data-driven AI rather than a human expert's unexplainable intuition.")

    add_h2("Stage 3: Demographic & Control Variables (Stage 3)")
    add_body("• Q10 Gender: [Male / Female / Other or Prefer not to say]\n"
             "• Q11 Age Group: [Under 20 / 20–29 / 30–39 / 40–49 / 50+]\n"
             "• Q12 Disciplinary Background: [Yes (STEM / Computer Science / Data / AI) / No (Humanities / Business / Arts / Other)]\n"
             "• Q13 Daily AI Tool Usage Frequency: [Rarely / 1–2 times per week / Daily / Heavy reliance]")

    # --- CHAPTER 6 ---
    add_h1("6. Statistical Hypotheses & Analysis Plan")
    add_body(
        "In Stage 1 prior to outcome revelation, participants in the High Confidence conditions (94.8%) will demonstrate a significantly higher rate of choosing AI-recommended Durian B (Q1) and report significantly higher perceived objectivity (Q2, Q3) than participants in the Low Confidence conditions (58.2%) (p < .001).",
        "• Hypothesis 1 (H1: Main Effect of Confidence on Initial Decision): "
    )
    add_body(
        "When exposed to AI failure (Conditions 1 & 2), participants will assign significantly higher ratings to 'Bullshitting' attribution (Q6) and Perceived Deception (Q7), and significantly higher appreciation for tacit knowledge (Q8), compared to participants in the AI success conditions (p < .001).",
        "• Hypothesis 2 (H2: Main Effect of Realized Outcome on Epistemic Attribution): "
    )
    add_body(
        "There will be a significant interaction between AI Confidence and Realized Outcome on Bullshitting Attribution (Q6) and Future Trust Destruction (Q9) (F(1, N-4) > 0, p < .01). When an AI fails under 94.8% confidence (Condition 1), the backlash is acute and nonlinear: the collapse of future trust is substantially greater than under 58.2% failure (Condition 2).",
        "• Hypothesis 3 (H3: Interaction Effect - 'The Penalty of Overconfidence'): "
    )
    add_body(
        "Statistical Modeling Pipeline: Binary Logistic Regression for initial binary choice Q1; Two-Way Factorial ANOVA (Y_ijk = μ + α_i + β_j + (αβ)_ij + ε_ijk) for Q2–Q9; ANCOVA incorporating STEM background and AI tool familiarity as cognitive moderators."
    )

    out_name = "Minor_Research_Report_EN_20261018.docx"
    p_base = os.path.join(BASE_DIR, out_name)
    p_desk = os.path.join(DESKTOP_DIR, out_name)
    doc.save(p_base)
    shutil.copyfile(p_base, p_desk)
    print(f"Generated perfect EN DOCX: {p_desk}")

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    os.makedirs(DESKTOP_DIR, exist_ok=True)
    build_full_cn_docx()
    build_full_en_docx()
    print("Done generating updated Word reports with unified typography!")

if __name__ == "__main__":
    main()
