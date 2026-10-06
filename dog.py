from pet import Pet

class Dog(Pet):
     def __init__(self, name, age):
          super().__init__(name, age)

     def bark(self):
          print("ит уреди")

     def make_sound(self):
          print("gaw-gaw")
