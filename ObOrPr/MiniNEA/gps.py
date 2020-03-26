import sys,time


def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()

class Location:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.connectedLocations = {}
        self.connectedNPCs = {}
        self.connectedItems = {}
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_connectedLocations(self):
        return self.connectedLocations
    def get_connectedNPCs(self):
        return self.connectedNPCs
    def get_connectedItems(self):
        return self.connectedItems
    def set_name(self,name):
        self.name = name
    def set_description(self,description):
        self.description = description
    def link_location(self,location,type,type2):
        self.connectedLocations[type] = location
        location.connectedLocations[type2] = self
    def link_npc(self,npc,ShortDescription):
        self.connectedNPCs[ShortDescription] = npc
    def link_item(self,item,type):
        self.connectedItems[type] = item
    def goto(self,place):
        if place.lower() in self.connectedLocations:
            return self.connectedLocations[place.lower()]
        else:
            type("There is no"+" "+place+" "+"here")
            return self
    def info(self):
        type(self.name)
        line = ["-" for char in range(len(self.name)-2)]
        type("="+"".join(map(str,line))+"=")
        type(self.description.title())
        line = ["-" for char in range(len(self.description)-2)]
        type("="+"".join(map(str,line))+"=")
        for place in self.connectedLocations:
            type("There is an enterance to "+self.connectedLocations[place].get_description())
        for npc in self.connectedNPCs:
            type("There is a "+npc.title()+" here!")
        for item in self.connectedItems:
            type("You can see a "+item.title())

        print()