import { appendResponse } from './_store.js';

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method === 'POST') {
    const data = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
    const resp = data.responses || {};
    const timings = data.timings || {};

    const record = {
      sessionId: data.sessionId || 'EXP_' + Date.now(),
      timestamp: data.timestamp || new Date().toISOString(),
      conditionId: data.conditionId,
      confidenceLevel: data.confidenceLevel,
      confidenceVal: data.confidenceVal,
      outcomeType: data.outcomeType,
      language: data.language || 'en',
      q1_choice: resp.q1,
      q2: resp.q2,
      q3: resp.q3,
      q4: resp.q4,
      q5: resp.q5,
      q6: resp.q6,
      q7: resp.q7,
      q8: resp.q8,
      q9: resp.q9,
      q10_gender: resp.q10,
      q11_age: resp.q11,
      q12_stem: resp.q12,
      q13_ai_freq: resp.q13,
      stage1_ms: timings.stage1Ms || 0,
      stage2_ms: timings.stage2Ms || 0,
      stage3_ms: timings.stage3Ms || 0,
      total_duration_ms: data.totalDurationMs || 0,
      userAgent: req.headers['user-agent'] || ''
    };

    const storageMode = await appendResponse(record);

    return res.status(200).json({ status: 'ok', sessionId: record.sessionId, storageMode });
  }

  res.status(405).json({ error: 'Method not allowed' });
}
