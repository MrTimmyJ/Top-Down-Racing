import sys, pygame
from States import States
from MenuManager import MenuManager


# Menu State
class Menu(States, MenuManager):
    def __init__(self):
        # State and Menu Manager
        States.__init__(self)
        MenuManager.__init__(self)
        # Set Menu Options
        self.next = 'levelselect'
        self.options = ['Play', 'Options', 'Quit']
        self.next_list = ['levelselect', 'options', 'quit']
        self.pre_render_options()
        self.from_bottom = 200
        self.spacer = 75

    # Cleanup Method
    def cleanup(self):
        print('cleaning up Main Menu state stuff')

    # Startup Method
    def startup(self):
        print('starting Main Menu state stuff')

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
