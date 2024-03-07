# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:14:37 2024

@author: Baalaji.Ravichandran
"""
#Import Pywake

import  py_wake
 # except ModuleNotFoundError:
  #  !pip install git+https://gitlab.windenergy.dtu.dk/TOPFARM/PyWake.git

# Importing Hornrev1Site
from py_wake.examples.data.hornsrev1 import Hornsrev1Site, V80, wt_x, wt_y, wt16_x, wt16_y
from py_wake import NOJ

#here we import the turbine, site and wake deficit model to use.
windTurbines = V80()
site = Hornsrev1Site()
noj = NOJ(site,windTurbines)


simulationResult = noj(wt16_x,wt16_y)    

simulationResult.aep()