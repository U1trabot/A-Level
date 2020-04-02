import sys,time


def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")
    sys.stdout.flush()

class Location:
    """Main Location Object"""
    def __init__(self,name,description):
        self.name = name #Name Of Location
        self.description = description #Description Of Location
        self.connectedLocations = {} #Dictionary Of Connected Locations
        self.connectedNPCs = {} #Dictionary Of Connected NPCs
        self.connectedItems = {} #Dictionary Of Connected Items
    def get_name(self):
        """Returns Name For Location Object"""
        return self.name
    def get_description(self):
        """Returns Description For Location Object"""
        return self.description
    def get_connectedLocations(self):
        """Returns The Dictionary Of Connected Locations For The Location Object"""
        return self.connectedLocations
    def get_connectedNPCs(self):
        """Returns The Dictionary Of Connected NPCs For The Location Object"""
        return self.connectedNPCs
    def get_connectedItems(self):
        """Returns The Dictionary Of Connected Items For The Location Object"""
        return self.connectedItems
    def set_name(self,name):
        """Sets The Name Attribute"""
        self.name = name
    def set_description(self,description):
        """Sets The Description Attribute"""
        self.description = description
    def link_location(self,location,type,type2):
        """Adds A Location To The Dictionary Of Connected Locations"""
        self.connectedLocations[type] = location
        location.connectedLocations[type2] = self
    def link_npc(self,npc,ShortDescription):
        """Adds A NPC To The Dictionary Of Connected NPCs"""
        self.connectedNPCs[ShortDescription] = npc
    def link_item(self,item,type):
        """Adds An Item To The Dictionary Of Connected Items"""
        self.connectedItems[type] = item
    def goto(self,place):
        """Returns A Valid Location From The Connected Locations Dictionary Based On Input"""
        if place.lower() in self.connectedLocations:
            return self.connectedLocations[place.lower()]
        else:
            type("There is no"+" "+place+" "+"here")
            return self
    def info(self):
        """Outputs Infomartion About Itself"""
        type(self.name)
        line = ["-" for char in range(len(self.name)-2)]
        type("="+"".join(map(str,line))+"=")
        type(self.description.title())
        line = ["-" for char in range(118)]
        type("="+"".join(map(str,line))+"=")
        for place in self.connectedLocations:
            type("There is an enterance to "+place.title())
        for npc in self.connectedNPCs:
            type("There is a "+npc.title()+" here!")
        for item in self.connectedItems:
            type("You can see a "+item.title())

        print()