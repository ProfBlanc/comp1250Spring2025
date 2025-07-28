import sys


class Square:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
        
    # You can validate in class]
    # decorators: @text
    # @property
    # def blah(self): pass
    # @blah.setter
    # def blah(self, value): pass

    @property
    def length(self):
        return self.__length  # private property
    @length.setter
    def length(self, value_to_validate):
        if isinstance(value_to_validate, int) \
            and value_to_validate > 0:
            self.__length = value_to_validate
        else:
            self.__length = 1  # default value

    @property
    def width(self): return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) and value > 0 and value <= self.__length:
            self.__width = value
        else:
            self.__width = 1

    def __add__(self, other):
        if isinstance(other, Square):
            return Square( (self.length + other.length) // 2,
                           (self.width + other.width ) // 2
                           )
        else:
            print("Error!", file=sys.stderr)
            return Square(1, 1)

    def __str__(self):
        return f"Length={self.length}, Width={self.width}"
    

s1 = Square(length=10, width=5)
print(s1)

s1.length = -100

print(s1.length, s1)

print("*" * 20)

s2 = Square(length=-10, width=-5)
print(s2)

s3 = Square(10, 8)
s4 = Square(16, 14)
s5 = s3 + s4
print(s5)


# Be back at 12:18