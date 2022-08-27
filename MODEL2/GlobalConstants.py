# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:37:08 2019

@author: Antonia Praetorius
"""

#this files stores all constants needed for running the model (i.e. for 
#particulate & environmental compartment objects & calcualting rate processes)

k_B_J_K = 1.38*10**-23 #Boltzmann constant k_B (in J/K)
g_m_s2 = 9.81 #gravitational acceleration on earth (in m/s2)

density_w_21C_kg_m3 = 998 #density of water at 21 degree C (in kg?m2)

mu_w_21C_mPas = 0.9764 #dynamic viscosit of water at 21 degree C (in mPa*s)
mu_w_21C_kg_ms = mu_w_21C_mPas/1000 #dynamic viscosit of water at 21 degree C (in kg/(m*s))



# vset=5.581728799672265e-06
# k7 = vset/7
# k31 = vset/3.1
# k5 = vset/5
# k51 = vset/5.1
# print(k7, k31, k5, k51)

# Cs7 = 100/7
# Cs5 =100/5

# C17 = Cs7 - Cs7*k7
# C15 = Cs5 - Cs5*k5

# C131 =  Cs7*k7*7/3.1
# C151 = Cs5*k5*5/5.1

# C27 = C17- C17*k7
# C25 = C15 - C15*k5
 
# C231 = C131 + C17*k7*7/3.1 - C131*k31
# C251 = C151 + C15*k5*5/5.1 - C151*k51

# Ns12 = C131*k31*5.1
# Ns22 = C151*k51*3.1

# Ns13 = Ns12 + C231*k31*5.1
# Ns23 = Ns22 + C251*k51*3.1