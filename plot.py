import matplotlib
from matplotlib import pyplot as plt
from matplotlib.colors import rgb2hex
from matplotlib.ticker import ScalarFormatter
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
    cmap = plt.cm.get_cmap(name=cmap,lut = n_colors)
    colors = [ rgb2hex(cmap(i)[:3]) for i  in range(n_colors)]
    # Convert RGB to Hex Value, and return an array.
    return colors

class OOMFormatter(ScalarFormatter):
    """
    Shamelessly copied from stack overflow.
    Set custom Formatter.
    order    : Order which appears on the top as multiplier.
    fformat  : Float Format
    mathtext : Use mathtext if possible.
    """
    def __init__(self, order=0, fformat="%1.1f", offset=True, mathText=True):
        self.oom = order
        self.fformat = fformat
        ScalarFormatter.__init__(self,useOffset=offset,useMathText=mathText)
    def _set_orderOfMagnitude(self, nothing):
        self.orderOfMagnitude = self.oom
    def _set_format(self, vmin, vmax):
        self.format = self.fformat
        if self._useMathText:
            self.format = '$%s$' % matplotlib.ticker._mathdefault(self.format) 
