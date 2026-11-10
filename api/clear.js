import { clearAllResponses } from './_store.js';

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const storageMode = await clearAllResponses();

  res.status(200).json({ status: 'cleared', storageMode, message: 'All data cleared successfully (N=0)' });
}
