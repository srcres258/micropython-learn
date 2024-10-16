# 无源蜂鸣器 示例代码

from machine import Pin
import time

# 13引脚为输出口
pin = Pin(13, Pin.OUT)

def main():
    pin.value(0)

    while True:
        for i in range(4):
            pin.value(1)
            time.sleep_ms(100)
            pin.value(0)
            time.sleep_ms(100)
        time.sleep_ms(1000)

if __name__ == '__main__':
    main()