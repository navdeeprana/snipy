import numpy as np
import h5py

def binary_to_hdf5(filename,n):
    u,v = np.split(np.fromfile(filename,dtype=np.float64,count=2*n[0]*n[1]),2)
    u = u.reshape(n[0],n[1])
    v = v.reshape(n[0],n[1])
    with h5py.File(filename+'.h5','w') as f:
        f.create_dataset('x',data=u)
        f.create_dataset('y',data=v)

filename = sys.argv[1]
n        = int(sys.argv[2])
binary_to_hdf5(filename,n)
