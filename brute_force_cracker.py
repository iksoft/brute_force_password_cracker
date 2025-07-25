import itertools
import hashlib
import sys
import time
import os

# ANSI color codes for green and red
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'

BANNER = f"""
{GREEN}
██████╗ ██████╗ ██╗   ██╗████████╗███████╗    ███████╗ ██████╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗      ███████╗██║     ███████║██║     █████╔╝ 
██╔═══╝ ██╔══██╗██║   ██║   ██║   ██╔══╝      ╚════██║██║     ██╔══██║██║     ██╔═██╗ 
██║     ██║  ██║╚██████╔╝   ██║   ███████╗    ███████║╚██████╗██║  ██║╚██████╗██║  ██╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

        Brute Force Password Cracker | For Ethical Hacking & Cyber Security
{RESET}
"""

# Supported hash algorithms
HASH_ALGOS = ['md5', 'sha1', 'sha256', 'sha512']


def get_hash_function(algo):
    if algo not in HASH_ALGOS:
        raise ValueError(f"Unsupported algorithm. Choose from: {', '.join(HASH_ALGOS)}")
    return getattr(hashlib, algo)


def brute_force_crack(target_hash, algo, charset, min_len, max_len):
    hash_func = get_hash_function(algo)
    for length in range(min_len, max_len + 1):
        for attempt in itertools.product(charset, repeat=length):
            password = ''.join(attempt)
            hashed = hash_func(password.encode()).hexdigest()
            if hashed == target_hash:
                return password
    return None


def hacker_delay(text, delay=0.1, dots=3):
    print(CYAN + text, end='', flush=True)
    for _ in range(dots):
        print('.', end='', flush=True)
        time.sleep(delay)
    print(RESET)
    time.sleep(0.3)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def interactive_menu():
    clear_screen()
    print(BANNER)
    print(f"{CYAN}Select the hash algorithm to crack:{RESET}")
    for idx, algo in enumerate(HASH_ALGOS, 1):
        print(f"  {idx}. {algo.upper()}")
    while True:
        try:
            choice = int(input(f"{CYAN}Enter choice [1-{len(HASH_ALGOS)}]: {RESET}"))
            if 1 <= choice <= len(HASH_ALGOS):
                algo = HASH_ALGOS[choice - 1]
                break
            else:
                print(f"{RED}Invalid choice. Try again.{RESET}")
        except ValueError:
            print(f"{RED}Invalid input. Enter a number.{RESET}")
    target_hash = input(f"{CYAN}Paste the hash to crack: {RESET}").strip()
    charset = input(f"{CYAN}Enter charset (default: abcdefghijklmnopqrstuvwxyz): {RESET}").strip()
    if not charset:
        charset = 'abcdefghijklmnopqrstuvwxyz'
    try:
        min_len = int(input(f"{CYAN}Minimum password length (default: 1): {RESET}") or 1)
        max_len = int(input(f"{CYAN}Maximum password length (default: 5): {RESET}") or 5)
    except ValueError:
        print(f"{RED}Invalid length. Using defaults 1-5.{RESET}")
        min_len, max_len = 1, 5
    return target_hash, algo, charset, min_len, max_len


def main():
    while True:
        target_hash, algo, charset, min_len, max_len = interactive_menu()
        hacker_delay("[*] Initializing brute force attack", 0.15, 5)
        hacker_delay(f"[*] Hash: {target_hash}", 0.07, 4)
        hacker_delay(f"[*] Algorithm: {algo}", 0.07, 4)
        hacker_delay(f"[*] Charset: {charset}", 0.07, 4)
        hacker_delay(f"[*] Length: {min_len} to {max_len}", 0.07, 4)
        print(f"{GREEN}[*] Cracking in progress...{RESET}")
        time.sleep(1)
        result = brute_force_crack(target_hash, algo, charset, min_len, max_len)
        time.sleep(0.5)
        if result:
            print(f"{GREEN}[+] Password found: {result}{RESET}")
        else:
            print(f"{RED}[-] Password not found in given range.{RESET}")
        print(f"\n{CYAN}Press Enter to return to the menu or type 'exit' to quit.{RESET}")
        choice = input().strip().lower()
        if choice == 'exit':
            print(f"{GREEN}Goodbye!{RESET}")
            break

if __name__ == '__main__':
    main() 