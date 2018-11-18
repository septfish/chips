#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: cl
@time: 2018/11/18 22:07
'''

'''
NumPy是Python语言的一个扩充程序库。支持高级大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。
Numpy内部解除了Python的PIL(全局解释器锁),运算效率极好,是大量机器学习框架的基础库!
'''


import numpy as np




if __name__ == '__main__':

    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # a = [1, 2, 3]
    c = np.array(a, dtype=np.complex)

    x = np.random.random(2)
    a = np.arange(24)
    b = a.reshape(2, 4, 3)
    print b
    # print b.ndim





