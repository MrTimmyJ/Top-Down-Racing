import sys, pygame
from States import States


class HighScore(States):
    def __init__(self):
        # Set up Highscore State
        States.__init__(self)
        # Set Up Menus
        self.next = 'levelselect'
        self.textSurfaces = []
        self.title = ''
        self.continue_text = ''

    # Cleanup Method
    def cleanup(self):
        print('cleaning up HighScore state stuff')

    # Startup Method
    def startup(self):
        print('starting HighScore state stuff')
        with open('highscore_list.txt', 'r') as file:
            lines = file.readlines()
            print(lines[0])

        myFont = pygame.font.SysFont('calibri', 30)
        self.title = (myFont.render(' HIGHSCORES: ', False, (255, 255, 255)))
        self.continue_text = (myFont.render('Left Click To Continue', False, (255, 255, 255)))

        for i in range(len(lines)):
            self.textSurfaces.append(myFont.render(lines[i][:len(lines[i])-1], False, (255, 255, 255)))

    # Event Method
    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            print('HighScore State keydown')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.done = True

    # Update Method
    def update(self, screen, dt):
        self.draw(screen)

    # Draw Method
    def draw(self, screen):
        screen.fill((0, 20, 150))

        screen.blit(self.title, (300, 0))
        screen.blit(self.continue_text, (250, 550))

        offset = 25;

        for i in range(len(self.textSurfaces)):
            screen.blit(self.textSurfaces[i], (320, (offset * i) + 25))
