# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:42:59 2020

@author: Akash S
"""

import pandas as pd
import numpy as np

#Read Local temperature and Global temperature into dataframe
df = pd.read_csv("Bengaluru.csv")

df_gloabl = pd.read_csv("Gloabl.csv")

df.columns

df['avg_temp'].describe()

#Replace nan with average temperature
df['avg_temp'] = df['avg_temp'].fillna(24.05)

#min_periods=1, center=True, 

#Create column with moving averages
df['Bnglr_Avg_temp'] = df.iloc[:,3].rolling(window=6).mean()

df = df[['year','Bnglr_Avg_temp']]

#df['Bnglr_Avg_temp1'] = df.iloc[:,3].rolling(min_periods=1, center=True,window=6).mean()

df_gloabl.columns

df_gloabl['Global_Avg_temp'] = df_gloabl['avg_temp'].rolling(window=6).mean()

df_gloabl = df_gloabl[['year','Global_Avg_temp']]


#merge and create single dataframe
s1 = pd.merge(df_gloabl, df, how='left', on=['year'])

#Line Graph
import matplotlib.pyplot as plt
# create figure and axis objects with subplots()
fig,ax = plt.subplots()
# make a plot
ax.plot(s1.year, s1.Global_Avg_temp, color="red", marker=".")
# set x-axis label
ax.set_xlabel("Year",fontsize=14)
# set y-axis label
ax.set_ylabel("Global Temperature $^\circ$C",color="red",fontsize=14)

ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(s1.year, s1["Bnglr_Avg_temp"],color="blue",marker=".")
ax2.set_ylabel("Bangalore Temperature $^\circ$C",color="blue",fontsize=14)
ax2.set_title("Bangalore Vs Global Average Temperature")
plt.show()
# save the plot as a file
fig.savefig('Weather Trends.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')



s1_copy = s1.copy()

s1_copy = s1_copy.fillna(0)

import scipy.stats
scipy.stats.linregress(s1_copy['Global_Avg_temp'][(s1['year']>=1801) & (s1['year']<=2013)], s1_copy['Bnglr_Avg_temp'][(s1['year']>=1801) & (s1['year']<=2013)])

s1['Bnglr_Avg_temp'].max()
s1['Bnglr_Avg_temp'].min()
s1['Global_Avg_temp'].max()
s1['Global_Avg_temp'].min()
