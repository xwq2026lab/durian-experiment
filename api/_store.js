import fs from 'fs';

const TMP_FILE = '/tmp/responses.json';
const REDIS_KEY = 'durian:responses:v1';

export function getRedisConfig() {
  const url =
    process.env.KV_REST_API_URL ||
    process.env.UPSTASH_REDIS_REST_URL ||
    Object.entries(process.env).find(
      ([k, v]) => (k.endsWith('_REST_API_URL') || k.endsWith('_REDIS_REST_URL')) && v
    )?.[1];

  const token =
    process.env.KV_REST_API_TOKEN ||
    process.env.UPSTASH_REDIS_REST_TOKEN ||
    Object.entries(process.env).find(
      ([k, v]) =>
        (k.endsWith('_REST_API_TOKEN') || k.endsWith('_REDIS_REST_TOKEN')) &&
        !k.includes('READ_ONLY') &&
        v
    )?.[1];

  if (url && token) {
    return { url: url.replace(/\/$/, ''), token };
  }
  return null;
}

async function redisCommand(cfg, cmdArray) {
  const res = await fetch(cfg.url, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${cfg.token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(cmdArray)
  });
  if (!res.ok) {
    throw new Error(`Redis HTTP ${res.status}`);
  }
  const json = await res.json();
  if (json && json.error) {
    throw new Error(String(json.error));
  }
  return json;
}

export async function getAllResponses() {
  const cfg = getRedisConfig();
  if (cfg) {
    try {
      const data = await redisCommand(cfg, ['LRANGE', REDIS_KEY, '0', '-1']);
      const rawList = Array.isArray(data?.result) ? data.result : [];
      return {
        storageMode: 'permanent_cloud_redis',
        list: rawList
          .map((item) => {
            try {
              return typeof item === 'string' ? JSON.parse(item) : item;
            } catch {
              return null;
            }
          })
          .filter(Boolean)
      };
    } catch (err) {
      console.error('Redis LRANGE failed, falling back to /tmp:', err);
    }
  }

  try {
    if (fs.existsSync(TMP_FILE)) {
      return {
        storageMode: 'temporary_tmp',
        list: JSON.parse(fs.readFileSync(TMP_FILE, 'utf8'))
      };
    }
  } catch (e) {}
  return { storageMode: 'temporary_tmp', list: [] };
}

export async function appendResponse(record) {
  const cfg = getRedisConfig();
  if (cfg) {
    try {
      await redisCommand(cfg, ['RPUSH', REDIS_KEY, JSON.stringify(record)]);
      return 'permanent_cloud_redis';
    } catch (err) {
      console.error('Redis RPUSH failed, falling back to /tmp:', err);
    }
  }

  let list = [];
  try {
    if (fs.existsSync(TMP_FILE)) {
      list = JSON.parse(fs.readFileSync(TMP_FILE, 'utf8'));
    }
  } catch (e) {}
  list.push(record);
  try {
    fs.writeFileSync(TMP_FILE, JSON.stringify(list, null, 2), 'utf8');
  } catch (e) {}
  return 'temporary_tmp';
}

export async function clearAllResponses() {
  const cfg = getRedisConfig();
  if (cfg) {
    try {
      await redisCommand(cfg, ['DEL', REDIS_KEY]);
      return 'permanent_cloud_redis';
    } catch (err) {
      console.error('Redis DEL failed, falling back to /tmp:', err);
    }
  }
  try {
    fs.writeFileSync(TMP_FILE, '[]', 'utf8');
  } catch (e) {}
  return 'temporary_tmp';
}
