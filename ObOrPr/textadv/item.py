class Item():
    def __init__(self,name,description,type):
        self.name = name
        self.description = description
        self.type = type
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_type(self):
        return self.type
    def set_name(self,name):
        self.name = name
    def set_description(self,description):
        self.description = description
    def set_type(self,type):
        self.type = type
    def get_details(self):
        print(self.name)
        print("Type:",self.type)
        print(self.description)

