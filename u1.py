#!/usr/bin/env python3
import math

cities = ["Prishtinë", "Shqipni", "Azi", "Atlantik", "Pejë"]
countries = ["Kosovë", "Buna", "Drini", "Prizren"]

cities.append(countries.pop(-1))
countries.append(cities.pop(1))
del cities[1:3]
countries.remove("Buna")
countries.pop(1)
print(cities, '\n', countries)
