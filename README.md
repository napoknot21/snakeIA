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
sudo apt-get install python-pygame
```
For **ARCH** based distros :
```
pip3 install pygame
```

Then, We install the rest of libraries
```
pip3 install torch torchvision matplotlib
```
## Snake Game AI
First, we have to download the repo by
```
git clone https://github.com/napoknot21/snakeIA.git
```

Then, we enter to the cloned directory
```
cd snakeIA
```

Finally, we run the ```agent.py``` file and enjoy the show !
> The projetc is based on **python3**, so if you have other versions, update your python version !
```
python3 agent.py
```

## Game
If you only want to get fun and game to snakegame, well there's a file for that ! so run
```
python3 snake_game.py
```


Made by Napoknot21 (C. M-A)
