import sys,time


def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()



class Item():
    def __init__(self,name,description,type):
        """Creates attributes for Item class"""
        self.name = name
        self.description = description
        self.type = type
    def get_name(self):
        """Returns name attribute"""
        return self.name
    def get_description(self):
        """Returns description attribute"""
        return self.description
    def get_type(self):
        """Returns type attribute"""
        return self.type
    def set_name(self,name):
        """Sets name attribute"""
        self.name = name
    def set_description(self,description):
        """Sets description attribute"""
        self.description = description
    def set_type(self,type):
        """Sets type attribute"""
        self.type = type
    def get_details(self):
        """Outputs item details"""
        type(self.name)
        type("Type:"+" "+self.type)
        type(self.description)
    def show(self):
        """Outputs simplified item details for use in a room"""
        type(("There is a"+" "+self.name+" "+"here"))
        type(self.description)

