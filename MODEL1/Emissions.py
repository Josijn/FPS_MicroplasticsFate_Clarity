
import numpy as np
import math


def Initialization():
    # internal variable definition
    # initial concentrations - MP forms & locations
    # size bin 1: 0.1 um
    Cw1_MP1_0 = 0  # concentration of free MPs in MainWater, size bin 1
    Cws_MP1_0 = 0  # concentration of free MPs in SurfWater, size bin 1
    Cse_MP1_0 = 0  # concentration of free MPs in Sediment, size bin 1
    Cw1_MP1_SPM_0 = 0  # concentration of SPM-bound MPs in MainWater, size bin 1
    Cws_MP1_SPM_0 = 0  # concentration of SPM-bound MPs in SurfWater, size bin 1
    Cse_MP1_SPM_0 = 0  # concentration of SPM-bound MPs in Sediment, size bin 1
    Cw1_MP1_BF_0 = 0  # concentration of biofilm covered MPs in MainWater, size bin 1
    Cws_MP1_BF_0 = 0  # concentration of biofilm covered MPs in SurfWater, size bin 1
    Cse_MP1_BF_0 = 0  # concentration of biofilm covered MPs in Sediment, size bin 1
    Cw1_MP1_BF_SPM_0 = 0  # concentration of biofilm covered SPM-bound MPs in MainWater, size bin 1
    Cws_MP1_BF_SPM_0 = 0  # concentration of biofilm covered SPM-bound MPs in SurfWater, size bin 1
    Cse_MP1_BF_SPM_0 = 0  # concentration of biofilm covered SPM-bound MPs in Sediment, size bin 1

    # lists to store final concentrations
    # size bin 1: 0.1 um
    Cw1_MP1_final = []  # concentration of free MPs in MainWater, size bin 1
    Cws_MP1_final = []  # concentration of free MPs in SurfWater, size bin 1
    Cse_MP1_final = []  # concentration of free MPs in Sediment, size bin 1
    Cw1_MP1_SPM_final = []  # concentration of SPM-bound MPs in MainWater, size bin 1
    Cws_MP1_SPM_final = []  # concentration of SPM-bound MPs in SurfWater, size bin 1
    Cse_MP1_SPM_final = []  # concentration of SPM-bound MPs in Sediment, size bin 1
    Cw1_MP1_BF_final = []  # concentration of biofilm covered MPs in MainWater, size bin 1
    Cws_MP1_BF_final = []  # concentration of biofilm covered MPs in SurfWater, size bin 1
    Cse_MP1_BF_final = []  # concentration of biofilm covered MPs in Sediment, size bin 1
    Cw1_MP1_BF_SPM_final = []  # concentration of biofilm covered SPM-bound MPs in MainWater, size bin 1
    Cws_MP1_BF_SPM_final = []  # concentration of biofilm covered SPM-bound MPs in SurfWater, size bin 1
    Cse_MP1_BF_SPM_final = []  # concentration of biofilm covered SPM-bound MPs in Sediment, size bin 1
    return Cse_MP1_0, Cse_MP1_BF_0, Cse_MP1_BF_SPM_0, Cse_MP1_BF_SPM_final, Cse_MP1_BF_final, Cse_MP1_SPM_0, Cse_MP1_SPM_final, Cse_MP1_final, Cw1_MP1_0, Cw1_MP1_BF_0, Cw1_MP1_BF_SPM_0, Cw1_MP1_BF_SPM_final, Cw1_MP1_BF_final, Cw1_MP1_SPM_0, Cw1_MP1_SPM_final, Cw1_MP1_final, Cws_MP1_0, Cws_MP1_BF_0, Cws_MP1_BF_SPM_0, Cws_MP1_BF_SPM_final, Cws_MP1_BF_final, Cws_MP1_SPM_0, Cws_MP1_SPM_final, Cws_MP1_final
