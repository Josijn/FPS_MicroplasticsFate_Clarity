# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:49:34 2022

@author: josij
"""
import math
import pandas as pd
import numpy as np
from statistics import mean
import sympy as sp
from scipy.integrate import odeint

### calculate the volume of the biofilm

r_pl = 0.00005 # micrometer 
t_bf = 0.000005 
r_tot = r_pl + t_bf

V_tot = (4/3)*math.pi*r_tot**3
V_pl = (4/3)*math.pi*r_pl**3

V_bf = V_tot - V_pl # m**-3

## calculate the number of attatched algae needed to form this biofilm

opp_pl = 4*math.pi*r_pl**2
V_a = 2.0e-16 # volume of an algal cell in m**-3

A_need = (V_bf/opp_pl)/V_a

## make df for the compartments and temperature

scen_comp = ["C1_surf", "C1_epi", "C1_hypo", "C2_surf", "C2_epi", "C2_hypo"]

# T in celcius
d = {'Temperature' : pd.Series([22.2,22.2, 7.2 ,25, 25, 5], index = scen_comp) } 
df = pd.DataFrame(d)

## calculate the encounter kernel rate (m**3/s)
k = 1.38*10**-23 # boltzman in m^2 kg s^-2 K^-1
mu_wat = 0.9764/1000 # viscosity water in kg m^-1 s^-1 (at 21 degrees C) 

# brownian

B_brown =[]
r_a = (V_a/((4/3)*math.pi))**(1/3)
for T in df["Temperature"].tolist():
    D_plastic =( k*(T + 273.16) ) / ( 6*math.pi*mu_wat*r_tot)
    D_algae = ( k*(T + 273.16) ) / ( 6*math.pi*mu_wat*r_a)
    B = 4*math.pi*(D_plastic+D_algae)*(r_tot+r_a)
    B_brown.append(B)

df['B_brown'] = pd.Series(B_brown, index = scen_comp)


# settling
Vs = 2/9*(999-998)/mu_wat*9.81*(r_tot)**2
B_sett = (1/2)*math.pi*r_tot**2*Vs
df['B_sett'] = pd.Series([B_sett,B_sett,B_sett,B_sett,B_sett,B_sett], index = scen_comp)

# shear
shear = 1.7e5/(24*60*60)
df["shear"] = pd.Series([5,5, 1,5,5, 1], index=scen_comp)
B_shear = []

for shear in df["shear"].tolist():
    B_s = 1.3*shear*(r_tot+r_a)**3
    B_shear.append(B)
df['B_shear'] = pd.Series(B_shear, index = scen_comp)

# total encounter kernel rate
B_tot = []

for i in scen_comp:
    B = df.loc[i,"B_brown"]+df.loc[i,"B_sett"]+df.loc[i,"B_shear"]
    B_tot.append(B)

df['B_tot'] = pd.Series(B_tot, index = scen_comp)


## average light intensity


## I_0 in microE/m^2 s
t_I = np.linspace(0,0.5,100)
I_0_t = []
I_m = 1.2e8/(24*60*60)
for i in t_I:
    I = I_m * math.sin(2* math.pi *i)
    I_0_t.append(I)
    
I_0 = mean(I_0_t)


# calculate mean I_z per compartment
z=sp.Symbol('z')

# extinction coefficient
k_scen1 = math.log(10/100)/15
k_scen2 = math.log(10/100)/7

IC1 = I_0 * math.e**(k_scen1*z)
IC2 = I_0 * math.e**(k_scen2*z)

IS1 =float(1/0.005 * sp.integrate(IC1,(z,0,0.005)))
IE1 = float(1/(7.5 - 0.005)* sp.integrate(IC1,(z,0.005,7.5)))
IH1 = float(1/(10.1 - 7.5) * sp.integrate(IC1,(z,7.5,10.1)))

IS2 = float(1/0.005 * sp.integrate(IC2,(z,0,0.005)))
IE2 = float(1/(5 - 0.005)* sp.integrate(IC2,(z,0.005,5)))
IH2 = float(1/(10.1 - 5) * sp.integrate(IC2,(z,5,10.1)))

df['I_z'] = pd.Series([IS1, IE1, IH1, IS2, IE2, IH2], index = scen_comp)  

## for Cyclotella

# mu_opt = mu_max * (I/(I +(mu_max/a))*((I/I_opt)-1)**2)
mu_opt_c = 1.2/(24*60*60)
mu_max = 1.45/(24*60*60)
I = 50
I_opt = 500

a = 1/((1/mu_max)*((I*(mu_max/mu_opt_c)-I)/((I/I_opt)-1)**2))

# optimal growth rate
gr_opt =[]
# mu_max = 1.85/(24*60*60)
# a = 0.12/(24*60*60)
# I_opt = 1.75392e13/(24*60*60)
for Iz in df['I_z'].tolist():
    mu_opt = mu_max* (Iz/(Iz + (mu_max/a)*((Iz/I_opt)-1)**2))
    gr_opt.append(mu_opt)
    
df["mu_opt"] = pd.Series(gr_opt, index=scen_comp)

# temperature influence

T_inf = []
Tmax = 28.7#33.
Tmin = -14.8
Topt =26.4#20.1

for T in df['Temperature'].tolist():
    tau = ( (1*((T-Tmax)*(T-Tmin)**2)))/((Topt-Tmin)*((Topt-Tmin)*(T-Topt)-(Topt-Tmax)*(Topt+Tmin-2*T)) )
    T_inf.append(tau)
    
df["T_inf"]= pd.Series(T_inf, index=scen_comp)

## algal growth rate
AG =[]
for i in scen_comp:
    ag = df.loc[i,'mu_opt'] * (1*df.loc[i, "T_inf"])
    AG.append(ag)
df['AG'] = pd.Series(AG, index = scen_comp)

# ambient algal concentration

# chla to C
chlA = 0.0007 * 1000 # milligram per m^3
C_A =[] # concentration algae per m^3
for i in scen_comp:
    chlA_C = 0.003 + 1.0154*math.e**(0.050*df.loc[i,"Temperature"])*math.e**(-0.059*df.loc[i,"I_z"]/10**6)
    C = chlA/chlA_C
    A_C = 2726e-9/C
   # A_C= 1.38127e-05
    C_A.append(A_C)
df['C_A'] = pd.Series(C_A, index = scen_comp)

## attatched algal growth

def model(A, t, B, Aa, muA, T ):
    mort =0.05/(24*60*60) # per sec
    Q = 2
    R= 0.1/(24*60*60) # per sec
    dAdt = ((12/24)*(B*Aa)/opp_pl + muA*A - mort*A - Q**((T-20)/10)*R*A + (12/24)*(B*Aa)/opp_pl- (mort)*A - Q**((T-20)/10)*(R)*A) ##/(24*60*60)
    return dAdt

## inputs needed to solve
year_sec =365*24*60*60
year_h = 365*24
t = np.linspace(0, year_sec, year_h)
models =[]



for i in scen_comp:
    inputs = [df.loc[i,"B_tot"], df.loc[i,"C_A"], df.loc[i, "AG"], df.loc[i,"Temperature"]]
    A_dAdt = odeint(model, 0,t, args= tuple(inputs))
    
    models.append(A_dAdt)

t_bf_g =[]

for i in models:
    t_biofilm = 0 

    for n in range(len(t)-1):
       
        if i[n]  >= A_need: 
            t_biofilm = t[n]/(24*60*60)
            t_bf_g.append(t_biofilm)
            break
    if t_biofilm == 0:
        t_bf_g.append(t_biofilm)
df['t_bf_growth'] = pd.Series(t_bf_g, index = scen_comp)
 


## calculations influx particles

flux_total = 1e6
SA_total = math.sqrt(480000)*10.105
flux_m2 = flux_total/SA_total

SA_s1 = math.sqrt(480000)*0.005
SA_e1 = math.sqrt(480000)*7.5
SA_h1 = math.sqrt(480000)*2.6

SA_s2 = math.sqrt(480000)*0.005
SA_e2 = math.sqrt(480000)*5
SA_h2 = math.sqrt(480000)*5.1

surface_area =[SA_s1, SA_e1, SA_h1, SA_s2, SA_e2, SA_h2]
flux =[]

for sa in surface_area:
    influx = flux_m2*sa
    flux.append(influx)

print(sum(flux))
    


