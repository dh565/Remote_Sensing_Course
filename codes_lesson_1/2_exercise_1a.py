# ========================================================================= #
# ========================================================================= #
# Exercise 1a: Play with the temperature... what happens when you change T 
# to hundreds instead of thousands K (Kelvin degrees)?
# ========================================================================= #
# ========================================================================= #
# Array generated for wavelengths: 
lamdas = np.arange(1e-9, 5e-6, 1e-9) 
# ========================================================================= #
# Input the temperature of the body in kelvin degrees (K):
# ========================================================================= #
T1 = 6000
# ========================================================================= #
# This calls the Planck's function:
# ========================================================================= #
B_body1  = PlanckFunc(lamdas, T1)
# ========================================================================= #
# Present the results as graphs:
# ========================================================================= #
fig = plt.figure(figsize=(3.5,2.5),dpi=300) 
fig.subplots_adjust(bottom=0.1,top=0.9,left=0.1,right=0.95) 

ax1 = fig.add_subplot(1,1,1)
ax1.fill_between(lamdas*1e6, y1=np.zeros(lamdas.shape), y2=B_body1,
                 color='#e6ab02',alpha=0.2) 

pl1l = ax1.plot(lamdas*1e6, B_body1, color='#e6ab02', 
                linewidth=1.5,label=str(T1)+' K') 

ax1.set_xlabel('Wavelength [\u00b5m]') 
ax1.set_ylabel('Intensity [W sr$^{-1}$ m$^{-2}$ m$^{-1}]$')

lgd = ax1.legend(fancybox=True,loc=0) 
