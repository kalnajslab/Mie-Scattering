
import PyMieScatt as ps
import numpy as np
import matplotlib.pyplot as plt

ri = 1.55  # Real part of refractive index
wvl = 780  # Wavelength in nm

diams = np.linspace(300, 2500, 10)  # Particle diameters from 10 nm to 500 nm

cext_list = []
csca_list = []
cratio_list = []

for d in diams:
    cext, csca, cabs, g, cpr, cback, cratio = ps.MieQ(ri, wvl, d, asCrossSection=False)
    cext_list.append(cext)
    csca_list.append(csca)
    cratio_list.append(cratio)

#cext, csca, cabs, g, cpr, cback, cratio = ps.MieQ(ri,wvl,d, asCrossSection=False) # returns cross section in nm2

plt.close('all')
#plt.plot(diams, cext_list, 'o-', label='Cext')
#plt.plot(diams, csca_list, 's--', label='Csca')
plt.plot(diams, cratio_list, '^-', label='Cratio')
plt.legend()
plt.xlabel('Particle Diameter (nm)')
plt.ylabel('Extinction Cross Section (nm²)')
plt.show()

