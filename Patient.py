import random


class Patient:
    def __init__(self, time):
        self.Age = random.randrange(20, 61)
        self.timestamp = time


    def getage(self):
        return self.Age

    def timestamp(self):
        return self.timestamp


    def wait_time(self, current_time):
        return current_time - self.timestamp




