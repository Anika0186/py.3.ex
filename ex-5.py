1.
import random

num_dice = int(input("How many dice would you like to roll? "))
total = 0

for _ in range(num_dice):
    roll = random.randint(1, 6)
    total += roll

print(f"The total sum of your dice rolls is: {total}")

2.
numbers = []

while True:
    entry = input("Enter a number (or press Enter to quit): ")
    if entry == "":
        break
    numbers.append(int(entry))

numbers.sort(reverse=True)
top_five = numbers[:5]

print("The five greatest numbers in descending order are:")
for num in top_five:
    print(num)
3.
num = int(input("Enter an integer: "))

if num < 2:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
4.
 cities = []

        for i in range(5):
            city = input(f"Enter the name of city {i + 1}: ")
            cities.append(city)

        print("You entered the following cities:")
        for city in cities:
            print(city)





