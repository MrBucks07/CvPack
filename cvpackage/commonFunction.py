# Author : Kartik Panchal
# All required dependency
import math


# ***********************

# method to find distance  between two points
def getDistance(self, point1, point2):
    self.passMethod()
    # points coordinates
    x0, y0 = point1
    x1, y1 = point2

    # using maths finding distance.
    dist = math.hypot(x1 - x0, y1 - y0)

    return dist

def passMethod():
    pass