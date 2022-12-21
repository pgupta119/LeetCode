import maths





class Statistics:

    def __init__(self,number):
        self.number = number

    def mean(self, number):
        return sum(number)/len(number)


    def median(self, number):
        return sum(number)

    def mode(self, number):
        return sum(number - number)

    def standard_deviation(self, number):
        return number + 10


numbers = []
for _ in range(0,10):
    number = int(input('Enter the numbers '))
    numbers.append(number)

print(numbers)



