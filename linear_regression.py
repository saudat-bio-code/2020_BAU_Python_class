#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 2020
"""

###Linear regression
#function ----

def draw_bs_pairs_linreg(x, y, size=1):
    """
    Perform pairs bootstrap for linear regression.
    Params: x-data, y-data, size
    """

    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))

    # Initialize replicates
    bs_slope_reps = np.empty(size)
    bs_intercept_reps = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, size=len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_slope_reps[i], bs_intercept_reps[i] = np.polyfit(bs_x, bs_y, 1)

    return bs_slope_reps, bs_intercept_reps
####
slope_1975, intercept_1975 = np.polyfit(length_1975, depth_1975, 1)
slope_2012, intercept_2012 = np.polyfit(length_2012, depth_2012, 1)

bs_slope_reps_1975, bs_intercept_reps_1975 = \
        draw_bs_pairs_linreg(length_1975, depth_1975, 1000)
bs_slope_reps_2012, bs_intercept_reps_2012 = \
        draw_bs_pairs_linreg(length_2012, depth_2012, 1000)

slope_conf_int_1975 = np.percentile(bs_slope_reps_1975, [2.5, 97.5])
slope_conf_int_2012 = np.percentile(bs_slope_reps_2012, [2.5, 97.5])
intercept_conf_int_1975 = np.percentile(bs_intercept_reps_1975, [2.5, 97.5])
intercept_conf_int_2012 = np.percentile(bs_intercept_reps_2012, [2.5, 97.5])

print('1975: slope =', slope_1975,
      '95% conf int =', slope_conf_int_1975)
print('1975: intercept =', intercept_1975,
      '95% conf int =', intercept_conf_int_1975)
print('2012: slope =', slope_2012,
      '95% conf int =', slope_conf_int_2012)
print('2012: intercept =', intercept_2012,
      '95% conf int =', intercept_conf_int_2012)

#now plot it
plt.plot(length_1975, depth_1975, marker='.',
         linestyle='none', color='blue', alpha=0.5)

plt.plot(length_2012, depth_2012, marker='.',
         linestyle='none', color='red', alpha=0.5)

plt.title('Linear regressions of G. scandens beak depth vs length')
plt.xlabel('beak length (mm)')
plt.ylabel('beak depth (mm)')
plt.legend(('1975', '2012'), loc='upper left')
plt.show()
