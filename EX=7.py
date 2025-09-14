# Define seasons as a tuple
seasons = ("Winter", "Spring", "Summer", "Autumn")

# Ask user for month number
month = int(input("Enter the number of a month (1-12): "))

# Determine season
if month in [12, 1, 2]:
    season = seasons[0]
elif month in [3, 4, 5]:
    season = seasons[1]
elif month in [6, 7, 8]:
    season = seasons[2]
elif month in [9, 10, 11]:
    season = seasons[3]
else:
    season = "Invalid month"

print("Season:", season)





# Create an empty set to store names
names = set()

while True:
    name = input("Enter a name (or press Enter to finish): ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

# Print all names
print("\nNames entered:")
for n in names:
    print(n)



# Dictionary to store ICAO codes and airport names
airports = {}

while True:
    print("\nChoose an option:")
    print("1 - Enter a new airport")
    print("2 - Fetch airport information")
    print("3 - Quit")
    choice = input("Your choice: ")

    if choice == "1":
        icao = input("Enter ICAO code: ").upper()
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport added.")
    elif choice == "2":
        icao = input("Enter ICAO code to fetch: ").upper()
        if icao in airports:
            print("Airport name:", airports[icao])
        else:
            print("Airport not found.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
