import gym
import numpy as np
import scipy.misc

class Game():
    def __init__(self):
        self.env = gym.make('BattleZone-ram-v0')

    def choose_action(self):
        return self.env.action_space.sample()


    ''' VIDEO PROCESSING '''
    def process_frame(self, frame):
        return True
        # print('frame', frame)
        # rgb = scipy.misc.toimage(frame)
        # scipy.misc.pilutil.mshow(rgb)
        # grey = np.mean(frame, axis=2).astype(np.uint8)
        # print('grey', grey)

    ''' TRAINING '''
    def train(self, rounds):
        for i in range(rounds):
            self.run_round()

    def run_round(self):
        old_state = self.env.reset()
        print('old_state', old_state.shape)

        while True:
            action = self.choose_action()
            new_state, reward, done, _ = self.env.step(action)
            # self.env.render()
            self.process_frame(new_state)
            if done:
                break
