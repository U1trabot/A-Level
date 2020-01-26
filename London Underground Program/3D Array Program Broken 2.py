#Mega Array Of Doom
import time
class Graph:
    def __init__(self):
        self.stations = [
            ["Marylebone",
                ["Marlyenbone",0],
                ["Baker Street",6],
                ["Edgeware Road",9999],
                ["Bond Street", 9999],
                ["South Kensington", 9999],
                ["Victoria", 9999],
                ["Oxford Circus", 9999],
                ["Westminster", 9999],
                ["Piccadilly Circus", 9999],
                ["Charing Cross", 9999],
                ["Embankment", 9999],
                ["Waterloo", 9999],
                ["Blackfriars", 9999],
                ["Cannon Street", 9999],
                ["Monument", 9999],
                ["London Bridge", 9999],
                ["Bank", 9999],
                ["Leicester Square", 9999],
                ["Tottenham Court Road", 9999],
                ["Green Park", 9999],
                ["Moorgate", 9999],
                ["Farringdon", 9999],
                ["Liverpool Street", 9999],
                ["King's Cross St. Pancras", 9999],
                ["Holborn", 9999],
                ["Euston",9999],
                ["Warren Street", 9999]],
            ["Edgeware Road",
                ["Baker Street",10]],
            ["Baker Street",
                ["Marylebone",6],
                ["Edgeware Road",10],
                ["King's Cross St. Pancras",38],
                ["Oxford Circus",25],
                ["Bond Street",16]],
            ["Bond Street",
                ["Baker Street",16],
                ["Oxford Circus",7],
                ["Green Park",14]],
            ["South Kensington",
                ["Victoria",30],
                ["Green Park",36]],
            ["Victoria",
                ["South Kensington",30],
                ["Green Park",19],
                ["Westminster",22]],
            ["Oxford Circus",
                ["Baker Street",25],
                ["Bond Street",7],
                ["Piccadilly Circus",12],
                ["Tottenham Court Road",9],
                ["Green Park",15],
                ["Warren Street",18]],
            ["Westminster",
                ["Victoria",22],
                ["Waterloo",17],
                ["Green Park",21],
                ["Embankment",10]],
            ["Piccadilly Circus",
                ["Green Park",8],
                ["Oxford Circus",12],
                ["Leicester Square",6],
                ["Charing Cross",11]],
            ["Charing Cross",
                ["Embankment",3],
                ["Leicester Square",7],
                ["Piccadilly Circus",11]],
            ["Embankment",
                ["Blackfriars",19],
                ["Waterloo",6],
                ["Charing Cross",3],
                ["Westminster",10]],
            ["Waterloo",
                ["Westminster",17],
                ["Embankment",6],
                ["Bank",33]],
            ["Blackfriars",
                ["Embankment",19],
                ["Cannon Street",14]],
            ["Cannon Street",
                ["Blackfriars",14],
                ["Monument",5]],
            ["Monument",
                ["Cannon Street",5],
                ["Bank",0],
                ["London Bridge",6],
                ["Moorgate",9]],
            ["London Bridge",
                ["Monument",6]],
            ["Bank",
                ["Monument",0],
                ["Liverpool Street",10],
                ["Holborn",31]],
            ["Leicester Square",
                ["Piccadilly Circus",6],
                ["Charing Cross",7],
                ["Tottenham Court Road",8],
                ["Holborn",12]],
            ["Tottenham Court Road",
                ["Oxford Circus",9],
                ["Warren Street",14],
                ["Holborn",10],
                ["Leicester Square",8]],
            ["Green Park",
                ["Victoria",19],
                ["South Kensington",36],
                ["Bond Street",14],
                ["Oxford Circus",15],
                ["Westminster",21],
                ["Piccadilly Circus",8]],
            ["Moorgate",
                ["Liverpool Street",6],
                ["Monument",9],
                ["Farringdon",18],
                ["Old Street",9]],
            ["Farringdon",
                ["Moorgate",18],
                ["King's Cross St. Pancras",26]],
            ["Liverpool Street",
                ["Moorgate",6],
                ["Bank",10]],
            ["King's Cross St. Pancras",
                ["Old Street",36],
                ["Euston",12],
                ["Holborn",23],
                ["Baker Street",38],
                ["Farringdon",26]],
            ["Holborn",
                ["Tottenham Court Road",10],
                ["Leicester Square",12],
                ["Bank",31],
                ["King's Cross St. Pancras",23]],
            ["Euston",
                ["King's Cross St. Pancras",12],
                ["Warren Street",9]],
            ["Warren Street",
                ["Tottenham Court Road",7],
                ["Euston",9],
                ["Oxford Circus",18]],
            ["Old Street",
                ["Moorgate", 9],
                ["King's Cross St. Pancras", 36]]
            ]
        self.passed = list()
        self.visited = list()
    def dijsktra(self):
        while len(self.visited) < 26:
            for station in self.stations[0]:
                if station != self.stations[0][0]:
                    time.sleep(0.1)
                    print(station[1])
                    time.sleep(0.05)
                    print("Plotting path of",station[0])
                    self.passed.append([station[0],station[1],self.stations[0][0]])
            for location in self.stations:
                if location[0] != self.stations[0][0]:
                    for stop in location:
                        if stop != location[0]:
                            Found = False
                            self.count = stop[1]
                            address = stop[0]
                            while not Found:
                                for place in self.passed:
                                    if place[0] == address and place[1] < 9999:
                                        time.sleep(0.1)
                                        print(self.count,"+",place[1])
                                        time.sleep(0.05)
                                        self.count += place[1]
                                        print("=",self.count)
                                        address = place[2]
                                        if address == self.stations[0][0]:
                                            Found = True
                                else:
                                    Found = True
                            run = 0
                            for place2 in self.passed:
                                if place2[0] == stop[0]:
                                    if self.count < place2[1] and place2[0] not in self.visited:
                                        time.sleep(0.1)
                                        print("Plotting path of",location[0])
                                        self.passed[run][1] = self.count
                                        self.passed[run][2] = location[0]
                                    else:
                                        pass
                                run += 1
                self.visited.append(location[0])

tube = Graph()
tube.dijsktra()
print()
print("________________________________________")
for item in tube.passed:
    time.sleep(0.1)
    print(item[0],"|"+str(item[1])+"|",item[2])
time.sleep(0.2)
print("________________________________________")
print()
print("Process Finished")
print()
for item2 in tube.passed:
    time.sleep(0.1)
    if item2[1] == 9999:
        print(item2[0],"has errored")
input()




