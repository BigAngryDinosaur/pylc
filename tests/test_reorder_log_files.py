
from pylc.reorder_log_files import Solution

def test_basic():
    s = Solution()

    input = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    output = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

    assert s.reorderLogFiles(input) == output
