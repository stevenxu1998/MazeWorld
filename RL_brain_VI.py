import numpy as np
import pandas as pd
from maze_env import Maze as m1

class rlalgorithm:

    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9):
        self.actions = actions  
        self.lr = learning_rate
        self.gamma = reward_decay
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
        self.display_name="Value Iteration"


    def choose_action(self, observation):
        self.check_state_exist(observation)
           
        state_action = self.q_table.loc[observation, :]

        action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        return action

    def learn(self, s, a, r, s_, d):
        self.check_state_exist(s_)
        if s_ != 'terminal':
            q_old = self.q_table.loc[s,a]
            q_target = r + self.gamma * self.q_table.loc[s_,].max()
            delta = max (d, abs(q_old - q_target))
        else:
            q_target = r  # next state is terminal
        self.q_table.loc[s, a] = q_target  # update
        return s_, delta

    '''States are dynamically added to the Q(S,A) table as they are encountered'''
    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # append new state to q table
            self.q_table = self.q_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )