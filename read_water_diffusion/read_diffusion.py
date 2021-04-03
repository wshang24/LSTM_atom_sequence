#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:27:38 2021

@author: dave
"""

import numpy as np 
import os
import matplotlib.pyplot as plt

path = '/Users/dave/Dropbox/2_toolbox/16_read_diffusion'
file = 'log.lammps'
header = 22341

# Step Temp TotEng KinEng PotEng Press Pxx Pyy Pzz Lx Ly Lz v_diff v_vcor 
#  0    1     2      3      4      5    6   7   8  9  10 11   12     13
      
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


step = data[:,0] * 1e-6 # convert fs to ns
diffusion = data[:,13] * 1e4

plt.style.use('ggplot')
plt.tight_layout()
fig, ax = plt.subplots()  

ax.plot(step, diffusion)

final_diffusion = np.mean(diffusion[-2500:])


ax.set_xlabel('time [ns]')

ax.set_ylabel('diffusion [$10^{-9}m^2S^{-1}$] ')

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

plt.savefig('diffusion.png', dpi= 1200, bbox_inches="tight")

# ax.legend(facecolor = 'white',loc='best', fontsize = 'small',ncol = 1)