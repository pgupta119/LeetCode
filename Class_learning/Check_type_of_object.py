class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)

## checking type of object
print(type(School_bus))

## checking the instance sharing with the class
print(isinstance(School_bus, Bus))
