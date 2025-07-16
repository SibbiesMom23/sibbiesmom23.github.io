import re
import subprocess

def analyze_auth_log(file_path):
    failed = 0
    successful = 0
    try:
        with open(file_path, 'r', errors='ignore') as file:
            for line in file:
                if "Failed password" in line:
                    failed += 1
                elif "Accepted password" in line:
                    successful += 1
    except FileNotFoundError:
        print(f"Auth log file '{file_path}' not found.")
    return failed, successful

def analyze_ufw_log(log_path='/var/log/ufw.log'):
    blocked = 0
    try:
        with open(log_path, 'r', errors='ignore') as file:
            for line in file:
                if 'BLOCK' in line:
                    blocked += 1
    except FileNotFoundError:
        print(f"UFW log file '{log_path}' not found.")
    return blocked

def get_recent_logins(limit=5):
    try:
        output = subprocess.check_output(['last', '-n', str(limit)], encoding='utf-8')
        logins = []
        for line in output.splitlines():
            if line.strip() == '' or 'wtmp' in line.lower():
                continue
            logins.append(line)
        return logins
    except Exception as e:
        print(f"Error fetching recent logins: {e}")
        return []

def main():
    auth_log = 'sample_auth.log'  # Or /var/log/auth.log for real system
    ufw_log = '/var/log/ufw.log'
    template_file = 'report_template.html'
    output_file = 'report.html'

    failed, successful = analyze_auth_log(auth_log)
    blocked = analyze_ufw_log(ufw_log)
    recent_logins = get_recent_logins()

    # Load HTML template
    with open(template_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace placeholders
    content = content.replace("{{failed}}", str(failed))
    content = content.replace("{{successful}}", str(successful))
    content = content.replace("{{blocked}}", str(blocked))
    content = content.replace("{{recent_logins}}", '<br>',join(recent_logins))

    # Save updated dashboard
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Dashboard updated: Failed={failed}, Successful={successful}, Blocked={blocked}")
