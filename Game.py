import sys, pygame, time
from AIRacer import AIRacer
from States import States
from Player import Player
from PowerUp import PowerUp, powerup_points


# Game State
class Game(States):
    def __init__(self):
        # Set up Game State
        States.__init__(self)
        self.next = 'highscore'
        # Set Up Background
        self.background = pygame.image.load("res/track1.png")
        # Set Up Player
        self.player = Player(420, 500, 50, 50, 2)
        # Set Up AI
        self.racer = AIRacer(420, 480)
        # Set Up PowerUps
        self.powerup = PowerUp()
        # Set Up Timer
        self.start = time.time()
        self.end = self.start
        # Highscore
        self.curr_highscore = 0

    # Cleanup Method
    def cleanup(self):
        print('cleaning up Game state stuff')

    # Startup Method
    def startup(self):
        print('starting Game state stuff')

    # Event Method
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player.up = True
            if event.key == pygame.K_DOWN:
                self.player.down = True
            if event.key == pygame.K_LEFT:
                self.player.left = True
            if event.key == pygame.K_RIGHT:
                self.player.right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.player.up = False
            if event.key == pygame.K_DOWN:
                self.player.down = False
            if event.key == pygame.K_LEFT:
                self.player.left = False
            if event.key == pygame.K_RIGHT:
                self.player.right = False

    # Update Method
    def update(self, screen, dt):
        self.draw(screen)
        self.player.update()
        self.racer.update()
        self.powerup.update(self.player)

        if self.powerup.done:
            # End Timer
            self.end = time.time()
            hours, rem = divmod(self.end-self.start, 3600)
            minutes, seconds = divmod(rem, 60)
            self.curr_highscore = "{:0>2}:{:0>2}:{:05.2f}\n".format(int(hours), int(minutes), seconds)

            with open('highscore_list.txt', 'a') as file:
                file.write(self.curr_highscore)

            # Reset
            # Set Up Player
            self.player = Player(420, 500, 50, 50, 2)
            # Set Up AI
            self.racer = AIRacer(420, 480)
            # Set Up PowerUps
            self.powerup = PowerUp()

            self.done = True

    # Draw Method
    def draw(self, screen):
        # screen.fill((0, 0, 255))
        screen.blit(self.background, (0, 0))

        self.powerup.render(screen)
        self.racer.render(screen)
        self.player.render(screen)

