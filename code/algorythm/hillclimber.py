import copy
import random

from .randomise import change_random_line

class HillClimber:
    def __init__(self, state, train_plan, connections):
        if not state.connections_covered(train_plan, connections):
            raise Exception("HillClimber requires a complete solution.")
            
        self.state = state
        self.plan = copy.deepcopy(train_plan)
        self.value = state.score(train_plan)
        
        self.connections = connections
        
    def run(self, iterations):
        self.iterations = iterations
        
        for iteration in range(iterations):
            new_plan = copy.deepcopy(self.plan)
            
            self.mutate_line() # TODO
            
            while state.connections_covered(new_plan, self.connections) != 1:
                self.mutate_previous_line() # TODO
                
            self.check_solution(new_plan) # TODO