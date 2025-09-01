name = input("What is your name? ")
print(f"Hello, {name}!")

2. radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle is {area:.2f}")

3.length = float(input("Enter the length of the rectangle: "))

width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is {area:.2f}")
print(f"The perimeter of the rectangle is {perimeter:.2f}")

4.
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
_sum = num1 + num2 + num3
product = num1 * num2 * num3
average = _sum / 3
print(f"Sum: {_sum}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")

5
# Constants GRAMS_PER_LOT = 13.3
# LOTS_PER_POUND = 32
# POUNDS_PER_TALENT = 20
# User input
# talents = float(input("Enter talents: "))
# pounds = float(input("Enter pounds: "))
# lots = float(input("Enter lots: "))
# Convert everything to lots
# total_lots = (talents * POUNDS_PER_TALENT + pounds) * LOTS_PER_POUND + lots total_grams = total_lots * GRAMS_PER_LOT
# Convert grams to kilograms and grams kilograms = int(total_grams // 1000) grams = total_grams % 1000 print(f"The weight in modern units: {kilograms} kilograms and {grams:.2f} grams.")

6. # 3-digit code (0–9
# three_digit_code = [random.randint(0, 9) for _ in range(3)]
# 4-digit code (1–6)
# four_digit_code = [random.randint(1, 6) for _ in range(4)]
# print("3-digit combination:", three_digit_code)
# print("4-digit combination:", four_digit_code)