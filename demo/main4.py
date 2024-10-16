# ULN2003AN电机驱动步进电机 示例代码

from machine import Pin
from libs.uln2003 import ULN2003

# motor1使用八拍模式
motor1 = ULN2003(ULN2003.HALF_STEP, Pin(2, Pin.OUT), Pin(3, Pin.OUT))

# todo