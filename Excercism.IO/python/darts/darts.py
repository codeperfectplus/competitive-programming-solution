import math

def score(x, y):
    r = math.sqrt((x ** 2) + (y ** 2))
    if 0 <= r <= 1:
        return 10
    elif 1 < r <= 5:
        return 5
    elif 5 < r <= 10:
        return 1
    elif r > 10:
        return 0