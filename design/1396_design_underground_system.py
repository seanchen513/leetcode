"""
1396. Design Underground System
Medium

Implement the class UndergroundSystem that supports three methods:

1. checkIn(int id, string stationName, int t)

A customer with id card equal to id, gets in the station stationName at time t.
A customer can only be checked into one place at a time.

2. checkOut(int id, string stationName, int t)

A customer with id card equal to id, gets out from the station stationName at time t.

3. getAverageTime(string startStation, string endStation) 

Returns the average time to travel between the startStation and the endStation.
The average time is computed from all the previous traveling from startStation to endStation that happened directly.
Call to getAverageTime is always valid.
You can assume all calls to checkIn and checkOut methods are consistent. That is, if a customer gets in at time t1 at some station, then it gets out at time t2 with t2 > t1. All events happen in chronological order.

Example 1:

Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.0,11.0,null,11.0,null,12.0]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
undergroundSystem.getAverageTime("Paradise", "Cambridge");       // return 14.0. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.0. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.0
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.0
undergroundSystem.checkOut(10, "Waterloo", 38);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 12.0
 
Constraints:

There will be at most 20000 operations.
1 <= id, t <= 10^6
All strings consist of uppercase, lowercase English letters and digits.
1 <= stationName.length <= 10
Answers within 10^-5 of the actual value will be accepted as correct.
"""

from typing import List
import collections

###############################################################################
"""
Solution: use two dicts:

start[id] = (station name, start time)

trips[(start station, end station)] = list of travel times (end time - start time)

"""
class UndergroundSystem:
    def __init__(self):
        self.start = {}
        self.trips = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_name, t1 = self.start[id]
        self.trips[(start_name, stationName)] += [t - t1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        lst = self.trips[(startStation, endStation)]
        return sum(lst) / len(lst)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

###############################################################################
"""
Solution 2: use two dicts:

start[id] = (station name, start time)

trips[(start station, end station)] = (count of trips, total time)

"""
class UndergroundSystem2:
    def __init__(self):
        self.start = {}
        self.trips = collections.defaultdict(lambda: (0,0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_name, t1 = self.start[id]
        count, time = self.trips[(start_name, stationName)]
        self.trips[(start_name, stationName)] = (count + 1, time + t - t1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, time = self.trips[(startStation, endStation)]
        return time / count

###############################################################################
"""
Solution 3: use two dicts:

start[startStation][id] = start time

end[endStation][id] = end time

"""
class UndergroundSystem3:
    def __init__(self):
        self.start = collections.defaultdict(lambda: collections.defaultdict(int))
        self.end = collections.defaultdict(lambda: collections.defaultdict(int))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[stationName][id] = t
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.end[stationName][id] = t
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = 0
        count = 0

        for id in self.end[endStation]:
            if id in self.start[startStation]:
                count += 1
                time += self.end[endStation][id] - self.start[startStation][id]
        
        return time / count if count else 0
        