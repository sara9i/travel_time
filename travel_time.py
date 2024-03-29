from collections import defaultdict

# NOTE: using defaultdict from the python's collections module, which returns a default value for a non-existent key
# so we don't have to check for key existence.

# NOTE: time complexity = O(n) where n is the number of rows in the CSV file
# NOTE: space complexity = O(m) where m is the number of unique delivery persons
def calculate_travel_time(deliveries):
    # Create a dictionary to store the travel times for each delivery person
    travel_times = defaultdict(int)

    # Create a dictionary to store the current delivery times for each delivery person
    current_deliveries = {}
    for delivery in deliveries:
        start_time = delivery["start_time"]
        end_time = delivery["end_time"]
        delivery_person = delivery["delivery_person"]

        # Check if the delivery person is currently on another delivery
        if delivery_person in current_deliveries:
            # Calculate the overlap in time
            previous_delivery = current_deliveries[delivery_person]
            if previous_delivery["end_time"] > start_time:
                overlap = (
                    min(end_time, previous_delivery["end_time"])
                    - max(start_time, previous_delivery["start_time"])
                ).total_seconds() / 60
                # Subtract the overlap from the total travel time
                travel_times[delivery_person] -= overlap

        # Add the new delivery time to the current deliveries dictionary
        current_deliveries[delivery_person] = {
            "start_time": start_time,
            "end_time": end_time,
        }
        # Add the total travel time for the delivery
        travel_times[delivery_person] += (end_time - start_time).total_seconds() / 60
    return dict(travel_times)


# ################-------- SOLUTION ASSUMING CSV IS NOT SORTED ON TIME --------####################
# NOTE: time complexity = O(n log n) where n is the number of rows in the CSV file + built-in sort() of python = O(n log n)
# NOTE: space complexity = O(m) where m is the number of unique delivery persons


def calculate_travel_time_with_sort(deliveries):
    # Sort the deliveries based on start time
    deliveries.sort(key=lambda x: x["start_time"])
    return calculate_travel_time(deliveries)
