import random
import pygame
pygame.mixer.init(44100, -16, 2, 2048)
pygame.init()

DIRECTORY = "C:\\Users\\utente\\PycharmProjects\\testgame2\\resources"

class World:
    image = pygame.image.load(DIRECTORY + '\\backg.png')
    sf_alt = 430
    sf_lar = 700
    SCHERMO = pygame.display.set_mode((sf_lar, sf_alt))


class Ground:
    grposy = 370
    grposx = 0
    image = pygame.image.load(DIRECTORY + '\\ground.png')


class Entity:
    gravity = 0.5

    def __init__(self, height, width, posy, posx, velocity):
        self.height = height
        self.width = width
        self.posy = posy
        self.posx = posx
        self.velocity = velocity


class Human(Entity):
    sex = random.randint(0, 1)
    age = random.randint(18, 40)
    if sex == 0:
        sprite = pygame.image.load(DIRECTORY + '\\male.png')
        voice = pygame.mixer.Sound(DIRECTORY + '\\grunt.wav')
    else:
        sprite = pygame.image.load(DIRECTORY + '\\female.png')
        voice = pygame.mixer.Sound(DIRECTORY + '\\fgrunt.wav')


class Button(Entity):
    sprite = pygame.image.load(DIRECTORY + '\\button.gif')
