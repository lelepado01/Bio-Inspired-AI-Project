
# Lab 10

### Ex1

- Try out different parameter combinations of numOpponents, archiveType, archiveUpdate, and updateBothArchives, and observe what kind of robot behavior is evolved. Can you find cases where the prey "wins"? Can you find cases where the predator "wins"?

By keeping all parameters the same, the prey always wins, as it stays in the corner of the map where the predators can't see it.

By changing archiveType to HALL_OF_FAME, both the pray and the predators behaviour improves, as they are able to find each other.

It seems however, that the prey always stays in the corner of the map, as it tries to maximize the distance between itself and the predator.

### Ex2

- Is the co-evolutionary algorithm able to evolve an optimal (without sorting errors) SN, in the default configuration?

It seems like it always end up with sorting errors, but it does get better over time, at best it gets wrong only two items.

- Try to investigate this problem in different configurations. In particular, focus on the effect of the size of the input sequences (`INPUTS`), the number of input sequences per parasite (`P_NUM_SEQ`), and the two population sizes (`POP_SIZE_HOSTS` and` POP_SIZE_PARASITES`). If needed, also change the size of the Hall-of-Fame (`HOF_SIZE`) and the number of generations  (`MAXGEN`). What conclusions can you draw? For instance: What makes the problem harder? What is the effect of `P_NUM_SEQ`? What can you do to solve the harder problem instances?
 
By just increasing the number of generations, the sorting errors are reduced, but they are still present (it seems like it always ends up with one sorting error).
Raising the number of inputs inevitably creates a harder problem (yielding more errors). 
To solve these harder problems one solution could be to raise the population size, or increase the number of generations. 
It seems also having a larger tournament size doesn't help much, as it doesn't seem to reduce the number of sorting errors.