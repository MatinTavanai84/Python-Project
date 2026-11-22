import math as m

def jazr(a,b):
    y = m.sqrt(a/b+1)
    return y

def ghaderh_motlagh(a,b):
    y = abs(a/b-1)
    return y

def senos(x):
    y = m.sin(x+2)
    return y

def tanjant(x,b):
    y = m.tan(1+x/b)
    return y

print(jazr(64,64))
print(ghaderh_motlagh(10,5))
print(senos(1))
print(tanjant(15,10))