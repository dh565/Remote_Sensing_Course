# -*- coding: utf-8 -*-

"""

Created on Mon Mar 22 09:18:51 2021
https://stackoverflow.com/questions/15721094/detecting-mouse-event-in-an-image-with-matplotlib
@author: dhelman-lab {new 2 - change display color to grey}

=================================================================================
==========    This code displays the TB of each channel instead of Irr   ========
=================================================================================
1) displays RGB day natural color image (from Irr - CH3, CH2, CH1 = R, G, B)
2) removes first 3 bands from the graph
=================================================================================
=================================================================================
=================================================================================

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from astropy.visualization import make_lupton_rgb

fig, ax = plt.subplots(2,2)

ax[0,1].grid(False)
ax[0,1].set_xticks([])
ax[0,1].set_yticks([])
ax[1,1].remove()

gs      = gridspec.GridSpec(2,2)
ax[1,0] = plt.subplot(gs[1,:])
textbox = 'Channels and values:'
ax[0,1].text(0.0,1.0,textbox, fontsize=10, verticalalignment='top')

r1 = sub_data[2]
g1 = sub_data[1]
b1 = sub_data[0]

im = make_lupton_rgb(r1, g1, b1)

implot = ax[0,0].imshow(im, cmap='Greys_r')

ax[1,0].plot([0,0,0], [0,0,0])

def onclick(event):
   if event.xdata != None and event.ydata != None:
       x = event.xdata
       y = event.ydata
       # We need to select a single layer (channel) from the 3-D array: 
       t = T_rad[3:11,int(y),int(x)]
       round = np.around(t, 8) 

       # text =============================================================== #
       # Clear axis
       ax[0,1].clear()
       ax[0,1].grid(False)
       ax[0,1].set_xticks([])
       ax[0,1].set_yticks([])

       # Write new text
       textbox = 'Channel      Wavelength [\u00b5m]      Temp (\N{DEGREE SIGN}C)'  + \
        '  \n' + '----------------------------------------------------------'  + \
        '  \n' + 'CH04                     3.9                   ' + "{:.2f}".format(round[0]) + \
        '  \n' + 'CH05                     6.2                   ' + "{:.2f}".format(round[1]) + \
        '  \n' + 'CH06                     7.3                   ' + "{:.2f}".format(round[2]) + \
        '  \n' + 'CH07                     8.7                   ' + "{:.2f}".format(round[3]) + \
        '  \n' + 'CH08                     9.7                   ' + "{:.2f}".format(round[4]) + \
        '  \n' + 'CH09                     10.8                 '  + "{:.2f}".format(round[5]) + \
        '  \n' + 'CH10                     12.0                 '  + "{:.2f}".format(round[6]) + \
        '  \n' + 'CH11                     13.4                 '  + "{:.2f}".format(round[7]) #+ \
        #'  \n' + '-----------------------------------------------------------' + \
        #'  \n' + 'SST                      '

       ax[0,1].text(0.04,0.95,textbox, fontsize=10, verticalalignment='top')

       # ==================================================================== #
       # Lines ============================================================== #
       # Lines remove

       ax[1,0].lines.remove(ax[1,0].lines[0])
    
       # Draw new lines
       ax[1,0].plot([3.9,6.2,7.3,8.7,9.7,10.8,12,13.4], t, color='black', marker='o', linestyle='dashed')
       ax[1,0].set_xlabel('Wavelength [\u00b5m]')
       ax[1,0].set_ylabel('Radiance [mW m$^{-2}$ (cm$^{-1}$)$^{-1}$]') # mW m-2 sr-1 (cm-1)-1

       # ==================================================================== #

       plt.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
