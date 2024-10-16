# 有源蜂鸣器 示例代码

from machine import Pin, PWM
import time

# 音符频率（C大调）
C_FREQS = [262, 294, 330, 350, 393, 441, 495]

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
            time.sleep_ms(500)
        power.value(0)
        buzzer.duty(0)
        print("--------------------")
        time.sleep_ms(1000)

if __name__ == '__main__':
    main()