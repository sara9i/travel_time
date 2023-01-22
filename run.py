import csv
import os
import sys
import traceback
from datetime import datetime

from travel_time import calculate_travel_time_with_sort

filename = (
    sys.argv[1]
    if len(sys.argv) > 1
    else os.environ.get("FILENAME") or "sample_delivery_logs.csv"
)
try:
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        # Create a list of deliveries
        deliveries = []
        for row in reader:
            start_time = datetime.strptime(row["Pick up time"], "%Y-%m-%dT%H:%M:%SZ")
            end_time = datetime.strptime(row["Delivered time"], "%Y-%m-%dT%H:%M:%SZ")
            delivery_person = row["Delivery Person"]
            deliveries.append(
                {
                    "delivery_person": delivery_person,
                    "start_time": start_time,
                    "end_time": end_time,
                }
            )
        result = calculate_travel_time_with_sort(deliveries)
        print(f"result: {result}")
except FileNotFoundError:
    traceback.print_exc(f"No such file or directory: {filename}")
except Exception as e:
    traceback.print_exc(f"Error running the script: {e}")
