import matplotlib
from matplotlib import pyplot as plt

def mt(string):
    """
    Convert a string for math use.
    """
    return r'$%s$'%string

def no_ticks(ax,axis='both'):
    """
    Remove ticks and labels from one or both axis.
    ax   : matplotlib ax object.
    axis : "both", "x", "y"
    """
    import numpy as np
    def set(ax):
        if axis=='both' or axis == 'x':
            ax.get_xaxis().set_visible(False)
        if axis=='both' or axis == 'y':
            ax.get_yaxis().set_visible(False)
    if type(ax) == np.ndarray :
        for axi in ax:
            set(axi)
    else:
        set(ax)

def cmap_colors(n_colors,alpha = 1.0,cmap='viridis'):
    """
    Get colors from matplotlib colormap.
    n_colors : number of colors to draw.
    alpha    : alpha value.
    cmap     : colormap to choose from. Default is viridis.
    """
    
    from matplotlib.colors import rgb2hex
    cmap = plt.cm.get_cmap(name=cmap,lut = n_colors)
    colors = [(cmap(i)[0],cmap(i)[1],cmap(i)[2],alpha) for i in range(n_colors)]
    # Set corresponding alpha value and return an array.
    return colors

def add_colorbar(fig,ax,im,contours=False):
    """
    Add a colorbar to the image.
    """
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    cax = make_axes_locatable(ax).append_axes('right',size='5%',pad=0.05)
    cax.tick_params(axis='y',which='minor',bottom=False)
        
    if contours:
        norm = matplotlib.colors.Normalize(vmin=cs.cvalues.min(),vmax=cs.cvalues.max())
        sm   = plt.cm.ScalarMappable(norm=norm,cmap=cs.cmap)
        sm.set_array([])
        fig.colorbar(sm,cax=cax,orientation='vertical') 
    else:
        fig.colorbar(im,cax=cax,orientation='vertical') 

    for t in cax.get_yticklabels():
        t.set_horizontalalignment('right')
        t.set_verticalalignment('center')
        t.set_x(4)
    return cax
