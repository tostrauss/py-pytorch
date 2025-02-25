class Student:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def __str__(self):
        return f'{self.name} is {self.age} years old.'
    
    def get(cls):
        name = input('Enter name: ')
        age = input('Enter age: ')
        return cls(name, age)