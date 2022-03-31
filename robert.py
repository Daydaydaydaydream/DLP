# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:53:06 2022

@author: daydaydream
"""

from PIL import Image
import numpy as np


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

#定义robert算子
#算法G[f(x,y)]=abs[f(x,y)-f(x+1,y+1)]+abs[f(x+1,y)-f(x,y+1)]
new_img_arr = np.zeros((h, w))  # 拉普拉斯锐化后的图像像素矩阵
for i in range(1, h-1):
    for j in range(1, w-1):
        new_img_arr[i][j] = abs(img_arr[i, j]-img_arr[i+1, j+1])+abs(img_arr[i+1, j]-img_arr[i, j+1])
        
#将处理后的图像和原图像重叠
robert_img_arr = np.zeros((h, w))  # 拉普拉斯锐化图像和原图像相加所得的像素矩阵
for i in range(0, h):
    for j in range(0, w):
        robert_img_arr[i][j] = new_img_arr[i][j] + img_arr[i][j]
        
img_robert = Image.fromarray(np.uint8(new_img_arr))
img_robert.show()
img_robert.save(r'C:\Users\daydaydream\Desktop\DIP_homework\robert.png')

img_robert2 = Image.fromarray(np.uint8(robert_img_arr))
img_robert2.show()
img_robert2.save(r'C:\Users\daydaydream\Desktop\DIP_homework\robert2.png')