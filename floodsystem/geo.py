# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from haversine import haversine    #pip install haversine

#Task 1B
names = []
distance = []
def stations_by_distance(stations, p):

    for station in stations:
        names.append(station.name)
        distance.append(haversine(p, station.coord))
    
    tuples = list(zip(names, distance))
    tuples = sorted_by_key(tuples,1)
    return tuples

#Task 1C
def stations_within_radius(stations, centre, r):
    for station in stations:
        
        if r > haversine(centre, station.coord):
            names.append(station.name)
        
    return names

#Task 1D
set_river = set()
def rivers_with_station(stations):
    for station in stations:
        set_river.add(station.river)
    return set_river

def stations_by_river(stations):

    stations_by_rivers = {}    
    for station in stations:
        if station.river in stations_by_rivers:
            stations_by_rivers[station.river].append(station.name)
            #stations_by_rivers[station.river].sort
        else:
            stations_by_rivers[station.river] = [station.name]
    
    return stations_by_rivers

#Task 1E
def rivers_by_station_number(stations, N):
    "Return the N rivers with the greatest number of monitoring stations"

    number_of_stations_dict = {}
    for station in stations:
        if station.river in number_of_stations_dict:
            number_of_stations_dict[station.river] += 1
        else:
            number_of_stations_dict[station.river] = 1
    
    outlist = []
    for river, number in number_of_stations_dict.items():
        outlist.append((river, number))

    sorted_output = sorted_by_key(outlist, 1, reverse=True)

    while sorted_output[N][1] == sorted_output[N - 1][1]:
        N += 1

    return sorted_output[ :N]