import random

def random_lines(state, max_lines, max_time):
    train_plan = []
    for line_number in range(max_lines):
        current_line = []
        current_time = 0
        current_station = random.choice(state.stations)
        while True:
            added_any_connection = False
            current_connection = random.choice(current_station.connections)
            # print(current_station)
            # print(current_connection)
            start = current_connection.station_a
            end = current_connection.station_b
            time = current_connection.time
            if current_time + time <= max_time:
                current_line.append(current_connection)
                current_time += time
                current_station.name = end if start == current_station.name else start
                added_any_connection = True
            if not added_any_connection:
                if current_line:
                    train_plan.append(current_line)
                break
    for line in train_plan:
        print(line)
    return train_plan