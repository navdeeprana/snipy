import numpy as np
from scipy.optimize import curve_fit

def line(x,a,b):
    return a*x+b

def gaussian(x,A,mu,sigma):
    return (A/(np.sqrt(2*np.pi)*sigma))*np.exp(-0.5e0*((x-mu)/sigma)**2)

def fit_line(x,y):
    popt,pcov = curve_fit(line,x,y)
    return popt, np.sqrt(np.diag(pcov))

def fit_gaussian(x,y):
    popt,pcov = curve_fit(gaussian,x,y)
    return popt, np.sqrt(np.diag(pcov))

def fit_function(x,y,function):
    popt,pcov = curve_fit(function,x,y)
    return popt, np.sqrt(np.diag(pcov))

