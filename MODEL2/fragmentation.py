# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:30:38 2019

@author: AntoniaPraetorius
"""

#file containing functions for estimation of fragmentation rates for fixed size
#bins

import numpy as np
import math

size_d_bin_um = [0.1, 1, 10, 100, 1000] 
#create list with 5 size bins of fixed average diameter in micrometer

t_frag_d = [1, 10, 100, 1000, 10000]
#create list with fragmentation times for each size bin 
#in number of MPs fragementing per day


#function to estimate fragmentation relation between size bins
def frag_bin(size_d_bin_um, t_frag_d):
    bin_volumes = []
    



  self.k_frag_w = [math.log(2)/(num*24*60*60) for num in t_frag_w_1_d]
        #return self.k_frag_w
        #single line loop (https://blog.teamtreehouse.com/python-single-line-loops)
        #to calculate fragmentation rate constants from list of half-lives
      