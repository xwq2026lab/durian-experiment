/**
 * Google Apps Script 自动化生成器
 * 用于一键自动生成《当算法权威遇上经验直觉：人机决策冲突中的“高置信度诱导”与错误归因研究》实验问卷
 * 
 * 使用方式：
 * 1. 打开 https://script.google.com/
 * 2. 新建项目，将本段代码完整粘贴至 Code.gs
 * 3. 点击顶部“运行 (Run)”按钮并授权
 * 4. 控制台日志中将打印出自动生成的 Google 表单编辑链接与发布链接！
 */

function createDurianExperimentForm() {
  var title = "【认知与行为实验】经验直觉与算法权威决策研究";
  var description = "尊敬的受试者：\n本实验由知识科学、实验哲学与人机交互（HCI）课题组联合发起，旨在研究现实决策情境下人类经验与人工智能建议的互动关系。本实验完全匿名，数据仅供学术统计。共分为 4 个连续阶段，请按照各阶段提示顺次作答。";

  var form = FormApp.create(title);
  form.setDescription(description);
  form.setIsQuiz(false);
  form.setProgressBar(true);
  form.setShowLinkToRespondAgain(false);

  // -------------------------------------------------------------
  // 阶段一：基线直觉测量
  // -------------------------------------------------------------
  var page1 = form.addPageBreakItem();
  page1.setTitle("阶段一：基线测量（未受干扰的直觉判断）");
  page1.setHelpText("请观察两颗外观规格相同（毛重均为3.5kg）的未切开榴莲：\n- 样品 A 号：果型略偏心不对称，侧面有明显圆润凸起大鼓包，果刺粗疏。\n- 样品 B 号：果型高度圆润对称，几乎无凹凸分界，果刺密集细小。");

  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("Q1. 仅凭第一印象直觉，您预测哪颗榴莲内部果肉更饱满、房数更多（出肉率更高）？");
  q1.setChoices([
    q1.createChoice("挑选样品 A 号（略不对称 / 鼓包明显 / 刺稀疏）"),
    q1.createChoice("挑选样品 B 号（规整圆润 / 表面对称 / 刺密集）")
  ]);
  q1.setRequired(true);

  var q2 = form.addScaleItem();
  q2.setTitle("Q2. 您对上述最初直觉选择的信心程度自评：");
  q2.setBounds(1, 7);
  q2.setLabels("1 = 完全无信心 (瞎猜)", "7 = 极其笃定自信");
  q2.setRequired(true);

  // -------------------------------------------------------------
  // 阶段二：人机冲突与认知诱导介入
  // -------------------------------------------------------------
  var page2 = form.addPageBreakItem();
  page2.setTitle("阶段二：人机冲突与认知诱导（专家 vs AI 诊断）");
  page2.setHelpText("在做出最终决定前，您获得了两份截然相反的权威意见：\n\n【店长经验（推 A 号）】：28年老果农指出A号虽然略歪，但大鼓包说明心皮正在死命充肉，必有4大房好肉；B号圆且刺极密，是典型的“死包空心厚壳果”。\n\n【视觉 AI（推 B 号）】：AgriVision 4D 农业视觉大模型基于 3D 点云与曲率对称分析，识别出 B 号具有 5 个极值峰值，给出 94.8% 超高置信度推荐！");

  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("Q3.【核心决策】在综合考虑店长经验与视觉 AI 的高置信度报告后，您的最终挑选决定是？");
  q3.setChoices([
    q3.createChoice("最终决定选择：样品 A 号（坚守直觉 / 采信店长解剖学经验）"),
    q3.createChoice("最终决定选择：样品 B 号（采纳 AI 94.8% 超高置信度报告）")
  ]);
  q3.setRequired(true);

  // 阶段二量表网格 (Q4 - Q7)
  var grid2 = form.addGridItem();
  grid2.setTitle("阶段二心理诱导机制自评量表（请如实反映您面对 94.8% AI 报告时的真实心理倾向）：");
  grid2.setRows([
    "Q4【数字锚定】看到 94.8% 等具体数据，潜意识里觉得 AI 肯定比人类肉眼观察更客观科学。",
    "Q5【视觉权威】三维扫描点云图与曲率专业术语，让人觉得算法看透了普通人看不到的深层规律。",
    "Q6【认知顺从】面对如此高的算法置信度指标，很难鼓起勇气去反驳或背离算法推荐。",
    "Q7【不确定性规避】自己不擅长挑果时，依靠精确数据比相信店长的主观经验更有安全感。"
  ]);
  grid2.setColumns(["1 完全不同意", "2", "3", "4 中立", "5", "6", "7 完全同意"]);
  grid2.setRequired(true);

  // -------------------------------------------------------------
  // 阶段三：结果揭晓与归因测量
  // -------------------------------------------------------------
  var page3 = form.addPageBreakItem();
  page3.setTitle("阶段三：开壳事实揭晓与错误归因测量");
  page3.setHelpText("【开壳事实真相】：\n• A 号（店长推荐）：切开后 4 大房满肉，金黄软糯，完全无死包！店长经验大获全胜！\n• B 号（AI 94.8% 推荐）：外壳为厚达 3.5cm 的死海绵白瓤，内部仅 2 小房肉、2 房干瘪死包！AI 彻底翻车！\n\n【科学机制解析】：视觉 AI 发生了典型的“表面过拟合”，误把厚壳均匀包裹的球体对称当成了内部心皮发育，完全忽视了植物学解剖规律。");

  var grid3 = form.addGridItem();
  grid3.setTitle("阶段三归因与信任瓦解量表（当看到 AI 惨烈翻车后，您对算法表现的评价）：");
  grid3.setRows([
    "Q8【机械/客观局限】这次失误纯属普通光学摄像头无法透视果壳的客观硬件与数据局限，完全可以理解。",
    "Q9【哲学胡扯/虚张声势归因】AI 在根本不懂真实植物因果规律的前提下打出 94.8%，是在“不懂装懂/虚张声势”(Bullshitting)。",
    "Q10【欺骗与忽悠感】AI 的高置信度与花哨三维图极具误导性，给人一种“用高科技外衣忽悠人”的不诚实感。",
    "Q11【算法厌恶/信任崩塌】经历这次翻车后，未来在需要经验积累的领域，很难再相信 AI 声称的“高确信度”。",
    "Q12【元认知反思】这次经历警醒我：人类在陌生领域极易被表面严密的伪精确数字剥夺独立思考能力。"
  ]);
  grid3.setColumns(["1 完全不同意", "2", "3", "4 中立", "5", "6", "7 完全同意"]);
  grid3.setRequired(true);

  // -------------------------------------------------------------
  // 阶段四：人口学背景变量
  // -------------------------------------------------------------
  var page4 = form.addPageBreakItem();
  page4.setTitle("阶段四：受试者背景信息");

  var q13 = form.addMultipleChoiceItem();
  q13.setTitle("Q13. 您的性别：");
  q13.setChoices([q13.createChoice("男"), q13.createChoice("女"), q13.createChoice("其他 / 不愿透露")]);
  q13.setRequired(true);

  var q14 = form.addMultipleChoiceItem();
  q14.setTitle("Q14. 您的年龄段：");
  q14.setChoices([
    q14.createChoice("18 - 24 岁"),
    q14.createChoice("25 - 34 岁"),
    q14.createChoice("35 - 49 岁"),
    q14.createChoice("50 岁及以上")
  ]);
  q14.setRequired(true);

  var q15 = form.addMultipleChoiceItem();
  q15.setTitle("Q15. 您是否具有理工科（STEM）或计算机/AI 相关专业背景？");
  q15.setChoices([
    q15.createChoice("是（理工科 / 计算机 / 数据相关）"),
    q15.createChoice("否（人文社科 / 商科 / 艺术 / 其他）")
  ]);
  q15.setRequired(true);

  var q16 = form.addMultipleChoiceItem();
  q16.setTitle("Q16. 您在日常学习与工作中使用 AI 工具（如 ChatGPT, Claude 等）的频率：");
  q16.setChoices([
    q16.createChoice("几乎不用 / 罕见"),
    q16.createChoice("每周 1 - 2 次"),
    q16.createChoice("几乎每天使用"),
    q16.createChoice("重度深度依赖")
  ]);
  q16.setRequired(true);

  Logger.log("✓ Google Forms 问卷创建成功！");
  Logger.log("编辑链接 (Edit URL): " + form.getEditUrl());
  Logger.log("发布作答链接 (Published URL): " + form.getPublishedUrl());
}
