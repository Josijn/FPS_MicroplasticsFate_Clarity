# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:04:28 2019

@author: AntoniaPraetorius
"""

"""
this files contains an overview of all MP forms modelled and a compilation
of all rate constants including their relation to the different forms (i.e.
what transforms into what)

MP forms include: free pristine MPs (MP), MPs bound to SPM (MP_SPM), MP 
covered in biofilm (MP_BF)
5 different size bins are modelled, denominated with the numbers 1 to 5 (i.e. MP1
 to MP5) 
"""

def modelMatrix(MainWater, SurfWater, Sediment):
    
    #internal variable definition
    #initial concentrations - MP forms & locations
    
    #size bin 1: 0.1 um
    Cw1_MP1_0 = 0     #concentration of free MPs in MainWater, size bin 1
    Cws_MP1_0 = 0     #concentration of free MPs in SurfWater, size bin 1
    Cse_MP1_0 = 0      #concentration of free MPs in Sediment, size bin 1
    Cw1_MP1_SPM_0 = 0 #concentration of SPM-bound MPs in MainWater, size bin 1
    Cws_MP1_SPM_0 = 0 #concentration of SPM-bound MPs in SurfWater, size bin 1
    Cse_MP1_SPM_0  = 0 #concentration of SPM-bound MPs in Sediment, size bin 1
    Cw1_MP1_BF_0 = 0  #concentration of biofilm covered MPs in MainWater, size bin 1
    Cws_MP1_BF_0 = 0  #concentration of biofilm covered MPs in SurfWater, size bin 1
    Cse_MP1_BF_0 = 0   #concentration of biofilm covered MPs in Sediment, size bin 1
    Cw1_MP1_BF_SPM_0 = 0  #concentration of biofilm covered SPM-bound MPs in MainWater, size bin 1
    Cws_MP1_BF_SPM_0 = 0  #concentration of biofilm covered SPM-bound MPs in SurfWater, size bin 1
    Cse_MP1_BF_SPM_0 = 0   #concentration of biofilm covered SPM-bound MPs in Sediment, size bin 1

    #size bin 2: 1 um
    Cw1_MP2_0 = 0     #concentration of free MPs in MainWater, size bin 2
    Cws_MP2_0 = 0     #concentration of free MPs in SurfWater, size bin 2
    Cse_MP2_0 = 0      #concentration of free MPs in Sediment, size bin 2
    Cw1_MP2_SPM_0 = 0 #concentration of SPM-bound MPs in MainWater, size bin 2
    Cws_MP2_SPM_0 = 0 #concentration of SPM-bound MPs in SurfWater, size bin 2
    Cse_MP2_SPM_0  = 0 #concentration of SPM-bound MPs in Sediment, size bin 2
    Cw1_MP2_BF_0 = 0  #concentration of biofilm covered MPs in MainWater, size bin 2
    Cws_MP2_BF_0 = 0  #concentration of biofilm covered MPs in SurfWater, size bin 2
    Cse_MP2_BF_0 = 0   #concentration of biofilm covered MPs in Sediment, size bin 2
    Cw1_MP2_BF_SPM_0 = 0  #concentration of biofilm covered SPM-bound MPs in MainWater, size bin 2
    Cws_MP2_BF_SPM_0 = 0  #concentration of biofilm covered SPM-bound MPs in SurfWater, size bin 2
    Cse_MP2_BF_SPM_0 = 0   #concentration of biofilm covered SPM-bound MPs in Sediment, size bin 2
    
    #size bin 3: 10 um
    Cw1_MP3_0 = 0     #concentration of free MPs in MainWater, size bin 3
    Cws_MP3_0 = 0     #concentration of free MPs in SurfWater, size bin 3
    Cse_MP3_0 = 0      #concentration of free MPs in Sediment, size bin 3
    Cw1_MP3_SPM_0 = 0 #concentration of SPM-bound MPs in MainWater, size bin 3
    Cws_MP3_SPM_0 = 0 #concentration of SPM-bound MPs in SurfWater, size bin 3
    Cse_MP3_SPM_0  = 0 #concentration of SPM-bound MPs in Sediment, size bin 3
    Cw1_MP3_BF_0 = 0  #concentration of biofilm covered MPs in MainWater, size bin 3
    Cws_MP3_BF_0 = 0  #concentration of biofilm covered MPs in SurfWater, size bin 3
    Cse_MP3_BF_0 = 0   #concentration of biofilm covered MPs in Sediment, size bin 3
    Cw1_MP3_BF_SPM_0 = 0  #concentration of biofilm covered SPM-bound MPs in MainWater, size bin 3
    Cws_MP3_BF_SPM_0 = 0  #concentration of biofilm covered SPM-bound MPs in SurfWater, size bin 3
    Cse_MP3_BF_SPM_0 = 0   #concentration of biofilm covered SPM-bound MPs in Sediment, size bin 3
    
    #size bin 4: 100 um
    Cw1_MP4_0 = 0     #concentration of free MPs in MainWater, size bin 4
    Cws_MP4_0 = 0     #concentration of free MPs in SurfWater, size bin 4
    Cse_MP4_0 = 0      #concentration of free MPs in Sediment, size bin 4
    Cw1_MP4_SPM_0 = 0 #concentration of SPM-bound MPs in MainWater, size bin 4
    Cws_MP4_SPM_0 = 0 #concentration of SPM-bound MPs in SurfWater, size bin 4
    Cse_MP4_SPM_0  = 0 #concentration of SPM-bound MPs in Sediment, size bin 4
    Cw1_MP4_BF_0 = 0  #concentration of biofilm covered MPs in MainWater, size bin 4
    Cws_MP4_BF_0 = 0  #concentration of biofilm covered MPs in SurfWater, size bin 4
    Cse_MP4_BF_0 = 0   #concentration of biofilm covered MPs in Sediment, size bin 4
    Cw1_MP4_BF_SPM_0 = 0  #concentration of biofilm covered SPM-bound MPs in MainWater, size bin 4
    Cws_MP4_BF_SPM_0 = 0  #concentration of biofilm covered SPM-bound MPs in SurfWater, size bin 4
    Cse_MP4_BF_SPM_0 = 0   #concentration of biofilm covered SPM-bound MPs in Sediment, size bin 4

    #size bin 5: 1000 um
    Cw1_MP5_0 = 0     #concentration of free MPs in MainWater, size bin 5
    Cws_MP5_0 = 0     #concentration of free MPs in SurfWater, size bin 5
    Cse_MP5_0 = 0      #concentration of free MPs in Sediment, size bin 5
    Cw1_MP5_SPM_0 = 0 #concentration of SPM-bound MPs in MainWater, size bin 5
    Cws_MP5_SPM_0 = 0 #concentration of SPM-bound MPs in SurfWater, size bin 5
    Cse_MP_SPM_0  = 0 #concentration of SPM-bound MPs in Sediment, size bin 5
    Cw1_MP5_BF_0 = 0  #concentration of biofilm covered MPs in MainWater, size bin 5
    Cws_MP5_BF_0 = 0  #concentration of biofilm covered MPs in SurfWater, size bin 5
    Cse_MP5_BF_0 = 0   #concentration of biofilm covered MPs in Sediment, size bin 5
    Cw1_MP5_BF_SPM_0 = 0  #concentration of biofilm covered SPM-bound MPs in MainWater, size bin 5
    Cws_MP5_BF_SPM_0 = 0  #concentration of biofilm covered SPM-bound MPs in SurfWater, size bin 5
    Cse_MP5_BF_SPM_0 = 0   #concentration of biofilm covered SPM-bound MPs in Sediment, size bin 5

    
    #lists to store final concentrations
        
    #size bin 1: 0.1 um
    Cw1_MP1_final = []     #concentration of free MPs in MainWater, size bin 1
    Cws_MP1_final = []     #concentration of free MPs in SurfWater, size bin 1
    Cse_MP1_final = []      #concentration of free MPs in Sediment, size bin 1
    Cw1_MP1_SPM_final = [] #concentration of SPM-bound MPs in MainWater, size bin 1
    Cws_MP1_SPM_final = [] #concentration of SPM-bound MPs in SurfWater, size bin 1
    Cse_MP1_SPM_final = [] #concentration of SPM-bound MPs in Sediment, size bin 1
    Cw1_MP1_BF_final = []  #concentration of biofilm covered MPs in MainWater, size bin 1
    Cws_MP1_BF_final = []  #concentration of biofilm covered MPs in SurfWater, size bin 1
    Cse_MP1_BF_final = []   #concentration of biofilm covered MPs in Sediment, size bin 1
    Cw1_MP1_BF_SPM_final = []   #concentration of biofilm covered SPM-bound MPs in MainWater, size bin 1
    Cws_MP1_BF_SPM_final = []   #concentration of biofilm covered SPM-bound MPs in SurfWater, size bin 1
    Cse_MP1_BF_SPM_final = []    #concentration of biofilm covered SPM-bound MPs in Sediment, size bin 1
   
    #size bin 2: 1 um
    Cw1_MP2_final = []     #concentration of free MPs in MainWater, size bin 2
    Cws_MP2_final = []     #concentration of free MPs in SurfWater, size bin 2
    Cse_MP2_final = []      #concentration of free MPs in Sediment, size bin 2
    Cw1_MP2_SPM_final = [] #concentration of SPM-bound MPs in MainWater, size bin 2
    Cws_MP2_SPM_final = [] #concentration of SPM-bound MPs in SurfWater, size bin 2
    Cse_MP2_SPM_final = [] #concentration of SPM-bound MPs in Sediment, size bin 2
    Cw1_MP2_BF_final = []  #concentration of biofilm covered MPs in MainWater, size bin 2
    Cws_MP2_BF_final = []  #concentration of biofilm covered MPs in SurfWater, size bin 2
    Cse_MP2_BF_final = []   #concentration of biofilm covered MPs in Sediment, size bin 2
    Cw1_MP2_BF_SPM_final = []   #concentration of biofilm covered SPM-bound MPs in MainWater, size bin 2
    Cws_MP2_BF_SPM_final = []   #concentration of biofilm covered SPM-bound MPs in SurfWater, size bin 2
    Cse_MP2_BF_SPM_final = []    #concentration of biofilm covered SPM-bound MPs in Sediment, size bin 2
    
    #size bin 3: 10 um
    Cw1_MP3_final = []     #concentration of free MPs in MainWater, size bin 3
    Cws_MP3_final = []     #concentration of free MPs in SurfWater, size bin 3
    Cse_MP3_final = []      #concentration of free MPs in Sediment, size bin 3
    Cw1_MP3_SPM_final = [] #concentration of SPM-bound MPs in MainWater, size bin 3
    Cws_MP3_SPM_final = [] #concentration of SPM-bound MPs in SurfWater, size bin 3
    Cse_MP3_SPM_final = [] #concentration of SPM-bound MPs in Sediment, size bin 3
    Cw1_MP3_BF_final = []  #concentration of biofilm covered MPs in MainWater, size bin 3
    Cws_MP3_BF_final = []  #concentration of biofilm covered MPs in SurfWater, size bin 3
    Cse_MP3_BF_final = []   #concentration of biofilm covered MPs in Sediment, size bin 3
    Cw1_MP3_BF_SPM_final = []   #concentration of biofilm covered SPM-bound MPs in MainWater, size bin 3
    Cws_MP3_BF_SPM_final = []   #concentration of biofilm covered SPM-bound MPs in SurfWater, size bin 3
    Cse_MP3_BF_SPM_final = []    #concentration of biofilm covered SPM-bound MPs in Sediment, size bin 3
   
    #size bin 4: 100 um
    Cw1_MP4_final = []     #concentration of free MPs in MainWater, size bin 4
    Cws_MP4_final = []     #concentration of free MPs in SurfWater, size bin 4
    Cse_MP4_final = []      #concentration of free MPs in Sediment, size bin 4
    Cw1_MP4_SPM_final = [] #concentration of SPM-bound MPs in MainWater, size bin 4
    Cws_MP4_SPM_final = [] #concentration of SPM-bound MPs in SurfWater, size bin 4
    Cse_MP4_SPM_final = [] #concentration of SPM-bound MPs in Sediment, size bin 4
    Cw1_MP4_BF_final = []  #concentration of biofilm covered MPs in MainWater, size bin 4
    Cws_MP4_BF_final = []  #concentration of biofilm covered MPs in SurfWater, size bin 4
    Cse_MP4_BF_final = []   #concentration of biofilm covered MPs in Sediment, size bin 4
    Cw1_MP4_BF_SPM_final = []   #concentration of biofilm covered SPM-bound MPs in MainWater, size bin 4
    Cws_MP4_BF_SPM_final = []   #concentration of biofilm covered SPM-bound MPs in SurfWater, size bin 4
    Cse_MP4_BF_SPM_final = []    #concentration of biofilm covered SPM-bound MPs in Sediment, size bin 4
    
    #size bin 5: 1000 um
    Cw1_MP5_final = []     #concentration of free MPs in MainWater, size bin 5
    Cws_MP5_final = []     #concentration of free MPs in SurfWater, size bin 5
    Cse_MP5_final = []      #concentration of free MPs in Sediment, size bin 5
    Cw1_MP5_SPM_final = [] #concentration of SPM-bound MPs in MainWater, size bin 5
    Cws_MP5_SPM_final = [] #concentration of SPM-bound MPs in SurfWater, size bin 5
    Cse_MP_SPM_final = [] #concentration of SPM-bound MPs in Sediment, size bin 5
    Cw1_MP5_BF_final = [] #concentration of biofilm covered MPs in MainWater, size bin 5
    Cws_MP5_BF_final = [] #concentration of biofilm covered MPs in SurfWater, size bin 5
    Cse_MP5_BF_final = []  #concentration of biofilm covered MPs in Sediment, size bin 5
    Cw1_MP5_BF_SPM_final = []   #concentration of biofilm covered SPM-bound MPs in MainWater, size bin 5
    Cws_MP5_BF_SPM_final = []   #concentration of biofilm covered SPM-bound MPs in SurfWater, size bin 5
    Cse_MP5_BF_SPM_final = []    #concentration of biofilm covered SPM-bound MPs in Sediment, size bin 5

    
    #compilation of rate constants
     
    #heteroaggregation of pristine MPs in main water (for each size bin)
    K1 = MainWater.k_hetAgg_1 #Cw1_MP1 --> Cw1_MP1_SPM
    K2 = MainWater.k_hetAgg_2 #Cw1_MP2 --> Cw1_MP2_SPM
    K3 = MainWater.k_hetAgg_3 #Cw1_MP3 --> Cw1_MP3_SPM
    K4 = MainWater.k_hetAgg_4 #Cw1_MP4 --> Cw1_MP4_SPM
    K5 = MainWater.k_hetAgg_5 #Cw1_MP5 --> Cw1_MP5_SPM

    #heteroaggregation of biofilm covered MPs in main water (for each size bin)
    K1B = MainWater.k_hetAgg_1B #Cw1_MP1_BF --> Cw1_MP1_BF_SPM
    K2B = MainWater.k_hetAgg_2B #Cw1_MP2_BF --> Cw1_MP2_BF_SPM
    K3B = MainWater.k_hetAgg_3B #Cw1_MP3_BF --> Cw1_MP3_BF_SPM
    K4B = MainWater.k_hetAgg_4B #Cw1_MP4_BF --> Cw1_MP4_BF_SPM
    K5B = MainWater.k_hetAgg_5B #Cw1_MP5_BF --> Cw1_MP5_BF_SPM

    #breakup of MP-SPM heteroaggregates in main water (for each size bin)
    K6 = MainWater.k_aggBreakup_1 #Cw1_MP1_SPM --> Cw1_MP1
    K7 = MainWater.k_aggBreakup_2 #Cw1_MP2_SPM --> Cw1_MP2
    K8 = MainWater.k_aggBreakup_3 #Cw1_MP3_SPM --> Cw1_MP3
    K9 = MainWater.k_aggBreakup_4 #Cw1_MP4_SPM --> Cw1_MP4
    K10 = MainWater.k_aggBreakup_5 #Cw1_MP5_SPM --> Cw1_MP5

    #breakup of biofilm covered MP-SPM heteroaggregates in main water (for each size bin)
    K6B = MainWater.k_aggBreakup_1 #Cw1_MP1_BF_SPM --> Cw1_MP1_BF
    K7B = MainWater.k_aggBreakup_2 #Cw1_MP2_BF_SPM --> Cw1_MP2_BF
    K8B = MainWater.k_aggBreakup_3 #Cw1_MP3_BF_SPM --> Cw1_MP3_BF
    K9B = MainWater.k_aggBreakup_4 #Cw1_MP4_BF_SPM --> Cw1_MP4_BF
    K10B = MainWater.k_aggBreakup_5 #Cw1_MP5_BF_SPM --> Cw1_MP5_BF

    #settling of pristine MPs from main water to sediment (for each size bin)
    K11 = MainWater.k_set_Stokes_MP1 #Cw1_MP1 --> Cse_MP1
    K12 = MainWater.k_set_Stokes_MP2 #Cw1_MP2 --> Cse_MP2
    K13 = MainWater.k_set_Stokes_MP3 #Cw1_MP3 --> Cse_MP3
    K14 = MainWater.k_set_Stokes_MP4 #Cw1_MP4 --> Cse_MP4
    K15 = MainWater.k_set_Stokes_MP5 #Cw1_MP5 --> Cse_MP5

    #settling of SPM-bound MPs from main water to sediment (for each size bin)
    K11B = MainWater.k_set_Stokes_MP1SPM #Cw1_MP1_SPM --> Cse_MP1_SPM
    K12B = MainWater.k_set_Stokes_MP2SPM #Cw1_MP2_SPM --> Cse_MP2_SPM
    K13B = MainWater.k_set_Stokes_MP3SPM #Cw1_MP3_SPM --> Cse_MP3_SPM
    K14B = MainWater.k_set_Stokes_MP4SPM #Cw1_MP4_SPM --> Cse_MP4_SPM
    K15B = MainWater.k_set_Stokes_MP5SPM #Cw1_MP5_SPM --> Cse_MP5_SPM

    #settling of biofilm covered MPs from main water to sediment (for each size bin)
    K11C = MainWater.k_set_Stokes_MP1BF #Cw1_MP1_BF --> Cse_MP1_BF
    K12C = MainWater.k_set_Stokes_MP2BF #Cw1_MP2_BF --> Cse_MP2_BF
    K13C = MainWater.k_set_Stokes_MP3BF #Cw1_MP3_BF --> Cse_MP3_BF
    K14C = MainWater.k_set_Stokes_MP4BF #Cw1_MP4_BF --> Cse_MP4_BF
    K15C = MainWater.k_set_Stokes_MP5BF #Cw1_MP5_BF --> Cse_MP5_BF

    #settling of biofilm covered SPM-bound MPs from main water to sediment (for each size bin)
    K11D = MainWater.k_set_Stokes_MP1BFSPM #Cw1_MP1_BF_SPM --> Cse_MP1_BF_SPM
    K12D = MainWater.k_set_Stokes_MP2BFSPM #Cw1_MP2_BF_SPM --> Cse_MP2_BF_SPM
    K13D = MainWater.k_set_Stokes_MP3BFSPM #Cw1_MP3_BF_SPM --> Cse_MP3_BF_SPM
    K14D = MainWater.k_set_Stokes_MP4BFSPM #Cw1_MP4_BF_SPM --> Cse_MP4_BF_SPM
    K15D = MainWater.k_set_Stokes_MP5BFSPM #Cw1_MP5_BF_SPM --> Cse_MP5_BF_SPM

    #settling of pristine MPs from water surface to main water (for each size bin)
    K16 = SurfWater.k_set_Stokes_MP1 #Cws_MP1 --> Cw1_MP1
    K17 = SurfWater.k_set_Stokes_MP2 #Cws_MP2 --> Cw1_MP2
    K18 = SurfWater.k_set_Stokes_MP3 #Cws_MP3 --> Cw1_MP3
    K19 = SurfWater.k_set_Stokes_MP4 #Cws_MP4 --> Cw1_MP4
    K20 = SurfWater.k_set_Stokes_MP5 #Cws_MP5 --> Cw1_MP5

    #settling of SPM-bound MPs from water surface to main water (for each size bin)
    K16B = SurfWater.k_set_Stokes_MP1SPM #Cws_MP1_SPM --> Cw1_MP1_SPM
    K17B = SurfWater.k_set_Stokes_MP2SPM #Cws_MP2_SPM --> Cw1_MP2_SPM
    K18B = SurfWater.k_set_Stokes_MP3SPM #Cws_MP3_SPM --> Cw1_MP3_SPM
    K19B = SurfWater.k_set_Stokes_MP4SPM #Cws_MP4_SPM --> Cw1_MP4_SPM
    K20B = SurfWater.k_set_Stokes_MP5SPM #Cws_MP5_SPM --> Cw1_MP5_SPM

    #settling of biofilm covered MPs from water surface to main water (for each size bin)
    K16C = SurfWater.k_set_Stokes_MP1BF #Cws_MP1_BF --> Cw1_MP1_BF
    K17C = SurfWater.k_set_Stokes_MP2BF #Cws_MP2_BF --> Cw1_MP2_BF
    K18C = SurfWater.k_set_Stokes_MP3BF #Cws_MP3_BF --> Cw1_MP3_BF
    K19C = SurfWater.k_set_Stokes_MP4BF #Cws_MP4_BF --> Cw1_MP4_BF
    K20C = SurfWater.k_set_Stokes_MP5BF #Cws_MP5_BF --> Cw1_MP5_BF

    #settling of biofilm covered SPM-bound MPs from water surface to main water (for each size bin)
    K16D = SurfWater.k_set_Stokes_MP1BFSPM #Cws_MP1_BF_SPM --> Cw1_MP1_BF_SPM
    K17D = SurfWater.k_set_Stokes_MP2BFSPM #Cws_MP2_BF_SPM --> Cw1_MP2_BF_SPM
    K18D = SurfWater.k_set_Stokes_MP3BFSPM #Cws_MP3_BF_SPM --> Cw1_MP3_BF_SPM
    K19D = SurfWater.k_set_Stokes_MP4BFSPM #Cws_MP4_BF_SPM --> Cw1_MP4_BF_SPM
    K20D = SurfWater.k_set_Stokes_MP5BFSPM #Cws_MP5_BF_SPM --> Cw1_MP5_BF_SPM

    #rising of pristine MPs from main water to water surface (for each size bin)
    K21 = MainWater.k_rise_Stokes_MP1 #Cw1_MP1 --> Cws_MP1
    K22 = MainWater.k_rise_Stokes_MP2 #Cw1_MP2 --> Cws_MP2
    K23 = MainWater.k_rise_Stokes_MP3 #Cw1_MP3 --> Cws_MP3
    K24 = MainWater.k_rise_Stokes_MP4 #Cw1_MP4 --> Cws_MP4
    K25 = MainWater.k_rise_Stokes_MP5 #Cw1_MP5 --> Cws_MP5

    #rising of SPM-bound MPs from main water to water surface (for each size bin)
    K21B = MainWater.k_rise_Stokes_MP1SPM #Cw1_MP1_SPM --> Cws_MP1_SPM
    K22B = MainWater.k_rise_Stokes_MP2SPM #Cw1_MP2_SPM --> Cws_MP2_SPM
    K23B = MainWater.k_rise_Stokes_MP3SPM #Cw1_MP3_SPM --> Cws_MP3_SPM
    K24B = MainWater.k_rise_Stokes_MP4SPM #Cw1_MP4_SPM --> Cws_MP4_SPM
    K25B = MainWater.k_rise_Stokes_MP5SPM #Cw1_MP5_SPM --> Cws_MP5_SPM

    #rising of biofilm covered MPs from main water to water surface (for each size bin)
    K21C = MainWater.k_rise_Stokes_MP1BF #Cw1_MP1_BF --> Cws_MP1_BF
    K22C = MainWater.k_rise_Stokes_MP2BF #Cw1_MP2_BF --> Cws_MP2_BF
    K23C = MainWater.k_rise_Stokes_MP3BF #Cw1_MP3_BF --> Cws_MP3_BF
    K24C = MainWater.k_rise_Stokes_MP4BF #Cw1_MP4_BF --> Cws_MP4_BF
    K25C = MainWater.k_rise_Stokes_MP5BF #Cw1_MP5_BF --> Cws_MP5_BF

    #rising of biofilm covered SPM-bound MPs from main water to water surface (for each size bin)
    K21D = MainWater.k_rise_Stokes_MP1BFSPM #Cw1_MP1_BF_SPM --> Cws_MP1_BF_SPM
    K22D = MainWater.k_rise_Stokes_MP2BFSPM #Cw1_MP2_BF_SPM --> Cws_MP2_BF_SPM
    K23D = MainWater.k_rise_Stokes_MP3BFSPM #Cw1_MP3_BF_SPM --> Cws_MP3_BF_SPM
    K24D = MainWater.k_rise_Stokes_MP4BFSPM #Cw1_MP4_BF_SPM --> Cws_MP4_BF_SPM
    K25D = MainWater.k_rise_Stokes_MP5BFSPM #Cw1_MP5_BF_SPM --> Cws_MP5_BF_SPM

    #fragmentation of pristine MPs from 1 size bin to another, in main water
    K26 = MainWater.k_frag_MP1 #Cw1_MP1 --> (nothing, treated as complete degradation currently)
    K27 = MainWater.k_frag_MP2 #Cw1_MP2 --> Cw1_MP1
    K28 = MainWater.k_frag_MP3 #Cw1_MP3 --> Cw1_MP2
    K29 = MainWater.k_frag_MP4 #Cw1_MP4 --> Cw1_MP3
    K30 = MainWater.k_frag_MP5 #Cw1_MP5 --> Cw1_MP4

    #fragmentation of pristine MPs from 1 size bin to another, in surface water
    K26B = SurfWater.k_frag_MP1 #Cws_MP1 --> (nothing, treated as complete degradation currently)
    K27B = SurfWater.k_frag_MP2 #Cws_MP2 --> Cws_MP1
    K28B = SurfWater.k_frag_MP3 #Cws_MP3 --> Cws_MP2
    K29B = SurfWater.k_frag_MP4 #Cws_MP4 --> Cws_MP3
    K30B = SurfWater.k_frag_MP5 #Cws_MP5 --> Cws_MP4

    #advective flow out of the main water compartment 
    K31 = MainWater.k_outflow #Cw1_MP1/Cw1_MP2/Cw1_MP3/Cw1_MP4/Cw1_MP5 -->
    #Cw1_MP1/Cw1_MP2/Cw1_MP3/Cw1_MP4/Cw1_MP5 -->
    #Cw1_MP1_SPM/Cw1_MP2_SPM/Cw1_MP3_SPM/Cw1_MP4_SPM/Cw1_MP5_SPM -->
    #Cw1_MP1_BF/Cw1_MP2_BF/Cw1_MP3_BF/Cw1_MP4_BF/Cw1_MP5_BF -->
    #Cw1_MP1_BF_SPM/Cw1_MP2_BF_SPM/Cw1_MP3_BF_SPM/Cw1_MP4_BF_SPM/Cw1_MP5_BF_SPM -->
      
    #advective flow out of the surface water compartment 
    K32 = SurfWater.k_outflow #Cws_MP1/Cws_MP2/Cws_MP3/Cws_MP4/Cws_MP5 -->
    #Cws_MP1/Cws_MP2/Cws_MP3/Cws_MP4/Cws_MP5 -->
    #Cws_MP1_SPM/Cws_MP2_SPM/Cws_MP3_SPM/Cws_MP4_SPM/Cws_MP5_SPM -->
    #Cws_MP1_BF/Cws_MP2_BF/Cws_MP3_BF/Cws_MP4_BF/Cws_MP5_BF -->
    #Cws_MP1_BF_SPM/Cws_MP2_BF_SPM/Cws_MP3_BF_SPM/Cws_MP4_BF_SPM/Cws_MP5_BF_SPM -->

    #sediment resuspension
    K33 = Sediment.k_resusp 
    #Cse_MP1/Cse_MP2/Cse_MP3/Cse_MP4/Cse_MP5 --> Cw1_MP1/Cw1_MP2/Cw1_MP3/Cw1_MP4/Cw1_MP5
    #Cse_MP1_SPM/Cse_MP2_SPM/Cse_MP3_SPM/Cse_MP4_SPM/Cse_MP5_SPM --> Cw1_MP1_SPM/Cw1_MP2_SPM/Cw1_MP3_SPM/Cw1_MP4_SPM/Cw1_MP5_SPM 
    #Cse_MP1_BF/Cse_MP2_BF/Cse_MP3_BF/Cse_MP4_BF/Cse_MP5_BF --> Cw1_MP1_BF/Cw1_MP2_BF/Cw1_MP3_BF/Cw1_MP4_BF/Cw1_MP5_BF
    #Cse_MP1_BF_SPM/Cse_MP2_BF_SPM/Cse_MP3_BF_SPM/Cse_MP4_BF_SPM/Cse_MP5_BF_SPM --> Cw1_MP1_BF_SPM/Cw1_MP2_BF_SPM/Cw1_MP3_BF_SPM/Cw1_MP4_BF_SPM/Cw1_MP5_BF_SPM
 
    #burial in deep sediment
    K34 = Sediment.k_burial   
    #Cse_MP1/Cse_MP2/Cse_MP3/Cse_MP4/Cse_MP5 --> 
    #Cse_MP1_SPM/Cse_MP2_SPM/Cse_MP3_SPM/Cse_MP4_SPM/Cse_MP5_SPM --> 
    #Cse_MP1_BF/Cse_MP2_BF/Cse_MP3_BF/Cse_MP4_BF/Cse_MP5_BF --> 
    #Cse_MP1_BF_SPM/Cse_MP2_BF_SPM/Cse_MP3_BF_SPM/Cse_MP4_BF_SPM/Cse_MP5_BF_SPM --> 
   
             
