class Vehicle:
    ##class variable
    color = 'White'

    ##instance variable
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    ##overide parent class information
    # color = "Black"
    # name = "God"
    # max_speed = 100
    # mileage = 1000
    pass

class Car(Bus):
    pass

my_car = Car("Light year", 1000,100)
my_bus = Bus("Light year", 10,10)

print(my_car.color, my_car.name, my_car.max_speed, my_car.mileage)
print(my_bus.color, my_bus.name, my_bus.max_speed, my_bus.mileage)
