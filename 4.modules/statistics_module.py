# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/15 0015

# 模块计算数值数据的基本统计特性 （均值、 中位数、 方差，等）。

import statistics

data = [1,2,3,4,5,6,8,9]
print(statistics.mean(data))    # 计算平均值

print(statistics.median(data))  # 取最中间的两个数值的平均数作为中位数。

print(statistics.variance(data))    # 方差