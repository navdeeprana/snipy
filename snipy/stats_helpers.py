import glob
import numpy as np

def ensemble_average(pattern,std=True,**kwargs):
    files = sorted(glob.glob(pattern))
    data  = np.asarray([np.loadtxt(f,**kwargs) for f in files])
    if std:
        return data.mean(axis=0), data.std(axis=0)
    else:
        return data.mean(axis=0)

def histogram(data,**kwargs):
    h,e = np.histogram(data,**kwargs)
    return 0.5e0*(e[1:]+e[:-1]), h

def histogram_to_pdf(x,px):
    psum = np.sum(px*(x[-1]-x[0]))/len(x)
    return x, px/psum

def get_mean_std(x,px):
    L,N  = x[-1]-x[0], len(x)
    DX   = L/N
    mean = np.sum((x)*px*DX)
    std  = np.sqrt(np.sum((x-mean)**2*px*DX))
    return mean,std

def normalize_histogram(x,px):
    x,px=histogram_to_pdf(x,px)
    m,s = get_mean_std(x,px)
    return (x-m)/s, px*s

def pdf_gaussian(x,mu,sigma):
    return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5e0*((x-mu)/sigma)**2)
