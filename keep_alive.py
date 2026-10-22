#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Continuous Keep-Alive Heartbeat for Cloudflare Tunnel and Local Server.
Pings the public tunnel URL and local server every 60 seconds to prevent edge idle timeouts.
"""

import time
import urllib.request
import sys
from datetime import datetime

PUBLIC_URL = "https://ratio-employ-boston-zone.trycloudflare.com/"
LOCAL_URL = "http://localhost:8080/"

print(f"[{datetime.now()}] Starting Keep-Alive Heartbeat Daemon for {PUBLIC_URL}...")
sys.stdout.flush()

count = 0

while True:
    try:
        req = urllib.request.Request(
            PUBLIC_URL,
            headers={"User-Agent": "DurianExp-KeepAlive/1.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            code = resp.status
    except Exception as e:
        code = f"Err: {e}"

    count += 1
    # Print heartbeat every 10 iterations (~10 mins)
    if count % 10 == 1 or count <= 3:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Heartbeat #{count}: Public Tunnel Status = {code}")
        sys.stdout.flush()

    time.sleep(60)
