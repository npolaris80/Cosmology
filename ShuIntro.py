import math

# Astro constants in cgs
psc = 3.09e19       # parsecs in cm
H0 = 70/psc         # Hubbles constant
G = 6.674e-8        # Graviational constant
Msun = 1.989e33     # Solar mass in gm
ltyr = 7.096e18     # light year in cm



# Newtonian cosmology

# 15.1 density of universe (units in cgs)
rho_crit = 3*(H0**2)/(8*math.pi*G)

r_local_group = 7.5e6 * ltyr
m_local_group = (4e11)*Msun
rho_local_group = m_local_group/((4/3)*math.pi*(r_local_group**3))

print('rho_crit {}, rho_local_group {}'.format(rho_crit, rho_local_group))