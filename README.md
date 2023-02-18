# Kpattern
基于Klang扩展的 股票模式识别项目

(Detecting Technical Patterns),通过技术指标的探测，获取常见的股票模式，进行模式识别。

和其他zigzag不同的时，这里采用了自动探索拐点，找到更和时的peak和valley。
改进了原有 库的算法。波峰和波谷的探测更合理。

# 安装Klang
```
git clone https://github.com/KlangAlpha/Klang
cd Klang
pip3 install -r requirements.txt 
python3 setup.py install
```

关于 Klang 更多请参考  https://github.com/KlangAlpha/Klang

# zigzag
改进 波峰和波谷算法
原作者采用 2个周期值的差值比率做计算，存在一定的不灵活性，容易出现多个 波峰和波谷值。

改进后，通过调整 周期的最大值和最小值计算，动态滤波。获取相对平滑的 波形。

# 关键点是 zigzag
    波峰和波谷的转折点 是计算模式识别的关键点。 有了关键点，就可以很顺利的计算各种模型

## 杯柄形态
杯柄形态：是投资大师威廉.欧尼尔提出的，在股票的一段上升趋势中，前期已经涨了一波，缩量调整回落，然后放量上攻，到达前期高点处时，又再次缩量回落，然后再放量上攻，营造杯状带柄形态，及股价确定突破，就是大升势开始时。

```
src/zigzag_stock.py
pattern_cup_handle()
```

![image](https://forum.klang.org.cn/assets/uploads/files/1675904621408-sh.600.521_105_zigzag.png)

## W底部
W 底部形态是一种牛市形态，呈现上涨攻势
```
src/zigzag_stock.py
pattern_w_bottom()
```
![image](https://forum.klang.org.cn/assets/uploads/files/1675905248984-sh.600.719_105_zigzag.png)

## v-shaped
chatgpt: v-shaped trends in the stock market can be profitable

add v-shaped pattern recognition
```python
# V-shaped trends 回调买入
def pattern_V():
   ....

```


### 增加Javascript 版本的算法
```
  zigzag = require('./src/zigzag')
  zigzag.peak_valley_pivots([1,2,3,4,5,1,3,4,2,3,1,2,3])
  [
   -1, 0, 0, 0,  1, -1,
    0, 1, 0, 0, -1,  0,
    1
  ]
```

