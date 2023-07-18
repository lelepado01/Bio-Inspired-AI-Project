# Lab 7

## Ex1

- Which algorithm provides the best solution in most cases? 

The ant colony yields a distance of 291.0 with the default settings, while EA returns 381
ACS still outperforms EA in the other two problem instances.

- What can you say about the number of function evaluations needed to converge?

It seems ACS also converges quicker, taking a fraction of the evaluations necessary to the latter algorithm (circa 2000 in the first problem instance)

## Ex2 


- Which algorithm provides the best solution in most cases?

In this case the algorithms are very similar, with ACS edging EC in instance 05, while the latter performed better in 04, 07 and 08.
In all other instances the two algorithms reached what is probably the optimal solution, so it's a tie.

- What can you say about the number of function evaluations needed to converge?

As for the convergence, tho very close, it seems ACS reaches a plateau point slightly quicker.

## Ex3


- Which algorithm provides the best solution in most cases?

In this version of the knapsack problem, ACS clearly outperforms EC, where the fitness even stayies negative in some instances.

- What can you say about the number of function evaluations needed to converge? 

Similarly to the first exercise, ACS converges much quicker compared to EC

- Do you observe any difference on the algorithmic behavior between this exercise and the previous one?

Yes, maybe since the former problem was easier, it seemed the two were scoring much closer fitness values.

## Final Questions

- What are the main differences between continuous and discrete optimization problems? 

Discrete problems have a set of possible combinations, within which an algoritm has to find an optimal trade-off. 
An example of these types of problems is TSP

Continuous problems have to be optimized by choosing one value among a range of infinite possibilities.
Many of the previous laboratories focused on continuous problems.

- Do you think that any of these two classes of problems is more difficult than the other?

An issue with discrete problems, is that being centered around combinatory issues, these get exponentially more complex as the number of variables increases.
This is not the case with continuous problems, which are more easily solved, for example, using a gradient descent approaches.

- Why is ACS particularly suited for discrete optimization?

ACS uses pheromone trail to guide the search. This allows the algorithm to refine and improve a solution which is regarded to as best at the current iteration.

- Consider the two versions of the Knapsack problem (0/1, and with duplicates). Which of the two problems is more challenging from an optimization point of view? Why?

The 0/1 knapsack problem is more challenging, because it is a discrete problem, and the number of possible combinations increases exponentially with the number of variables.
The knapsack problem with duplicates on the other hand, can be solved often finding the most valuable item, adjusting for space occupied. This leads to easier solutions most of the times.
