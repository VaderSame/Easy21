import numpy as np
import random

class Easy21(object):
    def __init__(self):
        self.state = None

    def reset(self):
        player_card = np.random.randint(1, 11)
        dealer_card = np.random.randint(1, 11)
        self.state = (dealer_card, player_card)
        return np.array(self.state)

    def get_card(self):
        card = np.random.randint(1, 11)
        if random.random() < 2.0/3:
            return card
        else:
            return -card

    def step(self, action):
        dealer_card_up, player_sum = self.state
        if action == 0: #hit 
            player_sum += self.get_card()
            self.state = (dealer_card_up, player_sum)
            if player_sum > 21 or player_sum < 1:
                return self.state, -1.0, True
            return self.state, 0, False
        if action == 1: #stick
            dealer_sum = dealer_card_up
            while True:
                dealer_sum += self.get_card()
                if dealer_sum > 21 or dealer_sum < 1:
                    return self.state, 1.0, True
                if dealer_sum >= 17:
                    if dealer_sum > player_sum:
                        return self.state, -1.0, True
                    elif dealer_sum < player_sum:
                        return self.state, 1.0, True
                    else:
                        return self.state, 0, True
        return self.state, dealer_sum , player_sum       