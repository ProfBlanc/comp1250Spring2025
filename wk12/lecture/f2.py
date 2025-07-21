class Car:
    doors = 5
    cylinders = 4
    make = "Toyota"
    model = "MR2"

    def turn_engine_on(self):
        return "Engine is on"

    def turn_engine_off(self):
        return "Engine is off"


my_car = Car()
your_car = Car()

my_car.make = "Honda"
my_car.model = "Accord"

print(my_car.model)
print(your_car.model)

my_car.whatever = "blah"
print(my_car.whatever)
