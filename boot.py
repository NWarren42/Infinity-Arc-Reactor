# BASE MICORPYTHON BOOT.PY-----------------------------------------------|
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
#------------------------------------------------------------------------|


def setupRepl():
    global ring
    global c
    global lc
    
    from main import ring
    
    import colors as c
    import ledCommands as lc


    global off
    def off(np):
        lc.allOneColor(np, c.OFF)