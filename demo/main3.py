# 测试数码管的各管脚是否连通

from machine import Pin, PWM
import time

digit_pin_nums = [23, 22, 21, 18, 19, 5, 4]

digit_pins = []

def main():
    global digit_pins

    for pin_num in digit_pin_nums:
        pin = Pin(pin_num, Pin.OUT)
        pin.value(0)
        digit_pins.append(pin)

    while True:
        for i in range(len(digit_pins)):
            print("digit", i)
            digit_pins[i].value(1)
            time.sleep_ms(1000)
            digit_pins[i].value(0)
            time.sleep_ms(1000)
        print("end loop")

if __name__ == '__main__':
    main()
