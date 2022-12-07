class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass


school_bus = Bus('Maastricht', 50,10)
#
# print(school_bus.name)
# print(school_bus.max_speed)
# print(school_bus.mileage)

print("school name: ",school_bus.name,"Max Speed: ", school_bus.max_speed, "Mileage: ", school_bus.mileage )
