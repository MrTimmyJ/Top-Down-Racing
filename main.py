"""
Title: 2D Top Down Racing
Author: Timothy Johnson
Date: January 1, 2021
Finish Date: March 12, 2021
Game: Top Down Racing
"""


import sys, pygame
from Control import Control
from MenuManager import MenuManager
from States import States
from Menu import Menu
from Options import Options
from LevelManager import LevelManager
from LevelSelect import LevelSelect
from Game import Game
from GameTwo import GameTwo
from HighScore import HighScore

# Start Pygame
pygame.init()
pygame.display.set_caption("2D Top Down Racing");
programIcon = pygame.image.load('res/logo.png')
pygame.display.set_icon(programIcon)
pygame.font.init()

# Start State Machine & Menu Managers
curr_state = States()
menu_manager = MenuManager()
level_manager = LevelManager()

# Create Control
app = Control()
# Create Dictionary
state_dict = {
    'menu': Menu(),
    'levelselect': LevelSelect(),
    'game': Game(),
    'gameTwo': GameTwo(),
    'highscore': HighScore(),
    'options': Options()
}
# Set State and Main Game Loop
app.setup_states(state_dict, 'menu')
app.main_game_loop()
pygame.quit()
sys.exit()
