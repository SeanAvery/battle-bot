from Game import Game
from Memory import Memory
from Model import Model

hyperparams1 = {
    'alpha': 1,
    'alpha_decay': 0.995,
    'epsilon': 1,
    'epsilon_decay': 0.995,
    'batch_size': 100
}

if __name__ == '__main__':
    memory = Memory(500)
    model = Model(hyperparams1, memory)
    game = Game(model)
    game.train(1000)
