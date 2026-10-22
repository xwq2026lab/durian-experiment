export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method === 'POST') {
    return res.status(200).json({ status: 'success', message: 'Configuration updated' });
  }

  res.status(200).json({
    experimentTitle: "Data-Driven AI vs. Ineffable Expert Intuition: 2x2 Experiment",
    conditions: {
      "1": { confidenceVal: "94.8%", outcome: "AI Fails (Store Manager Correct)" },
      "2": { confidenceVal: "58.2%", outcome: "AI Fails (Store Manager Correct)" },
      "3": { confidenceVal: "94.8%", outcome: "AI Succeeds (Store Manager Fails)" },
      "4": { confidenceVal: "58.2%", outcome: "AI Succeeds (Store Manager Fails)" }
    }
  });
}
