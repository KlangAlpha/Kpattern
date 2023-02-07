# Kpattern
基于Klang扩展的 股票模式识别项目

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

