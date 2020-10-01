import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, punto):
        difx = punto.x - self.x
        dify = punto.y - self.y
        return math.sqrt(difx * difx + dify * dify)
