# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 11:38:01 2023

@author: ruyu.ma
"""

import numpy as np
import matplotlib.pyplot as plt
import xlrd
from scipy.optimize import curve_fit
import os

wb = xlrd.open_workbook("2.6X and 20X.xlsx")
print("sheet 数量:",wb.nsheets)
print("sheet 名称:",wb.sheet_names())
fig = plt.figure()
Gigajot_sh1 = wb.sheet_by_index(2)
Gigajot_x = Gigajot_sh1.col_values(0)
Gigajot_y = Gigajot_sh1.col_values(1)
def Lorentz(x,y0,A,xc,w):
    y = y0 + (2*A/np.pi)*(w/(4*(x-xc)**2 + w**2))
    return y

Gigajot_popt,Gigajot_pcov = curve_fit(Lorentz,Gigajot_x,Gigajot_y,p0=[0.2,2.86,200,0.5])
print(Gigajot_popt)
print(Gigajot_pcov)
Gigajot_yy = Lorentz(Gigajot_x,*Gigajot_popt)
print(max(Gigajot_yy)-min(Gigajot_yy))
ax = plt.gca()
ax.spines['top'].set_linewidth('2.0')
ax.spines['bottom'].set_linewidth('2.0')
ax.spines['left'].set_linewidth('2.0')
ax.spines['right'].set_linewidth('2.0')
ax.tick_params(axis='both', width=2)               
plt.plot(Gigajot_x,Gigajot_y,'.',label='QIScope data',color = 'steelblue', markersize = 5)
plt.plot(Gigajot_x,Lorentz(Gigajot_x,*Gigajot_popt),'-',label='QIScope fit',color = 'black',linewidth=3)#绘图
#plt.rcParams['font.size']=9
plt.xlabel(r'distance (μm)',fontsize=9)
plt.ylabel(r'gray value of pixel',fontsize=9)
plt.tick_params(labelsize=9)
plt.legend()
plt.show()
fig.savefig(os.path.join(os.getcwd(), 'Gigajot' + ".pdf"), format = 'pdf', dpi=300)

fig = plt.figure()
EMCCD_sh1 = wb.sheet_by_index(3)
EMCCD_x = EMCCD_sh1.col_values(0)
EMCCD_y = EMCCD_sh1.col_values(1)

EMCCD_popt,EMCCD_pcov = curve_fit(Lorentz,EMCCD_x,EMCCD_y,p0=[500,382,200,0.5])
print(EMCCD_popt)
print(EMCCD_pcov)
EMCCD_yy = Lorentz(EMCCD_x,*EMCCD_popt)
print(max(EMCCD_yy)-min(EMCCD_yy)) 
ax = plt.gca()
ax.spines['top'].set_linewidth('2.0')
ax.spines['bottom'].set_linewidth('2.0')
ax.spines['left'].set_linewidth('2.0')
ax.spines['right'].set_linewidth('2.0')
ax.tick_params(axis='both', width=2)                  
plt.plot(EMCCD_x,EMCCD_y,'.',label='LV200/EMCCD data',color = 'darkorange', markersize = 5)
plt.plot(EMCCD_x,Lorentz(EMCCD_x,*EMCCD_popt),'-',label='LV200/EMCCD fit',color = 'black',linewidth=3)#绘图
plt.rcParams['font.size']=9
plt.xlabel(r'distance (μm)',fontsize=9)
plt.ylabel(r'gray value of pixel',fontsize=9)
plt.tick_params(labelsize=9)
plt.legend()
plt.show()
fig.savefig(os.path.join(os.getcwd(), 'EMCCD' + ".pdf"), format = 'pdf', dpi=300)
#workbook = load_workbook(filename= "2.6X and 20X.xlsx")
#print(workbook.sheetname)
'''
plt.plot(Gigajot_x,Gigajot_y)
Gigajot_z = np.polyfit(Gigajot_x, Gigajot_y, 9) # 用5次多项式拟合，可改变多项式阶数；
Gigajot_p = np.poly1d(Gigajot_z) #得到多项式系数，按照阶数从高到低排列
print(Gigajot_p)  #显示多项式
Gigajot_yy = Gigajot_p(Gigajot_x)
plt.plot(Gigajot_x,Gigajot_yy,label='Gigajot fit')
plt.show()'''