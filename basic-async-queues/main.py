# main.py -- put your code here!
import time 

# time.sleep(5) # This is a save timer.. gives time to upload files esxc 

import uasyncio
from machine import Pin, UART
from lib.queue import Queue, QueueEmpty,QueueFull

uart = UART(2)
uart.init(115200)

# uart 
async def sender(q: Queue):

    writer = uasyncio.StreamWriter(uart, {})
    writer.write("Hellow world. ")

    while True: 
    
        item = await q.get()
        await writer.awrite(item) # type: ignore
        await writer.drain() # type: ignore    

async def receiver( q: Queue):

    reader = uasyncio.StreamReader(uart)
    while True:
        res = await reader.readline() # type: ignore
        print(f"Got: {res}")
        await q.put((res))


async def producer(q: Queue):
    pin = Pin(2, Pin.OUT)

    while True: 
        await uasyncio.sleep(1)
        await q.put((pin, not pin.value()))

async def comsumer(q: Queue):
    
    while True: 
        pin, rs = await q.get()
        pin.on() if rs else pin.off()


async def main():
    q = Queue()
    p1 = uasyncio.create_task(producer(q))
    c1 = uasyncio.create_task(producer(q))

    q2 = Queue()
    uasyncio.create_task(sender(q2))
    uasyncio.create_task(receiver(q2))
    

    
    while True:
        await uasyncio.sleep(1)
    
    # await uasyncio.sleep(1) 


try:
    uasyncio.run(main())
finally:
    print("rerun..")
    _ = uasyncio.new_event_loop()