# =================================================================================================== #
# Planck function's parameters and the calculation of constants C1 and C2:
# =================================================================================================== #

from numpy import log as ln
h     = 6.625e-34       # J s    or  m2 kg s-1
k     = 1.38e-23        # J K-1  or  m2 kg s-2 K-1
c     = 3e8             # m s-1
lamda = 9.7e-6          # in micrometers (um)

# Notice the units of conversion!!!
C1    = 2 * h * (c*100)**2 * 1000 * (100)**2 # x 1000 to convert to mW; x10^4 to convert m2 to cm2.
                                             # Note also that h is in J*s. Thus if J = m2 kg / s2  
                                             # we need to convert m to cm here as well...
C2    = h * (c*100) / k

# Notice that C1 and C2 are constants with values of:
#  C1 = 1.1925e-5       # in mW (cm-1)-4 m-2 sr-1 
#  C2 = 1.4402174       # in K (cm-1)-1
