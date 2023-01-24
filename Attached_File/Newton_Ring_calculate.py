import numpy as np
from PIL import Image
from math import pi
import matplotlib.pyplot as plt
import math
# import


# 图片相关量的定义
rho = 250  # 一厘米有多少个像素
px = 500  # 图片的宽度（像素）
size = px / rho  # 图片的尺寸（厘米）
print(size)

# 相关物理量的定义
n = 1  # 折射率
lambda_ = 453e-9  # 波长
R = 10  # 透镜的曲率半径
e = 0  # 平面玻璃与平凸透镜球面间的距离
I_source = 1  # 入射光强


def matrix_creat(size):
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i, j] = np.sqrt((int(matrix.shape[0] / 2) - i) ** 2 + (int(matrix.shape[1] / 2) - j) ** 2)
    return matrix


def lambda_to_RGB(lam):
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



a = matrix_creat(px) / rho / 100
I_origin = 4 * I_source * np.sin((n * pi * (a ** 2)) / (R * lambda_) + (2 * n * e * pi) / (lambda_)) ** 2
I_format = I_origin * (255 / 4)

color = lambda_to_RGB(lambda_ * 1e9)
temp = np.zeros((px, px, 4) ,dtype=float)
for i in range(px):
    for j in range(px):
        temp[i][j] = np.hstack((color, I_format[i][j]))

im = Image.fromarray(np.uint8(temp))
# im = Image.fromarray(I_format)
im = im.convert('RGBA')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB’
im.save('outfile.png')




