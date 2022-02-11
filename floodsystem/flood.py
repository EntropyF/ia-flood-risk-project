from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    list_of_over_threshold = []
    for station in stations:
        name_and_relative_water = []
        if station.relative_water_level() == None or station.relative_water_level() > 10:
            pass
        elif station.relative_water_level() > tol:
            name_and_relative_water.append(station.name)
            name_and_relative_water.append(station.relative_water_level())
            list_of_over_threshold.append(tuple(name_and_relative_water))
    list_of_over_threshold = sorted_by_key(list_of_over_threshold, 1, reverse=True)
    return list_of_over_threshold