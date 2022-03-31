# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 22:34:59 2022

@author: daydaydream
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
row = img_arr.shape[0]  # 行
col = img_arr.shape[1]  # 列


#对二维数组进行傅里叶变换
target = np.fft.fft2(img_gray)
#移到频谱中央
target1 = np.fft.fftshift(target)

#显示未处理频率图
res = np.log(np.abs(target1))
plt.subplot(131), plt.imshow(res, 'gray'), plt.title('Fourier Image')


#理想低通滤波器构建
d = input("enter d:")
d = int(d)
crow,ccol = int(row/2),int(col/2)#计算平铺中心
hl = np.zeros((row,col),np.uint8)
for i in range(row):
    for j in range(col):
        if np.sqrt(i*i+j*j) <= d:# 将距离频谱中心小于D的部分低通信息设置为1，属于低通滤波
            hl[crow-d:crow+d, ccol-d:ccol+d] = 1
            
#理想高通滤波器
hh=1-hl

#将待处理图像通过低通滤波器
img_lowpass = target1*hl
#对频率图复原
img_lowpass = np.fft.ifftshift(img_lowpass)
#逆变换
img_lowpass = np.fft.ifft2(img_lowpass)
img_lowpass = np.abs(img_lowpass)
img_lowpass = (img_lowpass-np.amin(img_lowpass))/(np.amax(img_lowpass)-np.amin(img_lowpass))
#显示
plt.figure()
plt.subplot(132), plt.imshow(img_lowpass,cmap='gray')
plt.show()


#将待处理图像通过高通滤波器
img_highpass = target1*hh
#对频率图复原
img_highpass = np.fft.ifftshift(img_highpass)
#逆变换
img_highpass = np.fft.ifft2(img_highpass)
#取绝对值
img_highpass = np.abs(img_highpass)
#img_highpass = (img_highpass-np.amin(img_highpass))/(np.amax(img_highpass)-np.amin(img_highpass))
#显示
plt.figure()
plt.subplot(133), plt.imshow(img_highpass,cmap='gray')
plt.show()
