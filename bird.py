from pet import Pet

class Bird(Pet):
     def __init__(self, name, age):
          super().__init__(name, age)
     def chirp(self):
          print("qus shiqyldaidy")
     def make_sound(self):
          print("pip-pip")
