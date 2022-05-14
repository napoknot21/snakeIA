import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

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

class SnakeGame:

    #Constructor for Snake
    def __init__(self, w=640, h=480) :
        self.w = w
        self.h = h
        #Here we init the display (window)
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        
        #we init game status

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

    
    #Place a new food in random place
    def _place_food (self) :
        x = random.randint(0, (self.w - BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake :
            self._place_food()
    

    #Get input events and modify direction, game state, and snake state
    def play_step (self) :
        #First, we need to collect the user input
        for event in pygame.event.get () :
            #Were in the case where we close the program
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            #The case where the user uses the keyboard directions
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT :
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP :
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN :
                    self.direction = Direction.DOWN

        #We move the snake with the input
        self._move(self.direction) #We update the head
        self.snake.insert(0, self.head) #The new head
        
        #We have to check if the snake is still alive (game over or not)
        game_over = False
        if self._is_collision () :
            game_over = True
            return game_over, self.score

        #We place new food and score incrise or just move
        if self.head == self.food :
            self.score += 1
            self._place_food()
        else :
            self.snake.pop()

        #We update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)

        #We return game over and score
        return game_over, self.score

    
    #check if the snake heats hits boundary or itsself
    def _is_collision (self) :
        #we check if it hits boudary
        if self.head.x > (self.w - BLOCK_SIZE) or self.head.x < 0 or self.head.y > (self.h - BLOCK_SIZE) or self.head.y < 0 :
            return True
        #Check if the snake head hits itself
        if self.head in self.snake[1:] :
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
    def _move (self, direction) :
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT :
            x += BLOCK_SIZE
        elif direction == Direction.LEFT :
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN :
            y += BLOCK_SIZE
        elif direction == Direction.UP :
            y -= BLOCK_SIZE

        self.head = Point(x, y)


if __name__ == '__main__' :
    game = SnakeGame()

    #game loop
    while True :
        game_over, score = game.play_step()

        if game_over == True :
            break
    print("Final Score: ", score)

    pygame.quit()
        
