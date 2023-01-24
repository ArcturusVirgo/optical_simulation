# -- coding: utf-8 --
# @Time: 2021/11/14 18:58
# @Author: Zavijah  zavijah@qq.com
# @File: main.py
# @Software: PyCharm
# @Purpose:
import os
import matplotlib.pyplot as plt
import numpy as np

# os.system("pyinstaller -Fw concave_lens.py")
# os.system("pyinstaller -Fw convex_lens.py")
# os.system("pyinstaller -Fw Double_slit_interference.py")
os.system("pyinstaller -Fw -i ./a.ico 光学虚拟演示平台.py")
# os.system("pyinstaller -Fw Newton_Ring.py")
# os.system("pyinstaller -Fw Equal_inclination_interference.py")


temp = [
    [0, 50, 100, 150, 200, 250],
    [0, 50, 100, 150, 200, 250],
    [0, 50, 100, 150, 200, 250],
    [0, 50, 100, 150, 200, 250],
        ]
plt.imshow(temp, cmap=plt.cm.gray)
plt.show()
