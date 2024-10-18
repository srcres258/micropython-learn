简谱 | 乐谱代码
:---: | :---:
$\mathrm{X}$ | `X`
$\mathop{\mathrm{X}}\limits_{\dot\ }$ | `X/`
$\dot{\mathrm{X}}$ | `X^`
$\underline{\mathrm{X}}$ | `X_`
$\underline{\underline{\mathrm{X}}}$ | `X__`
$\mathrm{X}-$ | `X-`
$\mathrm{X}---$ | `X--`
$\mathrm{X}.$ | `X.`
$\mathrm{X}--$ | `X-.`
$\underline{\mathrm{X}}.$ | `X_.`
$\mathop{\underline{\underline{\mathrm{X}}}}\limits_{\dot\ }.$ | `X/__.`
$\mathop{\mathop{\mathrm{X}}\limits_{\dot\ }}\limits_{\dot\ }$ | `X//`
$\dot{\dot{\mathrm{X}}}$ | `X^^`
$^♭\mathrm{X}$ | `Xb`
$^\#\mathrm{X}$ | `X#`

特殊乐谱代码：

- `=XX=`：定义乐谱的基大调。其中`XX`可取`A`,`A#`,`B`,`C`,`C#`,`D`,`D#`,`E`,`F`,`F#`,`G`,`G#`中的任意一个；或亦可取降半调`Bb`,`Db`,`Eb`,`Gb`,`Ab`中的任意一个。
- `~XX~`：定义乐谱的速率。其中`XX`为整数或小数。乐谱的默认速率为`1`（或用小数表示为`1.0`），速率小于`1`则乐谱减速演奏，大于`1`则乐谱加速演奏。

如下列简谱片段：

$0 \ 0 \ 0 \ \mathop{\underline{\underline5}}\limits_{\dot\ }\mathop{\underline{\underline6}}\limits_{\dot\ }\underline{\underline{12}} \ | \ 3. \ \underline{\mathrm5} \ 3 \mathop{\underline{\underline5}}\limits_{\dot\ }\mathop{\underline{\underline6}}\limits_{\dot\ }\underline{\underline{13}} \ | \ 6. \ \underline{\mathrm5} \ 3 \mathop{\underline{\underline5}}\limits_{\dot\ }\mathop{\underline{\underline6}}\limits_{\dot\ }\underline{\underline{13}}$

转换为乐谱代码为：

```
0-.5/__6/__1__2__ 3.5_35/__6/__1__3__ 6.5_35/__6/__1__3__
```