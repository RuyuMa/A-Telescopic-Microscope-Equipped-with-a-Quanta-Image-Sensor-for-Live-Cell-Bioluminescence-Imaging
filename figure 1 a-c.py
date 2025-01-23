# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:26:15 2022

@author: ruyu.ma
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import cv2

a=cv2.imread('Gimg.tif',-1)

fig = plt.figure()
ax = fig.gca(projection='3d')
X = len(a[1,:])*1.1/8
X = np.arange(0, X, 1.1/8)
Y = len(a[:,1])*1.1/8
Y = np.arange(0, Y, 1.1/8)
X, Y = np.meshgrid(X, Y)
Z = a
#Z = a[576:1728,576:1728]
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.rainbow, linewidth=0, antialiased=False)
# 画表面,x,y,z坐标， 横向步长，纵向步长，颜色，线宽，是否渐变
#ax.set_zlim(0, 2304)  # 坐标系的下边界和上边界
#ax.zaxis.set_major_locator(LinearLocator(25000))  # 设置Z轴标度
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  # Z轴精度
plt.rcParams['font.size']=9
fig.colorbar(surf, shrink=1, aspect=20, pad=0.12)  # shrink颜色条伸缩比例（0-1），aspect颜色条宽度（反比例，数值越大宽度越窄）
ax.set_zlim(0,80)
ax.set_ylim(0,563)
ax.set_xlim(0,563)
ax.set_xlabel(r'distance (μm)',fontsize=9)
ax.set_ylabel(r'distance (μm)',fontsize=9)
ax.set_zlabel(r'value',fontsize=9)
ax.axes.tick_params(labelsize=9)
plt.show()
