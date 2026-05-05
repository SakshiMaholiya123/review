# ask 3: Log Line Parsing
# Example log:
# 2026-05-04 10:12:15,234 INFO user=alice action=LOGIN status=OK
# a) Write regex with named groups:
# timestamp, level, user, action, status
# b) Implement:
# def parse_log_line(line: str) -> dict | None
# c) Write tests:
# Valid log
# Malformed log
# d) Test missing fields
# e) Refactor:
# Raise LogFormatError instead of returning None
import re
class LogFormatError(Exception):
    pass

def parse_log_line(line: str) -> dict:
    pattern = (
        r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+"
        r"(?P<level>\w+)\s+"
        r"user=(?P<user>\w+)\s+"
        r"action=(?P<action>\w+)\s+"
        r"status=(?P<status>\w+)"
    )
    match=re.fullmatch(pattern,line)
    if match:
        return match.groupdict()
    
    raise LogFormatError("invalid log")
