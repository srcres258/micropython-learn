# 利用无源蜂鸣器实现复杂音乐的播放（多曲目，多时长音符）

from machine import Pin, PWM
import time

# 音符频率表
FREQS = {
    'A': [441, 495, 556, 589, 661, 742, 833],
    'B': [495, 556, 624, 661, 742, 833, 935],
    'C': [262, 294, 330, 350, 393, 441, 495],
    'D': [294, 330, 350, 393, 441, 495, 556],
    'E': [330, 350, 393, 441, 495, 556, 624],
    'F': [350, 393, 441, 465, 556, 624, 661],
    'G': [393, 441, 495, 556, 624, 661, 742]
}

# 13引脚为音调频率输出口
buzzer = PWM(Pin(13, Pin.OUT))
# 12引脚为电源输出口
power = Pin(12, Pin.OUT)

def main():
    power.value(0)
    buzzer.duty(0)

    # 定义音乐旋律
    melody = "1155665-4433221-5544332-5544332-1155665-4433221"
    # 时间因子（调节播放快慢）
    factor = 0.5

    while True:
        power.value(1)
        for tone_num in melody:
            if tone_num == '-':
                time.sleep(0.5 * factor)
            else:
                tone_index = int(tone_num) - 1
                tone = FREQS['C'][tone_index]
                print("Playing tone: %d Hz" % tone)
                buzzer.duty(1)
                buzzer.freq(tone)
                time.sleep(0.4 * factor)
                buzzer.duty(0)
                time.sleep(0.1 * factor)
        power.value(0)
        print("--------------------")
        time.sleep(2)

if __name__ == '__main__':
    main()