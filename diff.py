import numpy as np
from scipy.ndimage import convolve

# Few stencils for first and second order derivatives.

def d1(u,axis,dx = 1.e0, n_points=5,mode='wrap'):
    """
    First order derivative of a two dimensional array.

    axis     : 'x' or 'y'
    n_points : Number of points to use in the stencil.
    mode     : scipy convolve mode. Use 'wrap' for periodic.
    """

    dx_inv = dx
    if n_points == 5:
        stencil = (dx_inv/12.e0)*np.array([[-1,8,0,-8,1]])
    elif n_points == 3:
        stencil = (dx_inv/2.e0)*np.array([[-1,0,1]])
    if axis == 'x':
        return convolve(u,stencil,mode=mode)
    if axis == 'y':
        return convolve(u,stencil.T,mode=mode)

def d2(u,axis,dx = 1.e0,n_points=5,mode='wrap'):
    """
    Second order derivative of a two dimensional array.

    axis     : 'x' or 'y'
    n_points : Number of points to use in the stencil.
    mode     : scipy convolve mode. Use 'wrap' for periodic.
    """
    dx_inv = dx
    if n_points == 5:
        stencil = (dx_inv**2/12.e0)*np.array([[-1,16,-30,16,-1]])
    elif n_points == 3:
        stencil = (dx_inv**2)*np.array([[1,-2,1]])
    if axis == 'x':
        return convolve(u,stencil,mode=mode)
    if axis == 'y':
        return convolve(u,stencil.T,mode=mode)