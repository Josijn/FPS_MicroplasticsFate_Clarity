# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:01:21 2019

@author: AntoniaPraetorius
"""

#import file storing required constants
from GlobalConstants import *

import RC_Generator 

                                       

def fillRCmatrix(RateConstants, MP1, SPM1, MP1_BF, MP1_SPM, MP1_BF_SPM, Surface, Epilimnion, Mixed_layer,  Hypolimnion, Sediment, process_prop):
##Adjust for volume differences!!!

# for surface to epilimnion - (Surface.volume_m3/Epilimnion.volume_m3)*
# for epilimnion to surface - (Epilimnion.volume_m3/Surface.volume_m3)*
# for epilimnion to mixed_layer - (Epilimnion.volume_m3/Mixed_layer.volume_m3)*
# for mixed_layer to epilimnion - (Mixed_layer.volume_m3/Epilimnion.volume_m3)*
# for mixed_layer to hypolimnion - (Mixed_layer.volume_m3/Hypolimnion.volume_m3)*
# for hypolimnion to mixed_layer - (Hypolimnion.volume_m3/Mixed_layer.volume_m3)*
# for hypolimnion to sediment - (Hypolimnion.volume_m3/Sediment.volume_m3)*:
# for sediment to hypolimnion - (Sediment.volume_m3/Hypolimnion.volume_m3)*



#make resuspension size dependent
#Surface, pristine MP
    RateConstants["k_1 (1/s)"]["k_A1-A1"] = -RC_Generator.degradation(process_prop.t_half_d_A[0]) 
    RateConstants["k_2 (1/s)"]["k_A1-A1"] = -RC_Generator.fragmentation(process_prop.k_frag_d_A[0], MP1.radius_m, MP1.volume_m3, MP1.diameter_um)
    RateConstants["k_3 (1/s)"]["k_A1-A1"] = -RC_Generator.heteroagg(process_prop.alpha_A[0], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Surface.G, Surface.T_K)
    RateConstants["k_4 (1/s)"]["k_A1-A1"] = -RC_Generator.settling(MP1.density_kg_m3, MP1.radius_m, Surface.depth_m, "Stokes")
    RateConstants["k_5 (1/s)"]["k_A1-A1"] = -RC_Generator.advection("surface", Surface.volume_m3)
    RateConstants["k_6 (1/s)"]["k_A1-A1"] = -RC_Generator.mixing(Surface, Epilimnion)
    RateConstants["k_7 (1/s)"]["k_A1-A1"] = -RC_Generator.biofilm(Surface, process_prop)
     
    RateConstants["k_1 (1/s)"]["k_A1-B1"] = RC_Generator.heteroagg(process_prop.alpha_A[0], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Surface.G, Surface.T_K)
    
    RateConstants["k_1 (1/s)"]["k_A1-C1"] = RC_Generator.biofilm(Surface, process_prop)
    
    RateConstants["k_1 (1/s)"]["k_A1-A2"] = RC_Generator.settling(MP1.density_kg_m3, MP1.radius_m, Surface.depth_m, "Stokes")*(Surface.volume_m3/Epilimnion.volume_m3)
    RateConstants["k_2 (1/s)"]["k_A1-A2"] = (Surface.volume_m3/Epilimnion.volume_m3)*RC_Generator.mixing(Surface, Epilimnion)
    
    #Surface, SPM-bound MP
    RateConstants["k_1 (1/s)"]["k_B1-B1"] = -RC_Generator.degradation(process_prop.t_half_d_B[0]) 
    RateConstants["k_2 (1/s)"]["k_B1-B1"] = -RC_Generator.fragmentation(process_prop.k_frag_d_B[0], MP1_SPM.radius_m, MP1_SPM.volume_m3, MP1_SPM.diameter_um)
    RateConstants["k_3 (1/s)"]["k_B1-B1"] = -RC_Generator.settling(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Surface.depth_m, "Stokes")
    RateConstants["k_4 (1/s)"]["k_B1-B1"] = -RC_Generator.advection("surface", Surface.volume_m3)
    RateConstants["k_5 (1/s)"]["k_B1-B1"] = -RC_Generator.mixing(Surface, Epilimnion)
    RateConstants["k_6 (1/s)"]["k_B1-B1"] = -RC_Generator.breakup(process_prop.alpha_A[0], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Surface.G, Surface.T_K)
    
    RateConstants["k_1 (1/s)"]["k_B1-A1"] = RC_Generator.breakup(process_prop.alpha_A[0], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Surface.G, Surface.T_K)
    
    RateConstants["k_1 (1/s)"]["k_B1-B2"] = RC_Generator.settling(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Surface.depth_m, "Stokes")*(Surface.volume_m3/Epilimnion.volume_m3)
    RateConstants["k_2 (1/s)"]["k_B1-B2"] = (Surface.volume_m3/Epilimnion.volume_m3)*RC_Generator.mixing(Surface, Epilimnion)
    
    #Surface, BF-covered MP
    RateConstants["k_1 (1/s)"]["k_C1-C1"] = -RC_Generator.degradation(process_prop.t_half_d_C[0]) 
    RateConstants["k_2 (1/s)"]["k_C1-C1"] = -RC_Generator.fragmentation(process_prop.k_frag_d_C[0], MP1_BF.radius_m, MP1_BF.volume_m3, MP1_BF.diameter_um)
    RateConstants["k_3 (1/s)"]["k_C1-C1"] = -RC_Generator.heteroagg(process_prop.alpha_C[0], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Surface.G, Surface.T_K)
    RateConstants["k_4 (1/s)"]["k_C1-C1"] = -RC_Generator.settling(MP1_BF.density_kg_m3, MP1_BF.radius_m, Surface.depth_m, "Stokes")
    RateConstants["k_5 (1/s)"]["k_C1-C1"] = -RC_Generator.advection("surface", Surface.volume_m3)
    RateConstants["k_6 (1/s)"]["k_C1-C1"] = -RC_Generator.mixing(Surface, Epilimnion)
    
    RateConstants["k_1 (1/s)"]["k_C1-D1"] = RC_Generator.heteroagg(process_prop.alpha_C[0], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Surface.G, Surface.T_K)
    
    RateConstants["k_1 (1/s)"]["k_C1-C2"] = RC_Generator.settling(MP1_BF.density_kg_m3, MP1_BF.radius_m, Surface.depth_m, "Stokes")*(Surface.volume_m3/Epilimnion.volume_m3)
    RateConstants["k_2 (1/s)"]["k_C1-C2"] = (Surface.volume_m3/Epilimnion.volume_m3)*RC_Generator.mixing(Surface, Epilimnion)
    
    
    #Surface, BF-covered SPM-bound MP
    RateConstants["k_1 (1/s)"]["k_D1-D1"] = -RC_Generator.degradation(process_prop.t_half_d_D[0]) 
    RateConstants["k_2 (1/s)"]["k_D1-D1"] = -RC_Generator.fragmentation(process_prop.k_frag_d_D[0], MP1_BF_SPM.radius_m, MP1_BF_SPM.volume_m3, MP1_BF_SPM.diameter_um)
    RateConstants["k_3 (1/s)"]["k_D1-D1"] = -RC_Generator.settling(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Surface.depth_m, "Stokes")
    RateConstants["k_4 (1/s)"]["k_D1-D1"] = -RC_Generator.advection("surface", Surface.volume_m3)
    RateConstants["k_5 (1/s)"]["k_D1-D1"] = -RC_Generator.mixing(Surface, Epilimnion)
    RateConstants["k_6 (1/s)"]["k_D1-D1"] = -RC_Generator.breakup(process_prop.alpha_C[0], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Surface.G, Surface.T_K)
    
    RateConstants["k_1 (1/s)"]["k_D1-C1"] = RC_Generator.breakup(process_prop.alpha_C[0], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Surface.G, Surface.T_K)
    
    RateConstants["k_1 (1/s)"]["k_D1-D2"] = RC_Generator.settling(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Surface.depth_m, "Stokes")*(Surface.volume_m3/Epilimnion.volume_m3)
    RateConstants["k_2 (1/s)"]["k_D1-D2"] = (Surface.volume_m3/Epilimnion.volume_m3)*RC_Generator.mixing(Surface, Epilimnion)
    
    ###############################################################################
    #Epilimnion, pristine MP
    RateConstants["k_1 (1/s)"]["k_A2-A2"] = -RC_Generator.degradation(process_prop.t_half_d_A[1])
    RateConstants["k_2 (1/s)"]["k_A2-A2"] = -RC_Generator.fragmentation(process_prop.k_frag_d_A[1], MP1.radius_m, MP1.volume_m3, MP1.diameter_um)
    RateConstants["k_3 (1/s)"]["k_A2-A2"] = -RC_Generator.heteroagg(process_prop.alpha_A[1], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Epilimnion.G, Epilimnion.T_K)
    RateConstants["k_4 (1/s)"]["k_A2-A2"] = -RC_Generator.settling(MP1.density_kg_m3, MP1.radius_m, Epilimnion.depth_m, "Stokes")
    RateConstants["k_5 (1/s)"]["k_A2-A2"] = -RC_Generator.advection("water", Epilimnion.volume_m3)
    RateConstants["k_6 (1/s)"]["k_A2-A2"] = -RC_Generator.mixing(Epilimnion, Epilimnion, "up")
    RateConstants["k_7 (1/s)"]["k_A2-A2"] = -RC_Generator.mixing(Epilimnion, Epilimnion, "down") 
    RateConstants["k_8 (1/s)"]["k_A2-A2"] = -RC_Generator.biofilm(Epilimnion, process_prop)
    RateConstants["k_9 (1/s)"]["k_A2-A2"] = -RC_Generator.rising(MP1.density_kg_m3, MP1.radius_m, Epilimnion.depth_m, "Stokes")
    
    RateConstants["k_1 (1/s)"]["k_A2-A1"] = RC_Generator.rising(MP1.density_kg_m3, MP1.radius_m, Epilimnion.depth_m, "Stokes")*Epilimnion.depth_m/Surface.depth_m
    RateConstants["k_2 (1/s)"]["k_A2-A1"] = Epilimnion.depth_m/Surface.depth_m*RC_Generator.mixing(Epilimnion, Epilimnion, "up")
    
    RateConstants["k_1 (1/s)"]["k_A2-A3"] = RC_Generator.settling(MP1.density_kg_m3, MP1.radius_m, Epilimnion.depth_m, "Stokes")*(Epilimnion.volume_m3/Mixed_layer.volume_m3)
    RateConstants["k_2 (1/s)"]["k_A2-A3"] = (Epilimnion.volume_m3/Mixed_layer.volume_m3)*RC_Generator.mixing(Epilimnion, Epilimnion, "down") 
    
    RateConstants["k_1 (1/s)"]["k_A2-B2"] = RC_Generator.heteroagg(process_prop.alpha_A[1], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Epilimnion.G, Epilimnion.T_K)
    
    RateConstants["k_1 (1/s)"]["k_A2-C2"] = RC_Generator.biofilm(Epilimnion, process_prop)
    
    
    #Epilimnion, SPM-bound MP
    RateConstants["k_1 (1/s)"]["k_B2-B2"] = -RC_Generator.degradation(process_prop.t_half_d_B[1]) 
    RateConstants["k_2 (1/s)"]["k_B2-B2"] = -RC_Generator.fragmentation(process_prop.k_frag_d_B[1], MP1_SPM.radius_m, MP1_SPM.volume_m3, MP1_SPM.diameter_um)
    RateConstants["k_3 (1/s)"]["k_B2-B2"] = -RC_Generator.settling(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Epilimnion.depth_m, "Stokes")
    RateConstants["k_4 (1/s)"]["k_B2-B2"] = -RC_Generator.advection("water", Epilimnion.volume_m3)
    RateConstants["k_5 (1/s)"]["k_B2-B2"] = -RC_Generator.mixing(Epilimnion, Epilimnion, "up")
    RateConstants["k_6 (1/s)"]["k_B2-B2"] = -RC_Generator.mixing(Epilimnion, Epilimnion, "down") 
    RateConstants["k_7 (1/s)"]["k_B2-B2"] = -RC_Generator.rising(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Epilimnion.depth_m, "Stokes")
    RateConstants["k_8 (1/s)"]["k_B2-B2"] = -RC_Generator.breakup(process_prop.alpha_A[1], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Epilimnion.G, Epilimnion.T_K)
    
    RateConstants["k_1 (1/s)"]["k_B2-A2"] = RC_Generator.breakup(process_prop.alpha_A[1], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Epilimnion.G, Epilimnion.T_K)
    
    RateConstants["k_1 (1/s)"]["k_B2-B1"] = RC_Generator.rising(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Epilimnion.depth_m, "Stokes")*(Epilimnion.volume_m3/Surface.volume_m3)
    RateConstants["k_2 (1/s)"]["k_B2-B1"] = (Epilimnion.volume_m3/Surface.volume_m3)*RC_Generator.mixing(Epilimnion, Epilimnion, "up")
    
    RateConstants["k_1 (1/s)"]["k_B2-B3"] = RC_Generator.settling(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Epilimnion.depth_m, "Stokes")*(Epilimnion.volume_m3/Mixed_layer.volume_m3)
    RateConstants["k_2 (1/s)"]["k_B2-B3"] = (Epilimnion.volume_m3/Mixed_layer.volume_m3)*RC_Generator.mixing(Epilimnion, Epilimnion, "down")
    
    
    #Epilimnion, BF-covered MP
    RateConstants["k_1 (1/s)"]["k_C2-C2"] = -RC_Generator.degradation(process_prop.t_half_d_C[1]) 
    RateConstants["k_2 (1/s)"]["k_C2-C2"] = -RC_Generator.fragmentation(process_prop.k_frag_d_C[1], MP1_BF.radius_m, MP1_BF.volume_m3, MP1_BF.diameter_um)
    RateConstants["k_3 (1/s)"]["k_C2-C2"] = -RC_Generator.heteroagg(process_prop.alpha_C[1], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Epilimnion.G, Epilimnion.T_K)
    RateConstants["k_4 (1/s)"]["k_C2-C2"] = -RC_Generator.settling(MP1_BF.density_kg_m3, MP1_BF.radius_m, Epilimnion.depth_m, "Stokes")
    RateConstants["k_5 (1/s)"]["k_C2-C2"] = -RC_Generator.advection("water", Epilimnion.volume_m3)
    RateConstants["k_6 (1/s)"]["k_C2-C2"] = -RC_Generator.mixing(Epilimnion, Epilimnion, "up")
    RateConstants["k_7 (1/s)"]["k_C2-C2"] = -RC_Generator.mixing(Epilimnion, Epilimnion, "down") 
    RateConstants["k_8 (1/s)"]["k_C2-C2"] = -RC_Generator.rising(MP1_BF.density_kg_m3, MP1_BF.radius_m, Epilimnion.depth_m, "Stokes")
    
    RateConstants["k_1 (1/s)"]["k_C2-D2"] = RC_Generator.heteroagg(process_prop.alpha_C[1], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Epilimnion.G, Epilimnion.T_K)
    
    RateConstants["k_1 (1/s)"]["k_C2-C1"] = RC_Generator.rising(MP1_BF.density_kg_m3, MP1_BF.radius_m, Epilimnion.depth_m, "Stokes")*(Epilimnion.volume_m3/Surface.volume_m3)
    RateConstants["k_2 (1/s)"]["k_C2-C1"] = (Epilimnion.volume_m3/Surface.volume_m3)*RC_Generator.mixing(Epilimnion, Epilimnion, "up") 
    
    RateConstants["k_1 (1/s)"]["k_C2-C3"] = RC_Generator.settling(MP1_BF.density_kg_m3, MP1_BF.radius_m, Epilimnion.depth_m, "Stokes")*(Epilimnion.volume_m3/Mixed_layer.volume_m3)
    RateConstants["k_2 (1/s)"]["k_C2-C3"] = (Epilimnion.volume_m3/Mixed_layer.volume_m3)*RC_Generator.mixing(Epilimnion, Epilimnion, "down")
    
       
    #Epilimnion, BF-covered SPM-bound MP
    RateConstants["k_1 (1/s)"]["k_D2-D2"] = -RC_Generator.degradation(process_prop.t_half_d_D[1]) 
    RateConstants["k_2 (1/s)"]["k_D2-D2"] = -RC_Generator.fragmentation(process_prop.k_frag_d_D[1], MP1_BF_SPM.radius_m, MP1_BF_SPM.volume_m3, MP1_BF_SPM.diameter_um)
    RateConstants["k_3 (1/s)"]["k_D2-D2"] = -RC_Generator.settling(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Epilimnion.depth_m, "Stokes")
    RateConstants["k_4 (1/s)"]["k_D2-D2"] = -RC_Generator.advection("water", Epilimnion.volume_m3)
    RateConstants["k_5 (1/s)"]["k_D2-D2"] = -RC_Generator.mixing(Epilimnion, Epilimnion, "up")
    RateConstants["k_6 (1/s)"]["k_D2-D2"] = -RC_Generator.mixing(Epilimnion, Epilimnion, "down") 
    RateConstants["k_7 (1/s)"]["k_D2-D2"] = -RC_Generator.rising(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Epilimnion.depth_m, "Stokes")
    RateConstants["k_8 (1/s)"]["k_D2-D2"] = -RC_Generator.breakup(process_prop.alpha_C[1], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Epilimnion.G, Epilimnion.T_K)
    
    RateConstants["k_1 (1/s)"]["k_D2-C2"] = RC_Generator.breakup(process_prop.alpha_C[1], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Epilimnion.G, Epilimnion.T_K)
    
    RateConstants["k_1 (1/s)"]["k_D2-D1"] = RC_Generator.rising(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Epilimnion.depth_m, "Stokes")*(Epilimnion.volume_m3/Surface.volume_m3)
    RateConstants["k_2 (1/s)"]["k_D2-D1"] = (Epilimnion.volume_m3/Surface.volume_m3)*RC_Generator.mixing(Epilimnion, Epilimnion, "up") 
    
    RateConstants["k_1 (1/s)"]["k_D2-D3"] = RC_Generator.settling(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Epilimnion.depth_m, "Stokes")*(Epilimnion.volume_m3/Mixed_layer.volume_m3)
    RateConstants["k_2 (1/s)"]["k_D2-D3"] = (Epilimnion.volume_m3/Mixed_layer.volume_m3)*RC_Generator.mixing(Epilimnion, Epilimnion, "down")
    
    ###############################################################################
    # Mixed layer, pristine MP
    RateConstants["k_1 (1/s)"]["k_A3-A3"] = -RC_Generator.degradation(process_prop.t_half_d_A[2])
    RateConstants["k_2 (1/s)"]["k_A3-A3"] = -RC_Generator.fragmentation(process_prop.k_frag_d_A[2], MP1.radius_m, MP1.volume_m3, MP1.diameter_um)
    RateConstants["k_3 (1/s)"]["k_A3-A3"] = -RC_Generator.heteroagg(process_prop.alpha_A[2], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Mixed_layer.G, Mixed_layer.T_K)
    RateConstants["k_4 (1/s)"]["k_A3-A3"] = -RC_Generator.settling(MP1.density_kg_m3, MP1.radius_m, Mixed_layer.depth_m, "Stokes")
    RateConstants["k_5 (1/s)"]["k_A3-A3"] = -RC_Generator.advection("water", Mixed_layer.volume_m3)
    RateConstants["k_6 (1/s)"]["k_A3-A3"] = -RC_Generator.mixing(Mixed_layer, Epilimnion, "up")
    RateConstants["k_7 (1/s)"]["k_A3-A3"] = -RC_Generator.mixing(Mixed_layer, Epilimnion, "down") 
    RateConstants["k_8 (1/s)"]["k_A3-A3"] = -RC_Generator.biofilm(Mixed_layer, process_prop)
    RateConstants["k_9 (1/s)"]["k_A3-A3"] = -RC_Generator.rising(MP1.density_kg_m3, MP1.radius_m, Mixed_layer.depth_m, "Stokes")
    
    RateConstants["k_1 (1/s)"]["k_A3-A2"] = RC_Generator.rising(MP1.density_kg_m3, MP1.radius_m, Mixed_layer.depth_m, "Stokes") *(Mixed_layer.volume_m3/Epilimnion.volume_m3)
    RateConstants["k_2 (1/s)"]["k_A3-A2"] = (Mixed_layer.volume_m3/Epilimnion.volume_m3)*RC_Generator.mixing(Mixed_layer, Epilimnion, "up")
    
    RateConstants["k_1 (1/s)"]["k_A3-A4"] = RC_Generator.settling(MP1.density_kg_m3, MP1.radius_m, Mixed_layer.depth_m, "Stokes")*(Mixed_layer.volume_m3/Hypolimnion.volume_m3)
    RateConstants["k_2 (1/s)"]["k_A3-A4"] = (Mixed_layer.volume_m3/Hypolimnion.volume_m3)*RC_Generator.mixing(Mixed_layer, Epilimnion, "down") 
    
    RateConstants["k_1 (1/s)"]["k_A3-B3"] = RC_Generator.heteroagg(process_prop.alpha_A[2], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Mixed_layer.G, Mixed_layer.T_K)
    
    RateConstants["k_1 (1/s)"]["k_A3-C3"] = RC_Generator.biofilm(Mixed_layer, process_prop)
    
    
    #mixed_layer, SPM-bound MP
    RateConstants["k_1 (1/s)"]["k_B3-B3"] = -RC_Generator.degradation(process_prop.t_half_d_B[2]) 
    RateConstants["k_2 (1/s)"]["k_B3-B3"] = -RC_Generator.fragmentation(process_prop.k_frag_d_B[2], MP1_SPM.radius_m, MP1_SPM.volume_m3, MP1_SPM.diameter_um)
    RateConstants["k_3 (1/s)"]["k_B3-B3"] = -RC_Generator.settling(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Mixed_layer.depth_m, "Stokes")
    RateConstants["k_4 (1/s)"]["k_B3-B3"] = -RC_Generator.advection("water", Mixed_layer.volume_m3)
    RateConstants["k_5 (1/s)"]["k_B3-B3"] = -RC_Generator.mixing(Mixed_layer, Epilimnion, "up")
    RateConstants["k_6 (1/s)"]["k_B3-B3"] = -RC_Generator.mixing(Mixed_layer, Epilimnion, "down") 
    RateConstants["k_7 (1/s)"]["k_B3-B3"] = -RC_Generator.rising(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Mixed_layer.depth_m, "Stokes")
    RateConstants["k_8 (1/s)"]["k_B3-B3"] = -RC_Generator.breakup(process_prop.alpha_A[2], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Mixed_layer.G, Mixed_layer.T_K)
    
    RateConstants["k_1 (1/s)"]["k_B3-A3"] = RC_Generator.breakup(process_prop.alpha_A[2], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Mixed_layer.G, Mixed_layer.T_K)
    
    RateConstants["k_1 (1/s)"]["k_B3-B2"] = RC_Generator.rising(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Mixed_layer.depth_m, "Stokes")*(Mixed_layer.volume_m3/Epilimnion.volume_m3)
    RateConstants["k_2 (1/s)"]["k_B3-B2"] = (Mixed_layer.volume_m3/Epilimnion.volume_m3)*RC_Generator.mixing(Mixed_layer, Epilimnion, "up")
    
    RateConstants["k_1 (1/s)"]["k_B3-B4"] =  RC_Generator.settling(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Mixed_layer.depth_m, "Stokes")*(Mixed_layer.volume_m3/Hypolimnion.volume_m3)
    RateConstants["k_2 (1/s)"]["k_B3-B4"] = (Mixed_layer.volume_m3/Hypolimnion.volume_m3)*RC_Generator.mixing(Mixed_layer, Epilimnion, "down")
    
    
    #Mixed_layer, BF-covered MP
    RateConstants["k_1 (1/s)"]["k_C3-C3"] = -RC_Generator.degradation(process_prop.t_half_d_C[2]) 
    RateConstants["k_2 (1/s)"]["k_C3-C3"] = -RC_Generator.fragmentation(process_prop.k_frag_d_C[2], MP1_BF.radius_m, MP1_BF.volume_m3, MP1_BF.diameter_um)
    RateConstants["k_3 (1/s)"]["k_C3-C3"] = -RC_Generator.heteroagg(process_prop.alpha_C[2], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Mixed_layer.G, Mixed_layer.T_K)
    RateConstants["k_4 (1/s)"]["k_C3-C3"] = -RC_Generator.settling(MP1_BF.density_kg_m3, MP1_BF.radius_m, Mixed_layer.depth_m, "Stokes")
    RateConstants["k_5 (1/s)"]["k_C3-C3"] = -RC_Generator.advection("water", Mixed_layer.volume_m3)
    RateConstants["k_6 (1/s)"]["k_C3-C3"] = -RC_Generator.mixing(Mixed_layer, Epilimnion, "up")
    RateConstants["k_7 (1/s)"]["k_C3-C3"] = -RC_Generator.mixing(Mixed_layer, Epilimnion, "down") 
    RateConstants["k_8 (1/s)"]["k_C3-C3"] = -RC_Generator.rising(MP1_BF.density_kg_m3, MP1_BF.radius_m, Mixed_layer.depth_m, "Stokes")
    
    RateConstants["k_1 (1/s)"]["k_C3-D3"] = RC_Generator.heteroagg(process_prop.alpha_C[2], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Mixed_layer.G, Mixed_layer.T_K)
    
    RateConstants["k_1 (1/s)"]["k_C3-C2"] = RC_Generator.rising(MP1_BF.density_kg_m3, MP1_BF.radius_m, Mixed_layer.depth_m, "Stokes")*(Mixed_layer.volume_m3/Epilimnion.volume_m3)
    RateConstants["k_2 (1/s)"]["k_C3-C2"] = (Mixed_layer.volume_m3/Epilimnion.volume_m3)* RC_Generator.mixing(Mixed_layer, Epilimnion, "up") 
    
    RateConstants["k_1 (1/s)"]["k_C3-C4"] = RC_Generator.settling(MP1_BF.density_kg_m3, MP1_BF.radius_m, Mixed_layer.depth_m, "Stokes")*(Mixed_layer.volume_m3/Hypolimnion.volume_m3)
    RateConstants["k_2 (1/s)"]["k_C3-C4"] = (Mixed_layer.volume_m3/Hypolimnion.volume_m3)*RC_Generator.mixing(Mixed_layer, Epilimnion, "down")
    
       
    #Mixed_layer, BF-covered SPM-bound MP
    RateConstants["k_1 (1/s)"]["k_D3-D3"] = -RC_Generator.degradation(process_prop.t_half_d_D[2]) 
    RateConstants["k_2 (1/s)"]["k_D3-D3"] = -RC_Generator.fragmentation(process_prop.k_frag_d_D[2], MP1_BF_SPM.radius_m, MP1_BF_SPM.volume_m3, MP1_BF_SPM.diameter_um)
    RateConstants["k_3 (1/s)"]["k_D3-D3"] = -RC_Generator.settling(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Mixed_layer.depth_m, "Stokes")
    RateConstants["k_4 (1/s)"]["k_D3-D3"] = -RC_Generator.advection("water", Mixed_layer.volume_m3)
    RateConstants["k_5 (1/s)"]["k_D3-D3"] = -RC_Generator.mixing(Mixed_layer, Epilimnion, "up")
    RateConstants["k_6 (1/s)"]["k_D3-D3"] = -RC_Generator.mixing(Mixed_layer, Epilimnion, "down") 
    RateConstants["k_7 (1/s)"]["k_D3-D3"] = -RC_Generator.rising(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Mixed_layer.depth_m, "Stokes")
    RateConstants["k_8 (1/s)"]["k_D3-D3"] = -RC_Generator.breakup(process_prop.alpha_C[2], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Mixed_layer.G, Mixed_layer.T_K)
    
    RateConstants["k_1 (1/s)"]["k_D3-C3"] = RC_Generator.breakup(process_prop.alpha_C[2], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Mixed_layer.G, Mixed_layer.T_K)
    
    RateConstants["k_1 (1/s)"]["k_D3-D2"] = RC_Generator.rising(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Mixed_layer.depth_m, "Stokes")*(Mixed_layer.volume_m3/Epilimnion.volume_m3)
    RateConstants["k_2 (1/s)"]["k_D3-D2"] = (Mixed_layer.volume_m3/Epilimnion.volume_m3)*RC_Generator.mixing(Mixed_layer, Epilimnion, "up") 
    
    RateConstants["k_1 (1/s)"]["k_D3-D4"] = RC_Generator.settling(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Mixed_layer.depth_m, "Stokes")*(Mixed_layer.volume_m3/Hypolimnion.volume_m3)
    RateConstants["k_2 (1/s)"]["k_D3-D4"] = (Mixed_layer.volume_m3/Hypolimnion.volume_m3)*RC_Generator.mixing(Mixed_layer, Epilimnion, "down")
    
    ###############################################################################
    #Hypolimnion _2 (or_1), pristine MP
    RateConstants["k_1 (1/s)"]["k_A4-A4"] = -RC_Generator.degradation(process_prop.t_half_d_A[3]) 
    RateConstants["k_2 (1/s)"]["k_A4-A4"] = -RC_Generator.fragmentation(process_prop.k_frag_d_A[3], MP1.radius_m, MP1.volume_m3, MP1.diameter_um)
    RateConstants["k_3 (1/s)"]["k_A4-A4"] = -RC_Generator.heteroagg(process_prop.alpha_A[3], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Hypolimnion.G, Hypolimnion.T_K)
    RateConstants["k_4 (1/s)"]["k_A4-A4"] = -RC_Generator.settling(MP1.density_kg_m3, MP1.radius_m, Hypolimnion.depth_m, "Stokes")
    RateConstants["k_5 (1/s)"]["k_A4-A4"] = -RC_Generator.mixing(Hypolimnion, Epilimnion, "up")
    RateConstants["k_6 (1/s)"]["k_A4-A4"] = -RC_Generator.biofilm(Hypolimnion, process_prop)
    RateConstants["k_7 (1/s)"]["k_A4-A4"] = -RC_Generator.rising(MP1.density_kg_m3, MP1.radius_m, Hypolimnion.depth_m, "Stokes")
    
    RateConstants["k_1 (1/s)"]["k_A4-A3"] = RC_Generator.rising(MP1.density_kg_m3, MP1.radius_m, Hypolimnion.depth_m, "Stokes")*(Hypolimnion.volume_m3/Mixed_layer.volume_m3)
    RateConstants["k_2 (1/s)"]["k_A4-A3"] = (Hypolimnion.volume_m3/Mixed_layer.volume_m3)*RC_Generator.mixing(Hypolimnion, Epilimnion, "up")
    
    RateConstants["k_1 (1/s)"]["k_A4-A5"] = RC_Generator.settling(MP1.density_kg_m3, MP1.radius_m, Hypolimnion.depth_m, "Stokes")*(Hypolimnion.volume_m3/Sediment.volume_m3)
    
    RateConstants["k_1 (1/s)"]["k_A4-B4"] = RC_Generator.heteroagg(process_prop.alpha_A[3], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Hypolimnion.G, Hypolimnion.T_K)
    
    RateConstants["k_1 (1/s)"]["k_A4-C4"] = RC_Generator.biofilm(Hypolimnion, process_prop)
    
    
    #Hypolimnion2 or 1, SPM-bound MP
    RateConstants["k_1 (1/s)"]["k_B4-B4"] = -RC_Generator.degradation(process_prop.t_half_d_B[3]) 
    RateConstants["k_2 (1/s)"]["k_B4-B4"] = -RC_Generator.fragmentation(process_prop.k_frag_d_B[3], MP1_SPM.radius_m, MP1_SPM.volume_m3, MP1_SPM.diameter_um)
    RateConstants["k_3 (1/s)"]["k_B4-B4"] = -RC_Generator.settling(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Hypolimnion.depth_m, "Stokes")
    RateConstants["k_4 (1/s)"]["k_B4-B4"] = -RC_Generator.mixing(Hypolimnion, Epilimnion, "up")
    RateConstants["k_5 (1/s)"]["k_B4-B4"] = -RC_Generator.rising(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Hypolimnion.depth_m, "Stokes")
    RateConstants["k_6 (1/s)"]["k_B4-B4"] = -RC_Generator.breakup(process_prop.alpha_A[3], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Hypolimnion.G, Hypolimnion.T_K)
    
    RateConstants["k_1 (1/s)"]["k_B4-A4"] = RC_Generator.breakup(process_prop.alpha_C[3], MP1.radius_m, SPM1.radius_m, MP1.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Hypolimnion.G, Hypolimnion.T_K)
    
    RateConstants["k_1 (1/s)"]["k_B4-B5"] = RC_Generator.settling(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Hypolimnion.depth_m, "Stokes")*(Hypolimnion.volume_m3/Sediment.volume_m3)
    
    RateConstants["k_1 (1/s)"]["k_B4-B3"] = RC_Generator.rising(MP1_SPM.density_kg_m3, MP1_SPM.radius_m, Hypolimnion.depth_m, "Stokes")*(Hypolimnion.volume_m3/Mixed_layer.volume_m3)
    RateConstants["k_2 (1/s)"]["k_B4-B3"] = (Hypolimnion.volume_m3/Mixed_layer.volume_m3)* RC_Generator.mixing(Hypolimnion, Epilimnion, "up")
    
    
    #Hypolimnion_end, BF-covered MP
    RateConstants["k_1 (1/s)"]["k_C4-C4"] = -RC_Generator.degradation(process_prop.t_half_d_C[3]) 
    RateConstants["k_2 (1/s)"]["k_C4-C4"] = -RC_Generator.fragmentation(process_prop.k_frag_d_C[3], MP1_BF.radius_m, MP1_BF.volume_m3, MP1_BF.diameter_um)
    RateConstants["k_3 (1/s)"]["k_C4-C4"] = -RC_Generator.heteroagg(process_prop.alpha_C[3], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Hypolimnion.G, Hypolimnion.T_K)
    RateConstants["k_4 (1/s)"]["k_C4-C4"] = -RC_Generator.settling(MP1_BF.density_kg_m3, MP1_BF.radius_m, Hypolimnion.depth_m, "Stokes")
    RateConstants["k_5 (1/s)"]["k_C4-C4"] = -RC_Generator.mixing(Hypolimnion, Epilimnion, "up")
    RateConstants["k_6 (1/s)"]["k_C4-C4"] = -RC_Generator.rising(MP1_BF.density_kg_m3, MP1_BF.radius_m, Hypolimnion.depth_m, "Stokes")
    
    RateConstants["k_1 (1/s)"]["k_C4-D4"] = RC_Generator.heteroagg(process_prop.alpha_C[3], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Hypolimnion.G, Hypolimnion.T_K)
    
    RateConstants["k_1 (1/s)"]["k_C4-C5"] = RC_Generator.settling(MP1_BF.density_kg_m3, MP1_BF.radius_m, Hypolimnion.depth_m, "Stokes")*(Hypolimnion.volume_m3/Sediment.volume_m3)
    
    RateConstants["k_1 (1/s)"]["k_C4-C3"] = RC_Generator.rising(MP1_BF.density_kg_m3, MP1_BF.radius_m, Hypolimnion.depth_m, "Stokes")*(Hypolimnion.volume_m3/Mixed_layer.volume_m3)
    RateConstants["k_2 (1/s)"]["k_C4-C3"] = (Hypolimnion.volume_m3/Mixed_layer.volume_m3)*RC_Generator.mixing(Hypolimnion, Epilimnion, "up")
    
    
    #Hypolimnion_end, BF-covered SPM-bound MP
    RateConstants["k_1 (1/s)"]["k_D4-D4"] = -RC_Generator.degradation(process_prop.t_half_d_D[3]) 
    RateConstants["k_2 (1/s)"]["k_D4-D4"] = -RC_Generator.fragmentation(process_prop.k_frag_d_D[3], MP1_BF_SPM.radius_m, MP1_BF_SPM.volume_m3, MP1_BF_SPM.diameter_um)
    RateConstants["k_3 (1/s)"]["k_D4-D4"] = -RC_Generator.settling(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Hypolimnion.depth_m, "Stokes")
    RateConstants["k_4 (1/s)"]["k_D4-D4"] = -RC_Generator.mixing(Hypolimnion, Epilimnion, "up")
    RateConstants["k_5 (1/s)"]["k_D4-D4"] = -RC_Generator.rising(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Hypolimnion.depth_m, "Stokes")
    RateConstants["k_6 (1/s)"]["k_D4-D4"] = -RC_Generator.breakup(process_prop.alpha_C[3], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Hypolimnion.G, Hypolimnion.T_K)
    
    RateConstants["k_1 (1/s)"]["k_D4-C4"] = RC_Generator.breakup(process_prop.alpha_C[3], MP1_BF.radius_m, SPM1.radius_m, MP1_BF.density_kg_m3, SPM1.density_kg_m3, SPM1.concNum_part_m3, Hypolimnion.G, Hypolimnion.T_K)
    
    RateConstants["k_1 (1/s)"]["k_D4-D5"] = RC_Generator.settling(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Hypolimnion.depth_m, "Stokes")*(Hypolimnion.volume_m3/Sediment.volume_m3)
    
    RateConstants["k_1 (1/s)"]["k_D4-D3"] = RC_Generator.rising(MP1_BF_SPM.density_kg_m3, MP1_BF_SPM.radius_m, Hypolimnion.depth_m, "Stokes")*(Hypolimnion.volume_m3/Mixed_layer.volume_m3)
    RateConstants["k_2 (1/s)"]["k_D4-D3"] = (Hypolimnion.volume_m3/Mixed_layer.volume_m3)*RC_Generator.mixing(Hypolimnion, Epilimnion, "up")
    
    
    ###############################################################################
    #Sediment, pristine MP
    RateConstants["k_1 (1/s)"]["k_A5-A5"] = -RC_Generator.degradation(process_prop.t_half_d_A[4]) 
    RateConstants["k_2 (1/s)"]["k_A5-A5"] = -RC_Generator.fragmentation(process_prop.k_frag_d_A[4], MP1.radius_m, MP1.volume_m3, MP1.diameter_um)
    RateConstants["k_3 (1/s)"]["k_A5-A5"] = -RC_Generator.resusp(Sediment)
    RateConstants["k_4 (1/s)"]["k_A5-A5"] = -RC_Generator.burial(Sediment)
    
    RateConstants["k_1 (1/s)"]["k_A5-A4"] = RC_Generator.resusp(Sediment)*(Sediment.volume_m3/Hypolimnion.volume_m3)
    
    
    #Sediment, SPM-bound MP
    RateConstants["k_1 (1/s)"]["k_B5-B5"] = -RC_Generator.degradation(process_prop.t_half_d_B[4]) 
    RateConstants["k_2 (1/s)"]["k_B5-B5"] = -RC_Generator.fragmentation(process_prop.k_frag_d_B[4], MP1_SPM.radius_m, MP1_SPM.volume_m3, MP1_SPM.diameter_um)
    RateConstants["k_3 (1/s)"]["k_B5-B5"] = -RC_Generator.resusp(Sediment)
    RateConstants["k_4 (1/s)"]["k_B5-B5"] = -RC_Generator.burial(Sediment)
    
    RateConstants["k_1 (1/s)"]["k_B5-B4"] = RC_Generator.resusp(Sediment)*(Sediment.volume_m3/Hypolimnion.volume_m3)
    
    #Sediment, BF-covered MP
    RateConstants["k_1 (1/s)"]["k_C5-C5"] = -RC_Generator.degradation(process_prop.t_half_d_C[4]) 
    RateConstants["k_2 (1/s)"]["k_C5-C5"] = -RC_Generator.fragmentation(process_prop.k_frag_d_C[4], MP1_BF.radius_m, MP1_BF.volume_m3, MP1_BF.diameter_um)
    RateConstants["k_3 (1/s)"]["k_C5-C5"] = -RC_Generator.resusp(Sediment)
    RateConstants["k_4 (1/s)"]["k_C5-C5"] = -RC_Generator.burial(Sediment)
    
    RateConstants["k_1 (1/s)"]["k_C5-C4"] = RC_Generator.resusp(Sediment)*(Sediment.volume_m3/Hypolimnion.volume_m3)
    
    
    #Sediment, BF-covered SPM-bound MP
    RateConstants["k_1 (1/s)"]["k_D5-D5"] = -RC_Generator.degradation(process_prop.t_half_d_D[4]) 
    RateConstants["k_2 (1/s)"]["k_D5-D5"] = -RC_Generator.fragmentation(process_prop.k_frag_d_D[4], MP1_BF_SPM.radius_m, MP1_BF_SPM.volume_m3, MP1_BF_SPM.diameter_um)
    RateConstants["k_3 (1/s)"]["k_D5-D5"] = -RC_Generator.resusp(Sediment)
    RateConstants["k_4 (1/s)"]["k_D5-D5"] = -RC_Generator.burial(Sediment)
    
    RateConstants["k_3 (1/s)"]["k_D5-D4"] = RC_Generator.resusp(Sediment)#*(Sediment.volume_m3/Hypolimnion.volume_m3)
    
    return RateConstants
