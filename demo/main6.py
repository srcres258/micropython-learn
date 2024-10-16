# 有源蜂鸣器 示例代码

from machine import Pin, PWM
import time

# 音符频率（C大调）
C_FREQS = [262, 294, 330, 350, 393, 441, 495]

# 13引脚为输出口
buzzer = PWM(Pin(13, Pin.OUT))

def main():
    buzzer.duty(0)

    while True:
        buzzer.duty(1000)
        for tone in C_FREQS:
            print("Playing tone: %d Hz" % tone)
            buzzer.freq(tone)
            time.sleep_ms(500)
        buzzer.duty(0)
        time.sleep_ms(1000)

if __name__ == '__main__':
    main()