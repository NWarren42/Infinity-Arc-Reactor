import math as m

def linearCombine(cStart, cEnd, frac):
    return tuple(int(cs * (1-frac) + ce * frac) for cs, ce in zip(cStart, cEnd))

def sineGen (amp, period_s, refreshRateHz):
    x = 0

    stepSize = 1 / refreshRateHz

    while True:
        yield amp * m.sin(2*m.pi*x/period_s)
        
        x += stepSize

        if x > period_s:
            x = 0