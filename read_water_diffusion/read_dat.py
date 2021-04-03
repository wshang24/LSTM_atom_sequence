#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:19:05 2021

@author: dave
"""



import numpy as np
import matplotlib.pyplot as plt
import os

num_chunks = 2000

c_r_1 = 0
c_r_2 = num_chunks - 0

header = 9 # unnecessary information in each substructured data


#%%
plt.style.use('fast')
plt.tight_layout()
file_path = './'
file_name = 'S0St.dat'
fname = os.path.join(file_path, file_name)
num_timeframe = 0 # timestep counter to count how many time frames 
data = [] # creating the list for storing the atom position and velocity information
with open(fname, 'r') as fo:
    next(fo)
    next(fo)
    next(fo)
    for line in fo:               
        for n in range(num_chunks):   
            line = next(fo)   
            info = line.split()  
            data.append(info)    
        num_timeframe += 1           

data = np.asfarray(data, dtype=np.float64).reshape(num_timeframe,num_chunks,-1) 

#%%
mean_chunk = np.mean(data[:,c_r_1:c_r_2,0],axis = 0)
vxx = np.mean(data[:,c_r_1:c_r_2,3],axis = 0) # mass
vyy = np.mean(data[:,c_r_1:c_r_2,4],axis = 0) # mass
vzz = np.mean(data[:,c_r_1:c_r_2,5],axis = 0) # mass

vv = ( vxx + vyy + vzz )/3

#%%
time = mean_chunk * 1# fs


vv_nor = vv / vv[0]
plt.plot(time, vv_nor,'-')   

plt.xlabel('time [fs]', fontsize=16)
plt.ylabel('VACF ', fontsize=16)
    
plt.savefig('vacf_vv.png', dpi= 1200, bbox_inches="tight")

