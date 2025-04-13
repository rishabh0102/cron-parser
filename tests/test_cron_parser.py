import unittest
from parameterized import parameterized

from src.cron_parser import CronParser


class TestCronParser(unittest.TestCase):
    @parameterized.expand([
        ("*/20 * * * * /path/to/command", [list(range(0, 60, 20)), list(range(24)), list(range(1, 32)), list(range(1, 13)), list(range(1, 8)),"/path/to/command"]),
        ("*/6 * * * * /path/to/command",[list(range(0, 60, 6)), list(range(24)), list(range(1, 32)), list(range(1, 13)), list(range(1, 8)),"/path/to/command"]),
        ("10 * * * * /path/to/command",[[10], list(range(24)), list(range(1, 32)), list(range(1, 13)), list(range(1, 8)), "/path/to/command"]),
        ("5 1 * * * /path/to/command",[[5], [1], list(range(1, 32)), list(range(1, 13)), list(range(1, 8)), "/path/to/command"]),
        ("45 16 * * * /path/to/command",[[45], [16], list(range(1, 32)), list(range(1, 13)), list(range(1, 8)), "/path/to/command"]),
        ("30 4 * * 2 /path/to/command",[[30], [4], list(range(1, 32)), list(range(1, 13)), [2], "/path/to/command"]),
        ("15 10 * * 2-6 /path/to/command",[[15], [10], list(range(1, 32)), list(range(1, 13)), [2, 3, 4, 5, 6], "/path/to/command"]),
        ("*/12 8-18 * * 2-6 /path/to/command",[list(range(0, 60, 12)), list(range(8, 19)), list(range(1, 32)), list(range(1, 13)), [2, 3, 4, 5, 6],"/path/to/command"]),
        ("0 0 5,20 * * /path/to/command",[[0], [0], [5, 20], list(range(1, 13)), list(range(1, 8)), "/path/to/command"]),
        ("0 0 10 2 * /path/to/command",[[0], [0], [10], [2], list(range(1, 8)), "/path/to/command"]),
        ("*/4 * * * 2-6 /path/to/command",[list(range(0, 60, 4)), list(range(24)), list(range(1, 32)), list(range(1, 13)), [2, 3, 4, 5, 6],"/path/to/command"]),
        ("0 */8 * * * /path/to/command",[[0], list(range(0, 24, 8)), list(range(1, 32)), list(range(1, 13)), list(range(1, 8)), "/path/to/command"]),
    ])
    def test_special_cases(self, cron_str, expected):
        parser = CronParser(cron_str)
        parsed = parser.parse()
        self.assertEqual(parsed["minute"], expected[0])
        self.assertEqual(parsed["hour"], expected[1])
        self.assertEqual(parsed["day of month"], expected[2])
        self.assertEqual(parsed["month"], expected[3])
        self.assertEqual(parsed["day of week"], expected[4])
        self.assertEqual(parsed["command"], expected[5])
