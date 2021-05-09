# This is a function that will help us to adust the size of the 
# colorbar to the map size
from mpl_toolkits.axes_grid1 import make_axes_locatable

def make_colorbar_with_padding(ax):
    """
    Create colorbar axis that fits the size of a plot - detailed here: http://chris35wills.github.io/matplotlib_axis/
    """
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    return(cax)
