import pandas as pd

# 1. Create a sample security alerts DataFrame
data = {
    "Timestamp": [
        "2026-10-18 08:22:15",
        "2026-10-18 09:14:02",
        "2026-10-18 10:05:48",
        "2026-10-18 11:01:30",
        "2026-10-18 12:15:00",
    ],
    "Alert_ID": ["SEC-9081", "SEC-9082", "SEC-9083", "SEC-9084", "SEC-9085"],
    "Source_IP": [
        "45.33.32.156",
        "185.220.101.5",
        "198.51.100.42",
        "203.0.113.88",
        "10.0.0.99",
    ],
    "Alert_Type": [
        "Brute Force Attack",
        "SQL Injection Attempt",
        "Suspicious PowerShell",
        "Ransomware Detected",
        "Port Scan",
    ],
    "Severity": ["High", "Low", "Critical", "Critical", "Medium"],
}

df = pd.DataFrame(data)

# --- YOUR FILTERING CODE ---

# Filter rows where Severity is 'High' or 'Critical'
high_priority_alerts = df[df["Severity"].isin(["High", "Critical"])]

# See how many high-priority alerts you need to investigate
print(f"Total High/Critical Alerts: {len(high_priority_alerts)}")

# View a summary of these alerts (Timestamp, Source IP, and Alert Type)
print("\n--- High Priority Alerts Summary ---")
print(high_priority_alerts[["Timestamp", "Source_IP", "Alert_Type"]].head(10))