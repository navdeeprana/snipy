import matplotlib
from matplotlib import pyplot as plt

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

def default_colors():
    return plt.rcParams['axes.prop_cycle'].by_key()['color']

def default_markers():
    return ['o','s','^','D','*','<']

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

def ax_colorbar(fig,ax,im,contours=False):
    """
    Add a colorbar to the image.
    """
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    cax = make_axes_locatable(ax).append_axes('right',size='5%',pad=0.05)
    cax.tick_params(axis='y',which='minor',bottom=False)
        
    if contours:
        norm = matplotlib.colors.Normalize(vmin=im.cvalues.min(),vmax=im.cvalues.max())
        sm   = plt.cm.ScalarMappable(norm=norm,cmap=im.cmap)
        sm.set_array([])
        fig.colorbar(sm,cax=cax,orientation='vertical') 
    else:
        fig.colorbar(im,cax=cax,orientation='vertical') 

    for t in cax.get_yticklabels():
        t.set_horizontalalignment('right')
        t.set_verticalalignment('center')
        t.set_x(4)
    return cax

def fig_colorbar(fig,cax,im,contours=False):
    """
    Add a colorbar to the figure.
    """
    cax.tick_params(axis='y',which='minor',bottom=False)
    if contours:
        norm = matplotlib.colors.Normalize(vmin=im.cvalues.min(),vmax=im.cvalues.max())
        sm   = plt.cm.ScalarMappable(norm=norm,cmap=im.cmap)
        sm.set_array([])
        fig.colorbar(sm,cax=cax,orientation='vertical') 
    else:
        fig.colorbar(im,cax=cax,orientation='vertical') 
    return cax

def ax_text(ax,x,y,text,**kwargs):
    ax.text(x,y,text,verticalalignment='center',horizontalalignment='center',
          transform=ax.transAxes,**kwargs)

def set_formatter(axis,l,r):
    form = matplotlib.ticker.ScalarFormatter()
    form.set_powerlimits((l,r))
    axis.set_major_formatter(form)

def search_rcParams(key):
    for name,value in plt.rcParams.items():
        if key in name:
            print(name,value)

def figure_grid(nrow,ncol,figsize=(5.0,3.5)):
    fig, grid = plt.subplots(nrow,ncol,figsize=(ncol*figsize[0],nrow*figsize[1]))
    return fig, grid.reshape(-1)
