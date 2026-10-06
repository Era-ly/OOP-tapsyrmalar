class Pet:
     def __init__(self,name,age):
          self._name = name
          self._age = age

     def set_name(self,new_name):
          self._name = new_name

     def get_name(self):
          return self._name

     def set_age(self,new_age):
          self._age = new_age

     def get_age(self):
          return self._age
