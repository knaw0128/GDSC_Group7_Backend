import json

class Habit:
    def __init__(self, habitName, habitIcon, habitStart, habitFrequency, habitReminder):
        self.HabitName = habitName
        self.HabitIcon = habitIcon
        self.HabitStart = habitStart
        self.HabitFrequency = habitFrequency
        self.HabitReminder = habitReminder
        # Init some property below if needed
    
    def toDict(self):
        return self.__dict__

