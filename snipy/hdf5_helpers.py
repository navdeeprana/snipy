import os
import h5py

def read_dataset(fname,dset,return_numpy_array=False):
    f = h5py.File(fname,'r')
    if return_numpy_array:
        # Return as numpy array, where all data is read from disk.
        return f[dset][()]
    else:
        # Return as a dataset, I think it can load partial data.
        return f[dset]

def write_dataset(fname,dsets,names):
    with h5py.File(fname,'w') as f:
        for name, dset in zip(names,dsets):
            f.create_dataset(name,data=dset)

def generate_xdmf(fname):
    def xdmf_write(xdmf,string,level=0,width=2):
        xdmf.write(string.rjust(len(string)+width*level,' ')+'\n')

    f      = h5py.File(fname,'r')
    dsets  = [key for key in f.keys()]
    shapes = [f[d].shape for d in dsets]

    print(dsets, shapes[0])

    n    = shapes[0]
    fnameabs = os.path.abspath(fname)
    with open(fname.replace('.h5','.xdmf'),'w') as xdmf:
        xdmf_write(xdmf,f'<?xml version="1.0" ?>')
        xdmf_write(xdmf,f'<!DOCTYPE Xdmf SYSTEM "Xdmf.dtd" []>')
        xdmf_write(xdmf,f'<Xdmf xmlns:xi="http://www.w3.org/2003/XInclude" Version="2.2">')
        xdmf_write(xdmf,f'<Domain>',level=1)
        xdmf_write(xdmf,f'<Grid Name="Vector" GridType="Uniform">',level=2)
        xdmf_write(xdmf,f'<Topology TopologyType="3DCORECTMesh" NumberOfElements="{n[0]} {n[1]} {n[2]}" />',level=3)
        xdmf_write(xdmf,f'<Geometry GeometryType="ORIGIN_DXDYDZ">',level=3)
        xdmf_write(xdmf,f'<DataItem Name="origin" Dimensions="3" NumberType="Float" Precision="8" Format="XML"> 0.0 0.0 0.0 </DataItem>',level=4)
        xdmf_write(xdmf,f'<DataItem Name="spacing" Dimensions="3" NumberType="Float" Precision="8" Format="XML"> 1.0 1.0 1.0 </DataItem>',level=4)
        xdmf_write(xdmf,f'</Geometry>',level=3)
        xdmf_write(xdmf,f'<Attribute Name="vectors" AttributeType="Vector" Center="Node">',level=3)
        xdmf_write(xdmf,f'<DataItem ItemType="Function" Function="join($0, $1, $2)" Dimensions="{n[0]} {n[1]} {n[2]} 3">',level=4)

        for dset in dsets:
            xdmf_write(xdmf,f'<DataItem Dimensions="{n[0]*n[1]*n[2]}" NumberType="Float" Precision="8" Format="HDF"> {fnameabs}:{dset} </DataItem>',level=5)

        xdmf_write(xdmf,f'</DataItem>',level=4)
        xdmf_write(xdmf,f'</Attribute>',level=3)
        xdmf_write(xdmf,f'</Grid>',level=2)
        xdmf_write(xdmf,f'</Domain>',level=1)
        xdmf_write(xdmf,f'</Xdmf>')

def generate_xdmf_scalar(fname):
    def xdmf_write(xdmf,string,level=0,width=2):
        xdmf.write(string.rjust(len(string)+width*level,' ')+'\n')

    f      = h5py.File(fname,'r')
    dsets  = [key for key in f.keys()]
    shapes = [f[d].shape for d in dsets]

    print(dsets, shapes[0])

    n    = shapes[0]
    fnameabs = os.path.abspath(fname)
    with open(fname.replace('.h5','.xdmf'),'w') as xdmf:
        xdmf_write(xdmf,f'<?xml version="1.0" ?>')
        xdmf_write(xdmf,f'<!DOCTYPE Xdmf SYSTEM "Xdmf.dtd" []>')
        xdmf_write(xdmf,f'<Xdmf xmlns:xi="http://www.w3.org/2003/XInclude" Version="2.2">')
        xdmf_write(xdmf,f'<Domain>',level=1)
        xdmf_write(xdmf,f'<Grid Name="Scalar" GridType="Uniform">',level=2)
        xdmf_write(xdmf,f'<Topology TopologyType="3DCORECTMesh" NumberOfElements="{n[0]} {n[1]} {n[2]}" />',level=3)
        xdmf_write(xdmf,f'<Geometry GeometryType="ORIGIN_DXDYDZ">',level=3)
        xdmf_write(xdmf,f'<DataItem Name="origin" Dimensions="3" NumberType="Float" Precision="8" Format="XML"> 0.0 0.0 0.0 </DataItem>',level=4)
        xdmf_write(xdmf,f'<DataItem Name="spacing" Dimensions="3" NumberType="Float" Precision="8" Format="XML"> 1.0 1.0 1.0 </DataItem>',level=4)
        xdmf_write(xdmf,f'</Geometry>',level=3)
        for dset in dsets:
            xdmf_write(xdmf,f'<Attribute Name="scalars" AttributeType="Scalar" Center="Node">',level=3)
            xdmf_write(xdmf,f'<DataItem ItemType="Function" Function="join($0)" Dimensions="{n[0]} {n[1]} {n[2]} 1">',level=4)
            xdmf_write(xdmf,f'<DataItem Dimensions="{n[0]*n[1]*n[2]}" NumberType="Float" Precision="8" Format="HDF"> {fnameabs}:{dset} </DataItem>',level=5)
            xdmf_write(xdmf,f'</DataItem>',level=4)
            xdmf_write(xdmf,f'</Attribute>',level=3)
        xdmf_write(xdmf,f'</Grid>',level=2)
        xdmf_write(xdmf,f'</Domain>',level=1)
        xdmf_write(xdmf,f'</Xdmf>')
