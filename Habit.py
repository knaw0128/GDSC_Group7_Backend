import json

class Habit:
    def __init__(self, habitName, ):
        self.HabitName = habitName
        # Init some property below if needed
    
    def toDict(self):
        return self.__dict__

