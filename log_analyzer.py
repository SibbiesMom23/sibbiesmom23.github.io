# log_analyzer.py

import re

def analyze_log(file_path):
    error_count = 0
    warning_count = 0
    fail_count = 0

    pattern_error = re.compile(r'error', re.IGNORECASE)
    pattern_warning = re.compile(r'warning', re.IGNORECASE)
    pattern_fail = re.compile(r'fail', re.IGNORECASE)

    filtered_lines = []

    with open(file_path, 'r', errors='ignore') as file:
        for line in file:
            if pattern_error.search(line):
                error_count += 1
                filtered_lines.append(line.strip())
            elif pattern_warning.search(line):
                warning_count += 1
                filtered_lines.append(line.strip())
            elif pattern_fail.search(line):
                fail_count += 1
                filtered_lines.append(line.strip())

    print(f"Errors found: {error_count}")
    print(f"Warnings found: {warning_count}")
    print(f"Failures found: {fail_count}")

    # Save filtered lines to a new file
    with open('filtered_logs.txt', 'w') as outfile:
        outfile.write('\n'.join(filtered_lines))

    print("Filtered lines saved to 'filtered_logs.txt'")

if __name__ == '__main__':
    log_file = input("Enter log file path (e.g., /var/log/syslog): ")
    analyze_log(log_file)
