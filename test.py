import csv
import unittest
from datetime import datetime

from script import calculate_travel_time_with_sort


class TestCalculateTravelTime(unittest.TestCase):
    def test_calculate_travel_time(self):
        fixtures = [
            {
                "deliveries": [
                    {
                        "delivery_person": "Alice",
                        "start_time": datetime(
                            2020, 12, 21, 23, 40
                        ),  # 21:12:2020 23:40:00
                        "end_time": datetime(2020, 12, 22, 0, 5),  # 22:12:2020 00:05:00
                        # total = 25 min
                    },
                    {
                        "delivery_person": "Alice",
                        "start_time": datetime(
                            2020, 12, 22, 0, 0
                        ),  # 22:12:2020 00:00:00
                        "end_time": datetime(
                            2020, 12, 22, 0, 25
                        ),  # 22:12:2020 00:25:00
                        # total = 25 min
                    },
                    {
                        "delivery_person": "Tony",
                        "start_time": datetime(
                            2020, 12, 22, 1, 25
                        ),  # 22:12:2020 01:25:00
                        "end_time": datetime(
                            2020, 12, 22, 2, 15
                        ),  # 22:12:2020 02:15:00
                        # total = 50 min
                    },
                ],
                # Alice = 25 min + 25 min - 5 min overlap = 45
                # Tony = 50
                "expected_output": {"Alice": 45.0, "Tony": 50.0},
            },
            {
                "deliveries": [
                    {
                        "delivery_person": "Alice",
                        "start_time": datetime(
                            2020, 12, 21, 23, 40
                        ),  # 21:12:2020 23:40:00
                        "end_time": datetime(2020, 12, 22, 0, 5),  # 22:12:2020 00:05:00
                        # total = 25 min
                    },
                    {
                        "delivery_person": "Tony",
                        "start_time": datetime(
                            2020, 12, 22, 0, 0
                        ),  # 22:12:2020 00:00:00
                        "end_time": datetime(
                            2020, 12, 22, 0, 25
                        ),  # 22:12:2020 00:25:00
                        # total = 25 min
                    },
                    {
                        "delivery_person": "Tony",
                        "start_time": datetime(
                            2020, 12, 22, 1, 25
                        ),  # 22:12:2020 01:25:00
                        "end_time": datetime(
                            2020, 12, 22, 2, 15
                        ),  # 22:12:2020 02:15:00
                        # total = 50 min
                    },
                ],
                # Alice = 25 min
                # Tony = 25 min + 50 min = 75 min
                "expected_output": {"Alice": 25.0, "Tony": 75.0},
            },
        ]
        for fixture in fixtures:
            with self.subTest(fixture=fixture):
                deliveries = fixture["deliveries"]
                expected_output = fixture["expected_output"]
                result = calculate_travel_time_with_sort(deliveries)
                self.assertEqual(result, expected_output)
