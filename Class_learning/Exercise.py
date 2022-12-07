##Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def  __init__(self,max_speed= 0, mileage =10):
        self.max_speed = max_speed
        self.mileage = mileage

cars = Vehicle(20,40 )

print(cars.max_speed)
print(cars.mileage)


