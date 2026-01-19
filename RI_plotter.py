#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 09:35:01 2026

@author: kalnajs
"""

import numpy as np
import matplotlib.pyplot as plt #import matplotlib library
import Refractive_Index as ri

WVL = 1000


T = np.linspace(190,300)

RIndex_2ppmv, dummy = ri.refractive_index(WVL,T,100,2)
RIndex_5ppmv, dummy = ri.refractive_index(WVL,T,100,5)
RIndex_10ppmv, dummy = ri.refractive_index(WVL,T,100,10)


WeightPercent_2ppmv = ri.sulfate_wtp(100, T, 2)
WeightPercent_5ppmv = ri.sulfate_wtp(100, T, 5)
WeightPercent_10ppmv = ri.sulfate_wtp(100, T, 10)

SolnDensity_2ppmv = ri.soln_density(ri.sulfate_wtp(100, T, 2),0, T)
SolnDensity_5ppmv = ri.soln_density(ri.sulfate_wtp(100, T, 5),0, T)
SolnDensity_10ppmv = ri.soln_density(ri.sulfate_wtp(100, T, 10),0, T)


#Tables from Steele and Hamill 1981

#Table 2
#  K   2      3     5     6     8    10     12    15   20    30
# 190 43.45 37.02 25.85 15.38
# 195 53.96 49.46 42.26 39.35 34.02 29.02 23.13
# 200 60.62 57.51 52.78 50.73 46.93 43.69 40.86 36.89 30.82
# 205 65.57 63.12 59.55 58.11 55.61 53.44 51.44 48.63 44.49 37.71
# 210 69.42 67.42 64.55 63.41 61.47 59.83 58.38 56.46 53.69 48.89
# 215 72.56 70.85 68.45 67.52 65.94 64.62 63.47 61.96 59.83 56.40
# 220 75.17 73.70 71.63 70.83 69.49 68.39 67.43 66.19 64.47 61.75
# 225 77.38 76.09 74.29 73.60 72.44 71.48 70.66 69.60 68.15 65.89
# 230 79.30 78.15 76.56 75.95 74.93 74.10 73.38 72.45 71.19 69.25
# 235 80.99 79.96 78.53 77.98 77.08 76.33 75.70 74.89 73.77 72.07
# 240 82.50 81.56 80.27 79.77 78.96 78.29 77.72 76.99 76.00 74.49
# 245 83.92 83.02 81.83 81.38 80.63 80.02 79.51 78.85 77.95 76.59
# 250 85.32 84.43 83.27 82.84 82.15 81.58 81.11 80.50 79.69 78.45
# 255 86.79 85.85 84.67 84.25 83.57 83.03 82.58 82.02 81.26 80.12
# 260 88.32 87.33 86.10 85.66 84.97 84.44 83.99 83.44 82.72 81.64

# Table 3 
# Temperature (K) H20 partial pressure (nab x 10 -4)
# K 2 3 5 6 8 10 12 15 20 30
# 190 1.410 1.401 1.383 1.365
# 195 1.422 1.416 1.407 1.403 1.396 1,388 1.378
# 200 1.429 1.425 1.419 1.416 1.412 1.408 1.404 1.399 1.389
# 205 1.434 1.431 1.426 1.424 1.421 1.418 1.416 1.412 t.407 1.399
# 210 1.439 1.436 1.432 1.430 1.427 1.425 1.423 1.421 1.417 1.411
# 215 1.442 1.440 1.436 1.435 1.432 1.431 1.429 1.427 1.424 1.420
# 220 1.445 1.443 1.440 1.438 1.436 1.435 1.433 1.432 1.429 1.426
# 225 1.445 1.444 1.442 1.441 1.440 1.438 1.437 1.435 1.433 1.430
# 230 1.445 1.444 1.443 1.443 1.442 1.441 1.440 1.438 t.437 1.434
# 235 1.445 1.444 1.443 1.443 1.442 1.442 1.441 1.441 1.439 1.436
# 240 1.444 1.443 1.443 1.442 1.442 1.441 1.441 1.441 1.440 1.439
# 245 1.443 1.443 1.442 1.442 1.441 1.441 1.441 1.440 1.440 1.439
# 250 1.442 1.442 1.441 1.441 1.441 1.440 1.440 1.440 1.439 1,439
# 255 1.440 1.440 1.440 1.440 1.440 1.440 1.439 1.439 1,439 1.438
# 260 1.439 1.439 1.439 1.439 1.439 1.439 1.439 1.438 1.438 1.437


T_SH = np.arange(190,265,5)
SH_WtPc_2ppmv = np.array([43.45,53.96,60.62,65.57,69.42,72.56,75.17,77.38,79.30,80.99,82.50,83.92,85.32,86.79,88.32])
SH_WtPc_5ppmv = np.array([25.85,42.26,52.78,59.55,64.55,68.45,71.63,74.29,76.56,78.53,80.27,81.83,83.27,84.67,86.10])
SH_WtPc_10ppmv = np.array([34.02,46.93,55.61,61.47,65.94,69.49,72.44,74.93,77.08,78.96,80.63,82.15,83.57,84.97])

SH_RI_2ppmv = np.array([1.410,1.422,1.429,1.434,1.439,1.442,1.445,1.445,1.445,1.445,1.444,1.443,1.442,1.440,1.439])
SH_RI_5ppmv = np.array([1.383,1.407,1.419,1.426,1.432,1.436,1.440,1.442,1.443,1.443,1.443,1.442,1.441,1.440,1.439])
SH_RI_10ppmv = np.array([1.388,1.408,1.418,1.425,1.431,1.435,1.438,1.441,1.442,1.441,1.441,1.440,1.440,1.439])

plt.close('all')

#Weight Percentage
plt.figure(1)
plt.plot(T,WeightPercent_2ppmv/100.0,'k.',label = '0.0002pp_wv_hPa')
plt.plot(T,WeightPercent_5ppmv/100.0,'k-',label = '0.0005pp_wv_hPa')
plt.plot(T,WeightPercent_10ppmv/100.0,'k--',label = '0.00010pp_wv_hPa')

#plt.plot(T_SH,SH_WtPc_2ppmv/100.0,'g.', label = 'S&H Table2 2 ppmv')
plt.plot(T_SH,SH_WtPc_5ppmv/100.0,'g-', label = 'S&H Table2 5 ppmv')
#plt.plot(T_SH[1:],SH_WtPc_10ppmv/100.0,'g--', label = 'S&H Table2 5 ppmv')

plt.ylim(0.2,1.0)
plt.xlabel('Temperature (k)')
plt.ylabel('Weight Fraction H2SO4')
plt.grid('both')
plt.title(str(WVL) + 'nm')
plt.legend()

#Solution Density
plt.figure(2)
plt.plot(T,SolnDensity_2ppmv,'k.',label = '0.0002pp_wv_hPa')
plt.plot(T,SolnDensity_5ppmv,'k-',label = '0.0005pp_wv_hPa')
plt.plot(T,SolnDensity_10ppmv,'k--',label = '0.00010pp_wv_hPa')
plt.ylim(1.0,2.0)
plt.xlabel('Temperature (k)')
plt.ylabel('Solution Density (g/cc)')
plt.grid('both')
plt.title(str(WVL) + 'nm')
plt.legend()

#Refrctive Index
plt.figure(3)
plt.plot(T,RIndex_2ppmv,'k.',label = '0.0002pp_wv_hPa')
plt.plot(T,RIndex_5ppmv,'k-',label = '0.0005pp_wv_hPa')
plt.plot(T,RIndex_10ppmv,'k--',label = '0.00010pp_wv_hPa')

plt.plot(T_SH, SH_RI_2ppmv, 'g.', label = 'S&H Table 3 2ppmV')
plt.plot(T_SH, SH_RI_5ppmv, 'g-', label = 'S&H Table 3 5ppmV')
plt.plot(T_SH[1:], SH_RI_10ppmv, 'g--', label = 'S&H Table 3 10ppmV')

plt.ylim(1.3,1.5)
plt.xlabel('Temperature (k)')
plt.ylabel('Real Index of Refraction')
plt.grid('both')
plt.title(str(WVL) + 'nm')
plt.legend()


#Recreate Figure 3 from Luo et al:
P = 55
vmr = 5
T = np.linspace(185,210)

RI_360, wtp = ri.refractive_index(360, T, P, vmr)
RI_532, wtp = ri.refractive_index(532, T, P, vmr)
RI_2000, wtp = ri.refractive_index(2000, T, P, vmr)

plt.figure(4)

plt.subplot2grid((3,1),(0,0),rowspan =2)
plt.plot(T,RI_360,'k.', label = '360nm')
plt.plot(T,RI_532,'k-', label = '532nm')
plt.plot(T,RI_2000,'k--', label = '2000nm')
plt.legend()
plt.ylabel('Refractive Index')
plt.ylim(1.32,1.47)
plt.xlim(185,210)
plt.title('Luo et al., 1996 Figure 3 - H2SO4 only at 55mbar')

plt.subplot2grid((3,1),(2,0))
plt.plot(T,wtp,'k', label = '360nm')
plt.xlim(185,210)
plt.ylabel('Concnetration [wt%]')
plt.xlabel('T [K]')
