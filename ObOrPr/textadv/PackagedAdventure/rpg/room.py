import sys,time


def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()

class Room():

    def __init__(self, room_name):
        """Creates attributes for Room class"""
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
    def set_description(self,room_description):
        """Sets description attribute"""
        self.description = room_description
    def get_description(self):
        """Returns description attribute"""
        return self.description
    def set_name(self,room_name):
        """Sets name attribute"""
        self.name = room_name
    def get_name(self):
        """Returns name attribute"""
        return self.name
    def set_character(self, new_char):
        """Sets character attribute"""
        self.character = new_char
    def set_item(self, new_item):
        """Sets item attribute"""
        self.item = new_item
    def get_item(self):
        """Returns item attribute"""
        return self.item
    def get_character(self):
        """Returns item attribute"""
        return self.character
    def describe(self):
        """Outputs room description"""
        type(self.description)
    def link_room(self, room_to_link, direction):
        """Adds room to the direcionary of linked rooms"""
        self.linked_rooms[direction] = room_to_link
    def get_details(self):
        """Outputs details of the room for use within a game"""
        type(self.name)
        type("--------------------")
        type(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            type(("The"+" "+room.get_name()+" "+"is"+" "+direction))
    def move(self,direction):
        """Will return a connected room if direction matches"""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            type("You cannot go that way")
            return self