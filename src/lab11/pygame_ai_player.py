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
        self.gold = 100
        pass

    def selectAction(self, state):
        #Closely following the structure of pygame_human_player.py
        for event in pygame.event.get():
            return ord(str(random.randint(0,9))) #Return random town
        #    if state.current_city != 9:
        #        return ord(str(state.current_city + 1))
        #    else:
        #        return None
        return ord(str(random.randint(0,9)))
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
        #rcc: This policy dictionary is from lab13, but I couldn't import anything because it caused a circular import cycle
        self.policy = {(100, 100): 1, (100, 90): 1, (100, 80): 1, (90, 80): 1, (80, 80): 1, (70, 80): 1, (70, 70): 1, (60, 70): 1, (60, 60): 1, (50, 60): 1, (50, 50): 0, (40, 40): 0, (30, 30): 2, (20, 30): 2, (10, 20): 2, (10, 10): 2, (90, 100): 1, (90, 90): 1, (80, 70): 1, (80, 60): 1, (70, 60): 1, (40, 60): 1, (40, 50): 0, (30, 50): 0, (20, 50): 0, (10, 50): 0, (10, 40): 0, (10, 30): 2, (90, 70): 1, (90, 60): 1, (90, 50): 2, (80, 50): 0, (70, 40): 0, (60, 40): 0, (50, 40): 2, (30, 20): 2, (20, 10): 1, (60, 50): 0, (60, 30): 2, (50, 30): 2, (40, 20): 1, (40, 10): 2, (80, 100): 1, (80, 90): 1, (30, 40): 0, (40, 30): 2, (60, 80): 1, (30, 10): 1, (70, 50): 0, (30, 60): 1, (20, 60): 1, (10, 60): 2, (70, 90): 1, (60, 90): 1, (50, 90): 1, (40, 90): 1, (40, 80): 1, (30, 80): 1, (30, 70): 1, (20, 70): 0, (10, 70): 2, (100, 70): 1, (80, 40): 0, (60, 20): 2, (60, 10): 2, (70, 100): 1, (50, 80): 
1, (50, 70): 1, (20, 20): 2, (40, 70): 1, (20, 40): 0, (60, 100): 1, (50, 100): 2, (40, 100): 1, (30, 100): 1, (30, 90): 0, (100, 60): 1, (100, 50): 0, (90, 40): 0, (90, 30): 1, (80, 20): 0, (70, 20): 0, (20, 90): 0, (20, 80): 0, (10, 80): 0, (70, 30): 2, (50, 20): 2, (50, 10): 2, (70, 10): 1, (80, 30): 0, (90, 20): 0, (90, 10): 2, (100, 40): 2, (100, 30): 0, (20, 100): 1, (10, 90): 0, (10, 100): 1, (80, 10): 2, (100, 20): 2, (100, 10): 1} 
    
    def weapon_selecting_strategy(self):
        #rcc: This code will wait a second, then choose a random weapon. Not the best strategy of course,
        #but a better one can be implemented later
        time.sleep(.3)
        #self.weapon_select=random.randint(0,2) #0 is sword, 1 is arrow, 2 is fire
        #return self.weapon_select
        self.weapon = self.policy[self.current_env_state]
        return self.weapon

