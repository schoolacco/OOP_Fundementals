from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
         pass
	
    def volume(self):
         pass
class Circle(Shape):
    def __init__(self, radius):
      self.radius = radius
    	
    def perimeter(self):
       return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius ** 2
    def volume(self):
        return math.pi * (4/3) * self.radius ** 3
class Rectangle(Shape):
    def __init__(self, width, height, breadth):
        self.width = width
        self.breadth = breadth
        self.height = height
    def perimeter(self):
      return 2 * (self.width + self.breadth)

    def area(self):
      return self.width * self.breadth
    
    def volume(self):
        return self.width * self.breadth * self.height
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def perimeter(self):
        return self.length * 4
    def area(self):
        return self.length ** 2
    def volume(self):
        return self.length ** 3