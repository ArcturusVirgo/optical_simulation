# -- coding: utf-8 --
# @Time: 2021/2/18 17:46
# @Author: Zavijah
# @File: Equal_inclination_interference_caculate.py
# @Software: PyCharm
# @Purpose:等倾干涉计算部分

import pygame as pg
import sys
import numpy as np
import math
from PIL import Image
import pygame.freetype

# 图片相关量的定义
rho = 40  # 一厘米有多少个像素
px = 1000  # 图片的宽度（像素）
size = px / rho  # 图片的尺寸（厘米）
RGBA = 0


# 相关物理量的定义
n = 1.5  # 折射率
lambda_ = 453e-9  # 波长
I_source = 1.0  # 入射光强
d = 0.1  # 厚度
f = 0.8


def matrix_creat(size):
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i, j] = np.sqrt((int(matrix.shape[0] / 2) - i) ** 2 + (int(matrix.shape[1] / 2) - j) ** 2)
    return matrix


def caculator_L(d):
    a = matrix_creat(px) / rho / 100
    I_origin = 2 * I_source + 2 * I_source * np.cos(
        2 * math.pi / lambda_ * (2 * d * np.sqrt(n ** 2 - (a ** 2) / (a ** 2 + f ** 2))))
    I_format = I_origin * (255 / 4)
    im = Image.fromarray(I_format)
    im = im.convert('L')
    im = im.resize((320, 320))
    im.save(r"Equal_inclination_interference.png")

    # pic = pg.image.load(r"image\Newtons rings.png")
    # return pic


caculator_L(3e-3)