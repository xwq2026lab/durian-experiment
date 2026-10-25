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
    experimentTitle: "Human Intuition vs. AI Intuition: 2x2 Experiment",
    conditions: {
      "1": { confidenceVal: "90%", outcome: "AI Fails (Store Manager Correct)" },
      "2": { confidenceVal: "60%", outcome: "AI Fails (Store Manager Correct)" },
      "3": { confidenceVal: "90%", outcome: "Store Manager Fails (AI Correct)" },
      "4": { confidenceVal: "60%", outcome: "Store Manager Fails (AI Correct)" }
    }
  });
}
