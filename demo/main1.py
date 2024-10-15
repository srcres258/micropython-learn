from machine import Pin
import time

led_pin_nums = [27, 14, 12, 13, 26]

def main():
    led_pins = []
    for pin_num in led_pin_nums:
        led_pins.append(Pin(pin_num, Pin.OUT))

    while True:
        for i in range(len(led_pins)):
            led_pins[i].value(1)
            time.sleep_ms(100)
            led_pins[i].value(0)
        for i in range(len(led_pins) - 1, -1, -1):
            led_pins[i].value(1)
            time.sleep_ms(100)
            led_pins[i].value(0)

if __name__ == '__main__':
    main()