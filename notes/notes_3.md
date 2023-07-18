# Lab1

## Ex1

- What happens if you make $\lambda$ smaller e.g. $\lambda=\mu$?

Changing $\lambda=\mu$ (so both parameters have a value of 20), the fitness obtained is much higher (so worst). 
From a best fitness value of 285 we get 1050. This means that more offsprings lead to better mutation (just through sheer numbers).
However this is due to the lowering of the population size, in fact by setting both parameters to 200, the fitness is 170.

- What happens if you increase the mixing number $\rho$?

By increasing the mixing number, we raise the number of parents which are averaged to have offspring in the next generation, leading to more exploitation through crossover and the search space. 
The higher the mixing number is, the more offsprings will be closer to an average over the full population.
(more mixed parents also cause slower performance)
The best fitness obtained is 70 instead of 285 (so better).

- Does this confirm or contradict the conclusions you drew in the first module?

This confirms that the balance in mutation and crossover phases is a crucial aspect of evolutionary algorithms.
So if the correct focus is placed on exploitation and exploration, the algorithm will perform better.

## Ex2

- How does the self-adaptation strategy influence performance on this problem?

It seems having an adaptation strategy is better at converging to a lower fitness score (which is better) than not having one. 
That being said, there is not much difference between global and individual adaptation strategies in performance.

- Does what you see here confirm what you suspected from the previous exercise?

It doesn't confirm, as having an Individual strategy supposedly allows for more flexible optimization.
It might be the case though, that the algorithm gets stuck in some local minimum due to the individual step size, while the global strategy may act as a generalization factor (simil to neural networks).

- How do the values of $\mu$, $\rho$, and $\lambda$ influence the performance given a particular self-adaptation strategy and other parameters?

A larger population size increases the exploration capacity of the algorithm (find diverse and globally optimal solutions)
lower offspring number -> better with global self-adaptation (Higher values of ρ increase the selection pressure --> fitter indivoduals)
Increasing the value of λ allows for a larger number of new solutions, which promotes exploration.

- Can you come up with any rules of thumb for choosing these parameters?

Ideally the parameters should balance the exploration and exploitation phases, so that the algorithm doesn't get stuck in a local minimum, but also doesn't waste time exploring the search space.

- Can you find a choice of parameters that works properly across several problems?

It may be possible to find a choice of parameters that works properly across several problems, but these might be similar problems. The parameters should be chosen based on the problem at hand, as there is no "one size fits all" solution.

## Ex3 

- Can CMA-ES find optima to different problems with fewer function evaluations?

Yes, it takes less evaluations to converge, only 1500 or so are necessary.

- How do these differences change with different pop. sizes and problem dimensions?

With a larger problem (more dimensions) the algorithm takes longer to converge.
Increasing population size doesn't seem to decrease the number of iterations necessary.

## Final Questions

- Do the observations you made while varying μ, ρ, and λ confirm or contradict the conclusions you drew in the previous module's exercises?

The observations made while varying μ, ρ, and λ confirm the conclusions drawn in the previous module's exercises, as the balance between exploration and exploitation is crucial to the performance of the algorithm. 
So having a good balance between the number of offsprings (large implies more exploration), and the population size (lower means more selection pressure to choose only fit individuals) is important.

- What are the advantages of self-adaptation in evolutionary computation?

self-adaptation algorithms, compared to other evolutionary ones, can show better convergence, adjust the trade-off between exploration and exploitation, be able to handle changes in search space. 

- In what ways might self-adaptation be occurring in biological organisms?

self-adaptation might be occurring in biological organisms when the organism is able to raise or lower some behaviour or trait, to respond to a change in the environment. 
One example could be metabolic rate regulation, adjusted based on the availability of food.

- Compare the different self-adaptation strategies explored in this exercise. 

In this module we explored global and individual self-adaptation strategies, as well as not using an ES at all. 
It seems clear that having a self-adaptation strategy is better than not having one, and that choosing between global and individual strategies depends on the problem at hand.
A global optimization strategy might be more performant, as parameters dont need to be updated for each individual, but it might also be less flexible. On the other hand a global strategy may help to generalize the solution, and avoid "overfitting".

- In what ways are certain strategies better than others for optimization? 

Certain strategies are better than others due to, for example, computational complexity, adaptation rate, complexity of the problem.

- In what ways are certain strategies more biologically plausible than others?

Some strategies might be more biologically plausible, for example because of the standard deviation used as step size. In biology this delta is not that large and probably doesn't adapt to the problem, as evolution is "open ended".

- Describe what reasons may contribute to better performance of CMA-ES and what can be the conditions when CMA-ES is not better than a basic ES.

CMA-ES achieves normally better performance due to it's ability to adapt with the covariance matrix, adjusting the step-size. 
A basic ES might be more performant on simple problems, with for example low dimensionality. 
Or objective functions with a long gradual slope, where CMA-ES might slow down and struggle to converge, while other ES systems don't.