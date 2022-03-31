# -*-coding: utf-8 -*-
"""
Created on Fri Mar 18 19:43:04 2022

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

#平均算子平滑图像
#3*3
a3 = 1/9*np.ones((3, 3))#3*3单位矩阵
new_img_arr = signal.convolve2d(img_arr, a3)  # 平滑化后的图像像素矩阵
img_3 = Image.fromarray(np.uint8(new_img_arr))
img_3.show()
img_3.save(r'C:\Users\daydaydream\Desktop\DIP_homework\soomth3.png')



a5 = (1/25)*np.ones((5, 5))#5*5单位矩阵
new_img_arr = signal.convolve2d(img_arr, a5)  # 平滑化后的图像像素矩阵
img_5 = Image.fromarray(np.uint8(new_img_arr))
img_5.show()
img_5.save(r'C:\Users\daydaydream\Desktop\DIP_homework\soomth5.png')



a7 = (1/49)*np.ones((7, 7))#5*5单位矩阵
new_img_arr = signal.convolve2d(img_arr, a7)  # 平滑化后的图像像素矩阵
img_7 = Image.fromarray(np.uint8(new_img_arr))
img_7.show()
img_7.save(r'C:\Users\daydaydream\Desktop\DIP_homework\soomth7.png')