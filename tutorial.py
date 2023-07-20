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

game = Game(window=window, width=width, height=height)
