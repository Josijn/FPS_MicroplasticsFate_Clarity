# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:13:51 2019

@author: AntoniaPraetorius
"""

import math
from GlobalConstants import *


#define environmental compartment class
class EnvCompartment:
    "This is a class to create environmental compartment objects of the lake"
    
    #class attribute
    species = "compartment"
        #constructor
    def __init__(self, name, compType, density_kg_m3, mu_w_kg_ms, depth_m, length_m, width_m, surfArea_m2, G, T_K):
        self.name = name
        self.compType = compType
        self.density_kg_m3 = density_kg_m3
        self.mu_w_kg_ms = mu_w_kg_ms
        self.depth_m = depth_m
        self.length_m = length_m
        self.width_m = width_m
        self.surfArea_m2 = surfArea_m2
        self.G = G
        self.T_K = T_K
 
    
    #methods
    #dimension calculation --> calculates surface area and volume
    def calc_dimensions(self):
        
        if self.surfArea_m2 == 0:
            self.surfArea_m2 = self.length_m*self.width_m 
        else:
            self.surfArea_m2 = self.surfArea_m2
        #calculates surface area (in m2)
        
        self.volume_m3 = self.depth_m*self.surfArea_m2
        #calculates volume (in m3)
        
    #rate constants
    #generate rate constants for transport and transformation processes
    def def_rateConsts(self, MP, SPM, k_B_J_K, alpha, alpha_BF):
                
        if self.compType == "sediment":
            self.k_resusp = 2.3*10**-7/self.depth_m
            self.k_burial = 5.6*10**-7/self.depth_m
            #self.k_degradation = MP.k_deg_sed
            #for the sediment compartment rate constants for resuspension and
            #burial in deep sediment are calculated & degradation rate assigned

        
        else:
            #for the water and surface water compartments:
            #settling and rising rate constants for free MP
            if MP.vSet_Stokes_m_s > 0:
                self.k_set_Stokes_MP = MP.vSet_Stokes_m_s/self.depth_m
                self.k_rise_Stokes_MP = 0
            
            elif MP.vSet_Stokes_m_s < 0:
                self.k_set_Stokes_MP = 0
                self.k_rise_Stokes_MP = -MP.vSet_Stokes_m_s/self.depth_m
            
            else:
                self.k_set_Stokes_MP = 0
                self.k_rise_Stokes_MP = 0
                
            #settling and rising rate constants for MP bound to SPM 
            #!! preliminary calculations, to be improved !!
            
            
            BF_thickness_m = 5*10**-6 #assuming a biofilm thickness of 5 um (very roughly estimated from algae volum in Kooi et al, to be refined!!)
            BF_density_kg_m3 = 1388 #from Kooi et al
            
            equiv_radius_MPSPM_m = (3*(MP.volume_m3+SPM.volume_m3)/(4*math.pi))**(1/3)
            equiv_radius_MPBF_m = MP.radius_m + BF_thickness_m #estimated radius of biofilm covered MP 
            MPBF_volume_m3 = 4/3*math.pi*equiv_radius_MPBF_m**3
            equiv_radius_MPBFSPM_m = (3*(MPBF_volume_m3+SPM.volume_m3)/(4*math.pi))**(1/3)

            MPSPM_density_kg_m3 = MP.density_kg_m3*(MP.volume_m3/(MP.volume_m3+SPM.volume_m3))+SPM.density_kg_m3*(SPM.volume_m3/(MP.volume_m3+SPM.volume_m3))
            self.vSet_Stokes_MPSPM_m_s = 2/9*(MPSPM_density_kg_m3-density_w_21C_kg_m3)/mu_w_21C_kg_ms*g_m_s2*(equiv_radius_MPSPM_m)**2
            
            MPBF_density_kg_m3 = (MP.radius_m**3*MP.density_kg_m3 + ((MP.radius_m + BF_thickness_m)**3 - MP.radius_m**3)*BF_density_kg_m3)/((MP.radius_m + BF_thickness_m)**3)
            #equation from Kooi et al for density
            self.vSet_Stokes_MPBF_m_s = 2/9*(MPBF_density_kg_m3-density_w_21C_kg_m3)/mu_w_21C_kg_ms*g_m_s2*(equiv_radius_MPBF_m)**2

            MPBFSPM_density_kg_m3 = MPBF_density_kg_m3*(MPBF_volume_m3/(MPBF_volume_m3+SPM.volume_m3))+SPM.density_kg_m3*(SPM.volume_m3/(MPBF_volume_m3+SPM.volume_m3))
            self.vSet_Stokes_MPBFSPM_m_s = 2/9*(MPBFSPM_density_kg_m3-density_w_21C_kg_m3)/mu_w_21C_kg_ms*g_m_s2*(equiv_radius_MPBFSPM_m)**2
            
            #settling and rising rate constants for MP bound to SPM 
            if self.vSet_Stokes_MPSPM_m_s > 0:
                self.k_set_Stokes_MPSPM = self.vSet_Stokes_MPSPM_m_s/self.depth_m
                self.k_rise_Stokes_MPSPM = 0
            
            elif self.vSet_Stokes_MPSPM_m_s < 0:
                self.k_set_Stokes_MPSPM = 0
                self.k_rise_Stokes_MPSPM = -self.vSet_Stokes_MPSPM_m_s/self.depth_m
            
            else:
                self.k_set_Stokes_MPSPM = 0
                self.k_rise_Stokes_MPSPM = 0
            
            #settling and rising rate constants for MP covered with biofilm
            if self.vSet_Stokes_MPBF_m_s > 0:
                self.k_set_Stokes_MPBF = self.vSet_Stokes_MPBF_m_s/self.depth_m
                self.k_rise_Stokes_MPBF = 0
            
            elif self.vSet_Stokes_MPBF_m_s < 0:
                self.k_set_Stokes_MPBF = 0
                self.k_rise_Stokes_MPBF = -self.vSet_Stokes_MPBF_m_s/self.depth_m
            
            else:
                self.k_set_Stokes_MPBF = 0
                self.k_rise_Stokes_MPBF = 0

            #settling and rising rate constants for MP covered with biofilm bound to SPM
            if self.vSet_Stokes_MPBFSPM_m_s > 0:
                self.k_set_Stokes_MPBFSPM = self.vSet_Stokes_MPBFSPM_m_s/self.depth_m
                self.k_rise_Stokes_MPBFSPM = 0
            
            elif self.vSet_Stokes_MPBFSPM_m_s < 0:
                self.k_set_Stokes_MPBFSPM = 0
                self.k_rise_Stokes_MPBFSPM = -self.vSet_Stokes_MPBFSPM_m_s/self.depth_m
            
            else:
                self.k_set_Stokes_MPBFSPM = 0
                self.k_rise_Stokes_MPBFSPM = 0


            
            #degradation rate constants
            #if self.compType == "water":
               # self.k_degradation = MP.k_deg_w
                
            #elif self.compType == "surface":
               # self.k_degradation = MP.k_deg_w + MP.k_deg_UV
                #for surface water layer may add 2 rate constants, one for 
                #degradation in water and 1 specific for UV degradation
                #!! if we later implement the transformation products as well
                #we need to keep the rate constants separate!!
               
                      
            #heteroaggregation rate constants
            """heteroaggregation requires to particles to collide and interact
            favorably for the collision to result in attachment
            the heteroaggregation rate constants is therefore composed of two
            parts, 1) a collision rate constant and 2) and attachement 
            efficiency (alpha) (representing the probability of attachement).
            For heteroaggregation a common simplifaction is the assumption that
            SPM concentration is not signficantly affected by the heteroaggre-
            gation process. Therefore, a pseudo first-order heteroaggregation 
            rate constant is obtained by multiplying collision rate with alpha 
            and with the SPM number concentration"""
            
#            #first the different collision mechanisms are calculated
#            k_peri = (2*k_B_J_K*self.T_K)/(3*self.mu_w_kg_ms)*(MP.radius_m + SPM.radius_m)**2/(MP.radius_m * SPM.radius_m)
#            #perikinetic contributions to collision rate constant (Brownian motion)
#            
#            k_ortho = 4/3*self.G*(MP.radius_m + SPM.radius_m)**3
#            #orthokinetic contributions to collision rate constant (caused by fluid motion)
#            
#            k_diffSettling = math.pi*(MP.radius_m + SPM.radius_m)**2 * abs(MP.vSet_Stokes_m_s-SPM.vSet_Stokes_m_s)
#            #differential settling contributions to collision rate constant
#
#            k_coll = k_peri + k_ortho + k_diffSettling
#            #the collision rate constant
#            
#            self.k_hetAgg = alpha*k_coll*SPM.concNum_part_m3
#            #the pseudo first-order heteroaggregation rate constant
#        
            #data is limited on aggregate breakup, but this process is likely
            #more relvant for larger aggregates
            #!! 1/10 of k_hetAgg is just a placeholder,  needs to be refined
            #possibly using a size dependent function !!
            self.k_aggBreakup = 1/10*self.k_hetAgg
     
        
            #for biofilm covered MP       
            #first the different collision mechanisms are calculated
            k_peri = (2*k_B_J_K*self.T_K)/(3*self.mu_w_kg_ms)*(equiv_radius_MPBF_m + SPM.radius_m)**2/(equiv_radius_MPBF_m * SPM.radius_m)
            #perikinetic contributions to collision rate constant (Brownian motion)
            
            k_ortho = 4/3*self.G*(equiv_radius_MPBF_m + SPM.radius_m)**3
            #orthokinetic contributions to collision rate constant (caused by fluid motion)
            
            k_diffSettling = math.pi*(equiv_radius_MPBF_m + SPM.radius_m)**2 * abs(self.vSet_Stokes_MPBF_m_s-SPM.vSet_Stokes_m_s)
            #differential settling contributions to collision rate constant

            k_coll = k_peri + k_ortho + k_diffSettling
            #the collision rate constant
            
            self.k_hetAgg_MPBF = alpha_BF*k_coll*SPM.concNum_part_m3
            #the pseudo first-order heteroaggregation rate constant
        
            #data is limited on aggregate breakup, but this process is likely
            #more relvant for larger aggregates
            #!! 1/10 of k_hetAgg is just a placeholder,  needs to be refined
            #possibly using a size dependent function !!
            self.k_aggBreakup_MPBF = 1/10*self.k_hetAgg_MPBF
      
#            #advective transport
#            #currently  based on assumption of total residence time of lake 
#            #water to be 2 years (Bogdal 2010 lake model)
#            #!! will be revised!!
#            if self.compType == "water":
#                self.k_outflow = self.volume_m3/(2*365*24*60*60) 
#        
#            if self.compType == "surface":
#                self.k_outflow = self.volume_m3/(2*365*24*60*60) 
      
