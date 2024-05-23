# -*- coding: utf-8 -*-

"""

Created on Mon Mar 22 09:18:51 2021
https://stackoverflow.com/questions/15721094/detecting-mouse-event-in-an-image-with-matplotlib
@author: dhelman-lab {new 1 - change the text}

=================================================================================
==================== This code changes the header of the Table ==================
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

im = band
x  = np.array([0, 1, 2, 3 ])
y  = np.array([3, 8, 1, 10])

implot = ax[0,0].imshow(im)

ax[1,0].plot([0,0,0], [0,0,0])

def onclick(event):
   if event.xdata != None and event.ydata != None:
       x = event.xdata
       y = event.ydata
       # We need to select a single layer (channel) from the 3-D array: 
       t = sub_data[:,int(y),int(x)]
       round = np.around(t, 11) 

       # text =============================================================== #
       # Clear axis
       ax[0,1].clear()
       ax[0,1].grid(False)
       ax[0,1].set_xticks([])
       ax[0,1].set_yticks([])

       # Write new text
       textbox = 'Wavelength [\u00b5m]      Rad [mW m$^{-2}$ (cm$^{-1}$)$^{-1}$]'  + \
        '  \n' + '----------------------------------------------------------'  + \
        '  \n' + '         0.6                         ' + str(round[0]) + \
        '  \n' + '         0.8                         ' + str(round[1]) + \
        '  \n' + '         1.6                         ' + str(round[2]) + \
        '  \n' + '         3.9                         ' + str(round[3]) + \
        '  \n' + '         6.2                         ' + str(round[4]) + \
        '  \n' + '         7.3                         ' + str(round[5]) + \
        '  \n' + '         8.7                         ' + str(round[6]) + \
        '  \n' + '         9.7                         ' + str(round[7]) + \
        '  \n' + '         10.8                       '  + str(round[8]) + \
        '  \n' + '         12.0                       '  + str(round[9]) + \
        '  \n' + '         13.4                       '  + str(round[10])

       ax[0,1].text(0.04,0.95,textbox, fontsize=10, verticalalignment='top')

       # ==================================================================== #
       # Lines ============================================================== #
       # Lines remove

       ax[1,0].lines.remove(ax[1,0].lines[0])
    
       # Draw new lines
       ax[1,0].plot([0.6,0.8,1.6,3.9,6.2,7.3,8.7,9.7,10.8,12,13.4], t, color='black', marker='o', linestyle='dashed')
       ax[1,0].set_xlabel('Wavelength [\u00b5m]')
       ax[1,0].set_ylabel('Irradiance [mW m$^{-2}$ (cm$^{-1}$)$^{-1}$]') # mW m-2 sr-1 (cm-1)-1

       # ==================================================================== #

       plt.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
