## Orbital Period Calculator ##

This project calculates how long it takes for an object to complete an orbit, either:
-around the Sun using Kepler's 3rd law or
-around any Planet in our Solar System using Newton's law of gravitation

## How this works ##

At the start user has two options:
1. Orbit around the Sun (Kepler's 3rd law)
2. Orbit around the Planet

User then types 1. or 2.
If user types "1." than user needs to type distance from the Sun in Astronomical Units (AU).

*1 AU (Astronomical Unit) = 93,000,000 miles = 149,598,000 kilometers.*

After that, program calculates how long will it take to complete that orbit and result will be presented in Earth years.

If "2." is selected, user needs to select a planet, after which program will show "Enter orbit altitude above Mars in kilometers (km):"
After that program will calculate Orbital period around selected planet.

However, to keep results realistic, the program includes minimum safe orbit altitudes for each planet:
# Minimum safe orbit altitudes (in km)
*And yeah I added Pluto for people how love it soo much*

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

If the entered altitude is lower than the safe limit, program auto-corrects and and calculates with minimum altitude.

After program calculates Orbital period around selected planet, than it will calculate Orbital velocity using Vis-Vira Equation.

Vis-Vira Equation (Orbital velocity) = Determines the velocity of an orbiter at any point in its orbit
**v = √[ μ (2/r - 1/a) ]**



## How to run ##
Install Python and pandas 'pip install pandas' You can install IDE of your choice, in my case, I used PyCharm

*Created by Filip, a high school mechatronics student passionate about space industry*






