# Fuzzy Token Tester

A Python script for testing tokens against a web endpoint. Useful for security testing and token validation.

## Installation

1. Install the required Python package:
```bash
pip install requests
```

2. Create a tokens file (see Token Generation section below)

## Usage

1. Edit `fuzzy.py` to configure:
   - Target URL
   - Cookies
   - Headers
   - Request data template

2. Run the script:
```bash
python fuzzy.py
```

## Token Generation

Here are several ways to generate token files using bash commands:

### Sequential Numbers
```bash
# Generate 4-digit numbers (0000-9999)
seq -w 0 9999 > tokens.txt

# Generate 6-digit numbers (000000-999999)
seq -w 0 999999 > tokens.txt
```

### Hexadecimal Tokens
```bash
# Generate 4-character hex tokens
for i in {0..65535}; do printf "%04x\n" $i; done > tokens.txt

# Generate 8-character hex tokens
for i in {0..65535}; do printf "%08x\n" $i; done > tokens.txt
```

### Random Strings
```bash
# Generate 1000 random 8-character alphanumeric tokens
for i in {1..1000}; do tr -dc 'a-zA-Z0-9' < /dev/urandom | head -c 8; echo; done > tokens.txt

# Generate 1000 random 16-character alphanumeric tokens
for i in {1..1000}; do tr -dc 'a-zA-Z0-9' < /dev/urandom | head -c 16; echo; done > tokens.txt
```

### Custom Pattern Tokens
```bash
# Generate tokens with prefix (e.g., "TOKEN_0000" to "TOKEN_9999")
for i in $(seq -w 0 9999); do echo "TOKEN_$i"; done > tokens.txt

# Generate date-based tokens for a month (YYYYMMDD format)
seq -w 20240301 20240331 > tokens.txt
```

## Security Note

This tool is intended for authorized security testing only. Ensure you have permission to test the target system.
