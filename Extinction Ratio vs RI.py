
import PyMieScatt as ps
import numpy as np
import matplotlib.pyplot as plt

ri_1 = 1.55  # Real part of refractive index
ri_2 = 1.39
wvl = 780  # Wavelength in nm

diams = np.linspace(300, 2500, 10)  # Particle diameters from 10 nm to 500 nm

cext_list = []
csca_list = []
cratio_list_1 = []
cratio_list_2 = []
for d in diams:
    cext, csca, cabs, g, cpr, cback, cratio = ps.MieQ(ri_1, wvl, d, asCrossSection=False)
    cext_2, csca_2, cabs_2, g_2, cpr_2, cback_2, cratio_2 = ps.MieQ(ri_2, wvl, d, asCrossSection=False)
    #cext_list.append(cext)
    #csca_list.append(cscation)
    cratio_list_1.append(cratio)
    cratio_list_2.append(cratio_2)    

#cext, csca, cabs, g, cpr, cback, cratio = ps.MieQ(ri,wvl,d, asCrossSection=False) # returns cross section in nm2

plt.close('all')
#plt.plot(diams, cext_list, 'o-', label='Cext')
#plt.plot(diams, csca_list, 's--', label='Csca')
plt.plot(diams, cratio_list_1, '^-', label='Cratio at ' + str(ri_1))
plt.plot(diams, cratio_list_2, 'v-', label='Cratio at ' + str(ri_2))
plt.legend()
plt.xlabel('Particle Diameter (nm)')
plt.ylabel('Back Scattering Ratio')
plt.title('Extinction and Scattering Cross Sections vs Particle Diameter\nWavelength = ' + str(wvl) + ' nm')
plt.show()

