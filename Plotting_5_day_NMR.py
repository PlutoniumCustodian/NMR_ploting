# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:55:31 2023

@author: Titus
"""

import nmrglue as ng
import matplotlib.pyplot as plt
import pandas as pd

#%% Names
names = pd.read_excel("Data/names.xlsx", index_col=0)

#%% Import data 27Al data
names = []
address = ["Data/5dayWashed/27Al_HPDEC_August2023/1/pdata/1","Data/5dayWashed/27Al_HPDEC_August2023/2/pdata/1",
          "Data/5dayWashed/27Al_HPDEC_August2023/3/pdata/1","Data/5dayWashed/27Al_HPDEC_August2023/4/pdata/1"]
Al_data = []
Al_ppm_scale = []

# reads data
for n in range(len(address)):
    dic,data = ng.bruker.read_pdata(address[n]) 
    Al_data.append(data)
    # makes array that is scale in ppm
    udic = ng.bruker.guess_udic(dic, data)
    uc = ng.fileiobase.uc_from_udic(udic)
    Al_ppm_scale.append(uc.ppm_scale()) 
    
#%% Import data 31P data
address2 = ["Data/5dayWashed/31P_HPDEC_August2023/1/pdata/1","Data/5dayWashed/31P_HPDEC_August2023/2/pdata/1",
          "Data/5dayWashed/31P_HPDEC_August2023/3/pdata/1","Data/5dayWashed/31P_HPDEC_August2023/4/pdata/1"]
P_data = []
P_ppm_scale = []

# reads data
for n in range(len(address2)):
    dic,data = ng.bruker.read_pdata(address2[n]) 
    P_data.append(data)
    # makes array that is scale in ppm
    udic = ng.bruker.guess_udic(dic, data)
    uc = ng.fileiobase.uc_from_udic(udic)
    P_ppm_scale.append(uc.ppm_scale()) 

#%% Plot

for n in range(len(address)):
    plt.plot(Al_ppm_scale[n], Al_data[n])
    
for n in range(len(address)):
    plt.plot(P_ppm_scale[n], P_data[n])


