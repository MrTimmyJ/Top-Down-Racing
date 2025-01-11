import sys, pygame

# Finite State Machine
SPRITE_LEFT = 0
SPRITE_RIGHT = 1
SPRITE_UP = 2
SPRITE_DOWN = 3


# Player Class
class Player:
    def __init__(self, x, y, width, height, speed):
        # Set Direction Facing
        self.direction = None
        # x, y, width, height of Player
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Speed of player
        self.speed = speed
        # Sprites
        self.car_left = pygame.image.load("res/Car_Left.png").convert_alpha()
        self.car_right = pygame.image.load("res/Car_Right.png").convert_alpha()
        self.car_up = pygame.image.load("res/Car_Up.png").convert_alpha()
        self.car_down = pygame.image.load("res/Car_Down.png").convert_alpha()
        # Sprite List
        self.sprites = [self.car_left, self.car_right, self.car_up, self.car_down]
        self.curr_sprite = SPRITE_LEFT

        self.rect = self.car_left.get_rect()
        # Direction you can face
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    # Update Method
    def update(self):
        if self.left:
            self.x -= self.speed
            self.curr_sprite = SPRITE_LEFT
        if self.right:
            self.x += self.speed
            self.curr_sprite = SPRITE_RIGHT
        if self.up:
            self.y -= self.speed
            self.curr_sprite = SPRITE_UP
        if self.down:
            self.y += self.speed
            self.curr_sprite = SPRITE_DOWN

        self.rect = self.sprites[self.curr_sprite].get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

    # Render Method
    def render(self, screen):
        screen.blit(self.sprites[self.curr_sprite], self.rect)

    # Key Down Method
    def key_down(self, key):
        if key == pygame.K_w:
            self.up = True
        if key == pygame.K_s:
            self.down = True
        if key == pygame.K_a:
            self.left = True
        if key == pygame.K_d:
            self.right = True

    # Key Up Method
    def key_up(self, key):
        if key == pygame.K_w:
            self.up = False
        if key == pygame.K_s:
            self.down = False
        if key == pygame.K_a:
            self.left = False
        if key == pygame.K_d:
            self.right = False
