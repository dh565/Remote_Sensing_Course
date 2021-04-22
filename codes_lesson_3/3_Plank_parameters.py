# =================================================================================================== #
# Planck function's parameters and the calculation of constants C1 and C2:
# =================================================================================================== #

from numpy import log as ln
h     = 6.625e-34
k     = 1.38e-23
c     = 3e8
lamda = 9.7e-6          # in micrometers (um)

# Note the units conversion!!!
C1    = 2 * h * (c*100)**2 * 1000 * (100)**2 # x 1000 to convert to mW; x10^4 to convert to cm-2
C2    = h * (c*100) / k
wn    = 1e4/(lamda*1e6) # wavenumber in (cm-1)-1

# Notice that C1 and C2 are constant with values:
#  C1 = 1.1925e-5       # in mW (cm-1)-4 m-2 sr-1 
#  C2 = 1.4402174       # in K (cm-1)-1
