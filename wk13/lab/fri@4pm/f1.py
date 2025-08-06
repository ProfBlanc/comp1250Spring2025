"""
Person
    properties
        name: min 3 chars & 1 space
        age: b/t 0-100
    actions
        get_initials
        create_adult
        get_age_categories
"""
import random
import sys


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self): return f"Name is {self.name}, Age is {self.age}"

    @property
    def age(self): return self.__age
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0 and value <=100:
            self.__age = value
        else:
            raise ValueError(f"'{value}' is invalid. Only integers between 0 and 100 acceptable")

    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3 and " " in value:
            self.__name = value
        else:
            raise ValueError(f"'{value}' is invalid!")

    def get_initials(self):
        initials = ""

        for name in self.__name.split(" "):
            initials += name[0].upper() + "."
        return initials

    @staticmethod
    def get_age_categories(): return "Enfant,Child,Teen,Adult,Senior".split(",")

    @classmethod
    def create_adult(cls, name="Old Person", age=''):
        if isinstance(age, str):
            age = random.randint(18,65)
        elif not isinstance(age, int) or age < 18 or age > 65:
            raise ValueError("Age must be between 18 and 65")
        return cls(name, age)


try:
    old_person = Person.create_adult(age=54)
    print(old_person)
    me = Person("Ben Blanc", 20)
    #me1 = Person(1234, {9,4,3})
    #print(me1)

    me.age = 80
    print(me)
    print(me.get_initials())
except Exception as e:
    print("Error!", e, file=sys.stderr)