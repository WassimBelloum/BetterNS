import random

def random_plan(state, max_lines, max_time):
    plan = []
    for line in range(max_lines):
        current_line = []
        cur_time = 0

        while cur_time < max_time:
            random_conn = random.choice(list(state.connections.values()))
            
            if cur_time + random_conn.time <= max_time:
                current_line.append(random_conn)
                cur_time += random_conn.time
            else:
                break
        
        plan.append(current_line)
    
    return plan