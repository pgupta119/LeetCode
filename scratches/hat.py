import random
class Hat:
    # def __init__(self):
    #     self.houses =["Red", "Blue", "Green", "Yellow"]
    houses = ["Red", "Blue", "Green", "Yellow"]

    @classmethod
    def sort(self, name):
        print(name, "is in", random.choice(self.houses))



# hat = Hat()
Hat.sort("Deepak")