import math
def desiredloc(y1,y2,d1,d2):
    #formula to calculate distance
    q = (y2 - y1)
    p = (d2 -d1 )
    return (math.sqrt((q*2)+(p*2)))