import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_COLOR = 'black'

FIRST_PLAYER_COORDINATE = (SCREEN_WIDTH / 2 - 25, SCREEN_HEIGHT - 25)
SECOND_PLAYER_COORDINATE = (SCREEN_WIDTH / 2 - 25, 25)

RACKET_SPEED = 2

BALL_SPEED = 4

FPS = 60
pygame.font.init()
BASIC_FONT = pygame.font.Font('Game/Materials/fonts/Roboto-Medium.ttf', 200)


