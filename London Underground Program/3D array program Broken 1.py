#Mega Array Of Doom

class Graph:
    def __init__(self):
        self.stations = [
            ["Marylebone",
                ["Marlyenbone",0],
                ["Baker Street",6]],
            ["Edgeware Road",
                ["Baker Street",5]],
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
tube = Graph()

run = 0
for station in tube.stations:
    for stop in station:
        if stop != station[0] and stop[0] not in tube.visited:
            if not tube.passed:
                tube.passed.append([stop[0],stop[1],station[0]])
            else:
                found = True
                for station2 in tube.passed:
                    if station2[0] != station[0]:
                        if stop[0] == station2[0]:

                            for location in tube.passed:
                                if location[0] == stop[0]:
                                    path = stop[1] + location[1]
                            if stop[1] < station2[1]:
                                tube.passed[run][1] = path
                                tube.passed[run][2] = station[0]
                            run =+ 1
                            found = False
                print(stop[0],"!=",station[0])
                if found:
                    tube.passed.append([stop[0],stop[1],station[0]])
    tube.visited.append(station[0])
for item in tube.passed:
    print (item)

