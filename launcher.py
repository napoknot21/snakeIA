import sys, subprocess, os, pygame
subprocess.check_call([sys.executable, 'extras/setup/setup.py'])

from extras import snakeGame
from src.play import play_with_trained_model
from src.agent import train

class Launcher :

    def __init__(self):
        self.menu()


    def menu(self):

        print("\n=== SNAKE AI LAUNCHER ===\n")
        print("1. Train a new AI (generate model_training.pth)")
        print("2. Use a pre-trained AI (model_trained.pth)")
        print("3. Play the classic snake game")
        choice = input("Choose an option (1, 2, or 3): ").strip()

        if choice == "1":

            print("\n[*] Starting training...\n")
            train()

        elif choice == "2":

            print("\n[*] Using pre-trained AI...\n")
            play_with_trained_model()

        elif choice == "3":

            print("\n[*] Starting the classic snake game !\n")
            game = snakeGame.SnakeGame()

            #game loop
            while True :
                game_over, score = game.play_step()

                if game_over == True :
                    break
            print("\n[*] Final Score: ", score)

            pygame.quit()

        else:
            print("\n[-] Invalid option. Please restart the program !\n")
            sys.exit(1)


def main () :
    Launcher()

if __name__ == '__main__' :
    main()
