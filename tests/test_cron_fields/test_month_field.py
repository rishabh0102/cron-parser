import unittest
from parameterized import parameterized

from src.fields import MonthField


class TestMonthField(unittest.TestCase):
    @parameterized.expand([
        ("*", list(range(1, 13))),
        ("*/4", [1, 5, 9]),
        ("2-6", [2, 3, 4, 5, 6]),
        ("2-11/3", [2, 5, 8, 11]),
        ("2-4/1,7-12/2", [2, 3, 4, 7, 9, 11]),
    ])
    def test_month_field(self, cron_string, expected_output):
        field = MonthField(cron_string)
        self.assertEqual(expected_output, field.parse())