# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from haversine import haversine
#from . import datafetcher
#from .station import MonitoringStation
#from floodsystem.stationdata import build_station_list

names = []
distance = []
def stations_by_distance(stations, p):

    for station in stations:
        names.append(station.name)
        distance.append(haversine(p, station.coord))
    
    turples = list(zip(names, distance))
    turples = sorted_by_key(turples,1)
    return turples

#Task 1C
def stations_within_radius(stations, centre, r):
    for station in stations:
        
        if r > haversine(centre, station.coord):
            names.append(station.name)
        
    return names

#Task 1D
stations_by_rivers = {}
def stations_by_river(stations):
    
    for station in stations:
        stations_by_rivers[station.river] = station.name
    
    return set(stations_by_rivers)