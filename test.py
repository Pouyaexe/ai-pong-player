import neat

# Define the XOR problem inputs and outputs
xor_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
xor_outputs = [0, 1, 1, 0]

# Define the fitness function to evaluate the neural network's performance on the XOR problem
def evaluate_xor_network(genome, config):
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    error = 0.0
    for i in range(len(xor_inputs)):
        output = net.activate(xor_inputs[i])
        error += (output[0] - xor_outputs[i]) ** 2
    return 4 - error,  # The fitness function should return a tuple

# Create the NEAT configuration
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'config.txt')

# Create the population and evolve the neural networks
population = neat.Population(config)
stats = neat.StatisticsReporter()
population.add_reporter(stats)
winner = population.run(evaluate_xor_network, 300)  # Run for 300 generations

# Access the best performing neural network
best_network = neat.nn.FeedForwardNetwork.create(winner, config)

# Test the best network on the XOR problem
print("Test Results:")
for i in range(len(xor_inputs)):
    output = best_network.activate(xor_inputs[i])
    print(f"Input: {xor_inputs[i]} | Output: {output[0]} | Target: {xor_outputs[i]}")
