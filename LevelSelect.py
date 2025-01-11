import sys, pygame
from States import States
from LevelManager import LevelManager


# Level Select Manager
class LevelSelect(States, LevelManager):
    def __init__(self):
        # Setup States and Level Manager
        States.__init__(self)
        LevelManager.__init__(self)
        # Setup Menus
        self.next = 'game'
        self.options = ['Level 1', 'Level 2', 'Quit']
        self.next_list = ['game', 'gameTwo', 'menu']
        self.pre_render_options()
        self.from_bottom = 200
        self.spacer = 75

    # Cleanup Method
    def cleanup(self):
        print('cleaning up LevelSelect state stuff')

    # Startup Method
    def startup(self):
        print('starting LevelSelect state stuff')

    # Event Method
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        self.get_event_menu(event)

    # Update Method
    def update(self, screen, dt):
        self.update_menu()
        self.draw(screen)

    # Draw Method
    def draw(self, screen):
        screen.fill((255, 0, 0))
        self.draw_menu(screen)
