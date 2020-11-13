import pygame
import random
import sys
from pygame.locals import *

#variables
screen_width = 700
screen_height = 700
screen_setup = screen_width, screen_height
white = (255, 255, 255)
green = (0, 128, 0)
orange = (255, 165, 0)
black = (0, 0, 0)
screen = pygame.display.set_mode((screen_setup))
user_x = 310
user_y = 620
user_w = 80
user_h = 80
player = pygame.draw.rect(screen, green, pygame.Rect(user_x, user_y, user_w, user_h))
speed = 8
fps = 40
enemyMinSize = 10
enemyMaxSize = 30
enemyMinSpeed = 1
enemyMaxSpeed = 8
newEnemyRate = 6

pygame.init()
mainClock = pygame.time.Clock()
pygame.display.set_caption("Dodger")

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                user_x -= speed
            if event.key == pygame.K_RIGHT:
                user_x += speed
    screen.fill((white))
    player
    pygame.display.flip()

  
