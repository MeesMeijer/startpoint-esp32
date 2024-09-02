# main.py -- put your code here!
import time 
time.sleep(5) # This is a save timer.. gives time to upload files esxc 


from machine import Timer, Pin 

led = Pin(2, Pin.OUT)

def swthLed(timer: Timer):

    if led.value(): 
        return led.off()

    led.on()

try:
    tim = Timer(0)
    tim.init(period=1000, mode=Timer.PERIODIC, callback=swthLed)

except KeyboardInterrupt:
    tim.deinit()
    print("Bye")