import random
# Real World Entity
# @classmethod = class method(Decorator)
# @staticmethod = static method(Decorator)
# @property = property(Decorator)

class Hat:
   houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
   @classmethod
   def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("ToFu")
