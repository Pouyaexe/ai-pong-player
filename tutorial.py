"""Example of how to make an AI that plays pong game.
"""
import pickle
import os
import neat
import pygame
from pong import Game


class PongGmae:
    def __init__(self, window, width, height):
        self.game = Game(window=window, window_width=width, window_height=height)
        self.left_paddle = self.game.left_paddle # location of left paddle
        self.right_paddle = self.game.right_paddle # location of right paddle
        self.ball = self.game.ball # location of ball
    
    def test_ai(self):
        """Test the AI by playing the game.
        """
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
                
            game_info = game.loop()
            print(game_info.left_score, game_info.right_score)
            game.draw(False, True)
            pygame.display.update() # Draw the screen

        pygame.quit() # Close the window. Outside the while loop





# Global variables
width, height = 700, 500 # Screen size
window = pygame.display.set_mode((width, height))

game = Game(window=window, window_width=width, window_height=height)


