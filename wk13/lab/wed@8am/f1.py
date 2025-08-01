"""
Create a Person class
    properties
        name    ensure at least 3 chars and has 1 space
        age     natural number (0 or more). 0-100
    methods
        get_initials    get the first char after a space

    if any restrictions not met, raise exception
"""
import random
import sys


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.__name}. Age: {self.__age}"

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3 and " " in value:
            self.__name = value
        else:
            raise ValueError(value + " is invalid")
    @property
    def age(self): return self.__age
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0 and value <= 100:
            self.__age = value
        else:
            raise ValueError(f"The age of {value} is not between 0-100")

    def get_initials(self):
        # "Ben Blanc"  values = ["Ben", "Blanc"]
        values = self.__name.split(" ")
        first_initial = values[0][0]
        second_initial = values[1][0]
        return first_initial + "." + second_initial + "."

    @staticmethod
    def get_age_categories():
        return "Enfant,Child,Teenager,Adult,Senior".split(",")

    @classmethod
    def create_teenager(cls, name="Angry Teen"):
        return cls(name=name, age=random.randint(13, 19))

try:
    p = Person("Ben Blanc", 20)
    print(p)
    print(Person.get_age_categories())
    teen = Person.create_teenager("High Schooler")
    print(teen)

except ValueError as e:
    print(e, file=sys.stderr)
