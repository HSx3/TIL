def isWall(x, y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True
    return False

def calAbs(y, x):
    if y - x > 0:
        return y - x
    else:
        return x - y