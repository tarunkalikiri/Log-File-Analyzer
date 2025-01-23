import re
from collections import Counter

# Configuration
LOG_FILE_PATH = "web_server.log"  # Path to the web server log file

# Regular Expressions for Parsing Logs
LOG_PATTERN = (
    r'(?P<ip>\S+) '  # IP Address
    r'(\S+) '  # Identd
    r'(\S+) '  # User ID
    r'\[(?P<datetime>[^\]]+)\] '  # Timestamp
    r'"(?P<method>[A-Z]+) (?P<url>[^ ]+) (?P<protocol>[^"]+)" '  # Request
    r'(?P<status_code>\d{3}) '  # Status Code
    r'(?P<size>\S+)'  # Response Size
)

# Define fields of interest
COMMON_PATTERNS = {
    "404_errors": r'\s404\s',
}

def parse_log_line(line):
    """Parses and extracts URL, status code information"""
    match = re.match(LOG_FILE_PATH,line)
