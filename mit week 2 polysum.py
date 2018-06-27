from math import pi,tan

def polysum(n,s):
    perimeter = n*s
    area = (0.25*n*s**2)/tan(pi/n)
    #return area+(perim squared)
    final= area+perimeter**2 
    return round(final,4)
