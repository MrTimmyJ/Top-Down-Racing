import sys, pygame, math

# Finite State Machine
SPRITE_LEFT = 0
SPRITE_RIGHT = 1
SPRITE_UP = 2
SPRITE_DOWN = 3


# AIRacer Class
class AIRacer:
    def __init__(self, x, y, speed=2):
        # Set Direction Facing
        self.direction = None
        self.x = x
        self.y = y
        # list of x, y
        self.points = []
        self.speed = speed
        # Sprites
        self.truck_left = pygame.image.load("res/Truck_Left.png").convert_alpha()
        self.truck_right = pygame.image.load("res/Truck_Right.png").convert_alpha()
        self.truck_up = pygame.image.load("res/Truck_Up.png").convert_alpha()
        self.truck_down = pygame.image.load("res/Truck_Down.png").convert_alpha()
        # Sprite List
        self.sprites = [self.truck_left, self.truck_right, self.truck_up, self.truck_down]
        self.curr_sprite = SPRITE_LEFT

        # Open File
        self.fileName = "AI.txt"
        # temp variables
        i = 0
        x = 0
        y = 0
        with open(self.fileName) as f:
            # Read First 2 Values | Read x , Read y
            content = f.read().splitlines()
            # content = the list of x,y,x,y,x,y

        # last index - 1
        while i < len(content) - 1:
            x = content[i]
            y = content[i + 1]
            # Make into ints (x, y) then append tuple to list
            self.points.append((int(x), int(y)))
            i += 2

        self.point_index = 0
        self.next_point = self.points[0]

        # AI Racer Rectangle
        self.rect = self.truck_left.get_rect()

    # Update Method
    def update(self):

        # Get Angle Ai Racer is facing/ moving toward next
        self.theta = math.atan2(self.next_point[1] - self.y, self.next_point[0] - self.x)
        # Calculate speed
        self.vx = math.cos(self.theta) * self.speed
        self.vy = math.sin(self.theta) * self.speed

        self.x += self.vx
        self.y += self.vy

        # Error Radius for AI, closer to 0: will follow each (x,y) exactly
        self.errorRadius = 5

        # Get distance of the 2 points
        if math.pow(self.next_point[0] - self.x, 2) + math.pow(self.next_point[1] - self.y, 2) < math.pow(
                self.errorRadius, 2):
            self.point_index = (self.point_index + 1) % len(self.points)
            self.next_point = self.points[self.point_index]

        # Move AI Racer Sprite the correct way
        if abs(self.vx) < abs(self.vy):
            if self.vy > 0:
                self.curr_sprite = SPRITE_DOWN
            elif self.vy < 0:
                self.curr_sprite = SPRITE_UP
        elif abs(self.vx) > abs(self.vy):
            if self.vx > 0:
                self.curr_sprite = SPRITE_RIGHT
            elif self.vx < 0:
                self.curr_sprite = SPRITE_LEFT

        self.rect = self.sprites[self.curr_sprite].get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

    # Render Method
    def render(self, screen):
        screen.blit(self.sprites[self.curr_sprite], self.rect)
