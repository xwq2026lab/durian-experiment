import fs from 'fs';

const TMP_FILE = '/tmp/responses.json';

export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  try {
    fs.writeFileSync(TMP_FILE, '[]', 'utf8');
  } catch (e) {}

  res.status(200).json({ status: 'cleared', message: 'All data cleared successfully (N=0)' });
}
