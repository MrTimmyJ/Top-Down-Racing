import sys, pygame


# Control Class
class Control:
    def __init__(self):
        # Setup basic pygame controls
        self.done = False
        self.fps = 60
        self.screen = pygame.display.set_mode((800, 600))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()

    # Setup States with State Dictionary
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    # Flip State Method
    def flip_state(self):
        # Go to next state from previous state
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous

    # Update Method
    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, dt)

    # Event Method
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.state.get_event(event)

    # Main Game Loop Method
    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick(self.fps) / 1000.0
            self.event_loop()
            self.update(delta_time)
            pygame.display.update()
