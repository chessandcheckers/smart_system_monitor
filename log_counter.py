counts = {}
total_logs = 0
logs= []
error_msgs = {}

with open("logs/sample.log", "r") as f:  
    for line in f:

        if "ERROR" in line:
            counts["ERROR"] = counts.get("ERROR", 0) + 1
        if "INFO" in line:
            counts["INFO"] = counts.get("INFO", 0) + 1
        if "WARNING" in line:
            counts["WARNING"] = counts.get("WARNING", 0) + 1

        parts = line.split()
        date = parts[0] 
        time = parts[1]
        level = parts[2]
        message = " ".join(parts[3:])

        log_entry = {
            "Date": date,
            "Time": time,
            "Level": level,
            "Message": message } 
        
        if level == "ERROR":
            error_msgs[message] = error_msgs.get(message, 0) + 1 

        logs.append(log_entry)

        total_logs += 1

for log in logs:
    print("-----------------------")
    print(f"Date: {log['Date']}")
    print(f"Time: {log['Time']}")
    print(f"Level: {log['Level']}")
    print(f"Message: {log['Message']}")

print("\n")
print("========ERROR ANALYSIS========")
for error, count in error_msgs.items():
    print(f"{error}: {count}")
print("==============================")

print("\n")

print("==========LOG REPORT==========")
print(f"Total Logs: {total_logs}")

for level, count in counts.items():
    print(f"{level}: {count}")
print("==============================")