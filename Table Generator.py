#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:12:32 2019

@author: kalnajs
"""

import PyMieScatt as ps
import numpy as np
import time

start = time.time()

w = np.array([449,521,755,869,1021]) #Extinction Wavelengths [nm]
m = np.arange(1.30,1.60,0.01) #Refractive Index
d = np.linspace(250,25000,200) #diameters [nm]

x_dim = int(len(w))
y_dim = int(len(m))
z_dim = int(len(d))

extinction = np.zeros((x_dim,y_dim,z_dim))
scatter = np.zeros((x_dim,y_dim,z_dim))
back_scatter = np.zeros((x_dim,y_dim,z_dim))

x = -1
y = -1
z = -1

for wavelength in w:
    x = x+1
    y = -1
    for r_indx in m:
        y = y+1
        z = -1
        for diam in d:
            z = z+1
            print(wavelength,r_indx,diam)
            print(x,y,z)
            result = ps.MieQ(r_indx,wavelength,diam,asDict=True)
            extinction[x,y,z] = result['Qext']
            scatter[x,y,z] = result['Qsca']
            back_scatter[x,y,z] = result['Qback']

np.save('Extinction Table.npy',extinction)
x = 0
for wavelength in w:
    np.savetxt('Extinction Table at '+str(wavelength)+ '.txt',extinction[x,:,:],fmt = '%.4E',delimiter = ',')

end = time.time()
print('Execution Time: ')
print(end - start)


           


