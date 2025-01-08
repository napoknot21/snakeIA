import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.Font('src/fonts/arial.ttf', 25)

class Direction (Enum) :
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

#colors rgb
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
SPEED = 20

class SnakeGameAI:

    #Constructor for Snake
    def __init__(self, w=640, h=480) :
        self.w = w
        self.h = h
        #Here we init the display (window)
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.reset()


    #reset all game stats (for the IA training)
    def reset (self) :
        #The game will always start by the snake going to the rigth direction
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [
                self.head,
                Point(self.head.x - BLOCK_SIZE, self.head.y),
                Point(self.head.x - (2*BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0

    
    #Place a new food in random place
    def _place_food (self) :
        x = random.randint(0, (self.w - BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake :
            self._place_food()
    

    #Get input events and modify direction, game state, and snake state
    def play_step (self, action) :
        self.frame_iteration += 1
        #First, we need to collect the user input
        for event in pygame.event.get () :
            #Were in the case where we close the program
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            
        #We move the snake with the input
        self._move(action) #We update the head
        self.snake.insert(0, self.head) #The new head
        
        #We have to check if the snake is still alive (game over or not)
        reward = 0 #if the snake eat food => +10; if snake dies (game over) => -10; else => 0
        game_over = False
        if self.is_collision () or self.frame_iteration > 100*len(self.snake) :
            game_over = True
            reward = -10 #if the snake eat food => +10; if snake dies (game over) => -10; else => 0
            return reward, game_over, self.score

        #We place new food and score incrise or just move
        if self.head == self.food :
            self.score += 1
            reward = 10 #if the snake eat food => +10; if snake dies (game over) => -10; else => 0
            self._place_food()
        else :
            self.snake.pop()

        #We update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)

        #We return game over and score
        return reward, game_over, self.score

    
    #check if the snake heats hits boundary or itsself
    def is_collision (self, pt=None) :
        if pt is None : pt = self.head
        #we check if it hits boudary
        if pt.x > (self.w - BLOCK_SIZE) or pt.x < 0 or pt.y > (self.h - BLOCK_SIZE) or pt.y < 0 :
            return True
        #Check if the snake head hits itself
        if pt in self.snake[1:] :
            return True
        return False


    #Update ui for snake
    def _update_ui (self) :
        self.display.fill(BLACK)
        for pt in self.snake :
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text =  font.render ("SCORE: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    
    #change movement depending de (new) direction
    def _move (self, action) :
        #[straight, right, left] 

        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]

        index = clock_wise.index(self.direction);

        if np.array_equal(action, [1, 0, 0]) :
            #We keep the courrent direction
            new_dir = clock_wise[index] #no change
        elif np.array_equal(action, [0, 1, 0]) :
            next_index = (index+1)%4
            new_dir = clock_wise[next_index] #right turn : r -> d -> l -> u
        else : # [0, 0, 1]
            next_index = (index - 1) % 4
            new_dir = clock_wise[next_index] #left turn : r -> u -> l -> d

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT :
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT :
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN :
            y += BLOCK_SIZE
        elif self.direction == Direction.UP :
            y -= BLOCK_SIZE

        self.head = Point(x, y)


