from pet import Pet


class Cat(Pet):
     def __init__(self, name, age):
          super().__init__(name, age)
     
     def meow(self):
          print("mysyk meowlaidy")

     def make_sound(self):
          print("meoww")
