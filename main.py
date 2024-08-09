import neopixel
import machine
import time

RUN_ON_BOOT = False
CONTROL_PIN = 16
LED_COUNT = 35

ring = neopixel.NeoPixel(machine.Pin(CONTROL_PIN), LED_COUNT)
ring.write()

def main():
    while True:
        print(__name__)
        print('tick')
        time.sleep(1)
        print('tock')
        time.sleep(1)

if RUN_ON_BOOT:
    main()


#lc.allOneColor(np, LIGHT_BLUE)