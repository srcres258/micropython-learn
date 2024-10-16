"""
以A大调为基准，计算十二平均律中各个音符的频率。
"""


def main():
    # A大调基准音的频率（第一国际音高：440Hz）
    base_freq = 220.0
    # 十二平均律计算因子（2的12次方根），升音阶时乘以该因子，降音阶时除以该因子
    factor = 2.0 ** (1 / 12.0)

    # 计算三个升音阶八度音中各音符的频率
    n = 3
    freqs_h = [base_freq * factor ** i for i in range(1, 12 * n + 1)]
    print("升音阶八度音（%d个）：" % n, freqs_h)
    freqs_int_h = [int(round(f, 0)) for f in freqs_h]
    print("四舍五入取整后：", freqs_int_h)

    # 计算两个降音阶八度音中各音符的频率
    n = 2
    freqs_l = [base_freq / factor ** i for i in range(1, 12 * n + 1)]
    print("降音阶八度音（%d个）：" % n, freqs_l)
    freqs_int_l = [int(round(f, 0)) for f in freqs_l]
    print("四舍五入取整后：", freqs_int_l)

    # 把降音阶八度音的频率和升音阶八度音的频率合并后输出
    freqs_int = freqs_int_l
    freqs_int.reverse()
    freqs_int = freqs_int + [int(round(base_freq, 0))] + freqs_int_h
    print("降音阶八度音与升音阶八度音合并后：", freqs_int)


if __name__ == '__main__':
    main()
