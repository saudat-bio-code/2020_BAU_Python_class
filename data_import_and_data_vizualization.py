#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 00:12:54 2020

@author: saudaalishaeva

This is analysis of evolution of finches on Galapagos islands that was 
collected over fourty years.

Official reference to the publication of the dataset:
    Grant, Rosemary B., and Peter R. Grant. 
    “What Darwin's Finche Can Teach Us about the Evolutionary Origin and Regulation of Biodiversity.” 
    BioScience 53, 10 (2003): 965–975. http://bioscience.oxfordjournals.org/content/53/10/965.full.pdf.
 
"""

#importing needed modules
#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')
#%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

os.chdir("/Users/saudaalishaeva/Desktop/LastSemesterBAU/python/homework/darwins-finches-evolution-dataset")
#lets import the earliest measurements taken back 1975

data_1975 = pd.read_csv('finch_beaks_1975.csv',
                           usecols=['species',
                                    'Beak length, mm',
                                    'Beak depth, mm'])

data_1975.rename(columns={'Beak depth, mm': 'bdepth',
                             'Beak length, mm': 'blength'}, inplace=True)
data_1975['year'] = 1975

new_data_2012 = pd.read_csv('finch_beaks_2012.csv',
                           usecols=['species',
                                    'blength',
                                    'bdepth'])
new_data_2012['year'] = 2012

concatinated_data = pd.concat([data_1975, new_data_2012], ignore_index=True)

###DATA Vizulaization
#1
sns.set()  # Set Seaborn default plot style

# Isolating scandens beak depth, bdepth
y = concatinated_data.loc[concatinated_data['species'] == 'scandens', 'bdepth']
sns.swarmplot(x='year', y=y, data=concatinated_data)
plt.title('G. scandens Beak Depth: 1975 vs. 2012')
plt.xlabel('Year')
plt.ylabel('Beak depth (mm)');
#2
# Extracting beak length (blength) from original Data Frame
length_1975 = np.array(concatinated_data.loc[(concatinated_data['species'] == 'scandens') &
                               (concatinated_data['year'] == 1975),
                               'blength'])
length_2012 = np.array(concatinated_data.loc[(concatinated_data['species'] == 'scandens') &
                               (concatinated_data['year'] == 2012),
                               'blength'])
depth_1975 = np.array(concatinated_data.loc[(concatinated_data['species'] == 'scandens') &
                               (concatinated_data['year'] == 1975),
                               'bdepth'])
depth_2012 = np.array(concatinated_data.loc[(concatinated_data['species'] == 'scandens') &
                               (concatinated_data['year'] == 2012),
                               'bdepth'])

#before we go to plotting steps it is  good to check if extracted data have any NaNs
if np.isnan(depth_1975).any():
  print("Your input tables have missing data. Please remove NaNs before proceeding with the next step")    
if np.isnan(depth_2012).any():
  print("Your input tables have missing data. Please remove NaNs before proceeding with the next step")    
if np.isnan(length_1975).any():
  print("Your input tables have missing data. Please remove NaNs before proceeding with the next step")    
if np.isnan(length_2012).any():
  print("Your input tables have missing data. Please remove NaNs before proceeding with the next step")    

#if nothing is printed we can go to the plots

# scatter plots comparison of 1975 and 2012 data

plt.plot(length_1975, depth_1975, marker='.',
         linestyle='none', color='black', alpha=0.5)

plt.plot(length_2012, depth_2012, marker='.',
         linestyle='none', color='orange', alpha=0.5)

plt.title('Changes in beak depth to length ratio overtime. Measured in 1975 and 2012')
plt.xlabel('Length of Beaks [mm]')
plt.ylabel('Depth of Beaks [mm]')
plt.legend(('1975', '2012'), loc='lower right');

plt.show()
### next we want to vizualize average difference overtime using boxplots ###
depth_list = [depth_1975,depth_2012]
length_list = [length_1975,length_2012]
fig = plt.figure(1, figsize=(9, 6))
cpd_plot_ex= fig.add_subplot(111)
##depth boxplot
bplot = cpd_plot_ex.boxplot(depth_list,patch_artist=True)
cpd_plot_ex.set_xticklabels(['1975', '2012'])

for box in bplot['boxes']:
    # change outline color
    box.set( color='black', linewidth=2)
    # change fill color
    box.set( facecolor = 'yellow' )
    
#fig.savefig('fig.png', bbox_inches='tight')
plt.show()
fig.clf()
## length boxplot

length_box = plt.figure(1, figsize=(9, 6))
length_box_plot_ex= length_box.add_subplot(111)
bplot = length_box_plot_ex.boxplot(length_list,
    patch_artist=True)
length_box_plot_ex.set_xticklabels(['1975', '2012'])

for box in bplot['boxes']:
    # change outline color
    box.set( color='black', linewidth=2)
    # change fill color
    box.set( facecolor = 'green' )
    
plt.ylabel('Length of Beaks [mm]')
plt.show()
fig.clf()


