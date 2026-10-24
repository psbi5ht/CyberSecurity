import pandas as pd

# Realistic security alert data for a SOC dashboard
alert_data = {
    "timestamp": [
        "2026-10-18 08:22:15",
        "2026-10-18 09:14:02",
        "2026-10-18 10:05:48",
        "2026-10-18 11:01:30",
    ],
    "alert_id": ["SEC-9081", "SEC-9082", "SEC-9083", "SEC-9084"],
    "src_ip": ["45.33.32.156", "185.220.101.5", "198.51.100.42", "203.0.113.88"],
    "dst_ip": ["10.10.50.20", "10.10.50.45", "10.10.50.88", "10.10.50.15"],
    "alert_type": [
        "Brute Force Attack",
        "SQL Injection Attempt",
        "Suspicious PowerShell Execution",
        "Ransomware Behavior Detected",
    ],
    "severity": ["High", "Medium", "Critical", "Critical"],
    "status": ["Investigating", "Mitigated", "Open", "Contained"],
}

# Convert dictionary into a Pandas DataFrame
df = pd.DataFrame(alert_data)

# Display the alerts table
print("--- Real-World Security Alerts DataFrame (df) ---")
print(df)