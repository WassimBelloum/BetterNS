import random

from .randomise import Random

class HillClimber:
    """
    The HillClimber class that changes 1 to 3 random lines in the complete planning
    to a different random line. Any solution that is better then the best current solution,
    is kept for the next iteration.
    """
    def __init__(self, state, train_plan, connections, max_lines, max_time):
        self.state = state
        self.plan = train_plan
        self.value = state.score(self.plan)
        self.max_lines = max_lines
        self.max_time = max_time
        self.connections = connections
        
    def mutate_lines(self, mutate_count):
        """
        Changes random amount of 1 to 3 lines in the current plan.
        Saves the removed and newly created lines.
        """
        randomise = Random(self.state, self.max_lines, self.max_time)
        removed_lines = []
        added_lines = []
        # Remove lines
        for _ in range(mutate_count):
            index_to_remove = random.randint(0, len(self.plan) - 1)
            removed_lines.append((index_to_remove, self.plan[index_to_remove]))
            self.plan.pop(index_to_remove)
        # Add new lines, possibly 1 less then what was removed
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
        """
        If the changes didn't make a better plan,
        this reverts the changes that were made.
        """
        for added_line in added_lines:
            if added_line in self.plan:
                self.plan.remove(added_line)
        
        for index, line in reversed(removed_lines):
            self.plan.insert(index, line)
        
    def check_solution(self):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = self.state.score(self.plan)
        if new_value > self.value:
            self.value = new_value
            return True
        return False
        
    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        for iteration in range(iterations):
            # Generate number between 1 and 3 and change that amount of lines
            mutate_count = random.randint(1, 3)
            removed_lines, added_lines = self.mutate_lines(mutate_count)
            # If new solution is not better, revert the changes
            if not self.check_solution():
                self.revert_mutation(removed_lines, added_lines)
    
    def reset_class(self):
        """
        Reset the class to allow looping.
        """
        self.state = None
        self.plan = None
        self.value = None
        self.max_lines = None
        self.max_time = None
        self.connections = None