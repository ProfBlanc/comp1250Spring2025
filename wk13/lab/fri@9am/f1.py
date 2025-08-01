"""
Person
    constructor
        name: at least 3 chars and contain 1 space
        age: b/t 0 and 100
    method
        initials: return first letter of every name sep by .
    static method: method that belongs to class
                    age_categories
                        return list of enfant,child,etc
    class method: method that creates a new object
                    create a category of object

"""
from random import randint
from sys import stderr


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3 and " " in value:
            self.__name = value
        else:
            raise ValueError(f"Name '{value}' is invalid")
    def get_initials(self):
        pieces =  self.__name.split(" ")
        initials = ""
        for letter in pieces:
            initials += letter[0].upper() + "."
        #B.B.
        # remove trailing .
        initials = initials[:-1]
        return initials
    @staticmethod
    def get_age_categories():
        return "Enfant,Child,Teen,Adult,Senior".split(",")

    def get_age_category(self):
        categories = self.get_age_categories()
        if self.age < 5: return categories[0]
        elif self.age < 13: return categories[1]
        elif self.age < 18: return categories[2]
        elif self.age < 66: return categories[3]
        else : return categories[4]

    @classmethod
    def create_adult(cls, name="Unknown Person"):
        return cls(name=name, age=randint(18, 65))

    def __str__(self): return f"Name: {self.name}, Age: {self.age}"


try:
    me = Person("Ben Prof Blanc Cool Teacher", 20)
    print(me.get_initials())
    print(Person.get_age_categories())
    print(me.get_age_category())

    friend = Person.create_adult("ab cd")
    print(friend)
except Exception as e:
    print(e, file=stderr)