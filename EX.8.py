import sqlite3

# Connect to the database
conn = sqlite3.connect("airports.db")
cursor = conn.cursor()

# Ask user for ICAO code
icao = input("Enter ICAO code: ").upper()

# Query the airport name and town
cursor.execute("SELECT name, municipality FROM airport WHERE ident = ?", (icao,))
result = cursor.fetchone()

# Display result
if result:
    print(f"Airport Name: {result[0]}")
    print(f"Location (Town): {result[1]}")
else:
    print("No airport found with that ICAO code.")

conn.close()


import sqlite3

# Connect to the database
conn = sqlite3.connect("airports.db")
cursor = conn.cursor()

# Ask user for country code
country_code = input("Enter area code (e.g., FI): ").upper()

# Query airports grouped by type
cursor.execute("""
    SELECT type, COUNT(*) 
    FROM airport 
    WHERE iso_country = ? 
    GROUP BY type 
    ORDER BY type
""", (country_code,))

results = cursor.fetchall()

# Display results
if results:
    print(f"\nAirports in {country_code} grouped by type:")
    for airport_type, count in results:
        print(f"{airport_type}: {count}")
else:
    print("No airports found for that country code.")

conn.close()
