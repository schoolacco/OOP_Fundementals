from shapepy import Circle, Rectangle, Square
# Creating instances of concrete subclasses 
circle = Circle(5) 
rectangle = Rectangle(4, 6, 3) 
square = Square(3)

# Using the same interface to compute perimeter 
print("Circle Perimeter:", circle.perimeter()) 
print("Rectangle Perimeter:", rectangle.perimeter()) 
print("Square Perimeter:", square.perimeter())

print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())
print("Square Area:", square.area())

print("Circle Volume:", circle.volume())
print("Rectange Volume:", rectangle.volume())
print("Square Volume", square.volume())