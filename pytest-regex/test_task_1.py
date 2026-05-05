import pytest
from task_1 import parse_log_line,LogFormatError
def test_valid_log():
    line="2026-05-04 10:12:15,234 INFO user=alice action=LOGIN status=OK"
    res=parse_log_line(line)
    assert res["action"]=="LOGIN"

def test_malformed_log():
    with pytest.raises(LogFormatError):
        parse_log_line("invalid log")

def test_missing():
    line="2026-05-04 10:12:15,234 INFO user=alice  status=OK"
    with pytest.raises(LogFormatError):
        parse_log_line(line)


