"""Example of how to make an AI that plays pong game.
"""
import pickle
import os
import neat
import pygame
from pong import Game

# Global variables
width, height = 700, 500 # Screen size
window = pygame.display.set_mode((width, height))

game = Game(window=window, window_width=width, window_height=height)

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60) # Max number of frames per second 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicks close (x)
            run = False
            break
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        game.move_paddle(left=True, up=True)
        
    if keys[pygame.K_s]:
        game.move_paddle(left=True, up=False)
        
    game.loop()
    game.draw(False, True)
    pygame.display.update() # Draw the screen

