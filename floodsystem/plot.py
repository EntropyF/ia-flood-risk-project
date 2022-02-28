import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
from .analysis import polyfit

# Task 2E
def plot_water_levels(station, dates, levels):
    '''Plot water level against time for a station'''

    tlow = station.typical_range[0]
    thigh = station.typical_range[1]
    tlow_list = []
    thigh_list = []
    for i in range(len(dates)):
        tlow_list.append(tlow)
        thigh_list.append(thigh)
    
    #Plot
    plt.plot(dates, levels)
    plt.plot(dates, tlow_list)
    plt.plot(dates, thigh_list)

    #Add axis labels and rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    #Display plot
    plt.tight_layout()  #make sure plot does not cut off date labels
    plt.show

# Task 2F
def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)    # Convert to floats
    x1 = np.linspace(x[0], x[-1], 1000)     # Create data points
    x_date = matplotlib.dates.num2date(x1)
    poly, d0 = polyfit(dates, levels, p)
    
    tlow = station.typical_range[0]
    thigh = station.typical_range[1]
    tlow_list = []
    thigh_list = []
    for i in range(len(x_date)):
        tlow_list.append(tlow)
        thigh_list.append(thigh)
    
    plt.plot(x_date, poly(x1-d0), label = "Best fit")
    plt.plot(x_date, tlow_list, label = "Typical low")
    plt.plot(x_date, thigh_list, label = "Typical high")
    plt.legend
    plt.xlabel("date")
    plt.ylabel("water level (m)")
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.tight_layout()