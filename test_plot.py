import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit

stations = build_station_list()

def test_plot_water_levels():
    '''Test water level - time plot'''
    assert plot_water_levels(stations[0], 2, stations[0].typical_range)

def test_plot_water_level_with_fit():
    '''Test polynomail plot of water level - time'''
    assert plot_water_level_with_fit(stations[0], 2, stations[0].typical_range, 3)