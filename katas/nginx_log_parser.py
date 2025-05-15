from typing import Dict
import re


def parse_log(log: str) -> Dict[str, str]:
    pattern = (
        r'(?P<client_ip>\S+)'  # IP address (e.g. 122.176.223.47)
        r' - - \['
        r'(?P<date>[^\]]+)'  # Date inside square brackets
        r'\] "'
        r'(?P<http_method>\S+)'  # HTTP method (GET/POST/...)
        r' (?P<path>\S+)'  # URL path
        r' HTTP/(?P<http_version>\S+)'  # HTTP version
        r'" (?P<status>\d{3})'  # Status code (e.g. 200)
        r' (?P<response_bytes>\d+|-)'  # Response size (or '-' if none)
        r' "[^"]*" "(?P<user_agent>[^"]+)"'  # User agent string
    )

    match = re.match(pattern, log)
    if not match:
        raise ValueError("Invalid log format")

    return match.groupdict()


if __name__ == "__main__":
    log_entry = (
        '122.176.223.47 - - [05/Feb/2024:08:29:40 +0000] '
        '"GET /web-enabled/Enhanced-portal/bifurcated-forecast.js HTTP/1.1" 200 1684 '
        '"-" "Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00"'
    )

    parsed_log = parse_log(log_entry)
    print("Parsed log data:", parsed_log)
