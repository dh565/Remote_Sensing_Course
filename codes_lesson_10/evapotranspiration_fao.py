# -*- coding: utf-8 -*-
"""
module evapotranspiration_fao
Daily evapotranspiration based on FAO / Allen formulations
http://www.fao.org/3/X0490E/x0490e05.htm#TopOfPage

Created on Wed Apr 29 13:21:39 2020

Samuli Launiainen (Luke)
@author: slauniai
"""

import numpy as np
EPS = np.finfo(float)

"""
Constants
"""
NT           = 273.15  # 0 degC in K
GAS_CONSTANT = 8.314462175  # J mol-1 K-1, universal gas constant. One gets specific gas constant by R/M where M is molar mass
CP_AIR_MOLAR = 29.3  # J mol-1 K-1 molar heat capacity of air at constant pressure
CP_AIR_MASS  = 1004.67  # J kg-1 K-1 heat capasity of the air at constant pressure
MAIR_DRY     = 28.964e-3  # kg mol-1, molar mass of dry air
MH2O         = 18.02e-3  # kg mol-1, molar mass of H2O

SIGMA        = 5.6697e-8  # Stefan-Boltzman constant W m-2 K-4
PAR_TO_UMOL  = 4.56  # conversion from Wm-2 to micromol m-2 s-1
PAR_TO_WM2   = 1.0/4.56  # conversion from micromol m-2 s-1 to Wm-2
PAR_FRACTION = 0.45  # PAR fraction of global radiation (-), Jones H.(1992): Plants and Microclimate: ... Cambridge, 1992
NIR_FRACTION = 0.55  # NIR fraction of global radiation (-)
DEG_TO_RAD   = np.pi / 180.0  #  conversion deg -->rad
RAD_TO_DEG   = 180.0 / np.pi  #  conversion rad -->deg
SOLAR_CONST  = 1367.0  # Wm-2, solar constant at top of atm.

"""
Penman-Monteith using radiation data from ERA-interim re-analysis products
+ weather station data. https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim
"""

def actual_evapotranspiration(Epot, Kc):
    """
    Args:
        Epot - potential evapotranspiration
        Kc [-] - crop coefficient; ecosystem and soil-moisture dependent
    Returns:
        E - actual evapotranspiration
    """
    return Kc * Epot

def fao_reference_et(Rn, T, U, ea, P=101.3):
    """
    Daily reference potential evapotranspiration ETo by FAO: http://www.fao.org/3/X0490E/x0490e06.htm
    "well-watered short grass surface"

    Args:
        Rn [MJ m-2 d-1]  - daily net radiation
        T [degC]         - daily mean temperature
        U [m s-1]        - 2m windspeed
        ea [kPa]         - 2m air humidity
        P [kPa]          - 2m air pressure
    Returns:
        ETo [kg m-2 d-1] - reference potential evapotranspiration
    """
    # mysterious constants in FAO / Allen formulation
    a = 0.408 # MJ m-2 d-1 --> kg m-2 d-1
    b = 900.0
    c = 0.34

    es, delta = saturation_vapor_pressure(T)  # kPa, kPa/K
    gamma     = psycrometric_constant(T, P=P) # kPa/K

    nom       = a * delta * Rn + gamma * b * U / (T + NT) * (es - ea)
    denom     = delta + gamma * (1.0 + c * U)

    return nom / denom

def hargreaves_reference_et(lat, jday, Tmin, Tmax):
    """
    daily reference ET using hargreaves formula based on temperature data only
    Args:
        lat [deg]         - latitude
        jday              - julian day
        Tmin, Tmax [degC] - minimum and maximum temperatures
    Returns:
        reference ET [mm d-1]
    """
    Ra = daily_extraterrestrial_radiation(lat, jday)

    ETo = 2.3e-3 * 0.408 * Ra * np.sqrt(Tmax - Tmin) * (0.5 * (Tmax + Tmin) + 17.8)

    return ETo

def pressure_from_altitude(ASL): # we'll not use it in our exercise...
    """
    Approximates station pressure from site altitude
    INPUT:
        ASL  - elevation above sea level (m)
    OUTPUT:
        Pamb - station pressure (kPa), assuming sea level at NP=101.3 kPa
    SOURCE:
        Campbell & Norman, 1998. Introduction to Environmental biophysics, Springer.
    """
    ASL = np.array(ASL)
    Pamb = 101.3 * np.exp(-(ASL/8200.0))
    return Pamb


# -- Functions related to saturation vapor pressure and phase changes of H2O

def latent_heat_vaporization(T, units="molar"):
    """
    Temperature dependency of latent heat of vaporization
    INPUT:
        T - temperature (degC)
        units - output units, "mass" = J kg-1 , "molar"= J mol-1
    OUTPUT:
        Lv - latent heat of vaporization in desired units
    """

    if np.any(T > 200):
        T = T - NT  #T must be in degC

    Lv = 1.0e6*(2.501 - 2.361e-3*T)*MH2O  # J mol-1

    if units=="mass":
        Lv = Lv / MH2O  # J kg-1
    return Lv


def Saturation_vapor_pressure(T):
    """
    Computes saturation vapor pressure with respect to free and flat water surface for given temperature T
    INPUT:
        T     - temperature (degC), scalar or array
    OUTPUT:
        esat  - saturation vapor pressure (kPa)
        delta - slope of saturation vapor pressure curve (kPa degC-1)
    SOURCE:
        Campbell & Norman, 1998. Introduction to Environmental Biophysics.
    """
    # constants
    a = 0.611   # kPa
    b = 17.502  # (-)
    c = 240.97  # degC

    esat = a*np.exp(b*T / (T+c))  # kPa
    delta = b*c*esat / ((c + T)**2)  # kPa degC-1
    return esat

def saturation_vapor_pressure(T):
    """
    Computes saturation vapor pressure with respect to free and flat water surface for given temperature T
    INPUT:
        T     - temperature (degC), scalar or array
    OUTPUT:
        esat  - saturation vapor pressure (kPa)
        delta - slope of saturation vapor pressure curve (kPa degC-1)
    SOURCE:
        Campbell & Norman, 1998. Introduction to Environmental Biophysics.
    """
    # constants
    a = 0.611  # kPa
    b = 17.502  # (-)
    c = 240.97  # degC

    esat = a*np.exp(b*T / (T+c))  # kPa
    delta = b*c*esat / ((c + T)**2)  # kPa degC-1
    return esat, delta


def psycrometric_constant(T, P=101.3):
    """
    Computes Psycrometric constant at temperature T
    INPUT:
        T - temperature (degC)
        P - ambient pressure (kPa)
    OUTPUT:
        g - psychrometric constant
    USES:
        latent_heat_vaporization
    """
    Lv_mass = latent_heat_vaporization(T, units="mass")  # J kg-1
    g = P * CP_AIR_MASS / (0.622 * Lv_mass)  # kPa K-1
    return g

"""
estimate daily radiation balance components in absense of measurements
"""

def fao_shortwave_radiation(lat, jday, Tmin, Tmax, krs=0.19):
    """
    The Hargreaves' radiation formula estimates daily shortwave from met. station data
    Args:
        lat, lon [deg]    - latitude, longitude
        jday              - julian day of year
        Tmin, Tmax [degC] - minimum and maximum temperatures
        krs.              - parameter ranging 0.16 ... 0.19
    Returns:
        Rs [MJ m-2 d-1]   - solar radiation at horizontal surface
        Rso [Mj m-2 d-1]  - clear-sky solar radiation at horizontal surface
    """

    Ra = daily_extraterrestrial_radiation(lat, jday)
    Rs = krs * np.sqrt(Tmax - Tmin) * Ra
    # clear-sky solar radiation
    Rso = 0.75 * Ra

    return Rs, Rso

def fao_net_longwave_radiation(Tmin, Tmax, ea, Rs, Rso):
    """
    daily net longwave-radiation by FAO Allen eq. 39
    Args:
        Tmin, Tmax - [degC] minimum and maximum temperatures
        ea         - [kPa] air humidity
        Rs.        - [MJ m-2 d-1] solar radiation at horizontal surface
        Rso        - [MJ m-2 d-1] clear-sky solar radiation  at horizontal surface
    Returns:
        Rnl        - [Mj m-2 d-1] net longwave radiation
    """
    cf   = 1e-6 * 86400.0
    Teff = (Tmin + Tmax) / 2.0 + NT #K
    Rnl  = cf * SIGMA * Teff**4.0 * (0.34 - 0.14 * np.sqrt(ea)) * (1.35 * Rs / Rso - 0.35)

    return Rnl

def daily_extraterrestrial_radiation(lat, jday):
    """
    daily solar radiation at top of atmosphere. FAO Allen eq.21-26
    Args:
        lat [deg] - latitude
        jday      - day of year
    Returns:
        Ra        - [MJ m-2 d-1] daily radiation at top of atm.
    """

    lat = lat * DEG_TO_RAD

    J = np.minimum(jday, 365.0)

    dr = 1.0 + 0.033 * np.cos(2.0 * np.pi / 365.0 * J)
    delta = 0.409 * np.sin(2.0 * np.pi / 365.0 * J - 1.39)
    ws = np.arccos(-np.tan(lat) * np.tan(delta))

    Ra = ( 1e-6 * 86400 * SOLAR_CONST / np.pi * dr *
          (ws * np.sin(lat) * np.sin(delta) + np.cos(lat)*np.cos(delta) * np.sin(ws))
         )

    return Ra
