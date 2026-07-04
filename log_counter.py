def print_log(log):
    print(f"{log['Date']} {log['Time']} [{log['Level']}]")
    print(f"{log['Message']}")
    print()

def show_logs(logs):
    for log in logs:
        print_log(log)
        print("-" * 30)

def show_summary(counts):
    for level, count in counts.items():
        print(f"{level}: {count}")

def show_error_analysis(error_msgs):
    for error, count in error_msgs.items():
        print(f"{error}: {count}")

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
print("========== LOG LEVEL SUMMARY ==========\n")
show_summary(counts)

print("\n======== ERROR ANALYSIS ========\n")
show_error_analysis(error_msgs)

print("\n============ SPECIFIC LOGS ==========\n")
for log in logs:
    if keyword in log['Message'] and log['Date'] == wanted_date and log['Level'] == wanted_level:
        print_log(log)

print("\n============ ALL LOGS ==========\n")
show_logs(logs)