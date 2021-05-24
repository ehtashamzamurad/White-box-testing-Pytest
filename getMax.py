def getMax1(a, b, c):
    maxValue = a
    if maxValue < b:
        maxValue = b
    if maxValue < c:
        maxValue = c
    return maxValue

def getMax2(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c