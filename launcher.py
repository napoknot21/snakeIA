import sys, subprocess, os
subprocess.check_call([sys.executable, 'extras/setup/setup.py'])

import src.agent as ag

class Launcher :

    def __init__ (self) :
        ag.Agent()


def main () :
    Launcher()

if __name__ == '__main__' :
    main()
