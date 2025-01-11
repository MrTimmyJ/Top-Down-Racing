import pygame, time

# Power Up Points List
powerup_points = [(725, 415), (575, 125), (150, 125), (450, 500)]  # Power Up Locations


# Power Up Class
class PowerUp:
    def __init__(self, width=50, height=50):
        # First Points = powerup_points[0]
        self.x = powerup_points[0][0]
        self.y = powerup_points[0][1]
        # Width and height of powerups
        self.width = width
        self.height = height
        # done means if race is over or 4 powerups are taken
        self.done = False
        # +1 if powerup taken
        self.powerups_activated = 0
        # Power Up Sprite
        self.power_up = pygame.image.load("res/PowerUp.png").convert_alpha()
        # Set Up Timer
        self.oldTime = time.time()

        self.point_index = 0

    # Update Method
    def update(self, player):
        # If the player collides with the Power Up
        if player.rect.x < self.x + self.width and player.rect.x + player.rect.width > self.x and player.rect.y < self.y + self.height and player.rect.y + player.height > self.y:
            # collision detected!
            self.point_index = (self.point_index + 1) % len(powerup_points)
            # Set x and y to new points
            self.x = powerup_points[self.point_index][0]
            self.y = powerup_points[self.point_index][1]
            self.powerups_activated += 1

            # If 4 powerups are taken, game over
            if self.powerups_activated == 4:
                self.done = True
        elif time.time() - self.oldTime > 19:
            self.done = True

    # Render Method
    def render(self, screen):
        screen.blit(self.power_up, (self.x, self.y))
