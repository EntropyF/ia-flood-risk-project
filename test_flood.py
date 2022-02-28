from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)

def test_stations_level_over_threshold():
    '''Test stations with relative levels above threshold in descending order'''
    test_stations = stations_level_over_threshold(stations, 0.8)
    for x in test_stations:
        assert x[1] > 0.8
    for x in range(len(test_stations)):
        assert test_stations[x][1] <= test_stations[x-1][1]

def test_stations_highest_rel_level():
    '''Test N stations with highest relative water level in descending order'''
    test_stations = stations_highest_rel_level(stations,10)
    for x in range(len(test_stations)):
        assert test_stations[x][1] <= test_stations[x-1][1]