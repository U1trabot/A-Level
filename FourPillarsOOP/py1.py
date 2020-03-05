class Rectangle():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
class Square(Rectangle):
    def __init__(self,width,height):
        if width == height:
            super().__init__(width, height)
        else:
            raise Exception("Squares have an equal width and height")


shape = Square(3,3)
print(shape.get_area())