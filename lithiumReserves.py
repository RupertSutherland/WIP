#!python3
"""
    Plot lithium P,R,R/P historical data and model
    Dataset is in metric tons (MT)
"""
import numpy as np
import matplotlib.pyplot as plt
# Force use of TrueType fonts in pdfs for later editing
from matplotlib import rc
rc("pdf", fonttype=42)


filename = "../DATA/lithium/Li_mine_production.csv"

year,production,reserves = np.loadtxt(filename,delimiter=',',skiprows=3,
                                      usecols=(0,1,2),unpack=True)

eYear = np.load('../453notebooks/eYear.npy')
LiNeededThousandsOfTons = np.load('../453notebooks/LiNeededThousandsOfTons.npy')
sel = np.logical_and(eYear >= 2016, eYear <= 2030)

plt.figure(figsize=[10,5])
plt.scatter(year,production/1000)
plt.plot(eYear[sel],LiNeededThousandsOfTons[sel])
plt.xlabel('Year')
plt.ylabel('Lithium production (kMT/year)')

plt.figure(figsize=[10,5])
plt.plot(year,reserves/1e6)
plt.xlabel('Year')
plt.ylabel('Lithium proven reserves (MMT)')

RP = reserves/production
plt.figure(figsize=[10,5])
plt.plot(year,RP)
plt.xlabel('Year')
plt.ylabel('Lithium R/P (years)')



