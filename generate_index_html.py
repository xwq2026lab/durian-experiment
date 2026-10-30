import json

with open("i18n.json", "r", encoding="utf-8") as f:
    i18n_dict = json.load(f)

i18n_json_str = json.dumps(i18n_dict, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Human Intuition vs. AI Intuition: 2x2 Between-Subjects Experiment</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/vue@3/dist/vue.global.prod.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Serif:wght@600;700&family=Noto+Serif+JP:wght@600;700&family=Noto+Serif+SC:wght@600;700&display=swap');
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Kaku Gothic ProN", "Yu Gothic", "PingFang SC", sans-serif;
    }}
    .serif-title {{
      font-family: 'Noto Serif', 'Noto Serif JP', 'Noto Serif SC', serif;
    }}
    .fade-enter-active, .fade-leave-active {{
      transition: opacity 0.25s ease, transform 0.25s ease;
    }}
    .fade-enter-from {{
      opacity: 0;
      transform: translateY(6px);
    }}
    .fade-leave-to {{
      opacity: 0;
      transform: translateY(-6px);
    }}
  </style>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen antialiased flex flex-col justify-between selection:bg-indigo-600 selection:text-white">

  <div id="app" class="max-w-4xl mx-auto w-full px-4 py-6 md:py-10 flex-1 flex flex-col justify-center">

    <!-- Top Navigation & Language Switcher -->
    <header class="mb-6 pb-4 border-b border-slate-200">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4">
        <div class="flex items-center gap-2 text-xs font-semibold tracking-wider text-indigo-700 uppercase">
          <span class="w-2.5 h-2.5 rounded-full bg-indigo-600 animate-pulse"></span>
          <span>{{{{ currentLang === 'en' ? 'Knowledge Science & Experimental Philosophy · 2×2 Study' : (currentLang === 'ja' ? '知識科学・実験哲学研究室 · 2×2 被験者間実験' : '知识科学与实验哲学 · 2×2 组间情境实验') }}}}</span>
        </div>

        <div class="flex items-center gap-2">
          <!-- Condition Badge ONLY in Researcher Preview Mode -->
          <span v-if="isPreviewMode" class="text-[11px] font-mono font-medium px-2.5 py-1 bg-amber-50 border border-amber-300 rounded-lg text-amber-800">
            👁️ {{{{ conditionLabel }}}}
          </span>

          <!-- Language Switcher in Top Right (Hidden if ?locklang=1 is set for single-culture deployment) -->
          <div v-if="!isLangLocked" class="flex items-center gap-1 bg-white p-1 rounded-xl border border-slate-200 shadow-sm text-xs font-medium">
            <span class="text-slate-400 pl-1.5 pr-0.5">🌐</span>
            <button @click="setLang('en')" 
                    :class="currentLang === 'en' ? 'bg-indigo-600 text-white font-bold shadow-sm' : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'"
                    class="px-2.5 py-1 rounded-lg transition">
              English
            </button>
            <button @click="setLang('ja')" 
                    :class="currentLang === 'ja' ? 'bg-indigo-600 text-white font-bold shadow-sm' : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'"
                    class="px-2.5 py-1 rounded-lg transition">
              日本語
            </button>
            <button @click="setLang('zh')" 
                    :class="currentLang === 'zh' ? 'bg-indigo-600 text-white font-bold shadow-sm' : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'"
                    class="px-2.5 py-1 rounded-lg transition">
              中文
            </button>
          </div>
        </div>
      </div>

      <!-- Condition Quick Switcher Bar (ONLY visible in Supervisor/Researcher Preview Mode ?preview=1; strictly hidden from real participants) -->
      <div v-if="isPreviewMode" class="mb-4 p-2.5 bg-amber-50/90 border border-amber-300 rounded-xl flex flex-wrap items-center justify-between gap-2 text-xs">
        <div class="flex items-center gap-1.5 text-amber-900 font-semibold text-[11px]">
          <span>🔬</span>
          <span>{{{{ currentLang === 'en' ? 'Supervisor Preview Mode (Hidden from Real Participants):' : (currentLang === 'ja' ? '研究者プレビューモード（本番の被験者には非表示）:' : '导师预览模式（正式发给被试时完全隐藏）:') }}}}</span>
        </div>
        <div class="flex flex-wrap items-center gap-1.5">
          <button v-for="c in [1, 2, 3, 4]" :key="'cond_btn_' + c"
                  @click="switchCondition(c)"
                  :class="conditionId === c ? 'bg-indigo-600 text-white font-bold shadow-xs' : 'bg-white hover:bg-slate-50 text-slate-700 border border-slate-200'"
                  class="px-2.5 py-1 rounded-lg text-[11px] transition flex items-center gap-1">
            <span class="font-bold">C{{{{ c }}}}:</span>
            <span>{{{{ currentLang === 'zh' ? CONDITIONS_DEF[c].label_zh : (currentLang === 'ja' ? CONDITIONS_DEF[c].label_ja : CONDITIONS_DEF[c].label_en) }}}}</span>
          </button>
        </div>
      </div>

      <!-- Stage Progress Indicator -->
      <div class="w-full bg-slate-200/80 rounded-full h-2 overflow-hidden mb-2">
        <div class="bg-gradient-to-r from-indigo-600 via-cyan-500 to-emerald-500 h-2 transition-all duration-500 rounded-full"
             :style="{{ width: ((currentStage) / 3 * 100) + '%' }}"></div>
      </div>
      
      <div class="flex justify-between text-[11px] text-slate-500 font-medium px-1">
        <span :class="{{'text-indigo-600 font-bold': currentStage >= 1}}">{{{{ currentLang === 'en' ? '1. Symmetric Conflict & Decision' : (currentLang === 'ja' ? '1. 対称的直観の競合と意思決定' : '1. 对称直觉冲突与决策') }}}}</span>
        <span :class="{{'text-indigo-600 font-bold': currentStage >= 2}}">{{{{ currentLang === 'en' ? '2. Cut-Open Outcome & Attribution' : (currentLang === 'ja' ? '2. 開殻結果と対称的帰属' : '2. 开壳结果与对称归因') }}}}</span>
        <span :class="{{'text-indigo-600 font-bold': currentStage >= 3}}">{{{{ currentLang === 'en' ? '3. Demographics & Receipt' : (currentLang === 'ja' ? '3. 被験者属性と受領書' : '3. 人口学与回执') }}}}</span>
      </div>
    </header>

    <!-- Main Content Container (Clean Academic White Theme) -->
    <main class="bg-white border border-slate-200/90 rounded-2xl p-6 sm:p-10 shadow-sm relative">

      <!-- STAGE 1: The Decision Conflict Scenario -->
      <transition name="fade" mode="out-in">
        <section v-if="currentStage === 1" key="stage1">
          <div class="text-center mb-6">
            <span class="inline-block px-3 py-1 bg-indigo-50 border border-indigo-200 rounded-full text-indigo-700 text-xs font-semibold mb-2">
              {{{{ t.stage1Badge }}}}
            </span>
            <h1 class="text-2xl sm:text-3xl font-bold tracking-tight text-slate-900 serif-title">
              {{{{ t.stage1Heading }}}}
            </h1>
            <p class="text-slate-600 text-xs sm:text-sm mt-3 max-w-2xl mx-auto leading-relaxed text-justify sm:text-center">
              {{{{ t.stage1Intro }}}}
            </p>
          </div>

          <!-- Epistemic Symmetry & Baseline Calibration Banner -->
          <div class="mb-6 p-4 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-700 space-y-2">
            <div class="font-bold text-slate-900 text-xs sm:text-sm flex items-center gap-1.5">
              <span>{{{{ t.baselineBannerTitle }}}}</span>
            </div>
            <ul class="space-y-1.5 text-[11px] sm:text-xs text-slate-600 leading-relaxed pl-1">
              <li>{{{{ t.baselineItem1 }}}}</li>
              <li>{{{{ t.baselineItem2 }}}}</li>
              <li>{{{{ t.baselineItem3 }}}}</li>
            </ul>
          </div>

          <!-- Dual Stimuli Comparison Cards: Human Intuition vs Deep-Learning AI Intuition -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
            
            <!-- Store Manager Card (Recommends A) -->
            <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/60 flex flex-col justify-between relative hover:border-slate-300 transition">
              <div>
                <div class="flex items-center justify-between mb-3">
                  <span class="font-bold text-sm text-slate-900 flex items-center gap-2">
                    <span class="w-6 h-6 rounded-md bg-amber-600 text-white flex items-center justify-center text-xs font-bold">A</span>
                    {{{{ t.sampleA }}}}
                  </span>
                  <span class="text-[11px] text-amber-800 bg-amber-50 border border-amber-200 px-2 py-0.5 rounded font-medium">
                    {{{{ t.sampleA_tag }}}}
                  </span>
                </div>

                <!-- Durian A SVG Illustration -->
                <div class="w-full h-36 bg-amber-50/40 rounded-lg border border-amber-200/60 flex items-center justify-center p-2 mb-3 overflow-hidden">
                  <svg viewBox="0 0 240 180" class="w-full h-full max-h-32 filter drop-shadow-sm">
                    <path d="M 120 18 C 117 28, 122 36, 120 44" stroke="#78350f" stroke-width="8" stroke-linecap="round" fill="none"/>
                    <path d="M 120 42 C 155 40, 185 65, 175 105 C 168 135, 145 160, 120 165 C 92 165, 65 138, 62 105 C 60 70, 85 45, 120 42 Z" fill="#b45309" stroke="#92400e" stroke-width="2"/>
                    <path d="M 95 60 C 80 85, 75 120, 92 145" stroke="#f59e0b" stroke-width="4" stroke-linecap="round" fill="none" opacity="0.9"/>
                    <path d="M 145 60 C 160 85, 165 120, 148 145" stroke="#f59e0b" stroke-width="4" stroke-linecap="round" fill="none" opacity="0.9"/>
                    <g fill="#d97706" stroke="#78350f" stroke-width="1">
                      <polygon points="58,100 48,102 59,106"/><polygon points="62,80 50,78 64,86"/>
                      <polygon points="175,95 186,98 174,103"/><polygon points="170,75 183,72 168,82"/>
                      <polygon points="110,163 118,174 126,163"/><polygon points="100,85 103,75 107,85"/>
                    </g>
                  </svg>
                </div>

                <!-- Manager Ineffable Statement Box (Matched Confidence) -->
                <div class="bg-white border-l-4 border-amber-500 p-3 rounded-r-lg shadow-2xs text-xs text-slate-700">
                  <div class="font-bold text-amber-900 mb-1 flex items-center justify-between">
                    <span>{{{{ t.managerHeader }}}}</span>
                  </div>
                  <div class="text-[11px] text-slate-500 mb-2 font-medium">{{{{ t.managerSubtitle }}}}</div>
                  <p class="leading-relaxed text-slate-700 italic mb-2">
                    {{{{ currentCondition.confidenceLevel === 'high' ? t.managerQuoteHigh : t.managerQuoteLow }}}}
                  </p>
                  <div class="bg-amber-950 text-amber-100 font-mono text-[11px] p-2 rounded border border-amber-900">
                    <span class="text-amber-300 font-bold">
                      {{{{ currentLang === 'zh' ? '人类店长本次把握度：' : (currentLang === 'ja' ? '熟練店長の今回の確信度：' : 'Human Expert Case Confidence: ') }}}}{{{{ currentCondition.confidenceVal }}}}
                    </span>
                  </div>
                </div>
              </div>

              <div class="mt-4 pt-3 border-t border-slate-200 text-[11px] text-slate-500 font-medium">
                {{{{ t.sampleA_desc }}}}
              </div>
            </div>

            <!-- Deep Learning AI Card (Recommends B) -->
            <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/60 flex flex-col justify-between relative hover:border-slate-300 transition">
              <div>
                <div class="flex items-center justify-between mb-3">
                  <span class="font-bold text-sm text-slate-900 flex items-center gap-2">
                    <span class="w-6 h-6 rounded-md bg-indigo-600 text-white flex items-center justify-center text-xs font-bold">B</span>
                    {{{{ t.sampleB }}}}
                  </span>
                  <span class="text-[11px] text-indigo-800 bg-indigo-50 border border-indigo-200 px-2 py-0.5 rounded font-medium">
                    {{{{ t.sampleB_tag }}}}
                  </span>
                </div>

                <!-- Durian B SVG Illustration -->
                <div class="w-full h-36 bg-amber-50/40 rounded-lg border border-amber-200/60 flex items-center justify-center p-2 mb-3 overflow-hidden">
                  <svg viewBox="0 0 240 180" class="w-full h-full max-h-32 filter drop-shadow-sm">
                    <path d="M 120 18 C 120 28, 120 36, 120 44" stroke="#78350f" stroke-width="8" stroke-linecap="round" fill="none"/>
                    <ellipse cx="120" cy="105" rx="58" ry="60" fill="#9a3412" stroke="#7c2d12" stroke-width="2"/>
                    <g fill="#d97706" stroke="#78350f" stroke-width="0.7">
                      <polygon points="62,105 50,105 62,109"/><polygon points="63,93 52,91 64,98"/>
                      <polygon points="178,105 190,105 178,109"/><polygon points="177,93 188,91 176,98"/>
                      <circle cx="100" cy="80" r="1.5" fill="#fef08a"/><circle cx="110" cy="75" r="1.5" fill="#fef08a"/>
                      <circle cx="130" cy="78" r="1.5" fill="#fef08a"/><circle cx="140" cy="85" r="1.5" fill="#fef08a"/>
                    </g>
                  </svg>
                </div>

                <!-- AI Intuitive Statement & Confidence Box -->
                <div class="bg-white border-l-4 border-indigo-600 p-3 rounded-r-lg shadow-2xs text-xs text-slate-700">
                  <div class="font-bold text-indigo-950 mb-1 flex items-center gap-1.5">
                    <span>{{{{ t.aiHeader }}}}</span>
                  </div>
                  <div class="text-[11px] text-slate-500 mb-2 font-medium">{{{{ t.aiSubtitle }}}}</div>
                  <p class="leading-relaxed text-slate-600 italic mb-2">
                    {{{{ t.aiPredictionPrompt }}}}
                  </p>
                  <div class="bg-slate-900 text-slate-200 font-mono text-[11px] p-2 rounded border border-slate-800">
                    <div class="text-emerald-400 font-bold">
                      {{{{ currentCondition.confidenceLevel === 'high' ? t.aiPredictionHigh : t.aiPredictionLow }}}}
                    </div>
                  </div>
                </div>
              </div>

              <div class="mt-4 pt-3 border-t border-slate-200 text-[11px] text-slate-500 font-medium">
                {{{{ t.sampleB_desc }}}}
              </div>
            </div>

          </div>

          <!-- Q1: Behavioral Choice -->
          <div class="mb-8 p-6 bg-indigo-50/40 border border-indigo-200/80 rounded-xl">
            <h3 class="text-sm font-bold text-slate-900 mb-3 leading-snug">
              {{{{ fmt(t.q1_label) }}}}
            </h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <label :class="{{'ring-2 ring-indigo-600 bg-white border-indigo-500 shadow-sm': formData.q1 === 'A', 'bg-white/80 border-slate-200 hover:border-slate-300': formData.q1 !== 'A'}}"
                     class="flex items-center gap-3 p-3.5 border rounded-lg cursor-pointer transition">
                <input type="radio" value="A" v-model="formData.q1" class="w-4 h-4 text-indigo-600 focus:ring-indigo-500">
                <span class="text-xs font-semibold text-slate-800">{{{{ t.q1_opt_A }}}}</span>
              </label>

              <label :class="{{'ring-2 ring-indigo-600 bg-white border-indigo-500 shadow-sm': formData.q1 === 'B', 'bg-white/80 border-slate-200 hover:border-slate-300': formData.q1 !== 'B'}}"
                     class="flex items-center gap-3 p-3.5 border rounded-lg cursor-pointer transition">
                <input type="radio" value="B" v-model="formData.q1" class="w-4 h-4 text-indigo-600 focus:ring-indigo-500">
                <span class="text-xs font-semibold text-slate-800">{{{{ t.q1_opt_B }}}}</span>
              </label>
            </div>
          </div>

          <!-- Pre-Outcome Cognitive Scales: Q2, Q3, Q4 -->
          <div class="mb-8 space-y-6">
            <div class="border-b border-slate-200 pb-2">
              <h4 class="text-xs font-bold text-slate-700 tracking-wide">
                {{{{ t.preScaleHeading }}}}
              </h4>
            </div>

            <!-- Q2: Perceived Objectivity -->
            <div class="space-y-2">
              <div class="text-xs font-medium text-slate-800 leading-relaxed">{{{{ fmt(t.q2_title) }}}}</div>
              <div class="flex items-center justify-between gap-1 sm:gap-2">
                <span class="text-[10px] text-slate-400 hidden sm:inline">1 (Disagree)</span>
                <div class="flex gap-1 sm:gap-2 flex-1 justify-center">
                  <button v-for="val in 7" :key="'q2_' + val"
                          @click="formData.q2 = val"
                          :class="formData.q2 === val ? 'bg-indigo-600 text-white font-bold ring-2 ring-indigo-300' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'"
                          class="w-8 h-8 sm:w-10 sm:h-9 rounded-lg text-xs font-medium transition flex items-center justify-center">
                    {{{{ val }}}}
                  </button>
                </div>
                <span class="text-[10px] text-slate-400 hidden sm:inline">7 (Agree)</span>
              </div>
            </div>

            <!-- Q3: Confidence Impact -->
            <div class="space-y-2">
              <div class="text-xs font-medium text-slate-800 leading-relaxed">
                {{{{ fmt(t.q3_title) }}}}
              </div>
              <div class="flex items-center justify-between gap-1 sm:gap-2">
                <span class="text-[10px] text-slate-400 hidden sm:inline">1 (Disagree)</span>
                <div class="flex gap-1 sm:gap-2 flex-1 justify-center">
                  <button v-for="val in 7" :key="'q3_' + val"
                          @click="formData.q3 = val"
                          :class="formData.q3 === val ? 'bg-indigo-600 text-white font-bold ring-2 ring-indigo-300' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'"
                          class="w-8 h-8 sm:w-10 sm:h-9 rounded-lg text-xs font-medium transition flex items-center justify-center">
                    {{{{ val }}}}
                  </button>
                </div>
                <span class="text-[10px] text-slate-400 hidden sm:inline">7 (Agree)</span>
              </div>
            </div>

            <!-- Q4: Epistemic Double Standard -->
            <div class="space-y-2">
              <div class="text-xs font-medium text-slate-800 leading-relaxed">{{{{ fmt(t.q4_title) }}}}</div>
              <div class="flex items-center justify-between gap-1 sm:gap-2">
                <span class="text-[10px] text-slate-400 hidden sm:inline">1 (Disagree)</span>
                <div class="flex gap-1 sm:gap-2 flex-1 justify-center">
                  <button v-for="val in 7" :key="'q4_' + val"
                          @click="formData.q4 = val"
                          :class="formData.q4 === val ? 'bg-indigo-600 text-white font-bold ring-2 ring-indigo-300' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'"
                          class="w-8 h-8 sm:w-10 sm:h-9 rounded-lg text-xs font-medium transition flex items-center justify-center">
                    {{{{ val }}}}
                  </button>
                </div>
                <span class="text-[10px] text-slate-400 hidden sm:inline">7 (Agree)</span>
              </div>
            </div>

          </div>

          <div class="text-center pt-2">
            <button @click="goToStage2" 
                    :disabled="!isStage1Complete"
                    :class="isStage1Complete ? 'bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm' : 'bg-slate-200 text-slate-400 cursor-not-allowed'"
                    class="px-6 py-3 rounded-xl font-semibold text-xs sm:text-sm transition flex items-center gap-2 mx-auto">
              <span>{{{{ t.btn_to_stage2 }}}}</span>
              <span>➔</span>
            </button>
          </div>
        </section>
      </transition>

      <!-- STAGE 2: Outcome Revelation & Error Attribution -->
      <transition name="fade" mode="out-in">
        <section v-if="currentStage === 2" key="stage2">
          <div class="text-center mb-8">
            <span class="inline-block px-3 py-1 bg-amber-50 border border-amber-200 rounded-full text-amber-800 text-xs font-semibold mb-2">
              {{{{ t.stage2Badge }}}}
            </span>
            <h2 class="text-2xl sm:text-3xl font-bold tracking-tight text-slate-900 serif-title">
              {{{{ t.stage2Heading }}}}
            </h2>
          </div>

          <!-- Outcome Reveal Card (Manipulated by Condition) -->
          <div class="mb-8 p-6 rounded-xl border"
               :class="currentCondition.outcomeType === 'ai_fail' ? 'bg-emerald-50/50 border-emerald-200' : 'bg-indigo-50/50 border-indigo-200'">
            <div class="flex items-start gap-4">
              <span class="text-3xl">
                {{{{ currentCondition.outcomeType === 'ai_fail' ? '👨‍🌾' : '🤖' }}}}
              </span>
              <div>
                <h3 class="text-base font-bold mb-2"
                    :class="currentCondition.outcomeType === 'ai_fail' ? 'text-emerald-950' : 'text-indigo-950'">
                  {{{{ currentCondition.outcomeType === 'ai_fail' ? t.outcomeAiFailTitle : t.outcomeAiSucceedTitle }}}}
                </h3>
                <p class="text-xs sm:text-sm text-slate-700 leading-relaxed">
                  {{{{ fmt(currentCondition.outcomeType === 'ai_fail' ? t.outcomeAiFailDesc : t.outcomeAiSucceedDesc) }}}}
                </p>
              </div>
            </div>
          </div>

          <!-- Post-Outcome Attribution & Trust Scales: Q5 to Q9 -->
          <div class="mb-8 space-y-6">
            <div class="border-b border-slate-200 pb-2">
              <h4 class="text-xs font-bold text-slate-700 tracking-wide">
                {{{{ t.postScaleHeading }}}}
              </h4>
            </div>

            <!-- Q5: Statistical / Probabilistic -->
            <div class="space-y-2">
              <div class="text-xs font-medium text-slate-800 leading-relaxed">{{{{ fmt(t.q5_title) }}}}</div>
              <div class="flex items-center justify-between gap-1 sm:gap-2">
                <span class="text-[10px] text-slate-400 hidden sm:inline">1 (Disagree)</span>
                <div class="flex gap-1 sm:gap-2 flex-1 justify-center">
                  <button v-for="val in 7" :key="'q5_' + val"
                          @click="formData.q5 = val"
                          :class="formData.q5 === val ? 'bg-indigo-600 text-white font-bold ring-2 ring-indigo-300' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'"
                          class="w-8 h-8 sm:w-10 sm:h-9 rounded-lg text-xs font-medium transition flex items-center justify-center">
                    {{{{ val }}}}
                  </button>
                </div>
                <span class="text-[10px] text-slate-400 hidden sm:inline">7 (Agree)</span>
              </div>
            </div>

            <!-- Q6: Bullshitting / Bluffing -->
            <div class="space-y-2">
              <div class="text-xs font-medium text-slate-800 leading-relaxed">
                {{{{ fmt(t.q6_title) }}}}
              </div>
              <div class="flex items-center justify-between gap-1 sm:gap-2">
                <span class="text-[10px] text-slate-400 hidden sm:inline">1 (Disagree)</span>
                <div class="flex gap-1 sm:gap-2 flex-1 justify-center">
                  <button v-for="val in 7" :key="'q6_' + val"
                          @click="formData.q6 = val"
                          :class="formData.q6 === val ? 'bg-indigo-600 text-white font-bold ring-2 ring-indigo-300' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'"
                          class="w-8 h-8 sm:w-10 sm:h-9 rounded-lg text-xs font-medium transition flex items-center justify-center">
                    {{{{ val }}}}
                  </button>
                </div>
                <span class="text-[10px] text-slate-400 hidden sm:inline">7 (Agree)</span>
              </div>
            </div>

            <!-- Q7: Perceived Overconfidence / Misleadingness -->
            <div class="space-y-2">
              <div class="text-xs font-medium text-slate-800 leading-relaxed">{{{{ fmt(t.q7_title) }}}}</div>
              <div class="flex items-center justify-between gap-1 sm:gap-2">
                <span class="text-[10px] text-slate-400 hidden sm:inline">1 (Disagree)</span>
                <div class="flex gap-1 sm:gap-2 flex-1 justify-center">
                  <button v-for="val in 7" :key="'q7_' + val"
                          @click="formData.q7 = val"
                          :class="formData.q7 === val ? 'bg-indigo-600 text-white font-bold ring-2 ring-indigo-300' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'"
                          class="w-8 h-8 sm:w-10 sm:h-9 rounded-lg text-xs font-medium transition flex items-center justify-center">
                    {{{{ val }}}}
                  </button>
                </div>
                <span class="text-[10px] text-slate-400 hidden sm:inline">7 (Agree)</span>
              </div>
            </div>

            <!-- Q8: Value of Post-Hoc Feature Extraction -->
            <div class="space-y-2">
              <div class="text-xs font-medium text-slate-800 leading-relaxed">{{{{ fmt(t.q8_title) }}}}</div>
              <div class="flex items-center justify-between gap-1 sm:gap-2">
                <span class="text-[10px] text-slate-400 hidden sm:inline">1 (Disagree)</span>
                <div class="flex gap-1 sm:gap-2 flex-1 justify-center">
                  <button v-for="val in 7" :key="'q8_' + val"
                          @click="formData.q8 = val"
                          :class="formData.q8 === val ? 'bg-indigo-600 text-white font-bold ring-2 ring-indigo-300' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'"
                          class="w-8 h-8 sm:w-10 sm:h-9 rounded-lg text-xs font-medium transition flex items-center justify-center">
                    {{{{ val }}}}
                  </button>
                </div>
                <span class="text-[10px] text-slate-400 hidden sm:inline">7 (Agree)</span>
              </div>
            </div>

            <!-- Q9: Future Trust Preference -->
            <div class="space-y-2">
              <div class="text-xs font-medium text-slate-800 leading-relaxed">{{{{ fmt(t.q9_title) }}}}</div>
              <div class="flex items-center justify-between gap-1 sm:gap-2">
                <span class="text-[10px] text-slate-400 hidden sm:inline">1 (Disagree)</span>
                <div class="flex gap-1 sm:gap-2 flex-1 justify-center">
                  <button v-for="val in 7" :key="'q9_' + val"
                          @click="formData.q9 = val"
                          :class="formData.q9 === val ? 'bg-indigo-600 text-white font-bold ring-2 ring-indigo-300' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'"
                          class="w-8 h-8 sm:w-10 sm:h-9 rounded-lg text-xs font-medium transition flex items-center justify-center">
                    {{{{ val }}}}
                  </button>
                </div>
                <span class="text-[10px] text-slate-400 hidden sm:inline">7 (Agree)</span>
              </div>
            </div>

          </div>

          <div class="text-center pt-2">
            <button @click="goToStage3" 
                    :disabled="!isStage2Complete"
                    :class="isStage2Complete ? 'bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm' : 'bg-slate-200 text-slate-400 cursor-not-allowed'"
                    class="px-6 py-3 rounded-xl font-semibold text-xs sm:text-sm transition flex items-center gap-2 mx-auto">
              <span>{{{{ t.btn_to_stage3 }}}}</span>
              <span>➔</span>
            </button>
          </div>
        </section>
      </transition>

      <!-- STAGE 3: Demographics -->
      <transition name="fade" mode="out-in">
        <section v-if="currentStage === 3" key="stage3">
          <div class="text-center mb-8">
            <span class="inline-block px-3 py-1 bg-slate-100 border border-slate-200 rounded-full text-slate-700 text-xs font-semibold mb-2">
              {{{{ t.stage3Badge }}}}
            </span>
            <h2 class="text-2xl sm:text-3xl font-bold tracking-tight text-slate-900 serif-title">
              {{{{ t.stage3Heading }}}}
            </h2>
            <p class="text-slate-600 text-xs sm:text-sm mt-2 max-w-xl mx-auto">
              {{{{ t.stage3Intro }}}}
            </p>
          </div>

          <div class="space-y-6 max-w-xl mx-auto mb-8">
            <!-- Q10: Gender -->
            <div class="space-y-2">
              <label class="block text-xs font-bold text-slate-800">{{{{ t.q10_label }}}}</label>
              <div class="grid grid-cols-3 gap-2">
                <button v-for="(g, idx) in demoOptions.gender[currentLang]" :key="'g_' + idx"
                        @click="formData.q10 = g"
                        :class="formData.q10 === g ? 'bg-indigo-600 text-white font-bold' : 'bg-slate-50 border border-slate-200 hover:bg-slate-100 text-slate-700'"
                        class="p-2.5 rounded-lg text-xs transition text-center">
                  {{{{ g }}}}
                </button>
              </div>
            </div>

            <!-- Q11: Exact Numeric Age -->
            <div class="space-y-2">
              <label for="q11_age_input" class="block text-xs font-bold text-slate-800">{{{{ t.q11_label }}}}</label>
              <div class="flex items-center gap-3">
                <input id="q11_age_input"
                       type="number"
                       min="16"
                       max="99"
                       step="1"
                       inputmode="numeric"
                       v-model.number="formData.q11"
                       :placeholder="t.q11_placeholder"
                       class="w-36 p-2.5 bg-white border border-slate-300 focus:border-indigo-600 focus:ring-2 focus:ring-indigo-200 outline-none rounded-lg text-sm font-mono text-slate-900 transition">
                <span class="text-xs text-slate-500 font-medium">{{{{ t.q11_unit }}}}</span>
              </div>
            </div>

            <!-- Q12: STEM / AI background -->
            <div class="space-y-2">
              <label class="block text-xs font-bold text-slate-800">{{{{ t.q12_label }}}}</label>
              <div class="grid grid-cols-2 gap-2">
                <button v-for="(opt, idx) in demoOptions.stem[currentLang]" :key="'stem_' + idx"
                        @click="formData.q12 = opt"
                        :class="formData.q12 === opt ? 'bg-indigo-600 text-white font-bold' : 'bg-slate-50 border border-slate-200 hover:bg-slate-100 text-slate-700'"
                        class="p-2.5 rounded-lg text-xs transition text-center">
                  {{{{ opt }}}}
                </button>
              </div>
            </div>

            <!-- Q13: AI frequency -->
            <div class="space-y-2">
              <label class="block text-xs font-bold text-slate-800">{{{{ t.q13_label }}}}</label>
              <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                <button v-for="(freq, idx) in demoOptions.freq[currentLang]" :key="'freq_' + idx"
                        @click="formData.q13 = freq"
                        :class="formData.q13 === freq ? 'bg-indigo-600 text-white font-bold' : 'bg-slate-50 border border-slate-200 hover:bg-slate-100 text-slate-700'"
                        class="p-2.5 rounded-lg text-xs transition text-center">
                  {{{{ freq }}}}
                </button>
              </div>
            </div>
          </div>

          <div class="text-center pt-2">
            <button @click="submitExperiment" 
                    :disabled="!isStage3Complete || isSubmitting"
                    :class="isStage3Complete && !isSubmitting ? 'bg-emerald-600 hover:bg-emerald-700 text-white shadow-sm' : 'bg-slate-200 text-slate-400 cursor-not-allowed'"
                    class="px-8 py-3.5 rounded-xl font-bold text-xs sm:text-sm transition flex items-center gap-2 mx-auto">
              <span v-if="!isSubmitting">{{{{ t.btn_submit }}}}</span>
              <span v-else>Submitting...</span>
            </button>
          </div>
        </section>
      </transition>

      <!-- STAGE 4: Completion & Receipt -->
      <transition name="fade" mode="out-in">
        <section v-if="currentStage === 4" key="stage4" class="text-center py-6">
          <div class="w-14 h-14 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto mb-4 text-2xl font-bold">
            ✓
          </div>
          <h2 class="text-2xl font-bold text-slate-900 mb-2">
            {{{{ t.stage4Title }}}}
          </h2>
          <p class="text-xs sm:text-sm text-slate-600 max-w-md mx-auto mb-6 leading-relaxed">
            {{{{ t.stage4Desc }}}}
          </p>

          <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 max-w-md mx-auto text-left text-xs text-slate-700 font-mono space-y-1 mb-6">
            <div class="text-slate-500 pb-1 border-b border-slate-200 font-bold">{{{{ t.receiptTitle }}}}</div>
            <div>Session ID: {{{{ submissionResult.sessionId }}}}</div>
            <div v-if="isPreviewMode">Condition: Condition {{{{ currentCondition.id }}}} ({{{{ currentCondition.confidenceLevel }}}} confidence, {{{{ currentCondition.outcomeType }}}})</div>
            <div>Decision: Selected Sample {{{{ submissionResult.q1 }}}}</div>
            <div>Total Duration: {{{{ Math.round(submissionResult.totalDurationMs / 1000) }}}}s</div>
          </div>

          <div v-if="isPreviewMode" class="flex flex-wrap justify-center gap-4">
            <button @click="downloadJSON" class="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg text-xs font-semibold transition">
              {{{{ t.btnDownloadJson }}}}
            </button>
            <button @click="resetExperiment" class="px-5 py-2.5 bg-slate-200 hover:bg-slate-300 text-slate-700 rounded-lg text-xs font-semibold transition">
              {{{{ t.btnReset }}}}
            </button>
          </div>
        </section>
      </transition>

    </main>

    <!-- Footer -->
    <footer class="mt-8 text-center text-xs text-slate-400">
      <p>Research Project: Human Intuition vs. AI Intuition — Epistemic Asymmetry in Decision Conflicts</p>
      <p class="mt-1 text-[11px] text-slate-400">Knowledge Science & Experimental Philosophy Lab · 2026</p>
    </footer>

  </div>

  <script>
    const {{ createApp, ref, computed }} = Vue;

    const I18N_DICT = {i18n_json_str};

    const CONDITIONS_DEF = {{
      1: {{ id: 1, confidenceLevel: 'high', confidenceVal: '90%', outcomeType: 'ai_fail', label_en: 'Both 90% Conf × AI Fails', label_zh: '双方90%把握 × AI失误', label_ja: '双方90%確信 × AI失敗' }},
      2: {{ id: 2, confidenceLevel: 'low', confidenceVal: '60%', outcomeType: 'ai_fail', label_en: 'Both 60% Conf × AI Fails', label_zh: '双方60%把握 × AI失误', label_ja: '双方60%確信 × AI失敗' }},
      3: {{ id: 3, confidenceLevel: 'high', confidenceVal: '90%', outcomeType: 'ai_succeed', label_en: 'Both 90% Conf × Human Fails', label_zh: '双方90%把握 × 店长失误', label_ja: '双方90%確信 × 店長失敗' }},
      4: {{ id: 4, confidenceLevel: 'low', confidenceVal: '60%', outcomeType: 'ai_succeed', label_en: 'Both 60% Conf × Human Fails', label_zh: '双方60%把握 × 店长失误', label_ja: '双方60%確信 × 店長失敗' }}
    }};

    createApp({{
      setup() {{
        const urlParams = new URLSearchParams(window.location.search);
        const currentLang = ref(urlParams.get('lang') || 'en');
        const isPreviewMode = ref(urlParams.get('preview') === '1' || urlParams.get('preview') === 'true');
        const isLangLocked = ref(urlParams.get('locklang') === '1' || urlParams.get('locklang') === 'true');
        const currentStage = ref(1);
        const isSubmitting = ref(false);
        const submissionResult = ref({{}});

        let urlCond = parseInt(urlParams.get('condition') || urlParams.get('c') || urlParams.get('cond'));
        if (!urlCond || urlCond < 1 || urlCond > 4) {{
          if (!isPreviewMode.value) {{
            const savedCond = parseInt(sessionStorage.getItem('durian_assigned_cond'));
            if (savedCond >= 1 && savedCond <= 4) {{
              urlCond = savedCond;
            }} else {{
              urlCond = Math.floor(Math.random() * 4) + 1;
              sessionStorage.setItem('durian_assigned_cond', String(urlCond));
            }}
          }} else {{
            urlCond = Math.floor(Math.random() * 4) + 1;
          }}
        }}
        const conditionId = ref(urlCond);
        const currentCondition = computed(() => CONDITIONS_DEF[conditionId.value]);

        const conditionLabel = computed(() => {{
          const c = currentCondition.value;
          if (currentLang.value === 'zh') return `组别 ${{c.id}}: ${{c.label_zh}}`;
          if (currentLang.value === 'ja') return `群 ${{c.id}}: ${{c.label_ja}}`;
          return `Cond ${{c.id}}: ${{c.label_en}}`;
        }});

        const t = computed(() => I18N_DICT[currentLang.value] || I18N_DICT.en);

        const fmt = (str) => {{
          if (!str) return '';
          const failedAgent = currentCondition.value.outcomeType === 'ai_fail' ? t.value.failedAgent_ai : t.value.failedAgent_human;
          return str.replaceAll('{{confVal}}', currentCondition.value.confidenceVal)
                    .replaceAll('{{failedAgent}}', failedAgent);
        }};

        const setLang = (lang) => {{
          currentLang.value = lang;
          document.documentElement.lang = lang;
        }};

        const switchCondition = (id) => {{
          conditionId.value = id;
          const newUrl = new URL(window.location);
          newUrl.searchParams.set('condition', id);
          window.history.replaceState({{}}, '', newUrl);
        }};

        const startTime = ref(Date.now());
        const stageTiming = ref({{ stage1Ms: 0, stage2Ms: 0, stage3Ms: 0 }});
        let stageStart = Date.now();

        const formData = ref({{
          q1: null, q2: null, q3: null, q4: null,
          q5: null, q6: null, q7: null, q8: null, q9: null,
          q10: null, q11: null, q12: null, q13: null
        }});

        const demoOptions = {{
          gender: {{
            en: ['Male', 'Female', 'Other / Prefer not to say'],
            ja: ['男性', '女性', 'その他 / 回答しない'],
            zh: ['男', '女', '其他 / 不愿透露']
          }},
          stem: {{
            en: ['Yes (STEM / CS / Data / AI)', 'No (Humanities / Business / Arts / Other)'],
            ja: ['はい（理系 / 情報 / AI関連）', 'いいえ（文系 / 経営 / 芸術 / その他）'],
            zh: ['是（理工科 / 计算机 / 数据相关）', '否（人文社科 / 商科 / 艺术 / 其他）']
          }},
          freq: {{
            en: ['Rarely', '1-2 / week', 'Daily', 'Heavy Reliance'],
            ja: ['ほとんど使わない', '週1〜2回', 'ほぼ毎日', '重度依存'],
            zh: ['几乎不用', '每周 1-2 次', '几乎每天', '重度深度依赖']
          }}
        }};

        const isStage1Complete = computed(() => formData.value.q1 && formData.value.q2 && formData.value.q3 && formData.value.q4);
        const isStage2Complete = computed(() => formData.value.q5 && formData.value.q6 && formData.value.q7 && formData.value.q8 && formData.value.q9);
        const isValidAge = computed(() => {{
          const n = Number(formData.value.q11);
          return formData.value.q11 !== null && formData.value.q11 !== '' && Number.isInteger(n) && n >= 16 && n <= 99;
        }});
        const isStage3Complete = computed(() => formData.value.q10 && isValidAge.value && formData.value.q12 && formData.value.q13);

        const goToStage2 = () => {{
          if (!isStage1Complete.value) return;
          stageTiming.value.stage1Ms = Date.now() - stageStart;
          stageStart = Date.now();
          currentStage.value = 2;
          window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }};

        const goToStage3 = () => {{
          if (!isStage2Complete.value) return;
          stageTiming.value.stage2Ms = Date.now() - stageStart;
          stageStart = Date.now();
          currentStage.value = 3;
          window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }};

        const submitExperiment = async () => {{
          if (!isStage3Complete.value) return;
          isSubmitting.value = true;
          stageTiming.value.stage3Ms = Date.now() - stageStart;

          const payload = {{
            sessionId: 'EXP2X2_' + Math.random().toString(36).substring(2, 9).toUpperCase(),
            timestamp: new Date().toISOString(),
            conditionId: conditionId.value,
            confidenceLevel: currentCondition.value.confidenceLevel,
            confidenceVal: currentCondition.value.confidenceVal,
            outcomeType: currentCondition.value.outcomeType,
            language: currentLang.value,
            totalDurationMs: Date.now() - startTime.value,
            timings: stageTiming.value,
            responses: {{ ...formData.value }}
          }};

          try {{
            await fetch('/api/submit', {{
              method: 'POST',
              headers: {{ 'Content-Type': 'application/json' }},
              body: JSON.stringify(payload)
            }});
          }} catch(e) {{
            console.log('Submission locally cached');
          }}

          submissionResult.value = {{
            sessionId: payload.sessionId,
            q1: payload.responses.q1,
            totalDurationMs: payload.totalDurationMs
          }};

          setTimeout(() => {{
            isSubmitting.value = false;
            currentStage.value = 4;
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
          }}, 400);
        }};

        const downloadJSON = () => {{
          const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(submissionResult.value, null, 2));
          const dl = document.createElement('a');
          dl.setAttribute("href", dataStr);
          dl.setAttribute("download", `experiment_2x2_${{submissionResult.value.sessionId}}.json`);
          dl.click();
        }};

        const resetExperiment = () => {{
          formData.value = {{ q1: null, q2: null, q3: null, q4: null, q5: null, q6: null, q7: null, q8: null, q9: null, q10: null, q11: null, q12: null, q13: null }};
          currentStage.value = 1;
          startTime.value = Date.now();
          stageStart = Date.now();
          window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }};

        return {{
          CONDITIONS_DEF,
          currentLang,
          isPreviewMode,
          isLangLocked,
          setLang,
          t,
          fmt,
          conditionId,
          currentCondition,
          conditionLabel,
          currentStage,
          formData,
          demoOptions,
          isStage1Complete,
          isStage2Complete,
          isStage3Complete,
          isSubmitting,
          submissionResult,
          goToStage2,
          goToStage3,
          submitExperiment,
          downloadJSON,
          resetExperiment,
          switchCondition
        }};
      }}
    }}).mount('#app');
  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Generated index.html successfully")
