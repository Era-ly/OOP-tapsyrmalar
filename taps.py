class Pet:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def set_name(self,new_name):
        self._name=new_name
    def get_name(self):
        return self._name
    def set_age(self,new_age):
            self._age=new_age
    def get_age(self):
            return self._age


class Dog(Pet):
    def __init__(self, name, age):
         super().__init__(name, age)
    def bark(self):
         print("ит уреди")
    def make_sound(self):
     print("gaw-gaw")


class Cat(Pet):
    def __init__(self, name, age):
         super().__init__(name, age)
    def meow(self):
         print("mysyk meowlaidy")
    def make_sound(self):
     print("meoww")


class Bird(Pet):
    def __init__(self, name, age):
         super().__init__(name, age)
    def chirp(self):
         print("qus shiqyldaidy")
    def make_sound(self):
     print("pip-pip")


dog=Dog("aqtos",5)
cat=Cat("murka",2)
bird=Bird("vlad",1)

pets=[dog,cat,bird]

for pet in pets:
    pet.make_sound()