def print_log(log):
    print(f"{log['Date']} {log['Time']} [{log['Level']}]")
    print(f"{log['Message']}")
    print()

def show_logs(logs):
    for log in logs:
        print_log(log)
        print("-" * 30)

def show_summary(level_counts):
    for level, count in level_counts.items():
        print(f"{level}: {count}")

def show_error_analysis(error_msgs):
    for error, count in error_msgs.items():
        print(f"{error}: {count}")

def show_logs_per_day(date_counts):
    for date, count in date_counts.items():
        print(f"{date}: {count}")

date_counts = {}
level_counts = {}
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
        level_counts[level] = level_counts.get(level, 0) + 1

        # 4 Error-Specific analysis
        if level == "ERROR":
            error_msgs[message] = error_msgs.get(message, 0) + 1

        # 5 count log dates
        date_counts[date] = date_counts.get(date, 0) + 1



#OUTPUT
print("========== LOG LEVEL SUMMARY ==========\n")
show_summary(level_counts)

print("========== FIRST AND LAST LOG ==========\n")
print_log(logs[0])
print_log(logs[-1])

print("\n======== ERROR ANALYSIS ========\n")
show_error_analysis(error_msgs)

print("========== MOST OCCURRING ERROR ==========\n")
for error, count in error_msgs.items():
        max_count = max(error_msgs, key=max_count.get) 
        print(f"{error}: {max_count}") #i dont understand how to print the number. help :/

print("\n============ SPECIFIC LOGS ==========\n")
for log in logs:
    if keyword in log['Message'] and log['Date'] == wanted_date and log['Level'] == wanted_level:
        print_log(log)

print("========== LOGS PER DAY ==========\n")
show_logs_per_day(date_counts)

print("\n============ ALL LOGS ==========\n")
show_logs(logs)