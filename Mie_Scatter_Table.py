#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:12:32 2019

@author: kalnajs
"""

import PyMieScatt as ps
import numpy as np


#Input: Wavelenghts and particle diameters are in nm
#Output: is extinction cross section in nm2

#wvl = np.array([521,1021])
#r_indx = np.array([1.4,1.45,1.5])
#diam = np.arange(0.3,10,20)

def make_table(wvl,r_indx,diam):
    x_dim = int(len(wvl))
    y_dim = int(len(r_indx))
    z_dim = int(len(diam))
    
    extinction = np.zeros((x_dim,y_dim,z_dim))
    scatter = np.zeros((x_dim,y_dim,z_dim))
    back_scatter = np.zeros((x_dim,y_dim,z_dim))
    x = -1
    y = -1
    z = -1
    cnt = 0
    
    for wavelength in wvl:
        x = x+1
        y = -1
        for ri in r_indx:
            y = y+1
            z = -1
            for d in diam:
                z = z+1
                #print(str(cnt) + ' ' + str(ri) + ' ' + str(wavelength) + ' ' + str(d))
                cext, csca, cabs, g, cpr, cback, cratio = ps.MieQ(ri,wavelength,d, asCrossSection=False) # returns cross section in nm2
                extinction[x,y,z] = cext
                scatter[x,y,z] = csca
                back_scatter[x,y,z] = cback
                cnt = cnt+1
    
    print("Calculating MieQ: " + str(cnt))
    return extinction, scatter, back_scatter

   




           


