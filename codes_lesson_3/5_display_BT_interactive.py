# -*- coding: utf-8 -*-

"""

Created on Mon Mar 22 09:18:51 2021
https://stackoverflow.com/questions/15721094/detecting-mouse-event-in-an-image-with-matplotlib
@author: dhelman-lab {new 2 - change display color to grey}

=================================================================================
===============      This code displays the BT of the channels      =============
=================================================================================
1) displays Tb (Brightness temperature)
2) changes the header to Tb and degrees
3) uses "{:.2f}".format() to display (in this case) 2 significant digits after
   the decimal point
=================================================================================
=================================================================================
=================================================================================

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig, ax = plt.subplots(2,2)

ax[0,1].grid(False)
ax[0,1].set_xticks([])
ax[0,1].set_yticks([])
ax[1,1].remove()

gs      = gridspec.GridSpec(2,2)
ax[1,0] = plt.subplot(gs[1,:])
textbox = 'Channels and values:'
ax[0,1].text(0.0,1.0,textbox, fontsize=10, verticalalignment='top')

band = T_rad[3]

im   = band

x    = np.array([0, 1, 2, 3 ])
y    = np.array([3, 8, 1, 10])

implot = ax[0,0].imshow(im, cmap='Greys_r')

ax[1,0].plot([0,0,0], [0,0,0])

def onclick(event):
   if event.xdata != None and event.ydata != None:
       x = event.xdata
       y = event.ydata
       # We need to select a single layer (channel) from the 3-D array: 
       t = T_rad[:,int(y),int(x)]
       round = np.around(t, 11) 

       # text =============================================================== #
       # Clear axis
       ax[0,1].clear()
       ax[0,1].grid(False)
       ax[0,1].set_xticks([])
       ax[0,1].set_yticks([])

       # Write new text
       textbox = 'Wavelength [\u00b5m]             Temp (\N{DEGREE SIGN}C)'  + \
        '  \n' + '----------------------------------------------------------'  + \
        '  \n' + '         0.6                         ' + "{:.2f}".format(round[0]) + \
        '  \n' + '         0.8                         ' + "{:.2f}".format(round[1]) + \
        '  \n' + '         1.6                         ' + "{:.2f}".format(round[2]) + \
        '  \n' + '         3.9                         ' + "{:.2f}".format(round[3]) + \
        '  \n' + '         6.2                         ' + "{:.2f}".format(round[4]) + \
        '  \n' + '         7.3                         ' + "{:.2f}".format(round[5]) + \
        '  \n' + '         8.7                         ' + "{:.2f}".format(round[6]) + \
        '  \n' + '         9.7                         ' + "{:.2f}".format(round[7]) + \
        '  \n' + '         10.8                       '  + "{:.2f}".format(round[8]) + \
        '  \n' + '         12.0                       '  + "{:.2f}".format(round[9]) + \
        '  \n' + '         13.4                       '  + "{:.2f}".format(round[10])

       ax[0,1].text(0.04,0.95,textbox, fontsize=10, verticalalignment='top')

       # ==================================================================== #
       # Lines ============================================================== #
       # Lines remove

       ax[1,0].lines.remove(ax[1,0].lines[0])
    
       # Draw new lines
       ax[1,0].plot([0.6,0.8,1.6,3.9,6.2,7.3,8.7,9.7,10.8,12,13.4], t, color='black', marker='o', linestyle='dashed')
       ax[1,0].set_xlabel('Wavelength [\u00b5m]')
       ax[1,0].set_ylabel('Radiance [mW m$^{-2}$ (cm$^{-1}$)$^{-1}$]') # mW m-2 sr-1 (cm-1)-1

       # ==================================================================== #

       plt.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
