# 利用无源蜂鸣器实现复杂音乐的播放（多曲目，多时长音符）

from machine import Pin, PWM
import time
from libs.music import Music, Note


# 13引脚为音调频率输出口
buzzer = PWM(Pin(13, Pin.OUT))
# 12引脚为电源输出口
power = Pin(12, Pin.OUT)

# 当前播放的音乐
music = None


def load_music(path):
    global music
    
    with open(path, 'r') as f:
        content = f.read()
        music = Music(path)
        music.load(content)


def play_music():
    for i, note in enumerate(music.notes):
        print("正在演奏第%d个音符..." % (i + 1))
        
        length = music.unit_length * music.speed * note.length
        print("音符时长：%.1f秒" % length)
        
        if note.id == 0:
            print("该音符为休止符")
            power.value(0)
            buzzer.duty(0)
            time.sleep(length)
        else:
            freq = music.note_freq(note)
            print("音符频率：%dHz" % freq)
            power.value(1)
            buzzer.duty(1000)
            buzzer.freq(freq)
            time.sleep(length)
            power.value(0)
            buzzer.duty(0)


def main():
    power.value(0)
    buzzer.duty(0)

    music_id = input("请输入要播放的音乐ID：")
    music_path = f"/musics/{music_id}.txt"
    print("正在加载音乐...")
    load_music(music_path)
    print("音乐加载完毕！")
    print(f"基大调：{music.base}")
    print(f"播放速度：{music.speed}")
    print(f"单位时长：{music.unit_length}")
    
    interval = 5.0
    i = 0
    while True:
        print("开始第%d次演奏..." % (i + 1))
        play_music()
        print("第%d次演奏完毕，暂停%.1f秒" % (i + 1, interval))
        time.sleep(interval)


if __name__ == '__main__':
    main()