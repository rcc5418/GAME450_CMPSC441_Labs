import sys
import pygame
from pathlib import Path
import random

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab11.sprite import Sprite
from lab11.turn_combat import CombatPlayer, Combat
from lab11.pygame_ai_player import PyGameAICombatPlayer
from lab11.pygame_human_player import PyGameHumanPlayer, PyGameHumanCombatPlayer
from lab11.pygame_ai_player import PyGameAIPlayer, PyGameAICombatPlayer

AI_SPRITE_PATH = Path("assets/ai.png")

pygame.font.init()
game_font = pygame.font.SysFont("Comic Sans MS", 15)


class PyGameComputerCombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        if 30 < self.health <= 50:
            self.weapon = 2
        elif self.health <= 30:
            self.weapon = 1
        else:
            self.weapon = 0
        return self.weapon


def draw_combat_on_window(combat_surface, screen, player_sprite, opponent_sprite):
    screen.blit(combat_surface, (0, 0))
    player_sprite.draw_sprite(screen)
    opponent_sprite.draw_sprite(screen)
    text_surface = game_font.render("Choose s-Sword a-Arrow f-Fire!", True, (0, 0, 150))
    screen.blit(text_surface, (50, 50))
    pygame.display.update()


def run_turn(currentGame, player, opponent):
    players = [player, opponent]
    states = list([tuple(player.health for player in players)]*2)
    for current_player, state in zip(players, states):
        current_player.selectAction(state)

    currentGame.newRound()
    currentGame.takeTurn(player, opponent)
    print("%s's health = %d" % (player.name, player.health))
    print("%s's health = %d" % (opponent.name, opponent.health))
    reward = currentGame.checkWin(player, opponent)
    return reward


def run_pygame_combat(combat_surface, screen, player_sprite, overworldPlayer, identity): #rcc: I've added the overworld player as a parameter so that they can get a gold reward for winning a battle, as well as an identity parameter to track if a human is playing or not
    currentGame = Combat()
    if (identity == "Human"):
        player = PyGameHumanCombatPlayer("Legolas")
    elif (identity == "AI"):
        player = PyGameAICombatPlayer("MrRoboto")
    else:
        player = PyGameHumanCombatPlayer("ThisShouldNeverRunButJustInCase")
    
    #player = PyGameHumanCombatPlayer("Legolas")
    #rcc: Change code to implement the AI combat player here (comment out line above):
    #player = PyGameAICombatPlayer("MrRoboto")
    """ Add a line below that will reset the player object
    to an instance of the PyGameAICombatPlayer class"""

    opponent = PyGameComputerCombatPlayer("Computer")
    opponent_sprite = Sprite(
        AI_SPRITE_PATH, (player_sprite.sprite_pos[0] - 100, player_sprite.sprite_pos[1])
    )

    #rcc: Added line to make debugging easy (lets the AI combat player win any battle easily)
    #opponent.health = 20

    # Main Game Loop
    while not currentGame.gameOver:
        draw_combat_on_window(combat_surface, screen, player_sprite, opponent_sprite)

        run_turn(currentGame, player, opponent)
    battle_reward = random.randint(5,25)
    print(f'Reward: {battle_reward} gold')
    overworldPlayer.gold += battle_reward
    print(f'Current gold: {overworldPlayer.gold}')
