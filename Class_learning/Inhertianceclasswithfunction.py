class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity=130):
        return print(f"The capacity of a {self.name} is {capacity} passengers")


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


bus_obj = Bus("Arriva", 120, 20)
print(bus_obj.seating_capacity())

# Bus.seating_capacity()
