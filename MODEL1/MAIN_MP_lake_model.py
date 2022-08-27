# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:49:04 2019

@author: AntoniaPraetorius

written for Python 3
"""
#Environmental fate and transport model for microplastics (MPs)
#Developed within Nano2Plast project
#Here: Lake version


"""FEATURES: """

""" 
MICROPLASTICS FORMS (x --> size class)
•	A --> pristine (free MP)
•	B --> heteroaggregated (MP attached to suspended particulate matter (SPM))
•	C --> biofiolm-covered (MP with biofilm (BF) layer on surface)
•	D --> biofilm-heteroaggregated (MP with BF layer attached to SPM)

"""

""" 
COMPARTMENTS
- surface (top water layer) (1)
- epilimnion (2)
- hypolimnion (3)
- surface sediment (4)

to add  --> calculate density (&viscosity) based on temperature and salinity)
"""

""" 
MICROPLASTICS CHARACTERISTICS
- composition
- density
- shape
- size --> currently 5 size classes, MP1 to 5
"""

"""
FATE PROCESSES
- settling
- rising
- biofilm formation/aquisition
- heteroaggregation
- aggregate breakup
- fragmentation
- advection
- resuspension
- burial

"""

"""IMPORT MODEDULES/SCRIPTS/CLASSES"""
#import relevant modules
import os
import math
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pandas as pd
from plots import *

from SteadyState import *
from Dynamic_ModelCore import *

from preProcess import preProcessLayers,preProcessElements,preprocessTags

from readInputs import lakeData,dateRangeGenerator,microplasticData, processData, generateFinalDataFrame, processDailyInputData
from datetime import datetime, timedelta

from pathlib import Path
from shutil import rmtree
data_folder = Path("inputs/") #insert folder containing input
data_folder_output = Path("output/smaller_timestep/print/")

#import file storing required constants
from GlobalConstants import *


#import classes to generate objects
#from Particulates import Particulates #class to generate MP and SPM objects
#from ParticulatesBF import ParticulatesBF #class to generate MP and SPM objects
#from ParticulatesSPM import ParticulatesSPM #class to generate MP and SPM objects

#from EnvCompartment import EnvCompartment #class to generate environmental 
#compartment objects (water, water surface, sediment)

import RC_Generator 
import fillRCmatrix 

"""DEFINE RUN PARAMETERS"""
#define solver --Y steady state versus time resolved
SOLVER = "Dynamic" #options: SteadyState OR Dynamic
INPUT = "Monthly" #options: Standard OR Monthly (later also Daily)

############## CHANGE HERE THE LENGTH OF SIMULATION AND TIMESTEP
#these values can be modified within the specified conditions: 
t0 = 0 #set starting time of simulation (typically 0)
daysSimulation = 5 #number of days to simulate
stepsize = 60 #define size of the calculation time step, in seconds. !! stepsize needs to be smaller than sec_day !! otherwise, code will not run and error message will be printed
##############

#DO NOT CHANGE THESE VALUES
tmax = 24*60*60*daysSimulation #set final simulation time (in seconds) !! DO NOT CHANGE!!
#min_day = 24*60 #number of minutes in a day !! DO NOT CHANGE !!
sec_day = 24*60*60 #number of seconds in a day !! DO NOT CHANGE !!

#stop code if site of the timestep is too big
if stepsize >= sec_day:
    print ("Error: stepsize too big")
    exit()

t_days = np.linspace(t0, tmax, daysSimulation + 1) #define timespan & time_step, e.g. 1min (min, max, number of elements) !! DO NOT CHANGE
timesteps = int(sec_day/stepsize) #number of simulation steps per day  !! DO NOT CHANGE

#############
date_time_str = '2020-07-01 00:00'
DayStart = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
LastDay = DayStart + timedelta(seconds=tmax)
#########

#set number and names of microplastic forms
MPforms = ["pristine", "heteroaggregated", "biofiolm-covered", "biofilm-heteroaggregated"] #define microplastic forms to be modelled
MPforms_labels = ["A", "B", "C", "D"] #define abbreviations of MP forms (used later for indexing/assigning rate constants)

#set number and names of compartments
compartments = ["surface", "epilimnion", "hypolimnion", "sediment"] #define environmental compartments
compartments_labels = ["1", "2", "3", "4"] #define abbreviations of compartments (used later for indexing/assigning rate constants)
#move into input files and remove also from preProcess

"""READ IN INPUT FILES""" 

compartments_prop = pd.DataFrame(index=compartments, columns = 
                                 ["compType", "depth_m", "length_m", "width_m",
                                  "surfArea_m2", "G", "T_K"])


compartments_prop=generateFinalDataFrame(DayStart, LastDay, INPUT, data_folder)

microplasticFile = data_folder / "microplastics_PA.txt"
plastic_prop = microplasticData(microplasticFile)
#currently also contains SPM properties, might need to move those to separate file

processinfoFile = data_folder / "process_info_ep.txt"
process_prop = processData(processinfoFile)
dailyInputData = data_folder / "Input_day_emissions_A2_1e6.csv"
inflow_data = processDailyInputData(dailyInputData)


total_time = 0

[MP1,SPM1,MP1_SPM,MP1_BF,MP1_BF_SPM]=preProcessElements(plastic_prop)
[RateConstants_rowNames, Concentrations_rowNames, Basic_Names, Inflow_rowNames] = preprocessTags()

#rate constant definition
RateConstants = pd.DataFrame(index=RateConstants_rowNames, 
                                 columns=["k_1 (1/s)", "k_2 (1/s)",  "k_3 (1/s)", 
                                          "k_4 (1/s)", "k_5 (1/s)", "k_6 (1/s)", 
                                          "k_7 (1/s)", "k_8 (1/s)", "k_9 (1/s)", 
                                          "k_10 (1/s)"])

Concentrations_t0 = pd.DataFrame(index=Concentrations_rowNames, columns=["number (#/m3)"])
Concentrations_t0.loc[:,:] = 0 #set starting concentration to 0
DynamicResults = Concentrations_t0
dayComputation=DayStart
#clean output directory if it exists
# if os.path.exists(data_folder_output):
#     rmtree(data_folder_output)

#loop on days expressed in seconds
for daySec in range(len(t_days)-1):
    print("Running Day: "+str(dayComputation))
    t0 = t_days[daySec]
    total_time = total_time + sec_day
    if daySec < len(t_days)-1:
        tmax = t_days[daySec+1]-stepsize
    else:
        tmax = t_days[daySec+1]    
    
    [Surface,Epilimnion,Hypolimnion,Sediment] = preProcessLayers(INPUT,compartments_prop, dayComputation)


    #Dataframes for storing starting concentrations and rate constants for all possible species
    #Concentrations_tO = pd.DataFrame(index=Concentrations_rowNames, columns=["number (#/m3)", "mass (mg/L)"])


    #set inflow
    inflow_vector = pd.DataFrame(index=Inflow_rowNames, columns=["number (#/m3)"])
    inflow_vector.loc[:,:] = 0
    dayFound = False
    # Iterate over the sequence of column names
    for column in inflow_data:
   # Select column contents by column name using [] operator
        columnSeriesObj = inflow_data[column]
        if column=="Compartment": 
            layer_vector = columnSeriesObj.values
            continue
        dateInput = datetime.strptime(column, '%Y-%m-%d')
        i=0
        if dateInput.day == dayComputation.day and dateInput.month == dayComputation.month and dateInput.year == dayComputation.year :
             for flow in columnSeriesObj.values:
                inflow_vector.loc[layer_vector[i]] = flow #Assuming the layers are fed in order
                i=i+1
             dayFound = True
             break
    
    if dayFound == False : 
        print("Day input not found using standard emission")
        inflow_vector.loc["I_A2"] = 100 # to be read in from emission files

    #rate constants will be changed daily based on input parameters
        
    RateConstants = fillRCmatrix.fillRCmatrix(RateConstants, MP1, SPM1, MP1_BF, 
                                              MP1_SPM, MP1_BF_SPM, Surface, 
                                              Epilimnion, Hypolimnion, Sediment, 
                                              process_prop)
    

    #solve model in steady state mode
    if SOLVER == "SteadyState":
        q=50 #MPs released to MainWater per second
        SteadyStateResults = SteadyState(MainWater, SurfWater, Sediment, q)

    #solve model dynamically
    elif SOLVER == "Dynamic":

        #these values represents the time emission. In this case there is a constant emission during the time
        #    inflow_1 = [100]
        #list of emission emitted every timespan (here: every hour)
        inflow_vector=inflow_vector/timesteps
        print (inflow_vector)#divide daily inputs over timesteps
        DynamicResults = diffEq(inflow_vector, Concentrations_t0,
                                RateConstants, Concentrations_rowNames, RateConstants_rowNames, 
                                Inflow_rowNames, compartments, MPforms, t0, tmax, 
                                timesteps,dayComputation)
        

        #set up the initial concetration of the following day with the last value coputed on the previous day
        Concentrations_t0 = DynamicResults
        #increment day
        dayComputation=DayStart + timedelta(seconds = total_time)

    else:
        print("Error: incorrect solver selected")
  
 
#Plot the results (uncomment next line to plot results)
finalPlotting(stepsize)
finalPlottingLOG(stepsize) #plot results on log scale

"""
to do:
    -external input files
        MP properties
        lake properties (e.g. monthly) (& think about case study and get that data)
        emission scenarios
    -save results
    -loop to run different scenarios
    - MP size (& type) bins
    - biofilm formation --> and density change
    - different settling modes
    - degradation (different pathway? degradation products as new species?)
    - import measured data and plot against results
    - water density/viscosity vs temperature & salinity
    - different water layers
    - main water to surface water transfer
    - add sources for all data/equations
    - implement uncertainty & sensitivity analysis
    - add mass to number converter
    - option to present results as mass and/or number (& surface area?)
    - make library of MP type vs density
    - make function and automate input matrix formation
"""
