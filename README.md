# ai-pong-player

# Pong Game AI using NEAT

This repository contains a Python implementation of the classic game Pong with an AI that learns to play the game using NEAT (NeuroEvolution of Augmenting Topologies). NEAT is a genetic algorithm-based method for evolving artificial neural networks to solve various tasks, including playing games.

## Getting Started

To get started, follow the steps below:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.

## How It Works

The `pong.py` file contains the game logic for Pong, including the ball, paddles, and game loop. The `neat` library is used to implement the NEAT algorithm for evolving neural networks.

- `PongGame` class: This class represents the Pong game environment and contains methods for testing the AI against a human player (`test_ai`) and training the AI (`train_ai`) by playing two neural networks against each other.
- `eval_genomes` function: This function runs each genome against each other one time to determine their fitness.
- `run_neat` function: This function sets up the NEAT population, runs the evolution process using `eval_genomes`, and saves the best-performing neural network to a pickle file.
- `test_best_network` function: This function loads the best-performing neural network from the pickle file and tests it against a human player.

## Configuration

The `config.txt` file contains the NEAT configuration parameters, including population size, mutation rates, and species settings. You can adjust these parameters to experiment with different evolutionary settings.

## Contributing

If you would like to contribute to this project or report any issues, feel free to open a pull request or create an issue on the GitHub repository.

## Credits

This project uses the NEAT library (https://neat-python.readthedocs.io/) for implementing the NEAT algorithm.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
