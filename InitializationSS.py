
def initSS(MainWater, Sediment, SurfWater):
    # heteroaggregation of pristine MPs in main water (for each size bin)
    K1 = MainWater.k_hetAgg_1  # Cw1_MP1 --> Cw1_MP1_SPM
    K2 = MainWater.k_hetAgg_2  # Cw1_MP2 --> Cw1_MP2_SPM
    K3 = MainWater.k_hetAgg_3  # Cw1_MP3 --> Cw1_MP3_SPM
    K4 = MainWater.k_hetAgg_4  # Cw1_MP4 --> Cw1_MP4_SPM
    K5 = MainWater.k_hetAgg_5  # Cw1_MP5 --> Cw1_MP5_SPM
    # heteroaggregation of biofilm covered MPs in main water (for each size bin)
    K1B = MainWater.k_hetAgg_1B  # Cw1_MP1_BF --> Cw1_MP1_BF_SPM
    K2B = MainWater.k_hetAgg_2B  # Cw1_MP2_BF --> Cw1_MP2_BF_SPM
    K3B = MainWater.k_hetAgg_3B  # Cw1_MP3_BF --> Cw1_MP3_BF_SPM
    K4B = MainWater.k_hetAgg_4B  # Cw1_MP4_BF --> Cw1_MP4_BF_SPM
    K5B = MainWater.k_hetAgg_5B  # Cw1_MP5_BF --> Cw1_MP5_BF_SPM
    # breakup of MP-SPM heteroaggregates in main water (for each size bin)
    K6 = MainWater.k_aggBreakup_1  # Cw1_MP1_SPM --> Cw1_MP1
    K7 = MainWater.k_aggBreakup_2  # Cw1_MP2_SPM --> Cw1_MP2
    K8 = MainWater.k_aggBreakup_3  # Cw1_MP3_SPM --> Cw1_MP3
    K9 = MainWater.k_aggBreakup_4  # Cw1_MP4_SPM --> Cw1_MP4
    K10 = MainWater.k_aggBreakup_5  # Cw1_MP5_SPM --> Cw1_MP5
    # breakup of biofilm covered MP-SPM heteroaggregates in main water (for each size bin)
    K6B = MainWater.k_aggBreakup_1B  # Cw1_MP1_BF_SPM --> Cw1_MP1_BF
    K7B = MainWater.k_aggBreakup_2B  # Cw1_MP2_BF_SPM --> Cw1_MP2_BF
    K8B = MainWater.k_aggBreakup_3B  # Cw1_MP3_BF_SPM --> Cw1_MP3_BF
    K9B = MainWater.k_aggBreakup_4B  # Cw1_MP4_BF_SPM --> Cw1_MP4_BF
    K10B = MainWater.k_aggBreakup_5B  # Cw1_MP5_BF_SPM --> Cw1_MP5_BF
    # settling of pristine MPs from main water to sediment (for each size bin)
    K11 = MainWater.k_set_Stokes_MP1  # Cw1_MP1 --> Cse_MP1
    K12 = MainWater.k_set_Stokes_MP2  # Cw1_MP2 --> Cse_MP2
    K13 = MainWater.k_set_Stokes_MP3  # Cw1_MP3 --> Cse_MP3
    K14 = MainWater.k_set_Stokes_MP4  # Cw1_MP4 --> Cse_MP4
    K15 = MainWater.k_set_Stokes_MP5  # Cw1_MP5 --> Cse_MP5
    # settling of SPM-bound MPs from main water to sediment (for each size bin)
    K11B = MainWater.k_set_Stokes_MP1SPM  # Cw1_MP1_SPM --> Cse_MP1_SPM
    K12B = MainWater.k_set_Stokes_MP2SPM  # Cw1_MP2_SPM --> Cse_MP2_SPM
    K13B = MainWater.k_set_Stokes_MP3SPM  # Cw1_MP3_SPM --> Cse_MP3_SPM
    K14B = MainWater.k_set_Stokes_MP4SPM  # Cw1_MP4_SPM --> Cse_MP4_SPM
    K15B = MainWater.k_set_Stokes_MP5SPM  # Cw1_MP5_SPM --> Cse_MP5_SPM
    # settling of biofilm covered MPs from main water to sediment (for each size bin)
    K11C = MainWater.k_set_Stokes_MP1BF  # Cw1_MP1_BF --> Cse_MP1_BF
    K12C = MainWater.k_set_Stokes_MP2BF  # Cw1_MP2_BF --> Cse_MP2_BF
    K13C = MainWater.k_set_Stokes_MP3BF  # Cw1_MP3_BF --> Cse_MP3_BF
    K14C = MainWater.k_set_Stokes_MP4BF  # Cw1_MP4_BF --> Cse_MP4_BF
    K15C = MainWater.k_set_Stokes_MP5BF  # Cw1_MP5_BF --> Cse_MP5_BF
    # settling of biofilm covered SPM-bound MPs from main water to sediment (for each size bin)
    K11D = MainWater.k_set_Stokes_MP1BFSPM  # Cw1_MP1_BF_SPM --> Cse_MP1_BF_SPM
    K12D = MainWater.k_set_Stokes_MP2BFSPM  # Cw1_MP2_BF_SPM --> Cse_MP2_BF_SPM
    K13D = MainWater.k_set_Stokes_MP3BFSPM  # Cw1_MP3_BF_SPM --> Cse_MP3_BF_SPM
    K14D = MainWater.k_set_Stokes_MP4BFSPM  # Cw1_MP4_BF_SPM --> Cse_MP4_BF_SPM
    K15D = MainWater.k_set_Stokes_MP5BFSPM  # Cw1_MP5_BF_SPM --> Cse_MP5_BF_SPM
    # settling of pristine MPs from water surface to main water (for each size bin)
    K16 = SurfWater.k_set_Stokes_MP1  # Cws_MP1 --> Cw1_MP1
    K17 = SurfWater.k_set_Stokes_MP2  # Cws_MP2 --> Cw1_MP2
    K18 = SurfWater.k_set_Stokes_MP3  # Cws_MP3 --> Cw1_MP3
    K19 = SurfWater.k_set_Stokes_MP4  # Cws_MP4 --> Cw1_MP4
    K20 = SurfWater.k_set_Stokes_MP5  # Cws_MP5 --> Cw1_MP5
    # settling of SPM-bound MPs from water surface to main water (for each size bin)
    K16B = SurfWater.k_set_Stokes_MP1SPM  # Cws_MP1_SPM --> Cw1_MP1_SPM
    K17B = SurfWater.k_set_Stokes_MP2SPM  # Cws_MP2_SPM --> Cw1_MP2_SPM
    K18B = SurfWater.k_set_Stokes_MP3SPM  # Cws_MP3_SPM --> Cw1_MP3_SPM
    K19B = SurfWater.k_set_Stokes_MP4SPM  # Cws_MP4_SPM --> Cw1_MP4_SPM
    K20B = SurfWater.k_set_Stokes_MP5SPM  # Cws_MP5_SPM --> Cw1_MP5_SPM
    # settling of biofilm covered MPs from water surface to main water (for each size bin)
    K16C = SurfWater.k_set_Stokes_MP1BF  # Cws_MP1_BF --> Cw1_MP1_BF
    K17C = SurfWater.k_set_Stokes_MP2BF  # Cws_MP2_BF --> Cw1_MP2_BF
    K18C = SurfWater.k_set_Stokes_MP3BF  # Cws_MP3_BF --> Cw1_MP3_BF
    K19C = SurfWater.k_set_Stokes_MP4BF  # Cws_MP4_BF --> Cw1_MP4_BF
    K20C = SurfWater.k_set_Stokes_MP5BF  # Cws_MP5_BF --> Cw1_MP5_BF
    # settling of biofilm covered SPM-bound MPs from water surface to main water (for each size bin)
    K16D = SurfWater.k_set_Stokes_MP1BFSPM  # Cws_MP1_BF_SPM --> Cw1_MP1_BF_SPM
    K17D = SurfWater.k_set_Stokes_MP2BFSPM  # Cws_MP2_BF_SPM --> Cw1_MP2_BF_SPM
    K18D = SurfWater.k_set_Stokes_MP3BFSPM  # Cws_MP3_BF_SPM --> Cw1_MP3_BF_SPM
    K19D = SurfWater.k_set_Stokes_MP4BFSPM  # Cws_MP4_BF_SPM --> Cw1_MP4_BF_SPM
    K20D = SurfWater.k_set_Stokes_MP5BFSPM  # Cws_MP5_BF_SPM --> Cw1_MP5_BF_SPM
    # rising of pristine MPs from main water to water surface (for each size bin)
    K21 = MainWater.k_rise_Stokes_MP1  # Cw1_MP1 --> Cws_MP1
    K22 = MainWater.k_rise_Stokes_MP2  # Cw1_MP2 --> Cws_MP2
    K23 = MainWater.k_rise_Stokes_MP3  # Cw1_MP3 --> Cws_MP3
    K24 = MainWater.k_rise_Stokes_MP4  # Cw1_MP4 --> Cws_MP4
    K25 = MainWater.k_rise_Stokes_MP5  # Cw1_MP5 --> Cws_MP5
    # rising of SPM-bound MPs from main water to water surface (for each size bin)
    K21B = MainWater.k_rise_Stokes_MP1SPM  # Cw1_MP1_SPM --> Cws_MP1_SPM
    K22B = MainWater.k_rise_Stokes_MP2SPM  # Cw1_MP2_SPM --> Cws_MP2_SPM
    K23B = MainWater.k_rise_Stokes_MP3SPM  # Cw1_MP3_SPM --> Cws_MP3_SPM
    K24B = MainWater.k_rise_Stokes_MP4SPM  # Cw1_MP4_SPM --> Cws_MP4_SPM
    K25B = MainWater.k_rise_Stokes_MP5SPM  # Cw1_MP5_SPM --> Cws_MP5_SPM
    # rising of biofilm covered MPs from main water to water surface (for each size bin)
    K21C = MainWater.k_rise_Stokes_MP1BF  # Cw1_MP1_BF --> Cws_MP1_BF
    K22C = MainWater.k_rise_Stokes_MP2BF  # Cw1_MP2_BF --> Cws_MP2_BF
    K23C = MainWater.k_rise_Stokes_MP3BF  # Cw1_MP3_BF --> Cws_MP3_BF
    K24C = MainWater.k_rise_Stokes_MP4BF  # Cw1_MP4_BF --> Cws_MP4_BF
    K25C = MainWater.k_rise_Stokes_MP5BF  # Cw1_MP5_BF --> Cws_MP5_BF
    # rising of biofilm covered SPM-bound MPs from main water to water surface (for each size bin)
    K21D = MainWater.k_rise_Stokes_MP1BFSPM  # Cw1_MP1_BF_SPM --> Cws_MP1_BF_SPM
    K22D = MainWater.k_rise_Stokes_MP2BFSPM  # Cw1_MP2_BF_SPM --> Cws_MP2_BF_SPM
    K23D = MainWater.k_rise_Stokes_MP3BFSPM  # Cw1_MP3_BF_SPM --> Cws_MP3_BF_SPM
    K24D = MainWater.k_rise_Stokes_MP4BFSPM  # Cw1_MP4_BF_SPM --> Cws_MP4_BF_SPM
    K25D = MainWater.k_rise_Stokes_MP5BFSPM  # Cw1_MP5_BF_SPM --> Cws_MP5_BF_SPM
    # fragmentation of pristine MPs from 1 size bin to another, in main water
    K26 = MainWater.k_frag_MP1  # Cw1_MP1 --> (nothing, treated as complete degradation currently)
    K27 = MainWater.k_frag_MP2  # Cw1_MP2 --> Cw1_MP1
    K28 = MainWater.k_frag_MP3  # Cw1_MP3 --> Cw1_MP2
    K29 = MainWater.k_frag_MP4  # Cw1_MP4 --> Cw1_MP3
    K30 = MainWater.k_frag_MP5  # Cw1_MP5 --> Cw1_MP4
    # fragmentation of pristine MPs from 1 size bin to another, in surface water
    K26B = SurfWater.k_frag_MP1  # Cws_MP1 --> (nothing, treated as complete degradation currently)
    K27B = SurfWater.k_frag_MP2  # Cws_MP2 --> Cws_MP1
    K28B = SurfWater.k_frag_MP3  # Cws_MP3 --> Cws_MP2
    K29B = SurfWater.k_frag_MP4  # Cws_MP4 --> Cws_MP3
    K30B = SurfWater.k_frag_MP5  # Cws_MP5 --> Cws_MP4
    # advective flow out of the main water compartment
    K31 = MainWater.k_outflow  # Cw1_MP1/Cw1_MP2/Cw1_MP3/Cw1_MP4/Cw1_MP5 -->
    # Cw1_MP1/Cw1_MP2/Cw1_MP3/Cw1_MP4/Cw1_MP5 -->
    # Cw1_MP1_SPM/Cw1_MP2_SPM/Cw1_MP3_SPM/Cw1_MP4_SPM/Cw1_MP5_SPM -->
    # Cw1_MP1_BF/Cw1_MP2_BF/Cw1_MP3_BF/Cw1_MP4_BF/Cw1_MP5_BF -->
    # Cw1_MP1_BF_SPM/Cw1_MP2_BF_SPM/Cw1_MP3_BF_SPM/Cw1_MP4_BF_SPM/Cw1_MP5_BF_SPM -->
    # advective flow out of the surface water compartment
    K32 = SurfWater.k_outflow  # Cws_MP1/Cws_MP2/Cws_MP3/Cws_MP4/Cws_MP5 -->
    # Cws_MP1/Cws_MP2/Cws_MP3/Cws_MP4/Cws_MP5 -->
    # Cws_MP1_SPM/Cws_MP2_SPM/Cws_MP3_SPM/Cws_MP4_SPM/Cws_MP5_SPM -->
    # Cws_MP1_BF/Cws_MP2_BF/Cws_MP3_BF/Cws_MP4_BF/Cws_MP5_BF -->
    # Cws_MP1_BF_SPM/Cws_MP2_BF_SPM/Cws_MP3_BF_SPM/Cws_MP4_BF_SPM/Cws_MP5_BF_SPM -->
    # sediment resuspension
    K33 = Sediment.k_resusp
    # Cse_MP1/Cse_MP2/Cse_MP3/Cse_MP4/Cse_MP5 --> Cw1_MP1/Cw1_MP2/Cw1_MP3/Cw1_MP4/Cw1_MP5
    # Cse_MP1_SPM/Cse_MP2_SPM/Cse_MP3_SPM/Cse_MP4_SPM/Cse_MP5_SPM --> Cw1_MP1_SPM/Cw1_MP2_SPM/Cw1_MP3_SPM/Cw1_MP4_SPM/Cw1_MP5_SPM
    # Cse_MP1_BF/Cse_MP2_BF/Cse_MP3_BF/Cse_MP4_BF/Cse_MP5_BF --> Cw1_MP1_BF/Cw1_MP2_BF/Cw1_MP3_BF/Cw1_MP4_BF/Cw1_MP5_BF
    # Cse_MP1_BF_SPM/Cse_MP2_BF_SPM/Cse_MP3_BF_SPM/Cse_MP4_BF_SPM/Cse_MP5_BF_SPM --> Cw1_MP1_BF_SPM/Cw1_MP2_BF_SPM/Cw1_MP3_BF_SPM/Cw1_MP4_BF_SPM/Cw1_MP5_BF_SPM
    # burial in deep sediment
    K34 = Sediment.k_burial
    # Cse_MP1/Cse_MP2/Cse_MP3/Cse_MP4/Cse_MP5 -->
    # Cse_MP1_SPM/Cse_MP2_SPM/Cse_MP3_SPM/Cse_MP4_SPM/Cse_MP5_SPM -->
    # Cse_MP1_BF/Cse_MP2_BF/Cse_MP3_BF/Cse_MP4_BF/Cse_MP5_BF -->
    # Cse_MP1_BF_SPM/Cse_MP2_BF_SPM/Cse_MP3_BF_SPM/Cse_MP4_BF_SPM/Cse_MP5_BF_SPM -->
    # biofilm formation on pristine MPs in main water (for each size bin)
    K35 = MainWater.k_biofilm_1  # Cw1_MP1 --> Cw1_MP1_SPM
    K36 = MainWater.k_biofilm_2  # Cw1_MP2 --> Cw1_MP2_SPM
    K37 = MainWater.k_biofilm_3  # Cw1_MP3 --> Cw1_MP3_SPM
    K38 = MainWater.k_biofilm_4  # Cw1_MP4 --> Cw1_MP4_SPM
    K39 = MainWater.k_biofilm_5  # Cw1_MP5 --> Cw1_MP5_SPM
    # biofilm formation on pristine MPs in surface water (for each size bin)
    K35B = SurfWater.k_biofilm_1  # Cws_MP1 --> Cws_MP1_SPM
    K36B = SurfWater.k_biofilm_2  # Cws_MP2 --> Cws_MP2_SPM
    K37B = SurfWater.k_biofilm_3  # Cws_MP3 --> Cws_MP3_SPM
    K38B = SurfWater.k_biofilm_4  # Cws_MP4 --> Cws_MP4_SPM
    K39B = SurfWater.k_biofilm_5  # Cws_MP5 --> Cws_MP5_SPM
    return K1, K10, K10B, K11, K11B, K11C, K11D, K12, K12B, K12C, K12D, K13, K13B, K13C, K13D, K14, K14B, K14C, K14D, K15, K15B, K15C, K15D, K16, K16B, K16C, K16D, K17, K17B, K17C, K17D, K18, K18B, K18C, K18D, K19, K19B, K19C, K19D, K1B, K2, K20, K20B, K20C, K20D, K21, K21B, K21C, K21D, K22, K22B, K22C, K22D, K23, K23B, K23C, K23D, K24, K24B, K24C, K24D, K25, K25B, K25C, K25D, K26, K26B, K27, K27B, K28, K28B, K29, K29B, K2B, K3, K30, K30B, K31, K32, K33, K34, K35, K35B, K36, K36B, K37, K37B, K38, K38B, K39, K39B, K3B, K4, K4B, K5, K5B, K6, K6B, K7, K7B, K8, K8B, K9, K9B
