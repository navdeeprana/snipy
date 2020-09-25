import h5py

def read_dataset(fname,dset,return_numpy_array=False):
    f = h5py.File(fname,'r')
    if return_numpy_array:
        # Return as numpy array, where all data is read from disk.
        return f[dset][()]
    else:
        # Return as a dataset, I think it can load partial data.
        return f[dset]

def write_dataset(fname,data,dset):
    with h5py.File(fname,'w') as f:
        f.create_dataset(dset,data=data)
