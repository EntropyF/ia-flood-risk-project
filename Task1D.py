from floodsystem.geo import stations_by_river, rivers_with_station
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    
    x = rivers_with_station(stations)
    
    print(len(x))
    rivers = []
    for river in x:
        rivers.append(river)
    rivers.sort()
    print(rivers[:10])

    #stations_by_river(stations)['River Aire'].sort()
    print(sorted((stations_by_river(stations))['River Aire']))

    #stations_by_river(stations)['River Cam'].sort()
    print(sorted((stations_by_river(stations))['River Cam']))

    #stations_by_river(stations)['River Thames'].sort()
    print(sorted((stations_by_river(stations))['River Thames']))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()