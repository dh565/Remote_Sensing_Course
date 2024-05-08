#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
Created on Thu Feb  4 11:50:24 2021
@author: davidhelman
"""
"""
============================================================================
   Evaluate the emission intensity of a blackbody of temperature T as 
   a function of wavelength (Planck's function)
============================================================================
Inputs:
wl  :: numpy array containing wavelengths [m] 
T   :: temperature [K]

Outputs:
B   :: intensity [W sr**-1 m**-2 m**-1]
============================================================================
"""
import numpy as np
import matplotlib.pyplot as plt
#import scipy.constants as spc # {useful shortcuts, including h, c, and kB}

# ========================================================================= #
# Planck Function:
# ========================================================================= #
def PlanckFunc(wl,T): 
    wl = np.array(wl)   # if the input is a list or a tuple, make it an array
    
    # {comment if import scipy.constants}:
    h  = 6.625e-34      # Planck constant [J s] 
    c  = 3e8            # speed of light [m s**−1] 
    kB = 1.38e-23       # Boltzmann constant [J K**−1] 
    
    # This is Planck's function:
    B  = ((2*h*c**2)/(wl**5))/(np.exp((h*c)/(wl*kB*T))-1) 
    
    # {uncomment next line if import scipy.constants}:
    # B = ((2*spc.h*spc.c**2)/(wl**5))/(np.exp((spc.h*spc.c)/(wl*spc. k*T)) -1)
    return B
