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
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const responses = getResponses();
  const total = responses.length;

  const condStats = {};
  for (let cid = 1; cid <= 4; cid++) {
    const list = responses.filter(r => String(r.conditionId) === String(cid));
    const n = list.length;
    const chooseAi = list.filter(r => r.q1_choice === 'B').length;
    const avg = (key) => n > 0 ? Number((list.reduce((acc, cur) => acc + (Number(cur[key]) || 0), 0) / n).toFixed(2)) : 0.0;

    condStats[String(cid)] = {
      n,
      chooseAi,
      chooseAiRate: n > 0 ? Number((chooseAi / n * 100).toFixed(1)) : 0.0,
      avg_q2: avg('q2'),
      avg_q3: avg('q3'),
      avg_q4: avg('q4'),
      avg_q5: avg('q5'),
      avg_q6: avg('q6'),
      avg_q7: avg('q7'),
      avg_q8: avg('q8'),
      avg_q9: avg('q9')
    };
  }

  const highList = responses.filter(r => r.confidenceLevel === 'high');
  const lowList = responses.filter(r => r.confidenceLevel === 'low');
  const highN = highList.length;
  const lowN = lowList.length;
  const highAi = highList.filter(r => r.q1_choice === 'B').length;
  const lowAi = lowList.filter(r => r.q1_choice === 'B').length;

  const confidenceEffect = {
    high: { n: highN, chooseAi: highAi, rate: highN > 0 ? Number((highAi / highN * 100).toFixed(1)) : 0.0 },
    low: { n: lowN, chooseAi: lowAi, rate: lowN > 0 ? Number((lowAi / lowN * 100).toFixed(1)) : 0.0 }
  };

  res.status(200).json({
    total,
    conditions: condStats,
    confidenceEffect
  });
}
