# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:53:45 2022

@author: daydaydream

butterworth_filter
"""

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

# 读入原图像
img = Image.open(r'C:\Users\daydaydream\Desktop\DIP_homework\imag.png')
# img.show()

# 为了减少计算的维度，因此将图像转为灰度图
img_gray = img.convert('L')
#img_gray.show()

# 得到转换后灰度图的像素矩阵
img_arr = np.array(img_gray)
img_arr = np.pad(img_arr,((0,0),(0,10)),'constant',constant_values = (0,0))
h = img_arr.shape[0]  # 行
w = img_arr.shape[1]  # 列

#对二维数组进行傅里叶变换
img_fft = np.fft.fft2(img_arr)
#移到频谱中央
img_fftshift = np.fft.fftshift(img_fft)


#构建巴特沃斯滤波器
u = np.arange(h)
v = np.arange(w)
u, v = np.meshgrid(u, v)
#每个点到中心的距离
r = input("输入滤波半径:")
r = int(r)
rank = input("滤波器阶数：")
rank = int(rank)
dis = np.sqrt((u-h/2)**2+(v-w/2)**2)
butterworthFILT_low = 1/(1+(dis/r)**(2*rank))
#低通滤波
dstlow = np.zeros_like(img_fftshift)
dstlow_filtered = butterworthFILT_low * img_fftshift
dstlow_ifftshift = np.fft.ifftshift(dstlow_filtered)
dstlow_ifft = np.fft.ifft2(dstlow_ifftshift)
dstlow = np.abs(np.real(dstlow_ifft))
dstlow = np.uint8(dstlow)
#高通滤波器构建
butterworthFILT_high = 1 - butterworthFILT_low
#高通滤波
dsthigh = np.zeros_like(img_fftshift)
dsthigh_filtered = butterworthFILT_high * img_fftshift
dsthigh_ifftshift = np.fft.ifftshift(dsthigh_filtered)
dsthigh_ifft = np.fft.ifft2(dsthigh_ifftshift)
dsthigh = np.abs(np.real(dsthigh_ifft))
dsthigh = np.uint8(dsthigh)

#显示图片
plt.figure()
plt.subplot(131), plt.imshow(dstlow,cmap='gray')
plt.subplot(132), plt.imshow(dsthigh,cmap='gray')
plt.show()