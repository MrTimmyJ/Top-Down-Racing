import sys, pygame
from States import States
from MenuManager import MenuManager


# Options Class
class Options(States, MenuManager):
    def __init__(self):
        # Setup States and Menu Manager
        States.__init__(self)
        MenuManager.__init__(self)
        # Menu Options
        self.next = 'menu'
        self.options = ['Music', 'Sound', 'Graphics', 'Controls', 'Main Menu']
        self.next_list = ['options', 'options', 'options', 'options', 'menu']
        self.pre_render_options()
        self.from_bottom = 200
        self.spacer = 75

    # Cleanup Method
    def cleanup(self):
        print('cleaning up Options state stuff')

    # Startup Method
    def startup(self):
        print('starting Options state stuff')

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
