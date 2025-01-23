# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:16:46 2023

@author: ruyu.ma
"""


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import xlrd
import os

fig = plt.figure()

wb = xlrd.open_workbook("2.6X and 20X.xlsx")
print("sheet 数量:",wb.nsheets)
print("sheet 名称:",wb.sheet_names())
Gigajot_sh1 = wb.sheet_by_index(1)
Gigajot_x = Gigajot_sh1.col_values(12)
Gigajot_x = np.array(Gigajot_x[0:20])
Gigajot_y = Gigajot_sh1.col_values(13)
Gigajot_y = np.array(Gigajot_y[0:20])
Gigajot_z = np.polyfit(Gigajot_x, Gigajot_y,3) # 用5次多项式拟合，可改变多项式阶数；
Gigajot_p = np.poly1d(Gigajot_z) #得到多项式系数，按照阶数从高到低排列
print(Gigajot_p)  #显示多项式
Gigajot_yy = Gigajot_p(Gigajot_x[0:20])



LV200_sh1 = wb.sheet_by_index(3)
LV200_x = LV200_sh1.col_values(12)
LV200_x = np.array(LV200_x[0:16])
LV200_y = LV200_sh1.col_values(13)
LV200_y = np.array(LV200_y[0:16])
LV200_z = np.polyfit(LV200_x, LV200_y, 3) # 用7次多项式拟合，可改变多项式阶数；
LV200_p = np.poly1d(LV200_z) #得到多项式系数，按照阶数从高到低排列
print(LV200_p)  #显示多项式
LV200_yy = LV200_p(LV200_x[0:15])

def to_percent(temp, position):
    return '%1.0f'%(100*temp)+'%'

ax = plt.gca()
ax.spines['top'].set_linewidth('2.0')
ax.spines['bottom'].set_linewidth('2.0')
ax.spines['left'].set_linewidth('2.0')
ax.spines['right'].set_linewidth('2.0')
ax.tick_params(axis='both', width=2)

plt.plot(LV200_x,LV200_y,'.',label='LV200/EMCCD data', color = 'darkorange',linewidth=2, markersize = 5)
plt.plot(LV200_x[0:15],LV200_yy,label='LV200/EMCCD fit', color = 'darkorange',linewidth=3)
plt.plot(Gigajot_x,Gigajot_y,'.',label='QIScope data', color = 'steelblue',linewidth=2, markersize = 5)
plt.plot(Gigajot_x[0:20],Gigajot_yy,label='QIScope fit', color = 'steelblue',linewidth=3)
plt.rcParams['font.size']=9
plt.xlabel(r'Line pairs/mm',fontsize=9)
plt.ylabel(r'MTF',fontsize=9)
plt.ylim(0, 1)
#plt.ylabel(r'distance (μm)',fontsize=9)
plt.tick_params(labelsize=9)
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
#plt.legend()
#plt.show()
plt.legend()
fig.savefig(os.path.join(os.getcwd(), 'MTF' + ".pdf"), format = 'pdf', dpi=300)

'''
#from __future__ import print_function
#import numpy as np
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
xdata = [ -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
ydata = [1.2, 4.2, 6.7, 8.3, 10.6, 11.7, 13.5, 14.5, 15.7, 16.1, 16.6, 16.0, 15.4, 14.4, 14.2, 12.7, 10.3, 8.6, 6.1, 3.9, 2.1]

# Recast xdata and ydata into numpy arrays so we can use their handy features
xdata = np.asarray(Gigajot_x)
ydata = np.asarray(Gigajot_y)
plt.plot(xdata, ydata, 'o')

# Define the Gaussian function
def Gauss(x, A, B):
    y = A*np.exp(-1*B*x**2)
    return y
parameters, covariance = curve_fit(Gauss, xdata, ydata)

fit_A = parameters[0]
fit_B = parameters[1]

fit_y = Gauss(xdata, fit_A, fit_B)
plt.plot(xdata, ydata, 'o', label='data')
plt.plot(xdata, fit_y, '-', label='fit')
plt.legend()'''