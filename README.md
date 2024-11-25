# Token Fuzzing Tool

A flexible Python-based token fuzzing tool designed for testing and discovering valid tokens in web applications. This tool can generate and test tokens of any length with customizable character sets.

## Features

- Generate tokens of any length
- Customizable character sets for token generation
- Load tokens from a file
- Cookie support for authenticated sessions
- Automatic header generation
- Detailed console output
- Support for POST requests
- Configurable through command-line arguments

## Installation

1. Clone the repository: 

bash
git clone https://github.com/yourusername/fuzzy_tokens.git
cd fuzzy_tokens
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Syntax
```bash
python fuzzy.py [-h] -u URL -n USERNAME -p PASSWORD (-l LENGTH | -f FILE) [-c CHARSET] [--cookie COOKIE]
```

### Required Arguments
- `-u, --url`: Target URL for token testing
- `-n, --username`: Username for authentication
- `-p, --password`: Password for authentication

### Optional Arguments
- `-l, --length`: Length of tokens to generate
- `-f, --file`: Path to file containing tokens
- `-c, --charset`: Custom character set (default: 0123456789)
- `--cookie`: Session cookie value (PHPSESSID)
- `-h, --help`: Show help message

### Examples

1. Test 4-digit numeric pins:
```bash
python fuzzy.py -u http://target.com/reset.php -n admin -p password123 -l 4
```

2. Use custom tokens from file:
```bash
python fuzzy.py -u http://target.com/reset.php -n admin -p password123 -f tokens.txt
```

3. Test with hexadecimal characters:
```bash
python fuzzy.py -u http://target.com/reset.php -n admin -p password123 -l 4 -c "0123456789abcdef"
```

4. Include session cookie:
```bash
python fuzzy.py -u http://target.com/reset.php -n admin -p password123 -l 4 --cookie "abc123def456"
```

## Token File Format
When using the `-f` option, format your token file with one token per line:
```text
1234
5678
9012
```

## Security Notice

This tool is intended for:
- Authorized security testing
- Educational purposes
- Penetration testing with explicit permission

Unauthorized testing may be illegal. Always ensure you have proper authorization before testing any systems.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License.
