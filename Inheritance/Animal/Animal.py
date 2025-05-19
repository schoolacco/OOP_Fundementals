class Animal:
    def __init__(self, _name):
     self.name = _name
    def get_sound(self):
       print(f"A {self.name} makes a sound.")
class Dog(Animal):
   def __init__(self, _name, _sound):
      super().__init__(_name)
      _name = "Dog"
      _sound = "Bark"
      self.sound = _sound
   def get_sound(self):
      print(F"A {self.name} makes a {self.sound} sound.")
class Cat(Animal):
   def __init__(self, _name, _sound):
      super().__init__(_name)
      _name = "Cat"
      _sound = "Meow"
      self.sound = _sound
   def get_sound(self):
      print(F"A {self.name} makes a {self.sound} sound.")