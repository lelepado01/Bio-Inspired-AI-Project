# Lab4

## Ex1

- What happens when you run the GA with this fitness function?

By using this fitness function, it's very likely that the algorithm will get stuck into a local optimum, as shown in the two final population images, because it tries to optimize a single pbjective and takes the best possibile result for the second one.
This is an acceptable solution, however it may neglect a better compromising point.

- Why do you obtain this result? (Hint: pay attention to the relative scaling of the two objectives!)

In this case the first objective has a lower optimum, spherically shaped, the algorithm finds the bottom of the higher slope (second objective) and gets stuck.

-  What happens if you give the first (or second) objective all of the weight?

By giving all the weight to the first objective, the algorithmm essentially neglects the second one, optimizing only the first.
The final population is in fact centered around the first objective's optimum. 
This happens since the algorithm can ignore the second objective, going against the gradient of the second objective's optimum.

- Can you find a weighting able to find a solution that approaches the optimum on both objectives? 

Between [0.75, 0.25] and [0.76, 0.24] the focus shifts from one objective to the other, it however difficult to find the balancing point.

- Does your weighting still work on the new problem? (NOTE: The size of the array `args["fitness_weights"]` must be the same as the number of objectives.)

The same weighting wouldn't work as hyperparameters are problem dependant. 
Also, in this case we have more objectives, so two weights wouln't work.

- Can you think of a method for combining the objectives that might work better than using a weighted sum? (NOTE: If you want to try your idea out, edit the `init` method of `CombinedObjectives`).

One idea could be to use a threshold system, where if the value is too small, the objective is ignored, so that the algorithm can focus on the ones which really matter.
Testing this method, it seems to be able to lower the fitness, with the default problem yielding a score of 1.54, while the latter one returns 1.14.


# Ex2

- How do the solutions you find here compare to those found in exercise 1?

The solutions found in this exercise are more distributed in the space between the optimum of the first and the second objective.

- Is there a single solution that is clearly the best?

Fitness-wise, yes. However it is not guaranteed that the best solution is also the one with the optimal fitness level. Many factors may influence that, as for example the way the "goodness of a solution" is translated into the fitness score. 

- Can you still find good solutions?

Yes, although this problem has three variables and the benchmark is more complex, the algorithm is still able to find good solutions.

- What happens if you increase the population size (change the variable `args[pop_size]` in the script) or the number of generations (see the parameter `args[max_generations]`?

Fitness gets lower, since the algorithm is able to search more thoroughly and for longer, but complexity raises.

- Is the algorithm able to find reasonable solutions to this problem? 

The algorithm is able to find a set of reasonable solutions but, since it's a balancing problem, it is not able to decide on the best one. 
This means the returned solutions are several, and are all compromises between the objectives.

- Do you see any patterns in the Pareto-optimal solutions that may help you in designing a well-performing disk-brake in the future?

Yes, depending on whether the brake mass or the stop time is valued more, an optimal solution can be found.

# Final

- When do you think it is appropriate to use a multi-objective evolutionary algorithm vs. combining multiple objectives into a single fitness function?

It may depend on the type of problem which has to be solved. Multi-objective evolutionary algorithm seem to be more suitable at dealing with conflicting objectives, while the combination of several objectives into a single one may be more useful with converging solutions, which have faster execution times and may not need a large exploration of all compromises.

- What can the results of a multi-objective algorithm teach us about exploring the design spaces of engineering problems?

The results of a multi-objective algorithm can show the different trade-offs which can be implemented to obtain the most suitable solution for our needs.

- In biological evolution it is possible to think of many phenotypic traits that contribute to the ultimate fitness of an organism (try to enumerate some of these). 

Some are, for example, strength, intelligence, speed.... 

- What (if any) relevance do multi-objective evolutionary algorithms have to biology?

multi-objective evolutionary algorithms are useful to understand the effect of several, contrastive or converging, objectives on the evolution of a species