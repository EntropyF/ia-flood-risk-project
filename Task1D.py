from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    
    x = stations_by_river(stations)
    
    print(len(x))
    rivers = []
    for river in x:
        rivers.append(river)
    rivers.sort()
    print(rivers[:10])

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()