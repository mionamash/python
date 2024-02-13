class Shapes:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width =width
        self.height = height
    def calculate_area(self):
        return self.width * self.height

class Circle(Shapes):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return





    def calculate_totalarea(shapes):