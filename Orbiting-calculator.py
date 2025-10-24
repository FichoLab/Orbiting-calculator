import math

G =  6.67430e-11  # Gravitational constant

# AU is short for astronomical unit
# 1 AU = 93,000,000 miles = 149,598,000 kilometers.
# μ = M * G

# Planet dictionary: (Planet name, Mass in kg, Radius in meters, μ)
planet = {
    "1": ("Mercury",  3.30e23, 2.4397e6, 3.30e23 * G),
    "2": ("Venus",    4.87e24, 6.0518e6, 4.87e24 * G),
    "3": ("Earth",    5.97e24, 6.371e6,  5.97e24 * G),
    "4": ("Mars",     6.39e23, 3.389e6,  6.39e23 * G),
    "5": ("Jupiter",  1.90e27, 6.9911e7, 1.90e27 * G),
    "6": ("Saturn",   5.68e26, 5.8232e7, 5.68e26 * G),
    "7": ("Uranus",   8.68e25, 2.5362e7, 8.68e25 * G),
    "8": ("Neptune",  1.02e26, 2.4622e7, 1.02e26 * G),

    # Pluto lovers
    "9": ("Pluto",    1.31e22, 1.1883e6, 1.31e22 * G)
}

# Minimum safe orbit altitudes (in km)
safe_orbit = {
    "1": 100,    # Mercury
    "2": 250,    # Venus
    "3": 160,    # Earth
    "4": 150,    # Mars
    "5": 5000,   # Jupiter
    "6": 6000,   # Saturn
    "7": 3000,   # Uranus
    "8": 3000,   # Neptune
    "9": 50      # Pluto
}

print("Orbital Period Calculator")
print("1. Orbit around the Sun (Kepler's 3rd law)")
print("2. Orbit around the Planet")
choice = input("Choose an option:")

if choice == "1":
    print("Orbit around the Sun")
    distance = float(input("Enter distance from Sun in AU: "))
    T = math.sqrt(distance ** 3)
    print(f"Orbital period: {T:.2f} Earth years")

elif choice == "2":
    print("Orbit around the Planet")
    planet_choice = input("Enter planet number: ")

    if planet_choice in planet:
        name, mass_planet, radius, μ = planet[planet_choice]

        # Ask for orbit altitude
        altitude_km = float(input(f"Enter orbit altitude above {name} in kilometers (km): "))

        # Checking for safe orbit
        min_altitude = safe_orbit[planet_choice]
        if altitude_km < min_altitude:
            print(f"===Warning: {altitude_km} km is too close and unable to orbit {name}.===")
            print(f"(Auto-Correct) Using realistic safe altitude: {min_altitude} km instead.")
            altitude_km = min_altitude

        altitude_m = altitude_km * 1000 # Convert to meters
        r = radius + altitude_m  # Total distance from planet center

        T = 2 * math.pi * math.sqrt(r**3 / (G * mass_planet))
        print(f"Orbital period around {name}:")
        print(f"{T:.2f} seconds")
        print(f"{T/60:.2f} minutes")
        print(f"{T/3600:.2f} hours")
        print(f"{T/86400:.2f} days")
    else:
        print("Invalid planet selection.")

    # Vis-Vira Equation (Orbital velocity) = Determines the velocity of an orbiter at any point in its orbit
    # v = √[ μ (2/r - 1/a) ]

    a = ((μ * T) / (4 * math.pi)) ** 1/3     # a = semi-major axis at the orbit

    inside = μ * (2/radius - 1/a)
    v = math.sqrt(inside)
    print(f"Orbital velocity: {v:.2f} m/s")

    # Specific Orbital Energy
    specific_orbital_energy = - (μ / 2 * a) # (J/kg)
    print(f"Specific Orbital Energy: {specific_orbital_energy:.2f} J/kg")



