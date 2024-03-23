import random
import numpy as np 
import matplotlib.pyplot as plt
import copy
from enum import Enum

class Action(Enum):
    hit = 0
    stick = 0
    
    @staticmethod
    def to_action(n):
        return Action.hit  if n==0 else Action.stick 
    
    @staticmethod
    def as_int(a):
        return 0 if a==Action.hit else 1

class Card :
    def __init__(self, force_black= False) :
        self.value = random.randint(1,10)
        if force_black or random.randint(1,3)!= 3 :
            self.is_black = True
        else: 
            self.is_black = False
            self.value = - self.value
            
class State(object):
    def __init__(self, dealer=0, agent=0, is_terminal=False):
        self.dealer = dealer
        self.agent = agent
        self.is_terminal = is_terminal
        
class Environment : 
    def __init__(self) -> None:
        self.dealer_value_count = 10 ,
        self.player_value_count = 21 ,
        self.action_count = 2 # hit or stick 

    def step(self, state, action):
#        new_state = state does not work because modifying new_state will influence state
        new_state = copy.copy(state)
        reward = 0
        if action == Action.hit:
            new_state.player  += Card().value
            if new_state.player > 21 or new_state.player <1:
                new_state.is_terminal = True
                reward = -1
                return new_state, reward
        elif action == Action.stick:
            while not new_state.is_terminal:
                new_state.dealer += Card().value
                if new_state.dealer > 21 or  new_state.dealer < 1:
                    new_state.is_terminal = True
                    reward = 1
                elif new_state.dealer> 17:
                    new_state.is_terminal = True
                    if new_state.player > new_state.dealer:
                        reward = 1
                    elif new_state.player < new_state.dealer:
                        reward = -1
        return new_state, reward
              