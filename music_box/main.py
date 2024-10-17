# 利用无源蜂鸣器实现复杂音乐的播放（多曲目，多时长音符）

from machine import Pin, PWM
import time


# 13引脚为音调频率输出口
buzzer = PWM(Pin(13, Pin.OUT))
# 12引脚为电源输出口
power = Pin(12, Pin.OUT)

def main():
    power.value(0)
    buzzer.duty(0)

    # TODO
    pass


if __name__ == '__main__':
    main()