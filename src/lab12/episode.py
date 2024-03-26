'''
Lab 12: Beginnings of Reinforcement Learning

Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''
import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab11.turn_combat import CombatPlayer, Combat, ComputerCombatPlayer
from lab11.pygame_combat import run_pygame_combat, run_turn

def run_episode(player1, player2):
    obsState = (player1.health, player2.health)
    action = player1.weapon
    reward = 0
    resultList = [(obsState, action, reward)]
    currentGame = Combat()
    while(player1.health != 0 and player2.health != 0):
            reward = run_turn(currentGame, player1, player2)
            obsState = (player1.health, player2.health)
            resultList.append((obsState, action, reward))
    print(resultList)
    return resultList
    pass

run_episode(ComputerCombatPlayer(CombatPlayer), ComputerCombatPlayer(CombatPlayer))
