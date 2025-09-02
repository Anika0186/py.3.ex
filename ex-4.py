1.
num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1
2.
while True:
    inches = float(input("Enter inches (negative to quit): "))
    if inches < 0:
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters:.2f} cm")
3.
    numbers = []

    while True:
        entry = input("Enter a number (or press Enter to quit): ")
        if entry == "":
            break
        try:
            number = float(entry)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")

    if numbers:
        print(f"Smallest number: {min(numbers)}")
        print(f"Largest number: {max(numbers)}")
    else:
        print("No numbers were entered.")

        import random

target = random.randint(1, 10)

while True:
    guess = input("Guess a number between 1 and 10: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    else:
        print("Correct!")
        break

        correct_username = "python"
        correct_password = "rules"
        attempts = 0

        while attempts < 5:
            username = input("Username: ")
            password = input("Password: ")

            if username == correct_username and password == correct_password:
                print("Welcome")
                break
            else:
                print("Incorrect credentials.")
                attempts += 1

        if attempts == 5:
            print("Access denied")

            import random

def approximate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            points_inside_circle += 1

    pi_estimate = 4 * points_inside_circle / num_points
    return pi_estimate

def main():
    try:
        num_points = int(input("Enter the number of random points to generate: "))
        if num_points <= 0:
            print("Please enter a positive integer.")
            return

        pi_value = approximate_pi(num_points)
        print(f"\nApproximation of π using {num_points} random points: {pi_value}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()




