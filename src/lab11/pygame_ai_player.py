import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

import pygame
from lab11.turn_combat import CombatPlayer
import time
import random


""" Create PyGameAIPlayer class here"""
class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        #Closely following the structure of pygame_human_player.py
        for event in pygame.event.get():
            if state.current_city != 9:
                return ord(str(state.current_city + 1))
            else:
                return None
        return ord(str(state.current_city))
    #rcc: Failed attempt:
    # def selectAction(self, state):
    #     if not state.travelling:
    #         if state.current_city != 9:
    #             return ord(str(state.current_city + 1))
    #             #The line below would instead make the AI choose a city randomly:
    #             # return ord(str(random.choice(range(len(state.cities)))))
    #     else:
    #         #Does nothing if trvelling
    #         return ord(str(state.current_city))
    #     return ord(str(state.current_city))  # Not a safe operation for >10 cities


""" Create PyGameAICombatPlayer class here"""
class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)
    
    def weapon_selecting_strategy(self):
        #rcc: This code will wait a second, then choose a random weapon. Not the best strategy of course,
        #but a better one can be implemented later
        time.sleep(1)
        self.weapon_select=random.randint(0,2) #0 is sword, 1 is arrow, 2 is fire
        return self.weapon_select
