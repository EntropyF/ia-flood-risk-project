from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """Return 9 rivers with the greatest number of monitoring stations"""
    
    stations = build_station_list()
    river_station = rivers_by_station_number(stations, 9)
    print(river_station)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()