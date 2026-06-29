counts = {}
logs= []
error_msgs = {}
keyword = "Database"
wanted_level = "ERROR"
wanted_date = "2026-07-25"

with open("logs/sample.log", "r") as f:  
    for line in f:

        # 1 Parse the line
        parts = line.split()
        date = parts[0] 
        time = parts[1]
        level = parts[2]
        message = " ".join(parts[3:])

        # 2 Store structured log    
        log_entry = {
            "Date": date,
            "Time": time,
            "Level": level,
            "Message": message 
        } 
        logs.append(log_entry)

        # 3 Count log levels, no repeated checks
        counts[level] = counts.get(level, 0) + 1

        # 4 Error-Specific analysis
        if level == "ERROR":
            error_msgs[message] = error_msgs.get(message, 0) + 1


#OUTPUT
print("\n============ ALL LOGS ==========\n")
for log in logs:
    print(f"{log['Date']} {log['Time']} [{log['Level']}]")
    print(f"{log['Message']}")
    print("-" * 30)

print("\n============ FILTER BY DATE ==========\n")
for log in logs:
    if wanted_date == log['Date']:
        print(f"{log['Date']} {log['Time']} [{log['Level']}]")
        print(f"{log['Message']}")
        print()

print("\n============ FILTER BY LEVEL ==========\n")
for log in logs:
    if wanted_level == log['Level']:
        print(f"{log['Date']} {log['Time']} [{log['Level']}]")
        print(f"{log['Message']}")
        print()

print("\n============ SEARCH BY KEYWORD ==========\n")
for log in logs:
    if keyword in log['Message']:
        print(f"{log['Date']} {log['Time']} [{log['Level']}]")
        print(f"{log['Message']}")
        print()

print("\n======== ERROR ANALYSIS ========\n")

for error, count in error_msgs.items():
    print(f"{error}: {count}")

print("========== LOG LEVEL SUMMARY ==========\n")

for level, count in counts.items():
    print(f"{level}: {count}")
