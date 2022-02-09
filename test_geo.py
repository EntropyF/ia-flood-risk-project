"""Unit test for the geo module"""

from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

#Create test stations
s_id1,s_id2,s_id3 = "test-s-id1","test-s-id2","test-s-id3"
m_id1,m_id2,m_id3 = "test-m-id1","test-m-id2","test-m-id3"
label1,label2,label3 = "station1","station2","station3"
coord1,coord2,coord3 = (-3.0, 4.0),(0.1,0.0),(0.0,3.0)
trange1,trange2,trange3 = (-5.0, 7.4),(-3.0,3.0),(2.4,6.8)
river1,river2,river3 = "River X","River Y","River X"
town1,town2,town3 = "Town X","Town Y","Town Z"

s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
s3 = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)

s = [s1,s2,s3]

def test_stations_by_distance():
    """Test stations sorted by distance"""
    test = stations_by_distance(s,(0.0,0.0))
    assert test[0] == ('station2', 0.1)


def test_stations_within_radius():
    """Test stations within certain radius"""
    test = stations_within_radius(s, (0.0,0.0), 1.0)
    assert test[0] == 'station2'

def test_rivers_with_station():
    """Test rivers with a monitoring station (no duplicate entries)"""
    assert rivers_with_station(s) == {'River X', 'River Y'}

def test_stations_by_river():
    """Test rivers (keys) mapping to stations (values)"""
    assert stations_by_river(s) == {'River X': ['station1', 'station3'], 'River Y': ['station2']}

def test_rivers_by_station_number():
    """Test rivers with the greatest number of stations"""
    assert rivers_by_station_number(s,1) == [('River X', 2)]