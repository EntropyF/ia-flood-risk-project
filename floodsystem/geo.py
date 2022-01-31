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
