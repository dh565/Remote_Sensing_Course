{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# =================================================================================================== #\n",
    "# Planck function's parameters and the calculation of constants C1 and C2:\n",
    "# =================================================================================================== #\n",
    "\n",
    "from numpy import log as ln\n",
    "h     = 6.625e-34\n",
    "k     = 1.38e-23\n",
    "c     = 3e8\n",
    "lamda = 9.7e-6          # in micrometers (um)\n",
    "\n",
    "C1    = 2 * h * (c*100)**2 * 1000 * (100)**2 # x 1000 to convert to mW; x10^4 to convert to cm-2\n",
    "C2    = h * (c*100) / k\n",
    "wn    = 1e4/(lamda*1e6) # wavenumber in (cm-1)-1\n",
    "\n",
    "# Notice that C1 and C2 are constant with values:\n",
    "#  C1 = 1.1925e-5       # in mW (cm-1)-4 m-2 sr-1 \n",
    "#  C2 = 1.4402174       # in K (cm-1)-1"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
