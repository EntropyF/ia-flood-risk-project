import matplotlib
import numpy as np
import datetime
import matplotlib.pyplot as plt

from .station import MonitoringStation
from .datafetcher import fetch_measure_levels

# Task 2F
def polyfit(dates, levels, p): 
    '''Compute a least-squares fit of a polynomial of degree p
    given the water level time history (dates, levels) for a station'''
    # Convert dates to floats
    x = matplotlib.dates.date2num(dates)    
    y = levels

    # Shift dates
    d0 = x[0]
    p_coeff = np.polyfit(x - d0, y, 4)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    # Return polynomial object & shift of the date axis 
    return poly, d0

# Task 2G
def floodrisk(station):
    '''Assess flooding risks of each station based on relative water level
    Return the risk rate as severe, high, moderate or low'''
    #if station.typical_range_consistent() == False:
    #        return None
    #else: 
    #    tol = station.typical_range[1] - station.typical_range[0]   

    # Fetch recent 10 days' data
    #dates, levels = fetch_measure_levels(station.measure_id,
                                     #dt=datetime.timedelta(days=10))

    #levels_tot, levels_ave = 0.0, 0.0
    #for i in range(len(levels)):
    #    levels_tot += levels[i]
    #    levels_ave = levels_tot / len(levels)

        # Define relative water level
    rwl = station.relative_water_level()
    if rwl == None:
        pass
    elif rwl < 0.25:
        return 'low'
    elif rwl < 0.5:
        return 'moderate'
    elif rwl < 0.75:
        return 'high'
    else: 
        return 'severe'

def floodwarning(stations):
    '''List the towns with the greatest risks
    rate the risk as severe, high, moderate or low'''
    
    severe = []
    high = []
    moderate =[]
    low = []
    
    for station in stations:
        risk = floodrisk(station)
        if risk == 'severe':
            severe.append(station.town)
        elif risk == 'high':
            high.append(station.town)
        elif risk == 'moderate':
            moderate.append(station.town)
        elif risk == 'low':
            low.append(station.town)

    S = "Severe risk towns: {}\n".format(severe)
    H = "High risk towns: {}\n".format(high)
    M = "Moderate risk towns: {}\n".format(moderate)
    L = "Low risk towns: {}\n".format(low)
    warning = [S,H,M,L]
    return warning