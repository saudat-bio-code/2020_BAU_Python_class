#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# backward elimination
"""
first run with all features
then you remove features in x_opt one by one with huge p-values
"""

import numpy as np
import statsmodels.api as sm
import pandas as pd
#prep data
df_hp = pd.read_csv("Finches_dataset.csv")
sel_cols = ['First adult year','Last Year', 'Weight (g)', 'Band','Wing (mm)','Tarsus (mm)','Beak Length (mm)', 'Beak Depth (mm)','Beak Width (mm)' ]
df = df_hp[sel_cols]
x = df.iloc[:, : -1].values
y = df.iloc[: , 8].values

#first run with all features
x_opt = x[:, [0, 1, 2, 3, 4, 5, 6, 7]]
#our array has 100 rows. Therefore we assign to np.ones of 100
x = np.append(arr = np.ones((100, 1)).astype(float), values = x, axis = 1)
elim_regr = sm.OLS(y, x_opt).fit()
elim_regr.summary()
print(elim_regr.summary())

#then you remove features in x_opt one by one with huge p-values

#this is my last run
x_opt = x[:, [2, 3, 5, 7]]
#our array has 100 rows. Therefore we assign to np.ones of 100
x = np.append(arr = np.ones((100, 1)).astype(float), values = x, axis = 1)
elim_regr = sm.OLS(y, x_opt).fit()
elim_regr.summary()
print(elim_regr.summary())
x = df.iloc[:, : -1].values
y = df.iloc[: , 8].values
