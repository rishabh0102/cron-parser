import unittest
from parameterized import parameterized

from src.fields import DayOfMonthField


class TestDayOfMonthField(unittest.TestCase):
    @parameterized.expand([
        ("*", list(range(1, 32))),
        ("*/4", [1, 5, 9, 13, 17, 21, 25, 29]),
        ("2-6", [2, 3, 4, 5, 6]),
        ("1-6/3", [1, 4]),
        ("10-30/5", [10, 15, 20, 25, 30]),
        ("5-15/3", [5, 8, 11, 14]),
        ("1-7/2,20-25/3", [1, 3, 5, 7, 20, 23]),
        ("5-10/2,15-18/3", [5, 7, 9, 15, 18]),
        ("1-5/1,25-30/3", [1, 2, 3, 4, 5, 25, 28])
    ])
    def test_day_of_month_field(self, cron_string, expected_output):
        field = DayOfMonthField(cron_string)
        assert field.parse() == expected_output