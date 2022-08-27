# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:06:35 2020

@author: AntoniaPraetorius
"""

from Particulates import Particulates #import class to generate MP and SPM objects
import pandas as pd 
from pathlib import Path
import sys
import datetime

from EnvCompartment import EnvCompartment #class to generate environmental 

#import file storing required constants
from GlobalConstants import *


#import classes to generate objects
from Particulates import Particulates #class to generate MP and SPM objects
from ParticulatesBF import ParticulatesBF #class to generate MP and SPM objects
from ParticulatesSPM import ParticulatesSPM #class to generate MP and SPM objects



#set number and names of compartments
compartments = ["surface", "epilimnion", "hypolimnion", "sediment"] #define environmental compartments
compartments_labels = ["1", "2", "3", "4"] #define abbreviations of compartments (used later for indexing/assigning rate constants)

MPforms_labels = ["A", "B", "C", "D"] #define abbreviations of MP forms (used later for indexing/assigning rate constants)



#function to read lake data
def preProcessLayers(mode,compartments_prop, date):
    try:
        df= pd.DataFrame()
        if mode =="Standard":
            df = compartments_prop
        elif mode == "Monthly":
            date =str(date.year)+"-"+str('%02d' % date.month)
            compartments_prop.loc[compartments_prop['date'] == date]
            df=compartments_prop
            
        Surface = EnvCompartment(compartments[0], df["compType"][0], 
                                     density_w_21C_kg_m3, mu_w_21C_kg_ms, 
                                     df["depth_m"][0], 0, 0, 
                                     df["surfArea_m2"][0],          
                                     df["G"][0], df["T_K"][0])
        Epilimnion = EnvCompartment(compartments[1], df["compType"][1], 
                                    density_w_21C_kg_m3, mu_w_21C_kg_ms, 
                                    df["depth_m"][1], 0, 0, 
                                    df["surfArea_m2"][1], 
                                    df["G"][1], df["T_K"][1])
        Hypolimnion = EnvCompartment(compartments[2], df["compType"][2],
                                    density_w_21C_kg_m3, mu_w_21C_kg_ms, 
                                    df["depth_m"][2], 0, 0, 
                                    df["surfArea_m2"][2], 
                                    df["G"][2], df["T_K"][2])
        Sediment = EnvCompartment(compartments[3], df["compType"][3], 
                                  density_w_21C_kg_m3, mu_w_21C_kg_ms, 
                                  df["depth_m"][3], 0, 0, 
                                  df["surfArea_m2"][3], 
                                  df["G"][3], compartments_prop["T_K"][3])
        
        Surface.calc_dimensions() #Compartment 1
        Epilimnion.calc_dimensions() #Compartment 2
        Hypolimnion.calc_dimensions() #Compartment 3
        Sediment.calc_dimensions() #Compartment 4
        
    except:    
        print("Error in data Preparation")
        sys.exit(1)  

    return Surface, Epilimnion, Hypolimnion, Sediment  

def preProcessElements(plastic_prop):
    #generate MicroPlastic object(s) --> A: pristine (free MP)
    
    MP_index = 0 #currently only runnign for the first MP in the list

    MP1= Particulates(plastic_prop, MP_index)
    MP1.calc_volume()
        
    #generate SPM object(s)
    SPM_index = 3 #need to move SPM in own input file
    SPM1 = Particulates(plastic_prop, SPM_index)
    SPM1.calc_volume()
    SPM1.calc_numConc(50, 0) #move this to lake input file
    #SPM1.calc_settling(density_w_21C_kg_m3, mu_w_21C_kg_ms, g_m_s2, "Stokes")
    
    #B: heteroaggregated (MP attached to suspended particulate matter (SPM)) 
    MP1_SPM = ParticulatesSPM("MP1-SPM", MP1, SPM1) 
    MP1_SPM.calc_volume(MP1, SPM1)
    #MP1_SPM.calc_settling()
    
    #C: biofiolm-covered (MP with biofilm (BF) layer on surface)
    MP1_BF = ParticulatesBF("MP1-BF", MP1, 1388, 5e-6) 
    MP1_BF.calc_volume()
    #MP1_BF.calc_settling()

    #D: biofilm-heteroaggregated (MP with BF layer attached to SPM)
    MP1_BF_SPM = ParticulatesSPM("MP1-BF-SPM", MP1_BF, SPM1) 
    MP1_BF_SPM.calc_volume(MP1_BF, SPM1)
    #MP1_BF_SPM.calc_settling()
    
    return MP1,SPM1,MP1_SPM,MP1_BF,MP1_BF_SPM


def preprocessTags():
    
    SPECIES = pd.DataFrame(index=MPforms_labels, columns=compartments_labels)
    RateConstants_rowNames = []
    Concentrations_rowNames = []
    Basic_Names=[]
    Inflow_rowNames=[] #names for inflow vector

    for cmp in range(len(compartments_labels)): 
        for mp in range(len(MPforms_labels)):   
            columnName = compartments_labels[cmp]
            SPECIES[columnName][mp] = MPforms_labels[mp]+compartments_labels[cmp]
            Basic_Names.append(SPECIES[columnName][mp])

    #create a list of the names of all species to store concentrations
    for cmp in range(len(compartments_labels)): 
        for mp in range(len(MPforms_labels)):   
            columnName = compartments_labels[cmp]
            SPECIES[columnName][mp] = MPforms_labels[mp]+compartments_labels[cmp]
            simpleindex = "C_" + SPECIES[columnName][mp]
            Concentrations_rowNames.append(simpleindex)
        
            #inflow vector rownames
            simpleindex2 = "I_" + SPECIES[columnName][mp]
            Inflow_rowNames.append(simpleindex2)

    #        for w in range(len(Basic_Names)):
    #           doubleindex = "k_" + SPECIES[columnName][mp] + "-" + Basic_Names[w]
    #           RateConstants_rowNames.append(doubleindex)

    #create a list of rate constants for the species
    for w in range(len(Basic_Names)):
        for sp in range(len(Concentrations_rowNames)):   
            doubleindex = "k_" + Basic_Names[sp] + "-" + Basic_Names[w] 
            RateConstants_rowNames.append(doubleindex)
            
    return RateConstants_rowNames, Concentrations_rowNames, Basic_Names, Inflow_rowNames          