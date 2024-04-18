import sys
from pathlib import Path
sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))
from lab2.cities_n_routes import get_randomly_spread_cities, get_routes
from lab5.landscape import get_landscape, elevation_to_rgba, get_elevation
from lab7.ga_cities import game_fitness, setup_GA, solution_to_cities

city_names = [
        "Morkomasto",
        "Morathrad",
        "Eregailin",
        "Corathrad",
        "Eregarta",
        "Numensari",
        "Rhunkadi",
        "Londathrad",
        "Baernlad",
        "Forthyr",
    ]

size = width, height = 640, 480

city_locations = get_randomly_spread_cities(size, len(city_names))

elevation_array = get_elevation(size)
elevation = (elevation_array - elevation_array.min()) / (elevation_array.max() - elevation_array.min())
    # setup fitness function and GA
fitness = lambda solution, idx: game_fitness(
    solution, idx, elevation=elevation, size=size
)
fitness_function, ga_instance = setup_GA(fitness, len(city_names), size)

ga_instance.run()

best_solution = ga_instance.best_solution()[0]
city_locations = solution_to_cities(best_solution, size)
routes = get_routes(city_locations, int(len(city_locations)/4))

print(city_locations)
print(routes)

def route_exists(routes, cities, city_idx1, city_idx2):
    city1 = tuple(cities[city_idx1])
    city2 = tuple(cities[city_idx2])
    print(city1, " ", city2)
    for route in routes:
        route = tuple(map(tuple, route))  # Convert NumPy arrays to tuples
        if (city1 in route) and (city2 in route):
            return True
    return False

city_idx1 = 0
city_idx2 = 1
print(route_exists(routes, city_locations, city_idx1, city_idx2))