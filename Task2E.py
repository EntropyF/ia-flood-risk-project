import datetime
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels

def run():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    # Find the 5 stations' names with highest relative water levels
    highest_5 = stations_highest_rel_level(stations, 5) 
    name_list = []
    for i in range(len(highest_5)):
        name_list.append(highest_5[i][0])

    # Create a list with the information of the 5 stations
    station_list = []
    for name in name_list:
        for station in stations:
            if station.name == name:
                station_list.append(station)
    
    # Plot
    for s in station_list:
        dates, levels = fetch_measure_levels(s.measure_id, dt=datetime.timedelta(days=10)) 
        plot_water_levels(s, dates, levels)
        
        #plt.show()

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()