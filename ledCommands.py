import time

import tools

def allOneColor(np, color, brt=100):
    for i in range(len(np)):
        np[i] = tuple(int(pix*(brt/100)) for pix in color)
    np.write()



def dimLedPercent(np, percent):
    frac = 1 - percent/100
    for i, led in enumerate(np):
        np[i] = tuple(int(frac*pix) for pix in led)
        
    np.write()

def fade(np, fadeTime, newPat, updateHz=100):
    pass

def sinePulse(np, color, baselineBrt=100, period_s=5, refreshRateHz=10, intensity=10, loop=True):
    
    stepCounter = 0

    sineAddition = tools.sineGen(intensity, period_s, refreshRateHz)
    timeStep = 1/refreshRateHz

    allOneColor(np, color, baselineBrt)
    baselineColor = list(np[0])

    if loop:
        while True:
            for i, led in enumerate(np):
                offset = next(sineAddition)
                np[i] = tuple(int(pix + offset) for pix in baselineColor)
                print(np[i])
            np.write()
            time.sleep(timeStep)
    else:  
        while stepCounter < refreshRateHz*period_s:
            for i, led in enumerate(np):
                offset = next(sineAddition)
                np[i] = tuple(int(pix + offset) for pix in baselineColor)
            np.write()
            stepCounter += 1
            time.sleep(timeStep)
