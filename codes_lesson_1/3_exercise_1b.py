# ========================================================================= #
# ========================================================================= #
# Exercise 1b: Compare and convert units (note the scale in the upper left
# corner of the plot). Change B to mW sr-1 cm-2 nm-1 and Wavelength to nm 
# (change axis titles accordingly)
# ========================================================================= #
# Array generated for wavelengths: 
lamdas = np.arange(1e-9, 5e-6, 1e-9) 
# ========================================================================= #
# Input the temperature for three bodies in kelvin degrees (K):
# ========================================================================= #
T1 = 6000
T2 = 5000
T3 = 4000
# ========================================================================= #
# ========================================================================= #
B_body1  = PlanckFunc(lamdas, T1)
B_body2  = PlanckFunc(lamdas, T2)
B_body3  = PlanckFunc(lamdas, T3)
# ========================================================================= #
# Display results:
# ========================================================================= #
fig = plt.figure(figsize=(3.5,2.5),dpi=300) 
fig.subplots_adjust(bottom=0.1,top=0.9,left=0.1,right=0.95) 
ax1 = fig.add_subplot(1,1,1)
# For body #1:
ax1.fill_between(lamdas*1e6, np.zeros(lamdas.shape), y2=B_body1,
                 color='#e6ab02',alpha=0.2) 
pl1l = ax1.plot(lamdas*1e6, B_body1, color='#e6ab02', 
                linewidth=1.5,label=str(T1)+' K') 
# For body #2:
ax1.fill_between(lamdas*1e6 ,np.zeros(lamdas.shape), y2=B_body2,
                 color='#377eb8',alpha=0.2) 
pl2l = ax1.plot(lamdas*1e6, B_body2,color='#377eb8',
                linewidth=1.5,label=str(T2)+' K') 
# For body #3:
ax1.fill_between(lamdas*1e6 ,np.zeros(lamdas.shape), y2=B_body3,
                 color='r',alpha=0.2) 
pl3l = ax1.plot(lamdas*1e6, B_body3,color='r',
                linewidth=1.5,label=str(T3)+' K') 

# Axes and legend:
ax1.set_xlabel('Wavelength [\u00b5m]') 
ax1.set_ylabel('Intensity [W sr$^{-1}$ m$^{-2}$ m$^{-1}]$')
lgd = ax1.legend(fancybox=True,loc=0)
