import sys, subprocess, os
subprocess.check_call([sys.executable, 'extras/setup/setup.py'])

from src.agent import train

class Launcher :

    def __init__ (self) :
        train()


def main () :
    Launcher()

if __name__ == '__main__' :
    main()
