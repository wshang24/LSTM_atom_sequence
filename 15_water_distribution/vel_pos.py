#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:39:49 2021

@author: dave
"""
import numpy as np 
import os
import matplotlib.pyplot as plt
import scipy.stats as scs
from scipy.stats import norm
import seaborn as sns

path = './'
file = 'velocity_position_nvt.out'
header =2

# TimeStep v_vcmx v_vcmy v_vcmz v_xcmx v_xcmy v_xcmz
#     0      1       2      3      4      5      6      
data = []
fname = os.path.join(path,file)  # read in file path
num_timeframe = 0 
with open(fname, 'r') as fo:
    for n in range(header):
            next(fo)  
    for line in fo:
        if 'Loop' in line:
            break
        info = line.split()
        data.append(info)
        num_timeframe += 1    
data = np.asfarray(data, dtype=np.float64).reshape(num_timeframe,-1)   

#%%

plt.style.use('ggplot')
plt.tight_layout()
fig, ax = plt.subplots()  

r1 = 1
r2 = 2
r3 = 3

free_x = data[:,r1]
free_y = data[:,r2]
free_z = data[:,r3]

onev = free_x
    
sample_mean = np.mean(onev)
sample_std = np.std(onev)

dist = norm(sample_mean, sample_std)

(mean, std) = norm.fit(onev)

n, bins, patches = ax.hist(onev, 60,density = 1 , alpha=0.45)

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std)

ax.plot(x, p, linewidth=2)

ax.set_xlabel('velocity ($a/fs$)')

ax.set_ylabel('Probability Density')
ax.grid(False)
ax.set_facecolor('white')
ax.spines['bottom'].set_color('k')
ax.spines['top'].set_color('k') 
ax.spines['right'].set_color('k')
ax.spines['left'].set_color('k')

ax.spines['bottom'].set_linewidth(1.25)
ax.spines['top'].set_linewidth(1.25) 
ax.spines['right'].set_linewidth(1.25)
ax.spines['left'].set_linewidth(1.25)
ax.legend(facecolor = 'white',loc='best', fontsize = 'small',ncol = 1)

# plt.savefig('./image/'+str(temps[sel])+'.png', dpi= 1000, bbox_inches="tight")  
# plt.savefig('./image/'+'all.png', dpi= 1000, bbox_inches="tight")  