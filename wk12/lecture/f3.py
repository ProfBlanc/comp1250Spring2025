class Car:
    # doors = 5
    # cylinders = 4
    # make = "Toyota"
    # model = "MR2"


    # constructor: allows user to create and customize all in 1 step
    def __init__(self, make="Toyota", model="MR2", cylinders=4, doors=5):
        self.make = make
        self.model = model
        self.cylinders = cylinders
        self.doors = doors

    def __str__(self):
        return f"Make={self.make}, Model={self.model}, " \
               f"Doors={self.doors}, Cylinders={self.cylinders}"
    def turn_engine_on(self):
        return "Engine is on"

    def turn_engine_off(self):
        return "Engine is off"


my_car = Car()
your_car = Car(make="Honda", model="Accord", doors=5, cylinders=4)
print(your_car)

print(my_car.turn_engine_off())
print(my_car.turn_engine_on())
