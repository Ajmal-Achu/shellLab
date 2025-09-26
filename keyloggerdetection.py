import psutil

SUSPICIOUS = ["keylog", "logkeys", "keylogger", "keyboard"]

print("=== Keylogger Detection Program ===")
print("Scanning running processes...\n")

found = False

for proc in psutil.process_iter(['pid', 'name']):
    try:
        name = proc.info['name'] or ""
        for word in SUSPICIOUS:
            if word.lower() in name.lower():
                print(f"[!] Suspicious process found: PID={proc.info['pid']} NAME={name}")
                found = True
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

if not found:
    print("No suspicious processes found.")
