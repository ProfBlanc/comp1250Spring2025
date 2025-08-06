"""
Person
    attributes
        name: min 3 chars & 1 space
        age: b/w 0 and 100
    action
        get_initials: return F.L.

    static method: method that belongs to class
                    1 instance in VM of method

                    get_age_categories
                        Enfant,Child,Teen,Adult,Senior

    class method: method that creates new instance
                  create preset categories of object

                  create_teen

"""
import random
import sys


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0 and value <= 100:
            self.__age = value
        else:
            raise ValueError(f"Invalid age value: {value}")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3 and " " in value:
            self.__name = value
        else: raise ValueError(f"Invalid name value: {value}")

    @classmethod
    def create_teen(cls, name="Angry Teen"):
        return cls(name, random.randint(13, 17))
    def __str__(self): return f"name: {self.name}, age: {self.age}"
    @staticmethod
    def get_age_categories(): return "Enfant,Child,Teen,Adult,Senior".split(",")
    def get_initials(self):
        names = self.__name.split(" ")
        initials = ""
        for name in names:
            initials += name[0].upper() + "."

        return initials[:-1]
try:
    me = Person("Prof Blanc", 20)
    print(me.get_initials())
    me.age
    me.age = 21
    # print(me._Person__age)
    teen1 = Person.create_teen("Hungry Teen")
    teen2 = Person.create_teen()
    print(teen1)
    print(Person.get_age_categories())
except Exception as e:
    print(e, file=sys.stderr)
