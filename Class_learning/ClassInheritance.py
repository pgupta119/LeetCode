class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):

    # def fare(self):
    #     return (self.capacity*100 + self.capacity*0.1)

    def fare(self):
        amount = super().fare()
        amount += amount * 0.1
        return amount


my_bus = Bus('Arriva', 10, 234)

print("Bus name is: ", my_bus.name, "Bus mileage is: ", my_bus.mileage, "Total Fare is: ", my_bus.fare())
