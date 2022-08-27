# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:02:31 2019

@author: AntoniaPraetorius
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Initialization import Initialization
from PlotResults import *
import pandas as pd
import os


     
def diffEq(inflow_vector, Conc0, RateConstants, 
           Concentrations_rowNames, RateConstants_rowNames, 
           Inflow_rowNames, compartments, MPforms, t0, 
           tmax, timesteps,dayComputation):

    
    Conc = Conc0
    
    d_Conc_dt = Conc0

    RC = RateConstants

    from pathlib import Path
    data_folder = Path("output/smaller_timestep/print")
    
    Concentrations_finalC_A1 = []
    Concentrations_finalC_B1 = [] 
    Concentrations_finalC_C1 = []  
    Concentrations_finalC_D1 = []  
    Concentrations_finalC_A2 = []         
    Concentrations_finalC_B2 = [] 
    Concentrations_finalC_C2 = [] 
    Concentrations_finalC_D2 = [] 
    Concentrations_finalC_A3 = [] 
    Concentrations_finalC_B3 = [] 
    Concentrations_finalC_C3 = [] 
    Concentrations_finalC_D3 = [] 
    Concentrations_finalC_A4 = [] 
    Concentrations_finalC_B4 = []  
    Concentrations_finalC_C4 = [] 
    Concentrations_finalC_D4 = [] 


    #fill concentrations_final data frame with empty lists
    #https://stackoverflow.com/questions/37415118/pandas-initialize-dataframe-column-cells-as-empty-lists/37415407
    

    emission_size=len(inflow_vector.columns)
    for w in range(emission_size):
        def dCdt(C, t):
            Conc_C_A1, Conc_C_B1, Conc_C_C1, Conc_C_D1, \
            Conc_C_A2, Conc_C_B2, Conc_C_C2, Conc_C_D2, \
            Conc_C_A3, Conc_C_B3, Conc_C_C3, Conc_C_D3, \
            Conc_C_A4, Conc_C_B4, Conc_C_C4, Conc_C_D4\
             = C
             
                        
            #system of differential equations 
            
            for SpC in range(len(Concentrations_rowNames)):
                rowi=16*SpC
                rowf=rowi+15
                i=0
                dQ = 0 
                for RCN in range(rowi,rowf):
                    dQ = dQ + RC.loc[RateConstants_rowNames[RCN]].sum()*C[i]
                    i=i+1
    #                    
                d_Conc_dt.loc[Concentrations_rowNames[SpC]]=dQ + inflow_vector.loc[Inflow_rowNames[SpC]]#[w]

            return [d_Conc_dt.iloc[0][0], d_Conc_dt.iloc[1][0], d_Conc_dt.iloc[2][0], d_Conc_dt.iloc[3][0],
                    d_Conc_dt.iloc[4][0], d_Conc_dt.iloc[5][0], d_Conc_dt.iloc[6][0], d_Conc_dt.iloc[7][0],
                    d_Conc_dt.iloc[8][0], d_Conc_dt.iloc[9][0], d_Conc_dt.iloc[10][0], d_Conc_dt.iloc[11][0],
                    d_Conc_dt.iloc[12][0], d_Conc_dt.iloc[13][0], d_Conc_dt.iloc[14][0], d_Conc_dt.iloc[15][0]]

        
        # Create time domain
        t_span = np.linspace(t0, tmax, timesteps + 1) #define timespan & time_step, e.g. 1min (min, max, number of elements)  The plus one is important
        
        
        Czero = [Conc0.iloc[0][0], Conc0.iloc[1][0], Conc0.iloc[2][0], Conc0.iloc[3][0], 
                Conc0.iloc[4][0], Conc0.iloc[5][0], Conc0.iloc[6][0], Conc0.iloc[7][0], 
                Conc0.iloc[8][0], Conc0.iloc[9][0], Conc0.iloc[10][0], Conc0.iloc[11][0], 
                Conc0.iloc[12][0], Conc0.iloc[13][0], Conc0.iloc[14][0], Conc0.iloc[15][0]]
       
        #initial conditions

        solution = odeint(dCdt, Czero, t_span)
        #https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html
        #https://stackoverflow.com/questions/51808922/how-to-solve-a-system-of-differential-equations-using-scipy-odeint
        
        #store results of last run
        Conc0.loc["C_A1"] = solution[int(timesteps-1), 0]
        Conc0.loc["C_B1"] = solution[int(timesteps-1), 1]
        Conc0.loc["C_C1"] = solution[int(timesteps-1), 2]
        Conc0.loc["C_D1"] = solution[int(timesteps-1), 3]
        Conc0.loc["C_A2"] = solution[int(timesteps-1), 4]
        Conc0.loc["C_B2"] = solution[int(timesteps-1), 5]
        Conc0.loc["C_C2"] = solution[int(timesteps-1), 6]
        Conc0.loc["C_D2"] = solution[int(timesteps-1), 7]
        Conc0.loc["C_A3"] = solution[int(timesteps-1), 8]
        Conc0.loc["C_B3"] = solution[int(timesteps-1), 9]
        Conc0.loc["C_C3"] = solution[int(timesteps-1), 10]
        Conc0.loc["C_D3"] = solution[int(timesteps-1), 11]
        Conc0.loc["C_A4"] = solution[int(timesteps-1), 12]
        Conc0.loc["C_B4"] = solution[int(timesteps-1), 13]
        Conc0.loc["C_C4"] = solution[int(timesteps-1), 14]
        Conc0.loc["C_D4"] = solution[int(timesteps-1), 15]

        
#        #concatenate results to results from previous run(s)        
        Concentrations_finalC_A1 = Concentrations_finalC_A1+solution[:, 0].tolist()
        Concentrations_finalC_B1 = Concentrations_finalC_B1+solution[:, 1].tolist()
        Concentrations_finalC_C1 = Concentrations_finalC_C1+solution[:, 2].tolist()
        Concentrations_finalC_D1 = Concentrations_finalC_D1+solution[:, 3].tolist()
        Concentrations_finalC_A2 = Concentrations_finalC_A2+solution[:, 4].tolist()
        Concentrations_finalC_B2 = Concentrations_finalC_B2+solution[:, 5].tolist()
        Concentrations_finalC_C2 = Concentrations_finalC_C2+solution[:, 6].tolist()
        Concentrations_finalC_D2 = Concentrations_finalC_D2+solution[:, 7].tolist()
        Concentrations_finalC_A3 = Concentrations_finalC_A3+solution[:, 8].tolist()
        Concentrations_finalC_B3 = Concentrations_finalC_B3+solution[:, 9].tolist()
        Concentrations_finalC_C3 = Concentrations_finalC_C3+solution[:, 10].tolist()
        Concentrations_finalC_D3 = Concentrations_finalC_D3+solution[:, 11].tolist()
        Concentrations_finalC_A4 = Concentrations_finalC_A4+solution[:, 12].tolist()
        Concentrations_finalC_B4 = Concentrations_finalC_B4+solution[:, 13].tolist()
        Concentrations_finalC_C4 = Concentrations_finalC_C4+solution[:, 14].tolist()
        Concentrations_finalC_D4 = Concentrations_finalC_D4+solution[:, 15].tolist()
        
#save results on file
    date =str(dayComputation.year)+"-"+str('%02d' % dayComputation.month)+"-"+str('%02d' % dayComputation.day)
    output_vector = pd.DataFrame(index=Concentrations_rowNames, columns = t_span)
    output_vector.loc["C_A1"] = Concentrations_finalC_A1
    output_vector.loc["C_B1"] = Concentrations_finalC_B1
    output_vector.loc["C_C1"] = Concentrations_finalC_C1
    output_vector.loc["C_D1"] = Concentrations_finalC_D1 
    output_vector.loc["C_A2"] = Concentrations_finalC_A2                
    output_vector.loc["C_B2"] = Concentrations_finalC_B2
    output_vector.loc["C_C2"] = Concentrations_finalC_C2
    output_vector.loc["C_D2"] = Concentrations_finalC_D2 
    output_vector.loc["C_A3"] = Concentrations_finalC_A3
    output_vector.loc["C_B3"] = Concentrations_finalC_B3
    output_vector.loc["C_C3"] = Concentrations_finalC_C3 
    output_vector.loc["C_D3"] = Concentrations_finalC_D3
    output_vector.loc["C_A4"] = Concentrations_finalC_A4
    output_vector.loc["C_B4"] = Concentrations_finalC_B4
    output_vector.loc["C_C4"] = Concentrations_finalC_C4 
    output_vector.loc["C_D4"] = Concentrations_finalC_D4
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)
    outputfile = str(data_folder)+ "/"+date+"_equal_properties_L2.csv"
    output_vector.T.to_csv(outputfile)


##No Graph for now

   # t_span_final = np.linspace(0, tmax*emission_size, timesteps*emission_size)

    # PlotResultsLogY(Concentrations_finalC_A1, Concentrations_finalC_B1,
    #             Concentrations_finalC_C1, Concentrations_finalC_D1,
    #             Concentrations_finalC_A2, Concentrations_finalC_B2, 
    #             Concentrations_finalC_C2, Concentrations_finalC_D2,
    #             Concentrations_finalC_A3, Concentrations_finalC_B3, 
    #             Concentrations_finalC_C3, Concentrations_finalC_D3, 
    #             Concentrations_finalC_A4, Concentrations_finalC_B4, 
    #             Concentrations_finalC_C4, Concentrations_finalC_D4, 
    #             t_span_final, compartments, MPforms)

    return Conc0



