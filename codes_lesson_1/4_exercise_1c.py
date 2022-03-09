# ========================================================================= #
# ========================================================================= #
# Exercise 1c: The temperature of the Sun is approx. 6000 K while that of 
#              the Earth is 255 K (i.e. c. 18C). Let's plot them together...
# ========================================================================= #
# ========================================================================= #
# Array generated for wavelengths: 
lamdas = np.arange(1e-9, 1e-2, 1e-9)
# ========================================================================= #
# Input temperatures (in Kelvin degrees):
# ========================================================================= #
T_Sun    = 6000
T_Earth  = 255
# ========================================================================= #
# ========================================================================= #
B_Sun    = PlanckFunc(lamdas, T_Sun)
B_Earth  = PlanckFunc(lamdas, T_Earth)
# ========================================================================= #
# Display graphs:
# ========================================================================= #
fig = plt.figure(figsize=(3.5,2.5),dpi=300) 
fig.subplots_adjust(bottom=0.1,top=0.9,left=0.1,right=0.95) 

ax1 = fig.add_subplot(1,1,1)
ax1.fill_between(lamdas*1e6, np.zeros(lamdas.shape), y2=B_Sun,
                 color='#e6ab02',alpha=0.2) 
pl1l = ax1.plot(lamdas*1e6, B_Sun, color='#e6ab02', 
                linewidth=1.5,label='Sun') 

ax1.fill_between(lamdas*1e6 ,np.zeros(lamdas.shape), y2=B_Earth,
                 color='#377eb8',alpha=0.2) 
pl2l = ax1.plot(lamdas*1e6, B_Earth,color='#377eb8',
                linewidth=1.5,label='Earth') 

# Axes and legend:
#ax1.set_xscale('log')
ax1.set_xlim(1e-1,5)
ax1.set_xlabel(u'Wavelength [\u00b5m]') 
ax1.set_ylabel(r'Intensity [W sr$^{-1}$ m$^{-2}$ m$^{-1}]$')
#ax1.set_ylabel(r'Relative Intensity')
lgd = ax1.legend(fancybox=True,loc=1) 

'''
# ========================================================================= #
# ========================================================================= # 
 What happened? why can't we see the B of the Earth?
 Let's normalize the Intensity by dividing it by Variable_name.max()
 
 !!! Hint: play with the axis format (hint: use logarithmic scale) 
 !!! and range (1e4). 
 !!! Don't forget to change the axis's title to "Relative intensity"

 Another way to look at it is by changing y-axis to log scale - let's do that
 Play with xlim and ylim functions to get something reasonable in your plot.

# ========================================================================= #
# ========================================================================= # 
'''
