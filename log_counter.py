import psutil
import time

counts = {}
total_logs = 0

with open("logs/sample.log", "r") as f:  
    for line in f:

        if "ERROR" in line:
            counts["ERROR"] = counts.get("ERROR", 0) + 1
        if "INFO" in line:
            counts["INFO"] = counts.get("INFO", 0) + 1
        if "WARNING" in line:
            counts["WARNING"] = counts.get("WARNING", 0) + 1

print("==========LOG REPORT==========")
print(f"Total Logs: {total_logs}")

for level, count in counts.items():
    print(f"{level}: {count}")
print("==============================")