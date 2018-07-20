# 1. Use append() to add Jupiter and Saturn at the end of the list.
# 2. Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
# 3. Use insert() to add Earth, and Venus in the correct order.
# 4. Use append() again to add Pluto to the end of the list.
# 5. Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
# 6. Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
planets = []
planets.append("Mercury")
planets.append("Mars")
planets.extend(["Jupiter", "Saturn"])
planets.extend(["Uranus", "Neptune"])
planets.insert(1, "Venus")
planets.insert(2, "Earth")
planets.append("Pluto")
print(planets)

rocky_planets = planets[0:4]
print(rocky_planets)
del(planets[8])
print(planets)

# Iterating over planets
# 1. Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
# 2. Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which sattelites have visited.

Anthony = ("Anthony", "Pluto")
Hayley = ("Hayley", "Saturn")
Jack = ("Jack", "Mars")
spacecrafts = [Anthony, Hayley, Jack]
print(spacecrafts[1])

for craft in spacecrafts:
    print(craft)
