"""
Implement an elevator in a building with floors 0 .. num_floors-1.

class Elevator:
    def __init__(self, num_floors): ...
    def request_floor(self, floor): ...   # someone wants to go to `floor`
    def step(self): ...                   # advance time by one tick
    def current_floor(self): ...

The elevator starts at floor 0 and moves at most one floor per step().


qns :
- in which direction to step towards?
- what is the lift algo? do we clear all up then clear all down?

discussion
- if we use a queue, doesnt rly make sense because it shouldnt be time based, or should it? hm
- to keep it simple first, it just always moves in the direction of the next request
"""
from collections import deque

class Elevator:
    def __init__(self, num_floors):
        self.num_floors = num_floors 
        self.queue = self.deque([])
        self.current = 0
        self.next = -1

    def request_floor(self, floor):
        self.queue.append(floor)

    def step(self):
        if self.next == -1:
            self.next = self.queue.popleft()

        if self.current_floor() > self.next: # Move down
            self.current_floor() -= 1
        elif self.current_floor() < self.next: # Move up
            self.current_floor() += 1
        else: # Reached level
            self.next = -1 # Reset

    def current_floor(self):
        return self.current
            





