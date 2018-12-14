from matplotlib import pyplot as plt
from matplotlib.colors import rgb2hex
def no_ticks(ax,axis='both'):
    """
    Remove ticks and labels from one or both axis.
    ax   : matplotlib ax object.
    axis : "both", "x", "y"
    """
    if axis=='both' or axis == 'x':
        ax.get_xaxis().set_visible(False)
    if axis=='both' or axis == 'y':
        ax.get_yaxis().set_visible(False)

def cmap_colors(n_colors,cmap='viridis'):
    """
    Get colors from matplotlib colormap.
    n_colors : number of colors to draw.
    cmap     : colormap to choose from. Default is viridis.
    """
    cmap = plt.cm.get_cmap(lut = n_colors)
    colors = [ rgb2hex(c(i)[:3]) for i  in range(n_colors)]
    # Convert RGB to Hex Value, and return an array.
    return colors
