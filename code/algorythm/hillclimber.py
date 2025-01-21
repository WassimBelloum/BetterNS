import copy
import random

from .randomise import Random

class HillClimber:
    def __init__(self, state, train_plan, connections, max_lines, max_time):
        if not state.connections_covered(train_plan, connections):
            raise Exception("HillClimber requires a complete solution.")
            
        self.state = state
        self.plan = copy.deepcopy(train_plan)
        self.value = state.score(train_plan)
        self.max_lines = max_lines
        self.max_time = max_time
        
        self.connections = connections
        
    def mutate_lines(self, new_plan, mutate_lines):
        randomise = Random(self.state, self.max_lines, self.max_time)
        for _ in range(mutate_lines):
            index_to_remove = random.randint(0, len(new_plan) - 1)
            new_plan.pop(index_to_remove)
            if self.state.connections_covered(new_plan, self.connections) == 1:
                continue
            else:
                randomise.add_random_line(new_plan)
                p = self.state.connections_covered(new_plan, self.connections)
                while p != 1:
                    new_plan.pop()
                    randomise.add_random_line(new_plan)
                    p = self.state.connections_covered(new_plan, self.connections)
        return new_plan
        
    def check_solution(self, new_plan):
        new_value = self.state.score(new_plan)
        old_value = self.value
        
        if new_value >= old_value:
            self.plan = new_plan
            self.value = new_value
        
    def run(self, iterations, mutate_lines):
        self.iterations = iterations
        
        for iteration in range(iterations):
            new_plan = copy.deepcopy(self.plan)
            
            self.mutate_lines(new_plan, mutate_lines)
                
            self.check_solution(new_plan)