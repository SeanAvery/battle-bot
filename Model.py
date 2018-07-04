import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

class Model():
    def __init__(self, hyperparams):
        self.init_hyperparams(hyperparams)
        self.build_model()

    def init_hyperparams(self,params):
        self.epsilon = params['epsilon']
        self.epsilon_decay = params['epsilon_decay']
        self.alpha = params['alpha']
        self.alpha_decay = params['alpha_decay']

    def build_model(self):
        model = Sequential()
        model.add(Dense(128, activation='relu', input_dim=128))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(18, activation='linear'))
        model.compile(optimizer=Adam(
            lr=self.alpha, decay=self.alpha_decay),
            loss='mse')
        self.model = model
