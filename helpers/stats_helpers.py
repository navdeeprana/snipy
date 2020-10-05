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

