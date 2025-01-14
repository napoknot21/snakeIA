# snakeIA

Based on the famous game : "Snake".

I incorporate an IA who learn how to game snake and get better creating a strategy.

## Prerequisites

It's imperative to have ```python3```. Update your python version [here](https://www.python.org/downloads/)

We need to install some external libraries like ```pygame```, ```pytorch``` for the game. So, depending your operanting system, there are different ways to install them


### Windows 

Open a cmd, and enter the following command
```
pip3 install pygame ipython matplotlib
```
For ```pyTorch```, you can download it from the offical web site [here](https://pytorch.org/).
```
pip3 install torch torchvision
```

### Mac
Open a terminal and do the following command **in case you DON'T have pip** 
```
curl https://bootstrap.pypa.io/get-pip.py
```
And then, we install the external libraries
```
pip3 install pygame torch torchvision matplotlib ipython
```

### Linux

For **DEBIAN** based distribution :
```
apt-get install python-pygame python-ipython libtorch-dev python3-matplotli
```

For **ARCH** based distros :
```
pacman -S python-pygame ipython python-pytorch matplotlib 
```

For other linux distributions, check the official documentation of your OS.

## Run the project

First, clone the repository
```
git clone https://github.com/napoknot21/snakeIA.git
```

Enter to the cloned directory
```
cd snakeIA
```

Finally, we run the ```launcher.py``` !
```
python3 launcher.py
```

3 options are available in this update
```
=== SNAKE AI LAUNCHER ===

1. Train a new AI (generate model_training.pth)
2. Use a pre-trained AI (model_trained.pth)
3. Play the classic snake game

Choose an option (1, 2, or 3):
```
> Choose the option you prefer !

Made by Napoknot21 (C. M-A)
