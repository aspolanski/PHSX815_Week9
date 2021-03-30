#!/usr/bin/env python3

#Default Modules:
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import os, glob, sys
from tqdm import tqdm
from astropy import units as u

#Other Modules:

from scipy.optimize import fmin, minimize
from mpl_toolkits.mplot3d import Axes3D
##### Author: Alex Polanski #####
#####  #####



def func(params):
    x, y = params
    return( (x-3)**2 + y**2 +1)


methods = ['Nelder-Mead', 'Powell', 'CG', 'BFGS']
func_evals = []

for i in methods:
    soln = minimize(func, [1,1],method=i)
    func_evals.append(soln.nfev)

print('Function Evals for Different Methods:\n')
for i in range(len(methods)):
    print(f'{methods[i]} : {func_evals[i]}\n')

x_plot = np.linspace(-1,5,1000)
y_plot = np.linspace(-5,5,1000)

X,Y = np.meshgrid(x_plot,y_plot)
z_plot = func([X,Y])



fig = plt.figure()
ax = fig.gca(projection='3d')
ax.contour(X,Y,z_plot, 50, cmap='coolwarm')
label = f'Minimum: ({soln.x[0]:0.2}, {soln.x[1]:0.2})'
ax.scatter(soln.x[0],soln.x[1],func(soln.x), marker ='o',c='red', label=label)
ax.set_zlim(-1,20)
ax.legend(loc = 'upper right')
plt.show()

