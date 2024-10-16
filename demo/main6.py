# 无源蜂鸣器 示例代码

from machine import Pin, PWM
import time

# 音符频率（A大调）
C_FREQS = [220, 233, 246, 261, 277, 293, 311, 329, 349, 369, 391, 415, 440, 466, 493, 523, 554, 587, 622, 659, 698, 739, 783, 830, 880]

# 13引脚为音调频率输出口
buzzer = PWM(Pin(13, Pin.OUT))
# 12引脚为电源输出口
power = Pin(12, Pin.OUT)

def main():
    power.value(0)
    buzzer.duty(0)

    while True:
        power.value(1)
        buzzer.duty(1000)
        for tone in C_FREQS:
            print("Playing tone: %d Hz" % tone)
            buzzer.freq(tone)
            time.sleep_ms(250)
        power.value(0)
        buzzer.duty(0)
        print("--------------------")
        time.sleep_ms(1000)

if __name__ == '__main__':
    main()