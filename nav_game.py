import pygame
import os
from pygame.constants import K_1


# initialize pygame
pygame.init()

# display vars
WIDTH, HEIGHT = 950, 650
# game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# window title
pygame.display.set_caption("Journey to Python")
# frames per second
FPS = 60

# fonts and text boxes
LETTER_FONT = pygame.font.SysFont('comicsans', 35)
INPUT_BOX = pygame.Rect(75, HEIGHT-65, 140, 32)
INFO_BOX = pygame.Rect(30, HEIGHT - 110, 425, 32)
DISTANCE_BOX = pygame.Rect(420, HEIGHT - 110, 425, 32)
MESSAGE_BOX = pygame.Rect(220, HEIGHT-65, 140, 32)
ERROR_BOX = pygame.Rect(220, HEIGHT-65, 140, 32)
# messages
MESSAGE_1 = "Press 1 or 2 to move the rocket."
MESSAGE_2 = "<-- Click here to Begin."
ERROR_1 = "Please press 1 or 2"
# game colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# boarders and message displays
BOARDER = pygame.Rect(WIDTH//4-2.5, 0, 5, HEIGHT)
INFO_BOARDER = pygame.Rect(0, HEIGHT - 125, WIDTH, HEIGHT)

# load images
HOME_PLANET = pygame.image.load(os.path.join("planet1.svg"))
PLANET_PYTHON = pygame.image.load(os.path.join("planet2.png"))
ROCKET_1_IMAGE = pygame.image.load(os.path.join("rocket1.svg"))
ROCKET_2_IMAGE = pygame.image.load(os.path.join("starting-rocket.svg"))
SPACE_BG_IMAGE = pygame.image.load(os.path.join("milky-way.jpg"))
# rotate and resize images
# resize values
ROCKET_WIDTH = 50
ROCKET_HEIGHT = 75
ROCKET_1 = pygame.transform.rotate(pygame.transform.scale(
    ROCKET_1_IMAGE, (ROCKET_WIDTH, ROCKET_HEIGHT)), 20)
ROCKET_2 = pygame.transform.rotate(pygame.transform.scale(
    ROCKET_2_IMAGE, (ROCKET_WIDTH-10, ROCKET_HEIGHT+10)), -25)
SPACE_BG = pygame.transform.scale(SPACE_BG_IMAGE, (WIDTH, HEIGHT))

# gameplay  vars
# speed of rocket
ROCKET_VEL = 3
COLOR_ACTIVE = (0, 0, 255)
COLOR_INACTIVE = (255, 255, 255)


class Rocket:
    def __init__(self, image, x, y):
        # move
        self.image = image
        self.x = x
        self.y = y
        self.clicks = 20
        self.vel1x = 28
        self.vel1y = 13

    def move_rocket(self, user_input, WIN):

        if int(user_input) == 1:
            self.x += self.vel1x
            self.y -= self.vel1y
            self.clicks -= 1
        elif int(user_input) == 2:
            self.x += self.vel1x * 2
            self.y -= self.vel1y * 2
            self.clicks -= 2

    def draw_rocket(self, WIN):
        # draw rocket to screen
        WIN.blit(ROCKET_1, (self.x, self.y))
        #WIN.blit(ROCKET_2, (red.x, red.y))


def draw_images(rocket):
    # game window background
    WIN.blit(SPACE_BG, (0, 0))
    # game images
    WIN.blit(HOME_PLANET, (50, 400))
    WIN.blit(PLANET_PYTHON, (600, 50))
    rocket.draw_rocket(WIN)


def draw_text(active, user_input, col, rocket):
    # make info rect
    pygame.draw.rect(WIN, GRAY, INFO_BOARDER)
    # text box

    pygame.draw.rect(WIN, col, INPUT_BOX, 2)

    text_surface = LETTER_FONT.render(user_input, True, WHITE)
    info_text = LETTER_FONT.render(MESSAGE_1, True, WHITE)
    distance_text = LETTER_FONT.render(
        'You have ' + str(rocket.clicks) + ' more jumps to Planet Python!', True, WHITE)
    message_text = LETTER_FONT.render(MESSAGE_2, True, WHITE)
    WIN.blit(text_surface, (INPUT_BOX.x+5, INPUT_BOX.y+5))
    WIN.blit(info_text, (INFO_BOX.x+5, INFO_BOX.y+5))
    WIN.blit(distance_text, (DISTANCE_BOX.x+5, DISTANCE_BOX.y+5))
    if active == False:
        WIN.blit(message_text, (MESSAGE_BOX.x+5, MESSAGE_BOX.y+5))
    if user_input != '' and user_input != str(1) and user_input != str(2):
        error_text = LETTER_FONT.render(ERROR_1, True, WHITE)
        WIN.blit(error_text, (ERROR_BOX.x+5, ERROR_BOX.y+5))


def create_game():
    # resize game window
    # boarder between game and code window
    # rect for code window
    # boilerplate code
    # rect for milestones
    # milestone text
    # milestone buttons
    # rocket movement
    pass


def main():

    # create rects to track and control game images
    rocket = Rocket(ROCKET_1, 50, 400)
    # create clock to control frame rate
    clock = pygame.time.Clock()

    # game vars
    user_input = ''
    col = COLOR_INACTIVE
    active = False
    run = True
    # main game loop
    while run:
        # identify events within game
        for event in pygame.event.get():
            # check if user ends the game
            if event.type == pygame.QUIT:
                run = False
            # check if mouse clicked input box
            if event.type == pygame.MOUSEBUTTONDOWN:
                # activate input box
                if INPUT_BOX.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            # check if key was pressed
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_RETURN:
                        if user_input.isdigit():
                            rocket.move_rocket(user_input, WIN)
                        user_input = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode

        # change color of input box
        if active:
            col = COLOR_ACTIVE
        else:
            col = COLOR_INACTIVE

        pygame.draw.rect(WIN, col, INPUT_BOX)

        # renter user input

        # draw images on window
        draw_images(rocket)
        draw_text(active, user_input, col, rocket)
        pygame.display.flip()
        # control the fps
        clock.tick(FPS)
    # close the game window
    pygame.quit()


if __name__ == '__main__':
    main()
