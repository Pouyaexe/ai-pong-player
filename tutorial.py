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
        self.left_paddle = self.game.left_paddle  # location of left paddle
        self.right_paddle = self.game.right_paddle  # location of right paddle
        self.ball = self.game.ball  # location of ball

    def test_ai(self):
        """Test the AI by playing the game."""
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)  # Max number of frames per second
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If user clicks close (x)
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
            pygame.display.update()  # Draw the screen

        pygame.quit()  # Close the window. Outside the while loop

def eval_genomes(genomes, config): #Genomes = Neural Networks in the current population
    pass

def run_neat(config):
    # p = neat.Checkpointer.restore_checkpoint("neat-checkpoint-0") # Load the last checkpoint
    p = neat.Population(
        config
    )  # Create a new population, comment this line if you want to load the last checkpoint
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))  # Save the best genome every 1 generation

    winner = p.run(eval_genomes, 50)
    
    

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)  # Get the current directory
    config_path = os.path.join(
        local_dir, "config.txt"
    )  # Get the path to the config file

    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path,
    )  # Load the config file

    run_neat(config)

# # Global variables
# width, height = 700, 500 # Screen size
# window = pygame.display.set_mode((width, height))

# game = Game(window=window, window_width=width, window_height=height)
