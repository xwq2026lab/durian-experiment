#!/usr/bin/env python3
"""
Data-Driven AI vs. Ineffable Expert Intuition - 2x2 Between-Subjects Experiment Server
Serves:
  - / -> index.html (Participant 2x2 Survey)
  - /admin -> admin.html (Professor 2x2 Dashboard & Config Console)
  - /api/config -> GET/POST experiment configuration
  - /api/clear -> POST purge all response data
  - /api/submit -> POST record respondent submission
  - /api/stats -> GET aggregated 2x2 metrics
  - /api/export.csv -> GET full CSV data export
"""

import http.server
import socketserver
import json
import sqlite3
import os
import csv
import io
from urllib.parse import urlparse

PORT = 8080
BASE_DIR = os.path.dirname(__file__)
DB_FILE = os.path.join(BASE_DIR, "durian_experiment.db")
CONFIG_FILE = os.path.join(BASE_DIR, "config.json")


def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def save_config(cfg):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS responses_2x2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT UNIQUE,
            timestamp TEXT,
            condition_id INTEGER,
            confidence_level TEXT,
            confidence_val TEXT,
            outcome_type TEXT,
            language TEXT,
            q1_choice TEXT,
            q2_data_authority INTEGER,
            q3_confidence_anchor INTEGER,
            q4_tacit_skepticism INTEGER,
            q5_probabilistic INTEGER,
            q6_bullshit INTEGER,
            q7_deception INTEGER,
            q8_tacit_reevaluation INTEGER,
            q9_future_trust INTEGER,
            q10_gender TEXT,
            q11_age TEXT,
            q12_stem TEXT,
            q13_ai_freq TEXT,
            stage1_ms INTEGER,
            stage2_ms INTEGER,
            stage3_ms INTEGER,
            total_duration_ms INTEGER,
            user_agent TEXT
        )
    """)
    conn.commit()
    conn.close()


def clear_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS responses_2x2")
    c.execute("DROP TABLE IF EXISTS responses")
    conn.commit()
    conn.close()
    init_db()


class ExperimentHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def serve_file(self, filename, content_type="text/html; charset=utf-8"):
        filepath = os.path.join(BASE_DIR, filename)
        if os.path.exists(filepath):
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(os.path.getsize(filepath)))
            self.end_headers()
            with open(filepath, "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, "File not found")

    def do_HEAD(self):
        url = urlparse(self.path)
        if url.path in ["/", "/index.html", "/admin", "/admin/", "/admin.html"]:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
        else:
            super().do_HEAD()

    def do_GET(self):
        url = urlparse(self.path)

        if url.path in ["/", "/index.html"]:
            return self.serve_file("index.html")

        elif url.path in ["/admin", "/admin/", "/admin.html"]:
            return self.serve_file("admin.html")

        elif url.path == "/api/config":
            cfg = load_config()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(cfg, ensure_ascii=False).encode("utf-8"))

        elif url.path == "/api/stats":
            self.handle_api_stats()

        elif url.path == "/api/export.csv":
            self.handle_export_csv()

        else:
            return super().do_GET()

    def do_POST(self):
        url = urlparse(self.path)

        if url.path == "/api/config":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)
            try:
                new_cfg = json.loads(post_data.decode("utf-8"))
                save_config(new_cfg)
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "message": "Configuration updated"}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode())

        elif url.path == "/api/clear":
            clear_db()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "cleared", "message": "All data cleared successfully (N=0)"}).encode("utf-8"))

        elif url.path == "/api/submit":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode("utf-8"))
                resp = data.get("responses", {})
                timings = data.get("timings", {})

                conn = sqlite3.connect(DB_FILE)
                c = conn.cursor()
                c.execute("""
                    INSERT INTO responses_2x2 (
                        session_id, timestamp, condition_id, confidence_level, confidence_val,
                        outcome_type, language, q1_choice, q2_data_authority, q3_confidence_anchor,
                        q4_tacit_skepticism, q5_probabilistic, q6_bullshit, q7_deception,
                        q8_tacit_reevaluation, q9_future_trust, q10_gender, q11_age,
                        q12_stem, q13_ai_freq, stage1_ms, stage2_ms, stage3_ms,
                        total_duration_ms, user_agent
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    data.get("sessionId"),
                    data.get("timestamp"),
                    data.get("conditionId"),
                    data.get("confidenceLevel"),
                    data.get("confidenceVal"),
                    data.get("outcomeType"),
                    data.get("language", "en"),
                    resp.get("q1"),
                    resp.get("q2"),
                    resp.get("q3"),
                    resp.get("q4"),
                    resp.get("q5"),
                    resp.get("q6"),
                    resp.get("q7"),
                    resp.get("q8"),
                    resp.get("q9"),
                    resp.get("q10"),
                    resp.get("q11"),
                    resp.get("q12"),
                    resp.get("q13"),
                    timings.get("stage1Ms", 0),
                    timings.get("stage2Ms", 0),
                    timings.get("stage3Ms", 0),
                    data.get("totalDurationMs", 0),
                    self.headers.get("User-Agent", "")
                ))
                conn.commit()
                conn.close()

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "ok", "sessionId": data.get("sessionId")}).encode())

            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode())

    def handle_api_stats(self):
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        c.execute("SELECT COUNT(*) as total FROM responses_2x2")
        total = c.fetchone()["total"]

        cond_stats = {}
        for cid in [1, 2, 3, 4]:
            c.execute("""
                SELECT 
                    COUNT(*) as n,
                    SUM(CASE WHEN q1_choice = 'B' THEN 1 ELSE 0 END) as choose_ai,
                    AVG(q2_data_authority) as avg_q2,
                    AVG(q3_confidence_anchor) as avg_q3,
                    AVG(q4_tacit_skepticism) as avg_q4,
                    AVG(q5_probabilistic) as avg_q5,
                    AVG(q6_bullshit) as avg_q6,
                    AVG(q7_deception) as avg_q7,
                    AVG(q8_tacit_reevaluation) as avg_q8,
                    AVG(q9_future_trust) as avg_q9
                FROM responses_2x2
                WHERE condition_id = ?
            """, (cid,))
            row = c.fetchone()
            n = row["n"]
            choose_ai = row["choose_ai"] or 0
            rate = round((choose_ai / n * 100), 1) if n > 0 else 0.0
            cond_stats[str(cid)] = {
                "n": n,
                "chooseAi": choose_ai,
                "chooseAiRate": rate,
                "avg_q2": round(row["avg_q2"], 2) if row["avg_q2"] is not None else 0.0,
                "avg_q3": round(row["avg_q3"], 2) if row["avg_q3"] is not None else 0.0,
                "avg_q4": round(row["avg_q4"], 2) if row["avg_q4"] is not None else 0.0,
                "avg_q5": round(row["avg_q5"], 2) if row["avg_q5"] is not None else 0.0,
                "avg_q6": round(row["avg_q6"], 2) if row["avg_q6"] is not None else 0.0,
                "avg_q7": round(row["avg_q7"], 2) if row["avg_q7"] is not None else 0.0,
                "avg_q8": round(row["avg_q8"], 2) if row["avg_q8"] is not None else 0.0,
                "avg_q9": round(row["avg_q9"], 2) if row["avg_q9"] is not None else 0.0,
            }

        # Main effect of confidence on Q1 choice rate
        c.execute("""
            SELECT 
                confidence_level,
                COUNT(*) as n,
                SUM(CASE WHEN q1_choice = 'B' THEN 1 ELSE 0 END) as choose_ai
            FROM responses_2x2
            GROUP BY confidence_level
        """)
        conf_summary = {}
        for r in c.fetchall():
            n = r["n"]
            c_ai = r["choose_ai"] or 0
            conf_summary[r["confidence_level"]] = {
                "n": n,
                "chooseAi": c_ai,
                "rate": round((c_ai / n * 100), 1) if n > 0 else 0.0
            }

        conn.close()

        output = {
            "total": total,
            "conditions": cond_stats,
            "confidenceEffect": conf_summary
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(output, ensure_ascii=False).encode("utf-8"))

    def handle_export_csv(self):
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT * FROM responses_2x2 ORDER BY id ASC")
        rows = c.fetchall()
        conn.close()

        output_io = io.StringIO()
        fieldnames = [
            "ID", "Session_ID", "Timestamp", "Condition_ID", "Confidence_Level", "Confidence_Value",
            "Actual_Outcome", "Language", "Q1_Choice", "Q2_Data_Authority", "Q3_Confidence_Anchor",
            "Q4_Tacit_Skepticism", "Q5_Probabilistic", "Q6_Bullshit", "Q7_Deception",
            "Q8_Tacit_Reevaluation", "Q9_Future_Trust", "Q10_Gender", "Q11_Age", "Q12_STEM",
            "Q13_AI_Freq", "Stage1_Ms", "Stage2_Ms", "Stage3_Ms", "Total_Duration_Ms", "User_Agent"
        ]
        writer = csv.DictWriter(output_io, fieldnames=fieldnames)
        writer.writeheader()

        for r in rows:
            writer.writerow({
                "ID": r["id"],
                "Session_ID": r["session_id"],
                "Timestamp": r["timestamp"],
                "Condition_ID": r["condition_id"],
                "Confidence_Level": r["confidence_level"],
                "Confidence_Value": r["confidence_val"],
                "Actual_Outcome": r["outcome_type"],
                "Language": r["language"],
                "Q1_Choice": r["q1_choice"],
                "Q2_Data_Authority": r["q2_data_authority"],
                "Q3_Confidence_Anchor": r["q3_confidence_anchor"],
                "Q4_Tacit_Skepticism": r["q4_tacit_skepticism"],
                "Q5_Probabilistic": r["q5_probabilistic"],
                "Q6_Bullshit": r["q6_bullshit"],
                "Q7_Deception": r["q7_deception"],
                "Q8_Tacit_Reevaluation": r["q8_tacit_reevaluation"],
                "Q9_Future_Trust": r["q9_future_trust"],
                "Q10_Gender": r["q10_gender"],
                "Q11_Age": r["q11_age"],
                "Q12_STEM": r["q12_stem"],
                "Q13_AI_Freq": r["q13_ai_freq"],
                "Stage1_Ms": r["stage1_ms"],
                "Stage2_Ms": r["stage2_ms"],
                "Stage3_Ms": r["stage3_ms"],
                "Total_Duration_Ms": r["total_duration_ms"],
                "User_Agent": r["user_agent"]
            })

        csv_data = output_io.getvalue().encode("utf-8-sig")
        self.send_response(200)
        self.send_header("Content-Type", "text/csv; charset=utf-8")
        self.send_header("Content-Disposition", "attachment; filename=durian_experiment_2x2_data.csv")
        self.send_header("Content-Length", str(len(csv_data)))
        self.end_headers()
        self.wfile.write(csv_data)


def run_server():
    init_db()
    with socketserver.TCPServer(("", PORT), ExperimentHandler) as httpd:
        httpd.allow_reuse_address = True
        print(f"2x2 Experiment Server running on port {PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer shutting down gracefully.")
            httpd.server_close()


if __name__ == "__main__":
    run_server()
