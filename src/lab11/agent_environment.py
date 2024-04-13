import sys
import pygame
import random
from sprite import Sprite
from pygame_combat import run_pygame_combat
from pygame_human_player import PyGameHumanPlayer
from lab5.landscape import get_landscape, elevation_to_rgba, get_elevation
from lab7.ga_cities import game_fitness, setup_GA, solution_to_cities
from pygame_ai_player import PyGameAIPlayer

from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab2.cities_n_routes import get_randomly_spread_cities, get_routes

get_combat_bg = lambda pixel_map: elevation_to_rgba(
    get_elevation(pixel_map), "RdPu"
)

pygame.font.init()
game_font = pygame.font.SysFont("Comic Sans MS", 15)

def print_skull():
    """
    This function prints a skull
    """
    skull = r"""
      _______
     /       \
    | X     X |
    |    O    |
     \_______/
      |_|_|_|
    """
    print(skull)
def print_smiley():
    """
    This function prints a smiley
    """
    smiley = r"""
      _______
     /       \
    | /\   /\ |
    |  \___/  |
     \_______/
    """
    print(smiley)

def get_landscape_surface(size):
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def get_combat_surface(size):
    landscape = get_combat_bg(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def setup_window(width, height, caption):
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return window


def displayCityNames(city_locations, city_names):
    for i, name in enumerate(city_names):
        text_surface = game_font.render(str(i) + " " + name, True, (0, 0, 150))
        screen.blit(text_surface, city_locations[i])


class State:
    def __init__(
        self,
        current_city,
        destination_city,
        travelling,
        encounter_event,
        cities,
        routes,
    ):
        self.current_city = current_city
        self.destination_city = destination_city
        self.travelling = travelling
        self.encounter_event = encounter_event
        self.cities = cities
        self.routes = routes


if __name__ == "__main__":
    size = width, height = 640, 480
    black = 1, 1, 1
    start_city = 0
    end_city = 9
    sprite_path = "assets/lego.png"
    sprite_speed = 1

    screen = setup_window(width, height, "Game World Gen Practice")

    landscape_surface = get_landscape_surface(size)
    combat_surface = get_combat_surface(size)
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

    city_locations = get_randomly_spread_cities(size, len(city_names))
    routes = get_routes(city_locations)
    #rcc: Here's where I'll implement the realistically spread cities, from lab 7
    # normalize landscape
    elevation_array = get_elevation(size)
    elevation = (elevation_array - elevation_array.min()) / (elevation_array.max() - elevation_array.min())
    # setup fitness function and GA
    fitness = lambda solution, idx: game_fitness(
        solution, idx, elevation=elevation, size=size
    )
    fitness_function, ga_instance = setup_GA(fitness, len(city_names), size)

    ga_instance.run()
    #ga_instance.plot_fitness() rcc: I think this was just showing the graph of the fitness over time, so I commented it out

    best_solution = ga_instance.best_solution()[0]
    city_locations = solution_to_cities(best_solution, size)
    routes = get_routes(city_locations)

    random.shuffle(routes)
    routes = routes[:10]

    player_sprite = Sprite(sprite_path, city_locations[start_city])

    #rcc: Implement the AI player here, if you'd like
    player = PyGameHumanPlayer()
    print(f'Current gold: {player.gold}')
    #player = PyGameAIPlayer()   
    
    state = State(
        current_city=start_city,
        destination_city=start_city,
        travelling=False,
        encounter_event=False,
        cities=city_locations,
        routes=routes,
    )
    steps = 0 #rcc: initial definition of the steps we'll use to calculate travel_cost
    while True:
        action = player.selectAction(state)
        if 0 <= int(chr(action)) <= 9:
            if int(chr(action)) != state.current_city and not state.travelling:
                ''' 
                Check if a route exist between the current city and the destination city.
                rcc: I'm not sure if we're going to implement this? The way the map builds itself,
                sometimes there just won't be a path to a certain city, so I'm really not sure.
                '''
                start = city_locations[state.current_city]
                state.destination_city = int(chr(action))
                destination = city_locations[state.destination_city]
                player_sprite.set_location(city_locations[state.current_city])
                state.travelling = True
                print(
                    "Travelling from", state.current_city, "to", state.destination_city
                )

        screen.fill(black)
        screen.blit(landscape_surface, (0, 0))

        for city in city_locations:
            pygame.draw.circle(screen, (255, 0, 0), city, 5)

        for line in routes:
            pygame.draw.line(screen, (255, 0, 0), *line)

        displayCityNames(city_locations, city_names)
        
        if state.travelling:
            steps += 1
            state.travelling = player_sprite.move_sprite(destination, sprite_speed)
            state.encounter_event = random.randint(0, 1000) < 2 #rcc: disable battles for debugging here
            if random.randint(0, 1000) < 2: #The player will randomly lose gold when travelling
                loss = random.randint(1,10)
                player.gold -= loss
                print(f'Encountered a toll-gate! Paid out {loss} gold.')
            if random.randint(0, 1000) < 2: #The player will randomly find gold on the ground.
                gain = random.randint(1,10)
                player.gold += gain
                print(f'You found {gain} gold on the ground!')
            if player.gold <= 0: #If the player runs out of gold, the game will end.
                print('------------------------')
                print('You ran out of money! You spend the rest of your days in destitution, miserable.')
                print_skull()
                print('------------------------')
                pygame.quit()
                quit()
                pass
            if not state.travelling:
                print('Arrived at', state.destination_city)
                #rcc: Here, I'm calculating the loss of gold just from traveling. As in, supplies bought with gold and stuff like that. Probably have to mess with the numbers to be balanced and whatnot.
                travel_cost = int(steps/15)
                print(f'Travel cost: {travel_cost}')
                player.gold -= travel_cost
                print(f'Current gold: {player.gold}')
                steps = 0

        if not state.travelling:
            encounter_event = False
            state.current_city = state.destination_city

        if state.encounter_event:
            run_pygame_combat(combat_surface, screen, player_sprite, player)
            state.encounter_event = False
        else:
            player_sprite.draw_sprite(screen)
        pygame.display.update()
        if state.current_city == end_city:
            print('------------------------')
            print('You have reached the end of the game!')
            print_smiley()
            print('------------------------')
            break
