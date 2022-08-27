# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:56:56 2019

@author: AntoniaPraetorius
"""

#file containing functions for particle conversions
#number to mass / mass to number
#creation of size distribution and size bins

import numpy as np
import math


#function to convert mass to number
def mass_to_num(mass_g, volume_m3, density_kg_m3):
    number = mass_g/1000/density_kg_m3/volume_m3
    return number


#function to convert number to mass
def num_to_mass(number, volume_m3, density_kg_m3):
    mass_g = number*volume_m3*density_kg_m3*1000
    return mass_g


def gen_logSD_NP_bins(d_mean_m, num_bins, d_variance):

    size_weights_Array = np.zeros(num_bins, dtype=float)
    support=80000 #integration support of the pdf

    if num_bins == 1:
        d_m_Array = d_mean_m
        #size_weights_Array = []
  
    else:
        sizeRange_Array = np.linspace(1,support,support) #!!define 80000 more specifically
        
        #create lognormal distribution using probability density function (pdf)
        mu = math.log(d_mean_m)-1/2*math.log(1+(d_variance/d_mean_m**2))
        sigma = math.sqrt(math.log(d_variance/d_mean_m**2+1))
        exponent=np.power(-(np.log10(sizeRange_Array)-mu),2)/(2*sigma**2)
        pdf = 1/(sizeRange_Array*sigma*math.sqrt(2*math.pi))*exponent
        
       #add stuff about non-zero pdf? probably not necessary? compare again with matlab NP version
       
       #create size groups of size distribution
        temp=np.around(np.linspace(sizeRange_Array.min(),
                                       sizeRange_Array.max(), num_bins))  
        
        d_m_Array= [(temp[i]+temp[i+1])/2 for i in range(0, len(temp)-1, 1)]

       
       #Extraction of particle concentrations for each NP size
        binUsed=0
        binRanges=np.arange(math.ceil(support/num_bins),support+math.ceil(support/num_bins),math.ceil(support/num_bins))
        
        for iSize in range(support):
            
            if binUsed>num_bins:
                break
            
            if(iSize<binRanges[binUsed]):
                size_weights_Array[binUsed]+=pdf[iSize]
            else:
                binUsed+=1 #increment the bean
                
       
#        for iSize in range(num_bins):
#           aa=(iSize)*math.ceil(rangeX)
#           bb=math.ceil(rangeX*(iSize+1))
#           for counter in range((iSize)*math.ceil(rangeX),math.ceil(rangeX*(iSize+1))):
#               if counter==size_Array:
#                   break
#               
#               size_weights_Array[iSize] += remaining
#               remaining=0
#               if counter<math.ceil(rangeX)*iSize:
#                   size_weights_Array[iSize] = size_weights_Array[iSize]
#                   +pdf[counter]
#               else:
#                   size_weights_Array[iSize] = size_weights_Array[iSize]
#                   +pdf[counter]*(counter-math.floor(rangeX*iSize))     
#                   remaining=pdf[counter]*(1-(counter-math.floor(rangeX*iSize)))
           
           
    return d_m_Array, size_weights_Array

gen_logSD_NP_bins(300,10,2000)


        
    
