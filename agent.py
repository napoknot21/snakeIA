import torch
import random
import numpy as np

from collections import deque
from game import SnakeGameAI, Direction, Point

#We define some const
MAX_MEMORY = 100_100
BATCH_SIZE = 1000
LR = 0.001

class Agent :

    def __init__ (self) :
        self.n_games = 0
        self.epsilon = 0 #randomness
        self.gama = 0 #discount rate
        self.memory = deque(max_len=MAX_MEMORY) #popleft()
        # TODO model, trainer

    
    def get_state (self, game) :
        head = game.snake[0] #snake head (a list)

        #Points next to the head in all directions
        point_l = Point(head.x - 20, head.y) # 20 beacuase we have defined bloc_size = 20
        point_r = Point(head.x + 20, head.y)
        point_u = Point(head.x, head.y - 20)
        point_d = Point(head.x, head.y + 20)

        #current directions
        dir_l = game.direction == Direction.LEFT
        dir_r = game.direction == Direction.RIGHT
        dir_u = game.direction == Direction.UP
        dir_d = game.direction == Direction.DOWN

        state = [
            #Danger straight
            (dir_r and game.is_collision(point_r)) or
            (dir_l and game.is_collision(point_l)) or 
            (dir_u and game.is_collision(point_u)) or
            (dir_d and game.is_collision(point_d)),

            #Danger right
            (dir_u and game.is_collision(point_r)) or
            (dir_d and game.is_collision(point_l)) or
            (dir_l and game.is_collision(point_u)) or
            (dir_r and game.is_collision(point_d)),  

            #Danger left
            (dir_d and game.is_collision(point_r)) or
            (dir_u and game.is_collision(point_l)) or
            (dir_r and game.is_collision(point_u)) or
            (dir_l and game.is_collision(point_d),

            #move direction
            dir_l,
            dir_r,
            dir_u,
            dir_d,

            #food location
            game.food.x < game.head.x, #food in the head snake left 
            game.food.x > game.head.x, #right
            game.food.y < game.head.y, #food up
            game.food.y > game.head.y #food down
        ]
        
        return np.array(state, dtype=int)
        
    
    def remember (self, state, action, reward, next_state, done) :
        pass


    def train_long_memory (self) :
        pass


    def train_short_memory (self, state, action, reward, next_state, done) :
        pass


    def get_action (self, state) :
        pass


def train () :
    plot_scores = []
    plot_mean_score = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    while True :
        #get old state
        state_old = agent.get_state(game)

        #get move 
        final_move = agent.get_action(state_old)

        #perform move and get new state 
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        #train the short memory
        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        #we have to remember this
        agent.rember(state_old, final_move, reward, state_new, done)

        if done :
            #train the long memory (experience) and show results
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record :
                record = score
                #TODO agent.model.save

            print('Game: ', agent.n_games, 'Score: ', score, 'Record: ', record)


if __name__ == '__main__' :
    train ()
