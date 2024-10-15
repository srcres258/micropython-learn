import time
from machine import Pin

pin2 = Pin(2, Pin.OUT)

while True:
    pin2.value(not pin2.value())
    time.sleep(1)