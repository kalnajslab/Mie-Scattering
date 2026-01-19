#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:59:01 2019

@author: kalnajs
"""
import numpy as np
import matplotlib.pyplot as plt #import matplotlib library

file = '/Users/kalnajs/Documents/SAGE III ISS Validation/STM Meeting 2019/POPSExample.txt'
#POPS
pops = np.genfromtxt(file, skip_header = 1)
#LOPC
lopc = np.load('/Users/kalnajs/Documents/SAGE III ISS Validation/STM Meeting 2019/' + 'LOPC_490nm.npy')
#WOPC
mu = 500
sigma = 64 # mean and standard deviation
bins = np.arange(0,2000) 
    
wyo = 7*1/(sigma * np.sqrt(2 * np.pi)) *  np.exp( - (bins - mu)**2 / (2 * sigma**2) )

plt.close(1)
plt.figure(1)
plt.plot(pops[10:,0], pops[10:,1]/np.sum(pops[10:,1]),'r-', label = 'POPS')
plt.plot(lopc[10:240,0], 2.0*lopc[10:240,1]/np.sum(lopc[10:240,1]), 'b-', label = 'LOPC')
plt.plot(bins,wyo,'g-', label = 'WOPC')
plt.xlim([200,2000])
plt.xlabel('Diameter [nm]')
plt.ylabel('Concentration [#/CC]')
plt.title('Instrument Response to 500nm PSL')
plt.legend(loc='upper right')        

plt.show()