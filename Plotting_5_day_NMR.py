# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:55:31 2023

@author: Titus
"""

import nmrglue as ng
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
from matplotlib.patches import Rectangle

#%% Names
names = pd.read_excel("Data/names.xlsx", index_col=0)

#%% Import data 27Al data
names = []
address = ["Data/5dayWashed/27Al_HPDEC_August2023/217/pdata/1","Data/5dayWashed/27Al_HPDEC_August2023/218/pdata/1",
          "Data/5dayWashed/27Al_HPDEC_August2023/220/pdata/1","Data/5dayWashed/27Al_HPDEC_August2023/222/pdata/1"]
howmany = range(len(address))
Al_data = []
Al_ppm_scale = []

# reads data
for n in howmany:
    dic,data = ng.bruker.read_pdata(address[n]) 
    Al_data.append(data)
    # makes array that is scale in ppm
    udic = ng.bruker.guess_udic(dic, data)
    uc = ng.fileiobase.uc_from_udic(udic)
    Al_ppm_scale.append(uc.ppm_scale()) 
    
#%% Import data 31P data
address2 = ["Data/5dayWashed/31P_HPDEC_August2023/217/pdata/1","Data/5dayWashed/31P_HPDEC_August2023/218/pdata/1",
          "Data/5dayWashed/31P_HPDEC_August2023/220/pdata/1","Data/5dayWashed/31P_HPDEC_August2023/222/pdata/1"]
P_data = []
P_ppm_scale = []

# reads data
for n in howmany:
    dic,data = ng.bruker.read_pdata(address2[n]) 
    P_data.append(data)
    # makes array that is scale in ppm
    udic = ng.bruker.guess_udic(dic, data)
    uc = ng.fileiobase.uc_from_udic(udic)
    P_ppm_scale.append(uc.ppm_scale()) 

#%% Plot Al fig

#Use this file to set style
plt.style.use('./style/publish2.mplstyle')

fig, ax = plt.subplots()
# fig.set_figwidth(1.75) #size is in inches
offs = 5.5e6
ax.plot(Al_ppm_scale[0], Al_data[0] + offs * 2, color='#58a265') #M-Mg, Mg-Axial
ax.plot(Al_ppm_scale[1], Al_data[1] + offs * 3, color='#0e0e77')  # H-Al, Al-Corner
ax.plot(Al_ppm_scale[2], Al_data[2] + offs * 1, color='#000000') # H-P, cent
ax.plot(Al_ppm_scale[3], Al_data[3] + offs * 0, color='#626161') #L-P, Phil-Mist

ax.spines[['right', 'top']].set_visible(False) #,'left'
ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
ax.set_xlim([-20, 80])
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim([-0.2e7,3.3e7])
ax.set_xlabel("Chemical shift (ppm)")
ax.set_ylabel("Intensity")
ax.invert_xaxis()
# fig.savefig('Plots/Washed_5day_27Al_NMR.svg', transparent=False, bbox_inches="tight")

#%% Plot P fig
fig, ax = plt.subplots()
# fig.set_figwidth(1.75) #size is in inches
# fig.set_figheight(5) #size is in inches
offs = 3.5e6
ax.plot(P_ppm_scale[0], P_data[0] + offs * 2, color='#58a265') #M-Mg, Mg-Axial
ax.plot(P_ppm_scale[1], P_data[1] + offs * 1, color='#0e0e77')  # H-Al, Al-Corner
ax.plot(P_ppm_scale[2], P_data[2] + offs * 3, color='#000000') # H-P, cent
ax.plot(P_ppm_scale[3], P_data[3] + offs * 0, color='#626161') #L-P, Phil-Mist

ax.spines[['right', 'top']].set_visible(False) #,'left'
ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim([-55, 15]) #-25, 15
ax.set_ylim([-0.1e7,2.1e7])
ax.set_xlabel("Chemical shift (ppm)")
ax.set_ylabel("Intensity")
ax.invert_xaxis()

# fig.savefig('Plots/Washed_5day_31P_NMR_alt.svg', transparent=False, bbox_inches="tight")

#%% Plot single for inset
fig, ax = plt.subplots()
fig.set_figwidth(1) #size is in inches
fig.set_figheight(1) #size is in inches

ax.plot(P_ppm_scale[1], P_data[1], color='#0e0e77')  # H-Al, Al-Corner

ax.spines[['right','left', 'top']].set_visible(False)
ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
ax.set_xlim([-10, 10])
# ax.set_xlabel("Chemical shift (ppm)")
ax.invert_xaxis()
# fig.savefig('Plots/Washed_5day_31P_NMR_H_AL.svg', transparent=False, bbox_inches="tight")

#%% Plot single for H-Al
fig, ax = plt.subplots()
# fig.set_figwidth(1) #size is in inches
# fig.set_figheight(1) #size is in inches

ax.plot(P_ppm_scale[1], P_data[1], color='#0e0e77')  # H-Al, Al-Corner

ax.spines[['right', 'top']].set_visible(False)
ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim([-10, 10])
ax.set_xlabel("Chemical shift (ppm)")
ax.invert_xaxis()
# fig.savefig('Plots/Washed_5day_31P_NMR_H_AL_big.svg', transparent=False, bbox_inches="tight")

#%% Plot single for H-Al
fig, ax = plt.subplots()
# fig.set_figwidth(1) #size is in inches
# fig.set_figheight(1) #size is in inches

ax.plot(P_ppm_scale[0], P_data[0] + offs * 2, color='#58a265') #M-Mg, Mg-Axial

ax.spines[['right', 'top']].set_visible(False)
ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim([-50, 10])
ax.set_xlabel("Chemical shift (ppm)")
ax.invert_xaxis()
# fig.savefig('Plots/Washed_5day_31P_NMR_M-Mg_big.svg', transparent=False, bbox_inches="tight")

#%% Plot P fig version two with rectangles
#Use this file to set style

plt.style.use('./style/publish2.mplstyle')
fig, ax = plt.subplots()

offs = 3.5e6
ax.plot(P_ppm_scale[0], P_data[0] + offs * 2, color='#58a265') #M-Mg, Mg-Axial
ax.plot(P_ppm_scale[1], P_data[1] + offs * 1, color='#0e0e77')  # H-Al, Al-Corner
ax.plot(P_ppm_scale[2], P_data[2] + offs * 3, color='#000000') # H-P, cent
ax.plot(P_ppm_scale[3], P_data[3] + offs * 0, color='#626161') #L-P, Phil-Mist

ylim = 2.4e7
ax.spines[['right', 'top']].set_visible(False) #,'left'
ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim([-55, 15]) #-25, 15
ax.set_ylim([-0.1e7,ylim])
ax.set_xlabel("Chemical shift (ppm)")
ax.set_ylabel("Intensity")
clr = '#262626'
rh = 1.7e6 #retangle height
lnsp = ylim - rh * 1.6
gp = 1.5e5
ax.add_patch(Rectangle((-2,lnsp-gp), 14, -rh, color=clr)) #Q0
ax.add_patch(Rectangle((-15,lnsp+gp), 18, rh, color=clr)) #Q1
ax.add_patch(Rectangle((-38,lnsp-gp), 23, -rh, color=clr)) #Q2
ax.add_patch(Rectangle((-50,lnsp+gp), 15, rh, color=clr)) #Q3
# ax.add_patch(Rectangle((-6,lnsp-rh), 6, -rh, color=clr, ec='w')) # inersphere
ax.invert_xaxis()

fig.savefig('Plots/Washed_5day_31P_NMR_alt2.svg', transparent=False, bbox_inches="tight")