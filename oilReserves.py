#!python3
"""
    Plot oil P,R,R/P historical data
"""
import numpy as np
import matplotlib.pyplot as plt
# Force use of TrueType fonts in pdfs for later editing
from matplotlib import rc
rc("pdf", fonttype=42)


filename = "../DATA/oil/bp-stats-review-2021-oil-summary_RS.csv"

year,production,reserves = np.loadtxt(filename,delimiter=',',skiprows=5,
                                      usecols=(0,1,2),unpack=True)

plt.figure(figsize=[10,5])
plt.plot(year,production)
plt.xlabel('Year')
plt.ylabel('Oil production (MMBL/day)')

plt.figure(figsize=[10,5])
plt.plot(year,reserves/1000)
plt.xlabel('Year')
plt.ylabel('Oil proven reserves (BMBL)')

RP = (reserves/production)/365.25
plt.figure(figsize=[10,5])
plt.plot(year,RP)
plt.xlabel('Year')
plt.ylabel('Oil R/P (years)')



