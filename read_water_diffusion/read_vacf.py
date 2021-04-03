#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:51:43 2021

@author: dave
"""



import numpy as np 
import os
import matplotlib.pyplot as plt

path = '/Users/dave/Dropbox/2_toolbox/16_read_diffusion'
file = 'log.lammps'
header = 20319

# # TimeStep c_1[1] c_1[2] c_1[3] c_1[4]
# #    0       1       2      3      4   
   
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


step = data[:,0][:100]
vacf = data[:,4][:100]
plt.style.use('ggplot')
plt.tight_layout()
fig, ax = plt.subplots()  

ax.plot(step, vacf)

ax.set_xlabel('step')

ax.set_ylabel('diffusion')
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
# ax.legend(facecolor = 'white',loc='best', fontsize = 'small',ncol = 1)