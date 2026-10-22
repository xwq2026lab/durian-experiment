import fs from 'fs';

const TMP_FILE = '/tmp/responses.json';

function getResponses() {
  try {
    if (fs.existsSync(TMP_FILE)) {
      return JSON.parse(fs.readFileSync(TMP_FILE, 'utf8'));
    }
  } catch (e) {}
  return [];
}

export default function handler(req, res) {
  const list = getResponses();
  const headers = [
    'session_id', 'timestamp', 'condition_id', 'confidence_level', 'confidence_val',
    'outcome_type', 'language', 'q1_choice', 'q2_data_authority', 'q3_confidence_anchor',
    'q4_tacit_skepticism', 'q5_probabilistic', 'q6_bullshit', 'q7_deception',
    'q8_tacit_reevaluation', 'q9_future_trust', 'q10_gender', 'q11_age',
    'q12_stem', 'q13_ai_freq', 'stage1_ms', 'stage2_ms', 'stage3_ms',
    'total_duration_ms'
  ];

  let csvContent = headers.join(',') + '\n';
  for (const r of list) {
    const row = [
      r.sessionId, r.timestamp, r.conditionId, r.confidenceLevel, r.confidenceVal,
      r.outcomeType, r.language, r.q1_choice, r.q2, r.q3,
      r.q4, r.q5, r.q6, r.q7,
      r.q8, r.q9, r.q10_gender, r.q11_age,
      r.q12_stem, r.q13_ai_freq, r.stage1_ms, r.stage2_ms, r.stage3_ms,
      r.total_duration_ms
    ];
    csvContent += row.map(v => v !== undefined && v !== null ? `"${String(v).replace(/"/g, '""')}"` : '""').join(',') + '\n';
  }

  res.setHeader('Content-Type', 'text/csv; charset=utf-8');
  res.setHeader('Content-Disposition', 'attachment; filename="durian_experiment_data.csv"');
  res.status(200).send(csvContent);
}
