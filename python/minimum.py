#!/usr/bin/env python3

#Default Modules:
import numpy as np
import pandas as pd
import scipy 
import matplotlib.pyplot as plt
import os, glob, sys
from tqdm import tqdm
from astropy import units as u

plt.style.use("/home/custom_style1.mplstyle")

#Other Modules:
from scipy.optimize import minimize 


##### Author: Alex Polanski #####

# define the function to minimize

def func(x):

    return(8 * x **4 + 3* x**3 +- 6 * x**2 +3)


# minimmize with two different initial guesses

soln1 = minimize(func, x0=[0.1])

soln2 = minimize(func, x0=[-0.5])


print(f'The minimum value obtained with an initial guess of 0.1 was {soln1.x[0]:0.3}.\n With an initial guess of -0.5 it was {soln2.x[0]:0.3}')


# Plot

x = np.linspace(-1.5,1,100)

plt.plot(x, func(x), color='blue')
plt.scatter(soln1.x[0], func(soln1.x[0]), c='red',s=100,label="Initial Guess: 0.1")
plt.scatter(soln2.x[0], func(soln2.x[0]), c='red',s=100,label="Initial Guess: -0.5")
plt.legend(loc='upper right')
plt.show()
