# Lab1

## Ex1

- Do you see any difference between the two results? Why?

With just mutations the individual quickly optmizes the current strategy, however it can't join different genomes. 
With crossover only, the individuals share different traits, but can't improve them, so we get the best "combination of initial traits"
By using both strategies, we get optimal results.

## Ex2

- Is there an optimal crossover fraction for this fitness function? 

Although there is some variation depending on the run, it seems the optimal crossover rate is around 0.75 / 0.8. 
This only applies to this specific problem however, as different problems may have different optimal crossover rates.

- Why?

Because it is the ratio which balances the best the mutation phase and the crossover part.

## Ex3

- Which tournament size gives better results for the fitness function sphere and why?

The results show large improvements in fitness for tournament sizes smaller than 5, but this trend tends to slow down after tournament size of 10. 
After this value, it tends to have very marginal improvements.

- Which tournament size is better for the fitness function Rastrigin (you can change the problem by changing the parameter problem_class in the script) and why?

It seems that a lower tournament size is better to optimize a Rastrigin fitness function, this because a lower tournament size gives high selection pressure, allowing only the best individuals to survive. 

In the sphere function, having a lower selection pressure yields anyway to the optimum.

## Ex4

- Do you see a different algorithmic behavior when you test the EA on different benchmark functions? Why?

Rosenbrock: converges very quickly to different global optimum points, even very distant ones, as this fitness functions has a parabola-shaped global optimum region.

Griewank: parabola shaped fitness function, all the individuals converge to a single central optimum relatively quickly.

Ackley: converges very slowly at the start, then once the cone is found it starts speeding up.

Rastrigin: converges quickly up to a certain point, then much slower, all individuals end up relatively far from the center.

Schwefel: converges quickly, almost uniformly due to the shape of the fitness function. Often doesn't reach the center of the curve, although it's not guaranteed there is too much difference in score between a pit on the outside and a pit in the center. 

- What is the effect of changing the number of variables on each tested function?

Increasing the number of variables, all algorithms take much longer to converge, and the best fitness achieved is much higher (so worst).
This is due to the exponential increase in search space, which makes it much harder to find the global optimum. 
To get relatively comparable results, the number of iterations should be increased, and the mutation step probably decreased.

## Final Questions

- Why is it useful to introduce crossover in EA?

Introducing crossover allows winning individuals of the same generation to share genome. In other words, in the exploration / exploitation duality, it refers to the exploration step.
Crossover allows to introduce diversity in the population, and explore different regions of search space. It also improves the robustness of the evolutionary algorithm, as it may allow to skip over local optimas. 

- Can you think of any cases when mutation only can work effectively, without crossover? 

Yes, there are cases when mutation only algorithms may work, such as when the search space is small and has a single global optimum, this allows the population to optimize the current traits. 
Without crossover, however, the algorithm will struggle to mix advantageous genomes.

- What about using crossover only, without mutation?

There are cases when just crossover may be enough to reach an optimal solution. These situations are however very rare, as crossover only allows to combine genetic material from the parents and struggles to create diversity in a population. 
The algorithm may converge too quickly to a suboptimal solution, and iterating too much will yield very similar offsprings (homogeneous population).

- What's the effect of changing the fraction of offspring created by crossover?

The fraction of offspring created with crossover has a direct impact on the convergence of the algorithm. The more individuals are created with crossover, the more the algorithm will be likely to combine good traits from different parents, leading to more thorrow exploitation of high performance solutions. 
With a higher percentage of offspring created via mutation, on the other hand, the algorithm increases the exploration capability of the search space. 

- Are there optimal parameters for an EA?

There are no optimal parameters for an evolutionary algorithm, as each problem may require different thresholds of, for example standard deviation. 
It is very important however, to balance the contribution of crossover and mutation, as both are fundamental for it to reach the optimal point.

- What are the advantages and disadvantages of low/high selection pressure?

A low selection pressure allows the algorithm to explore more the search space, which avoids individuals getting stuck in local optima. 
It however may lower the quality of the solution, as more crossover leads to less accuracy, so it may require more iterations to reach an optimal solution.

On the other hand, higher selection pressure yields a faster converging algorithm, which may get stuck in a locally optimal solution, since it shifts its focus on the exploitation part rather then on the exploration side. 