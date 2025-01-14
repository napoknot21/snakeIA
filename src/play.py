import torch
import numpy as np
from src.game import SnakeGameAI, Direction, Point
from src.model import Linear_QNet

class Agent:
    def __init__(self, model_path='model_trained.pth'):
        """
        Initialize the Agent class with the pre-trained model.
        :param model_path: Path to the pre-trained model file.
        """
        self.model = Linear_QNet(11, 256, 3)  # Input size = 11, Hidden size = 256, Output size = 3
        self.model.load(model_path)  # Load the pre-trained model
        self.model.eval()  # Set the model to evaluation mode

    def get_state(self, game):
        """
        Get the current state of the game as a feature vector.
        :param game: Instance of SnakeGameAI.
        :return: Numpy array representing the game state.
        """
        head = game.snake[0]
        point_l = Point(head.x - 20, head.y)
        point_r = Point(head.x + 20, head.y)
        point_u = Point(head.x, head.y - 20)
        point_d = Point(head.x, head.y + 20)

        dir_l = game.direction == Direction.LEFT
        dir_r = game.direction == Direction.RIGHT
        dir_u = game.direction == Direction.UP
        dir_d = game.direction == Direction.DOWN

        state = [
            # Danger straight
            (dir_r and game.is_collision(point_r)) or
            (dir_l and game.is_collision(point_l)) or
            (dir_u and game.is_collision(point_u)) or
            (dir_d and game.is_collision(point_d)),

            # Danger right
            (dir_u and game.is_collision(point_r)) or
            (dir_d and game.is_collision(point_l)) or
            (dir_l and game.is_collision(point_u)) or
            (dir_r and game.is_collision(point_d)),

            # Danger left
            (dir_d and game.is_collision(point_r)) or
            (dir_u and game.is_collision(point_l)) or
            (dir_r and game.is_collision(point_u)) or
            (dir_l and game.is_collision(point_d)),

            # Move direction
            dir_l,
            dir_r,
            dir_u,
            dir_d,

            # Food location
            game.food.x < game.head.x,  # Food is left
            game.food.x > game.head.x,  # Food is right
            game.food.y < game.head.y,  # Food is up
            game.food.y > game.head.y,  # Food is down
        ]

        return np.array(state, dtype=int)

    def get_action(self, state):
        """
        Get the action to perform based on the current game state.
        :param state: The game state as a feature vector.
        :return: A list representing the action [straight, right, left].
        """
        state0 = torch.tensor(state, dtype=torch.float)
        prediction = self.model(state0)  # Predict the Q-values for each action
        move = torch.argmax(prediction).item()  # Get the action with the highest Q-value
        final_move = [0, 0, 0]
        final_move[move] = 1  # Set the chosen action
        return final_move


def play_with_trained_model():
    """
    Play the snake game using the pre-trained AI model.
    """
    game = SnakeGameAI()  # Initialize the game
    agent = Agent()  # Initialize the agent with the pre-trained model

    while True:
        # Get the current game state
        state_old = agent.get_state(game)

        # Get the action from the agent
        final_move = agent.get_action(state_old)

        # Perform the action and get the new game state
        reward, done, score = game.play_step(final_move)

        if done:
            # If the game is over, reset the game and print the score
            game.reset()
            print(f"Game Over! Score: {score}")
