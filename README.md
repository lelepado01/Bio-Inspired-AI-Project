# 🐜 Bio-Inspired-AI-Project 🦖

## Authors 🦄

Gabriele Padovani ```229207```

Nadia Benini ```??????```

## Description 🐘
Boh

## Installation 🚀🐥

The library MAgent2 can supposedly be installed with pip, but in our case we encountered several difficulties. The way we ended up solving most of the issues is by installing the library following these steps:

#### 1. Install MAgent2 💿

```pip install magent2```

#### 2. Complete the library with the missing files 🛠️

Download the library from the github repository:

https://github.com/Farama-Foundation/MAgent2 

Only the *magent2* folder is necessary

#### 3. Copy the missing files 📁

Go to the source folder of the library and copy the files into the magent2 folder of the library installed with pip (this path can be found with the command ```pip show magent2```)

#### 4. Correct Runtime Error in MAgent2 🪚

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

#### 5. Test the library

Run the following code to test the library:

```
from magent2.environments import battle_v4
from pettingzoo.utils import random_demo

env = battle_v4.env(render_mode='human')
random_demo(env, render=True, episodes=1)
```

To run the project, execute the file *main.py*: 
    
```python main.py```

## TODOs

- [ ] aggiustare la posizione iniziale degli agenti sinistri (hanno ranged davanti e sono sempre in svantaggio rispetto agli agenti destri (che hanno melee davanti))
- [ ] aggiungere descrizioni alle funzioni, invece di avere commenti ovunque potrebbe essere più ordinato 
- [ ] correggere metodo di installazione, ci sono altri step (ex. correggere errore nel file della libreria)
- [ ] Fare descrizione del progetto su README.md
- [ ] testa che il salvataggio delle immagini e a file di testo funzioni (soprattutto la seconda, non l'ho testato)
- [ ] Implementare altri tipi di crossover
- [ ] Provare a parallelizzare l'algoritmo usando il CLUSTER Siiiiiii
- [ ] implementare tutte le formazioni iniziali (ex. square, triangolo, ecc.)
- [ ] espandere a più dimensioni (credo almeno due)

- [ ] iniziare a fare qualche test 
    - [ ] decidere quante epoche, quanti agenti, i parametri...
    - [ ] magari facciamo un'altra sezione nel readme in cui metta i risultati dei test
    - [ ] e motiviamo perchè abbiamo scelto quei parametri
- [ ] fare un po' di grafici
- [ ] provare a fare un sistema che salvi il video della battaglia finale

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

