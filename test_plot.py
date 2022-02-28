import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit

stations = build_station_list()

import numpy as np

def test_polt_water_level_with_fit():
    x = np.linspace(1, 1000, 100000)
    y = []
    for i in x:
        y.append(3*i**2 + 5)
    p_coeff = np.polyfit(x, y, 2)
    poly = np.poly1d(p_coeff)
    assert int(p_coeff[0]) == 2