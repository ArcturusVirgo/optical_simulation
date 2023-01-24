# -- coding: utf-8 --
# @Time: 2021/1/31 17:34
# @Author: Zavijah
# @File: 123.py
# @Software: PyCharm


import os
import numpy as np
from PIL import Image

# im = Image.open("12.png")  # 打开图片
# im_array = np.array(im)  # 将图片转化为numpy数组
#
# print(im_array)
# img = Image.fromarray(im_array).convert('RGB')  # 将数组转化回图片
# img.save("out.bmp")  # 将数组保存为图片


def chang(lam):
    if lam >= 380.0 and lam < 440.0:
        r = -1.0 * (lam - 440.0) / (440.0 - 380.0)
        g = 0.0
        b = 1.0
    elif (lam >= 440.0 and lam < 490.0):
        r = 0.0
        g = (lam - 440.0) / (490.0 - 440.0)
        b = 1.0
    elif (lam >= 490.0 and lam < 510.0):
        r = 0.0
        g = 1.0
        b = -1.0 * (lam - 510.0) / (510.0 - 490.0)
    elif (lam >= 510.0 and lam < 580.0):
        r = (lam - 510.0) / (580.0 - 510.0)
        g = 1.0
        b = 0.0
    elif (lam >= 580.0 and lam < 645.0):
        r = 1.0
        g = -1.0 * (lam - 645.0) / (645.0 - 580.0)
        b = 0.0
    elif (lam >= 645.0 and lam <= 780.0):
        r = 1.0
        g = 0.0
        b = 0.0
    else:
        r = 0.0
        g = 0.0
        b = 0.0
    temp = np.array((r, g, b))
    return temp * 255


print(chang(644))


