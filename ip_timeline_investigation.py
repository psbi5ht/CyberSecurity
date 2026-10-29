import pandas as pd

# 1. Create a security alerts DataFrame
data = {
    "Timestamp": [
        "2026-10-18 10:15:00",
        "2026-10-18 08:22:15",
        "2026-10-18 09:14:02",
        "2026-10-18 11:30:00",
    ],
    "Source_IP": [
        "192.168.1.100",
        "45.33.32.156",
        "192.168.1.100",
        "192.168.1.100",
    ],
    "Alert_Type": [
        "Port Scan",
        "Brute Force",
        "SQL Injection",
        "Data Exfiltration",
    ],
    "Destination_Port": [80, 443, 3306, 22],
    "Action_Taken": ["Blocked", "Logged", "Blocked", "Alerted"],
}

df = pd.DataFrame(data)

# --- YOUR CODE ---
# Isolate all logs associated with a specific suspicious IP
target_ip = "192.168.1.100"
ip_investigation = df[df["Source_IP"] == target_ip]

# Sort by timestamp to see the sequence of events
ip_investigation_sorted = ip_investigation.sort_values(by="Timestamp")

print(f"Detailed timeline for target IP {target_ip}:")
print(
    ip_investigation_sorted[
        ["Timestamp", "Alert_Type", "Destination_Port", "Action_Taken"]
    ]
)