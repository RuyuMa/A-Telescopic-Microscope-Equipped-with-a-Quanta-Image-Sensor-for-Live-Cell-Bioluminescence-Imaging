# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:09:32 2022

@author: ruyu.ma
"""

import matplotlib.cm as cm
from skimage import io
from matplotlib.colors import LogNorm
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
###################################################
filepath = r'N:\01 HPC\07 Team Cui\Data\Low Light Microscope\2022-08-12 EXESISERS\Gigajot\1 il\10s'
pathDir = os.listdir(filepath)
background = 0
for idx in range(len(pathDir)):
    filename = pathDir[idx]
    backgroundb = cv2.imread(os.path.join(filepath,filename),-1)/len(pathDir)
    #backgroundb = cv2.imread(os.path.join(filepath, filename),-1)
    background = background + backgroundb
x = len(background[1,:]) 
y = len(background[:,1]) 
plt.imshow(background,extent=(0, x, 0, y),norm=LogNorm())
#plt.imshow(background,extent=(0, x, 0, y),cmap=cm.Reds,norm=LogNorm())
plt.colorbar()
plt.show()
io.imsave('Gigajot2.tif',np.float64(background))
###########################################average 10 images of sample
filepath = r'N:\01 HPC\07 Team Cui\Data\Low Light Microscope\2022-08-12 EXESISERS\EMCCD\1ul\10s'
pathDir = os.listdir(filepath)
img = 0
for idx in range(len(pathDir)):
    filename = pathDir[idx]
    imgb = cv2.imread(os.path.join(filepath,filename),-1)/len(pathDir)
    #imgb = cv2.imread(os.path.join(filepath, filename),-1)
    img = img + imgb
 #img = img.astype(np.int64)
plt.imshow(img, extent=(0, x, 0, y),norm=LogNorm())
#plt.imshow(sample, extent=(0, x, 0, y),cmap=cm.Reds,norm=LogNorm())
plt.colorbar()
plt.show()
io.imsave('EMCCD.tif',np.float64(img))
###########################################average 10 images of background
###################################################
filepath = r'N:\01 HPC\07 Team Cui\Data\Low Light Microscope\2022-08-12 EXESISERS\Gigajot\1 il\10s no binning'
pathDir = os.listdir(filepath)
background = 0
for idx in range(len(pathDir)):
    filename = pathDir[idx]
    backgroundb = cv2.imread(os.path.join(filepath,filename),-1)/len(pathDir)
    #backgroundb = cv2.imread(os.path.join(filepath, filename),-1)
    background = background + backgroundb
x = len(background[1,:]) 
y = len(background[:,1]) 
plt.imshow(background,extent=(0, x, 0, y),norm=LogNorm())
#plt.imshow(background,extent=(0, x, 0, y),cmap=cm.Reds,norm=LogNorm())
plt.colorbar()
plt.show()
io.imsave('Gigajot.tif',np.float64(background))

'''filepath = r'N:\01 HPC\07 Team Cui\Data\Low Light Microscope\2022-07-09 compare different setups with EXISIZER cells\3X\0.1ul\10s'
pathDir = os.listdir(filepath)
img = 0
for idx in range(len(pathDir)):
    filename = pathDir[idx]
    imgb = cv2.imread(os.path.join(filepath,filename),-1)/len(pathDir)
    #imgb = cv2.imread(os.path.join(filepath, filename),-1)
    img = img + imgb
 #img = img.astype(np.int64)
plt.imshow(img, extent=(0, x, 0, y),norm=LogNorm())
#plt.imshow(sample, extent=(0, x, 0, y),cmap=cm.Reds,norm=LogNorm())
plt.colorbar()
plt.show()
io.imsave('10s 0.1ul.tif',np.float64(img))
###########################################average 10 images of sample
filepath = r'N:\01 HPC\07 Team Cui\Data\Low Light Microscope\2022-07-09 compare different setups with EXISIZER cells\3X\0.05ul\10s1'
pathDir = os.listdir(filepath)
img = 0
for idx in range(len(pathDir)):
    filename = pathDir[idx]
    imgb = cv2.imread(os.path.join(filepath,filename),-1)/len(pathDir)
    #imgb = cv2.imread(os.path.join(filepath, filename),-1)
    img = img + imgb
 #img = img.astype(np.int64)
plt.imshow(img, extent=(0, x, 0, y),norm=LogNorm())
#plt.imshow(sample, extent=(0, x, 0, y),cmap=cm.Reds,norm=LogNorm())
plt.colorbar()
plt.show()
io.imsave('10s 0.05ul.tif',np.float64(img))
###########################################average 10 images of sample'''
'''filepath = r'N:\01 HPC\07 Team Cui\Data\Low Light Microscope\2022-07-03 cells stability\background\10s'
pathDir = os.listdir(filepath)
img = 0
for idx in range(len(pathDir)):
    filename = pathDir[idx]
    imgb = cv2.imread(os.path.join(filepath,filename),-1)/len(pathDir)
    #imgb = cv2.imread(os.path.join(filepath, filename),-1)
    img = img + imgb
 #img = img.astype(np.int64)
plt.imshow(img, extent=(0, x, 0, y),norm=LogNorm())
#plt.imshow(sample, extent=(0, x, 0, y),cmap=cm.Reds,norm=LogNorm())
plt.colorbar()
plt.show()
io.imsave('10s.tif',np.float64(img))'''