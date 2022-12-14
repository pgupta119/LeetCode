## import random
import random
import statistics

# use of choice
coin = random.choice(["heads", "tails"])
print(coin)

# use of randint
number = random.randint(-100, -1)
print(number)

# use of shuffle
numbers = [1, 2, 4, 6, 7, 10]
random.shuffle(numbers)
for shuffle_number in numbers:
    print(shuffle_number)

print(" Mean is: ", statistics.mean([100, 80, 20, 15, 75]))