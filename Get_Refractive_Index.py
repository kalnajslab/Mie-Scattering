#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:01:12 2019

@author: kalnajs
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter




def pandw(wvl,wts):
    """
    This function loads a table of refractive index vs solution strength for 
    sulfuric acid as described in Palmer and Williams 1975.
    The table is in the file Palmer&Williams_0.36-7.2um.csv A bivariate spline 
    is used to interpolate between table values. 
    wvl = wavelenght in nm
    wp = Sulfuric acid weight percentage (%)
    returns real and imaginary parts of the refractive index
    """
    pandw_table = '/Users/kalnajs/Documents/Python/Mie Scattering/Palmer&Williams/Palmer&Williams_0.36-7.2um.csv'
    pandw = np.genfromtxt(pandw_table,comments='#', delimiter = ',' ) #read the csv file
    pandw_percentages = np.array([25.00,38.00,50.00,75.00,84.50,95.60]) / 100.0 #this is the header with weight percentages
    pandw_wavelengths =  np.flip(pandw[:,0]*1000.0)  #the first column is wavelengths, convert from um to nm
    pandw_real = np.flip(pandw[:,2:14:2],0) #pull out the real parts and flip to match inceasing wl
    pandw_imaginary = np.flip(pandw[:,3:14:2],0) #and the imaginary parts
    
    interp_real = interp.RectBivariateSpline(pandw_wavelengths, pandw_percentages,pandw_real)
    interp_imaginary = interp.RectBivariateSpline(pandw_wavelengths, pandw_percentages,pandw_imaginary)
    
    return interp_real.ev(wvl,wts), interp_imaginary.ev(wvl,wts)


def soln_density(wts,wtn,T):
    """  
    This is the formulation of Luo et al., GRL, 1997 
    for determining the solution density of liquid ternary aerosol (LTA).   It will return 
    the binary solution density for either h2o-h2so4 or h2o-hno3,  by setting the appropriate wt fraction=0
        
    t   = temp in K
    wts = wt. fraction h2so4 
    wtn = wt. fraction hno3 
    """
    
    x=[2.393284E-02,-4.359335E-05,7.961181E-08,0.0,-0.198716351,         
    1.39564574E-03,-2.020633E-06,0.51684706,-3.0539E-03,4.505475E-06, 
    -0.30119511,1.840408E-03,-2.7221253742E-06,-0.11331674116,        
    8.47763E-04,-1.22336185E-06,0.3455282,-2.2111E-03,3.503768245E-06,
    -0.2315332,1.60074E-03,-2.5827835E-06]
    
    w   = wts+wtn
    wth = 1.0 - w
    v1  = x[0] +x[1] *T +x[2] *T**2 +x[3]*T**3
    vs  = x[4] +x[5] *T +x[6] *T**2 +(x[7]+x[8]*T+x[9]*T**2)*w +(x[10] +x[11] *T +x[12] *T**2) *w *w
    vn  = x[13] +x[14] *T +x[15] * T**2 +(x[16] +x[17] *T +x[18] *T**2) *w +(x[19] +x[20] *T +x[21] *T**2) *w *w
    vmcal = v1*wth/18.016 + vs*wts/98.08 + vn*wtn/63.016
    
    result = 1/vmcal/1000. # g/cm3
    return result

def lorentz_lorenz(m0,T0,T,wtp):
    """
    This function translates refractive indicies to different temperatures based
    on the Lorentz-Lorenz equation.
    Input:
        m0: the known refractive index at T0
        T: the new temperature
        wtp: the sulfate weight fraction
    Returns the new refractive index
    """
    
    A = (m0**2 - 1.0)/((m0**2 + 2.0)*soln_density(wtp,0,T0))
    m = ((1.0 + 2 * A * soln_density(wtp,0,T))/(1.0 -  A*soln_density(wtp,0,T)))**0.5
    
    return m

def sulfate_wtp(press,T,H2Ovmr):
    
    pp     = np.log(press * (H2Ovmr * 1.e-6) )
    top    = (-14.458 + 0.62456 * pp) * T + 3565.0
    bot    = 44.777 + 1.3204 * pp - 0.19988 * T
    result = top / bot

    return result
     
      
def refractive_indx(wvl,T,P,H2Ovmr):
    
    wtp = sulfate_wtp(P,T,H2Ovmr)
    m, k = pandw(wvl,wtp)
    m_corrected = lorentz_lorenz(m,300,T,wtp)
    
    return m_corrected



wvl = 702.0 #wavelength in nm
wp = 0.50 #weight fraction

print(refractive_indx(wp,300,1013,4))
                