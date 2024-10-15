from machine import Pin, PWM
import time

led_pin_nums = [27, 14, 12, 13, 26]

digit_pin_nums = [23, 22, 21, 18, 19, 5, 4]
num_digit_pins = [
    [1, 2, 3, 4, 5, 6], # 0
    [3, 6], # 1
    [2, 3, 0, 4, 5], # 2
    [2, 3, 0, 6, 5], # 3
    [1, 0, 3, 6], # 4
    [2, 1, 0, 6, 5], # 5
    [2, 1, 0, 6, 5, 4], # 6
    [2, 3, 6], # 7
    [0, 1, 2, 3, 4, 5, 6], # 8
    [0, 1, 2, 3, 5, 6] # 9
]

led_pins = []
digit_pins = []

def led_twinkle(led_pin):
    # from dark to bright
    for i in range(1024):
        led_pin.duty(i)
        time.sleep_ms(1)
    # from bright to dark
    for i in range(1023, -1, -1):
        led_pin.duty(i)
        time.sleep_ms(1)

def set_digit_pin_value(digit_num, value):
    for digit_pin in num_digit_pins[digit_num]:
        pin = digit_pins[digit_pin]
        pin.value(value)

def main():
    global led_pins, digit_pins

    for pin_num in led_pin_nums:
        pwm = PWM(Pin(pin_num, Pin.OUT), freq=1000)
        pwm.duty(0)
        led_pins.append(pwm)
        
    for pin_num in digit_pin_nums:
        pin = Pin(pin_num, Pin.OUT)
        pin.value(0)
        digit_pins.append(pin)

    # components' self-check
    for led_pin in led_pins:
        led_pin.duty(1023)
        time.sleep_ms(100)
        led_pin.duty(0)
    for i in range(10):
        set_digit_pin_value(i, 1)
        time.sleep_ms(100)
        set_digit_pin_value(i, 0)
    for i in range(9, -1, -1):
        set_digit_pin_value(i, 1)
        time.sleep_ms(100)
        set_digit_pin_value(i, 0)
    for led_pin in led_pins:
        led_pin.duty(0)

    while True:
        for i in range(len(led_pins)):
            print("Displaying:", i)
            set_digit_pin_value(i, 1)
            led_twinkle(led_pins[i])
            set_digit_pin_value(i, 0)
        for i in range(len(led_pins) - 1, -1, -1):
            print("Displaying:", i)
            set_digit_pin_value(i, 1)
            led_twinkle(led_pins[i])
            set_digit_pin_value(i, 0)

if __name__ == '__main__':
    main()
