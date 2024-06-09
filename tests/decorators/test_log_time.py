import time
import unittest
from unittest.mock import patch

from src.kjpy.decorators.log_time import log_time_passed, LogTimePassedMemory

SLEEP_SECONDS = 0.001


class TestLogTime(unittest.TestCase):
    @patch("builtins.print")
    def test_log_time_passed(
        self,
        # ):
        mock_print,
    ):
        @log_time_passed
        def yoyo():
            time.sleep(SLEEP_SECONDS)

        yoyo()
        memories = LogTimePassedMemory.memory
        self.assertEqual(len(memories), 1)
        memory = memories[0]
        elapsed_time = memory["elapsed_time"]
        self.assertGreater(elapsed_time, SLEEP_SECONDS)
        self.assertLess(elapsed_time, SLEEP_SECONDS * 2)
        formatted_time = memory["formatted_time"]
        # print(LogTimePassedMemory.memory)
        mock_print.assert_called_with(f"Time passed: \t {formatted_time} \t yoyo")
