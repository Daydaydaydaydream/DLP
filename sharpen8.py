# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 22:33:50 2022

@author: daydaydream
"""

from PIL import Image
import numpy as np
from scipy import signal


# 读入原图像
img = Image.open(r'C:\Users\daydaydream\Desktop\DIP_homework\imag.png')
# img.show()

# 为了减少计算的维度，因此将图像转为灰度图
img_gray = img.convert('L')
img_gray.show()

# 得到转换后灰度图的像素矩阵
img_arr = np.array(img_gray)
h = img_arr.shape[0]  # 行
w = img_arr.shape[1]  # 列

#8临域锐化
value = [[-1,-1,-1], [-1,8,-1],[-1,-1,-1]]
array8 = 1/8*np.array(value)
new_img_arr = signal.convolve2d(img_arr, array8)

img_8 = Image.fromarray(np.uint8(new_img_arr))
img_8.show()
img_8.save(r'C:\Users\daydaydream\Desktop\DIP_homework\sharpen8.png')
