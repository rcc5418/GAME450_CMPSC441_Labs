''' 
Lab 2: Cities and Routes

In the final project, you will need a bunch of cities spread across a map. Here you 
will generate a bunch of cities and all possible routes between them.
'''
import random
import itertools

def get_randomly_spread_cities(size, n_cities):
    """
    > This function takes in the size of the map and the number of cities to be generated 
    and returns a list of cities with their x and y coordinates. The cities are randomly spread
    across the map.
    
    :param size: the size of the map as a tuple of 2 integers
    :param n_cities: The number of cities to generate
    :return: A list of tuples, each representing a city, with random x and y coordinates.
    """
    # Consider the condition where x size and y size are different
    city_locations=[]
    for i in range(n_cities):
        x_coord = random.randint(1, size[0])
        y_coord = random.randint(1, size[1])
        city_locations.append((x_coord,y_coord))
    return city_locations
    """
    Alternate solution:
    return [(random.randin(1,size[0]),random.randint(1,size[1]))
                for i in range(n_cities)]
    """

def get_routes(city_names):
    """
    It takes a list of cities and returns a list of all possible routes between those cities. 
    Equivalently, all possible routes is just all the possible pairs of the cities. 
    
    :param cities: a list of city names
    :return: A list of tuples representing all possible links between cities/ pairs of cities, 
            each item in the list (a link) represents a route between two cities.
    """
    city_routes=[]
    for i, city in enumerate(city_names):
        for j, other_city in enumerate(city_names):
            if(j!=i):
                city_routes.append((city,other_city))
    return city_routes
    """
    Alternate solution: (using itertools)
    return list(combinations(city_names,2))
    """

# TODO: Fix variable names
if __name__ == '__main__':
    city_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    '''print the cities and routes'''
    cities = get_randomly_spread_cities((100, 200), len(city_names))
    routes = get_routes(city_names)
    print('Cities:')
    for i, city in enumerate(cities):
        print(f'{city_names[i]}: {city}')
    print('Routes:')
    for i, route in enumerate(routes):
        print(f'{i}: {route[0]} to {route[1]}')
