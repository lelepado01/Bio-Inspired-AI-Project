# Bio-Inspired-AI-Project

## Authors
Noi

## Description
Boh

## Installation

The library MAgent2 can supposedly be installed with pip, but in our case we encountered several difficulties. The way we ended up solving most of the issues is by installing the library following these steps:

#### 1. Install MAgent2

```pip install magent2```

#### 2. Complete the library with the missing files

Download the library from the github repository:

https://github.com/Farama-Foundation/MAgent2 

Only the *magent2* folder is necessary

#### 3. Copy the missing files

Go to the source folder of the library and copy the files into the magent2 folder of the library installed with pip (this path can be found with the command ```pip show magent2```)

#### 4. Test the library

Run the following code to test the library:

```
from magent2.environments import battle_v4
from pettingzoo.utils import random_demo

env = battle_v4.env(render_mode='human')
random_demo(env, render=True, episodes=1)
```


## TODOs

- [ ] Finish README.md file of the project CIAO
- [x] visualizzazione della griglia del fitness (magari anche over time)
- [x] capire se si possono passare tutti i parametri alla funzione env
- [ ] fare la parte dell'enviroment
- [x] passare parametri della simulazione in una sola classe
- [x] spostare consts e metterle come parametri dell'algoritmo, vanno spostati nella classe e decisi nel main
- [ ] espandere a più dimensioni (credo almeno due)
- [ ] funzioni di mutation e crossover in environment_data.py
- [x] inizializzazione di EnvironmentData in base ai parametri passati
- [x] fare in modo che MAP_Elites non stampi sempre tutto tutto
- [ ] magari si puù fare più di un algoritmo... non sembra così tanto lavoro
- [ ] testa che il salvataggio delle immagini mostri anche il numero di agenti per ogni tipo

## Useful links

Paper del prof: 
https://arxiv.org/abs/2208.12758

Utile per cercare QD: 
https://quality-diversity.github.io/papers

Altri algoritmi di QD:
https://arxiv.org/pdf/2012.04322.pdf
https://arxiv.org/pdf/2104.03936.pdf

Magent2 (andrà citato sicuro): 
https://github.com/Farama-Foundation/MAgent2
//ciao
