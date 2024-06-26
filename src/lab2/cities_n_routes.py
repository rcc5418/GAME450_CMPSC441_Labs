''' 
Lab 2: Cities and Routes

In the final project, you will need a bunch of cities spread across a map. Here you 
will generate a bunch of cities and all possible routes between them.
'''
import random
import itertools

#rcc: DisjointSet class and kruskal_mst function generated by ChatGPT to create least number of routes possible
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
        return True

def kruskal_mst(edges, n):
    edges.sort(key=lambda x: x[2])
    mst = []
    ds = DisjointSet(n)
    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
    return mst

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
    return [(random.randint(1, size[0]), random.randint(1, size[1])) for city in range(n_cities)]
    

def get_routes(cities, num_extra_edges = 0):
    """
    It takes a list of cities and returns a list of all possible routes between those cities. 
    Equivalently, all possible routes is just all the possible pairs of the cities. 
    
    :param cities: a list of cities
    :return: A list of tuples representing all possible links between cities/ pairs of cities, 
            each item in the list (a link) represents a route between two cities.
    """
    #return list(itertools.combinations(cities, 2))
    n = len(cities)
    edges = [(i, j, random.randint(1, 100)) for i, j in itertools.combinations(range(n), 2)]
    mst_edges = kruskal_mst(edges, n)

     # Add extra edges beyond minimum spanning tree
    extra_edges = []
    while len(extra_edges) < num_extra_edges:
        u, v = random.sample(range(n), 2)
        if (u, v) not in mst_edges:
            extra_edges.append((u, v, random.randint(1, 100)))
        
    routes = [(cities[u], cities[v]) for u, v, _ in mst_edges + extra_edges]
    return routes


# TODO: Fix variable names
if __name__ == '__main__':
    city_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    '''print the cities and routes'''
    cities = get_randomly_spread_cities((100, 200), len(city_names))
    routes = get_routes(city_names, int(len(city_names)/2))
    print('Cities:')
    for i, city in enumerate(cities):
        print(f'{city_names[i]}: {city}')
    print('Routes:')
    for i, route in enumerate(routes):
        print(f'{i}: {route[0]} to {route[1]}')
    print(routes)
