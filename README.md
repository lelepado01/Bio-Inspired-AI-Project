# 🐜 Bio-Inspired-AI-Project 🦖

## Authors 🦄

Gabriele Padovani ```229207```

Nadia Benini ```241520```

## Description 🐘

The report for this project is in this github repository at: ``` BioInspiredAI.pdf ```


## Installation 🚀🐥

The library MAgent2 can supposedly be installed with pip, but in our case we encountered several difficulties. The way we ended up solving most of the issues is by installing the library following these steps:

#### 1. Clone Repository 🧬

```git clone https://github.com/lelepado01/Bio-Inspired-AI-Project.git```

#### 2. Install MAgent2 and Requirements💿

```pip install -r requirements.txt```

#### 3. Complete the library with the missing files 🛠️

Download the library from the github repository:

https://github.com/Farama-Foundation/MAgent2 

Only the *magent2* folder is necessary

#### 4. Copy the missing files 📁

Go to the source folder of the library and copy the files into the magent2 folder of the library installed with pip (this path can be found with the command ```pip show magent2```)

#### 5. Correct Runtime Error in MAgent2 🪚

In the same directory, open the file *gridworld.py* and remove: 

 - At line 191: the type annotation ```: list[AgentSymbol]```
 - At line 192: the type annotation ```: list[float]```
 - At line 562: the type annotation ```-> list[ctypes.c_int32]```

This should solve all the runtime errors which appeared when testing the library.

In the file *render.py* remove:

 - At line 99: substitute 

    ```screen_size = (infoObject.current_w - 50, infoObject.current_h - 50)```
    
    With
    
    ```screen_size = (infoObject.current_w, infoObject.current_h)```

This should fix a bug we encountered when running the environment several times, the window would get smaller and smaller, until the program crashed.

#### 6. Test the library

Run the following code to test the library:

```
from magent2.environments import battle_v4
from pettingzoo.utils import random_demo

env = battle_v4.env(render_mode='human')
random_demo(env, render=True, episodes=1)
```

To run the project, execute the file *main.py*: 
    
```python main.py```

## Useful links 🔗

Paper del prof: 
https://arxiv.org/abs/2208.12758

Utile per cercare QD: 
https://quality-diversity.github.io/papers

Altri algoritmi di QD:
https://arxiv.org/pdf/2012.04322.pdf
https://arxiv.org/pdf/2104.03936.pdf

Magent2 (andrà citato sicuro): 
https://github.com/Farama-Foundation/MAgent2

