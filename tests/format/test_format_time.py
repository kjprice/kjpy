import unittest
from src.kjpy.format.format_time import format_time

MS = 0.001
SECOND = MS * 1000
MINUTE = SECOND * 60
HOUR = MINUTE * 60
DAY = HOUR * 24


class TestFormatTime(unittest.TestCase):
    def test_format_time_without_trailing_ms(self):
        self.assertEqual(format_time(MS), "")
        self.assertEqual(format_time(MINUTE), "1m")
        self.assertEqual(format_time(DAY), "1d")
        self.assertEqual(
            format_time(2 * DAY + 3 * HOUR + 4 * MINUTE + 5 * SECOND + 6 * MS),
            "2d3h4m5s",
        )

    def test_format_time_with_trailing_ms(self):
        self.assertEqual(format_time(MS, True), "1ms")
        self.assertEqual(format_time(DAY + 6 * MS, True), "1d6ms")
