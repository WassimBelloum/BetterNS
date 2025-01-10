import random

max_lines = 7
max_time = 120

def random_lines(state):
    train_plan = []
    for line_number in range(max_lines):
        current_line = []
        current_time = 0
        current_station = random.choice(state.stations)
        while True:
            added_any_connection = False
            current_connection = random.choice(current_station.connections)
            start, end, time, times_covered = current_connection
            if current_time + time <= maximum_time:
                current_line.append(current_connection)
                current_time += time
                current_station = end if start == current_station else start
                added_any_connection = True
            if not added_any_connection:
                if current_line:
                    train_plan.append(current_line)
                break
    for line in train_plan:
        print(line)
    return train_plan