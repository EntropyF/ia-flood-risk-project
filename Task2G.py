import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import floodwarning
from floodsystem.station import MonitoringStation

def run():
    
    stations = build_station_list()
    update_water_levels(stations)
    
    warning = floodwarning(stations)
    print(warning[0])

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()