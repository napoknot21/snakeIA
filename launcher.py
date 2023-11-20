import sys, subprocess
subprocess.check_call([sys.executable, 'extras/setup/setup.py'])

from src import agent as ag

class Launcher :

    def __init__ (self) :
        ag.Agent()


def main () :
    Launcher()

if __name__ == '__main__' :
    main()
