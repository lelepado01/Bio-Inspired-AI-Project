# Lab 5

## Ex1

- How do your results change from the unconstrained version (from the previous lab)?

For f0 measurement not much changes, where the ranges of both f0 and f1 scores are similar to the unconstrained version. The pareto front obtained is however more rounded, and the solutions are more well distributed, where in the earlier lab there was lots of overlap.

- Do your previous parameters continue to solve the problem?

No, as the constraints eliminate a large part of the search space, the solutions are very likely to end up out of bounds, and the penalty function will make them less likely to be selected.

- Try to increase the population size and/or the number of generations to see if you can find better solutions.

Increasing the population size we get a more well-traced pareto front, which may help in deciding the magnitude of tradeoff to be applied to the two variables. 
Increasing the number of generations we get a more distinct pareto front, where points merge along a line, as opposed to cluster in more of a distribution-like formation.

## Ex2

- Do you see any difference in the GA's behavior (and results) when the penalty is enabled or disabled?

Yes, the penalty function disincentive to select points with a specific constraint violation, and thus the GA will tend to select points with lower constraint violation, which may not be the best performing points in absolute.

- Try to modify the penalty functions used in the code of each benchmark function (check the code corresponding to `if usePenalty`, and/or change the main parameters of the GA `max_generations`, `pop_size`, `gaussian_stdev`, `mutation_rate`, `tournament_size`, `num_elites`) in *Exercise 2*. Are you able to find the optimum on all the benchmark functions you tested?

It depends on which problem is chosen, and on whether the penalty function is used or not.

No Penalty:
 - RosenbrockCubicLine: yes, tho there is not much improvement
 - RosenbrockDisk: yes, again there is not much improvementda
 - MishraBirdConstrained: yes
 - Townsend: not as precise as last problem, but still good
 - Simionescu: very spread out points, fitness does not seem to improve
 - SphereCircle: points get closer, but fitness actually increases in early generations
 - SphereConstrained: yes

With Penalty: 
 - RosenbrockCubicLine: yes, tho there is not much improvement
 - RosenbrockDisk: yes, points are not as close
 - MishraBirdConstrained: converges slow, but points are very close at the end
 - Townsend: converges quickly, but points are not as close
 - Simionescu: no improvement in fitness
 - SphereCircle: same as the unconstrained version
 - SphereConstrained: yes

- Is the GA able to find the optimal solution lying on the unit circle? If not, try to change some of the GA's parameters to reach the optimum.

In the constrained version the GA is able to find the optimal solution, however there is large variation in the fitness function of the solutions, this is probably due to the fact that the values in this problem are very small.

- By default, the sphere function is defined in a domain $[-5.12,5.12]$ along each dimension. Try to increase the search space (to do so, change  `self.bounder` and `generator` in the class `SphereCircle`. To progressively increasing boundaries (e.g. $[-10,10]$, $[-20,20]$, etc.). Is the GA still able to explore the feasible region and find the optimum?

No, by setting the bounds to [-1000, 1000] the GA's fitness function does not improve, and the points are not close to the optimal solution.

-  If not, try to think of a way to guide the GA towards the feasible region. How could you change the penalty function to do so? (Hint: look at the `evaluator` method of the class `SphereCircle` and consider that we are maximizing the fitness function, while we want to minimize the violation given by $g_1(x)$.

By increasing the penalty constant returned I am able to get the GA to converge to the optimal solution, however the fitness function is still very unstable.

## Final Questions

- What do you think is the most efficient way to handle constraints in EAs?

It probably depends on the problem, but I would say that pareto dominance based approaches may be able to remove large parts of the search space efficiently, and several hybrid optimizations may be added to increase the performance.

- Do you think that the presence of constraints makes the search *always* more difficult? Can you think of cases in which the constraints could actually make the search easier?

If the constraint removes a large part of the search space where only low fitness solutions are present, then the penalty function may act as a incentive to move towards the better performing region

- Do you see any difference in performance between GA and ES? Why?

Genetic algorithms tend to be more computationally expensive then evolutionary search.
As for accuracy, genetic algorithms may perform better with constraints, as they allow for more thorrow search, while evolutionary search may perform better if the search space is larger.