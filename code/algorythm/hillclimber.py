import copy
import random

from .randomise import Random

class HillClimber:
    def __init__(self, state, train_plan, connections, max_lines, max_time):
        self.state = state
        self.plan = train_plan
        self.value = state.score(self.plan)
        self.max_lines = max_lines
        self.max_time = max_time
        self.connections = connections
        
    def mutate_lines(self, mutate_count):
        randomise = Random(self.state, self.max_lines, self.max_time)
        removed_lines = []
        added_lines = []
        for _ in range(mutate_count):
            index_to_remove = random.randint(0, len(self.plan) - 1)
            removed_lines.append((index_to_remove, self.plan[index_to_remove]))
            self.plan.pop(index_to_remove)
        
        if self.state.score(self.plan) >= self.value:
            for _ in range(mutate_count - 1):
                new_line = randomise.random_heuristics(self.plan)
                added_lines.append(new_line)
        else:
            for _ in range(mutate_count):
                new_line = randomise.random_heuristics(self.plan)
                added_lines.append(new_line)
        return removed_lines, added_lines
        
    def revert_mutation(self, removed_lines, added_lines):
        for added_line in added_lines:
            if added_line in self.plan:
                self.plan.remove(added_line)
        
        for index, line in reversed(removed_lines):
            self.plan.insert(index, line)
        
    def check_solution(self):
        new_value = self.state.score(self.plan)
        if new_value > self.value:
            self.value = new_value
            return True
        return False
        
    def run(self, iterations):
        for iteration in range(iterations):
            mutate_count = random.randint(1, 3)
            removed_lines, added_lines = self.mutate_lines(mutate_count)
            if not self.check_solution():
                self.revert_mutation(removed_lines, added_lines)