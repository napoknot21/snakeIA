import sys, subprocess, os
subprocess.check_call([sys.executable, 'extras/setup/setup.py'])

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".", "src"))
import agent as ag

class Launcher :

    def __init__ (self) :
        ag.Agent()


def main () :
    Launcher()

if __name__ == '__main__' :
    main()
