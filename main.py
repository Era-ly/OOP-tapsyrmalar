from dog import Dog
from cat import Cat
from bird import Bird


dog = Dog("aqtos",5)
cat = Cat("murka",2)
bird = Bird("vlad",1)

pets = [dog, cat, bird]

for pet in pets:
    pet.make_sound()
