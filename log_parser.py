import re
log_pattern=re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<date>.*?)\] "(?P<method>\S+)\s(?P<url>\S+)\s*(?P<protocol>\S+)?" (?P<status>\d{3}) (?P<size>\S+)'
)

def parse_log_line(line):
    match=log_pattern.match(line)
    if match:
        return match.groupdict()
    return None