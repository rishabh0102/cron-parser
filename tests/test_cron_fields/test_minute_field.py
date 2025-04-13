import unittest
from parameterized import parameterized

from src.fields import MinuteField


class TestMinuteField(unittest.TestCase):
    @parameterized.expand([
        ("*", list(range(0, 60))),
        ("*/12", [0, 12, 24, 36, 48]),
        ("*/6", list(range(0, 60, 6))),
        ("10-15", list(range(10, 16))),
        ("5-20/5", list(range(5, 21, 5))),
        ("3-18/3", list(range(3, 19, 3))),
        ("0-50/10,5-25/5", sorted(set(list(range(0, 51, 10)) + list(range(5, 26, 5))))),
    ])
    def test_minute_field(self, cron_string, expected_output):
        field = MinuteField(cron_string)
        self.assertEqual(expected_output, field.parse())

    @parameterized.expand([
        ("61", ValueError),
        ("-2", ValueError),
        ("*/65", ValueError),
        ("*/-3", ValueError),
        ("0-65/7", ValueError),
        ("10-70/4", ValueError),
    ])
    def test_minute_field_invalid(self, cron_str, expected_exception):
        field = MinuteField(cron_str)
        with self.assertRaises(expected_exception):
            field.parse()
