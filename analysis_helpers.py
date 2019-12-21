import numpy as np
from scipy.optimize import curve_fit

def line(x,a,b):
    return a*x+b

def fit_line(x,y):
    popt,pcov = curve_fit(line,x,y)
    return popt, np.sqrt(np.diag(pcov))
