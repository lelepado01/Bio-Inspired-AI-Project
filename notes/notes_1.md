# Lab1

## Ex1

- Do the mutations tend to improve or worsen the fitness of the parent?

The mean fitness is random (at least in this case, with a single iteration)
Having an infinite number of points, the mean fitness of the children would average to the parent's fitness.
So they neither improve nor worsen the fitness of the parent.

- Are low or high mutation magnitudes best for improving the fitness? 

If only one iteration is used then larger is better, as it may randomly result into a closer value to the optimium.
If several iterations are done, then smaller is probably better, as a large value may jump over the optimum.

- How does this depend on the initial value of the parent and on the number of dimensions of the search space? 

With larger magnitudes, a 'good' starting point may be beneficial to not skip the optimal value.
Also smaller magnitudes may benefit from a good initial point as a further start will take more generations to reach optimum.
A larger number of dimensions will increase the search space, resulting in a more computationally expensove search.

## Ex2

- Try to confirm the answers that you gave in the previous exercise

With a larger numer of dimensions, search space increases.
Even keeping the same standard deviation, the magnitude of mutations increases with the increase in space.

## Ex3

- How close is the best individual from the global optimum?

Best Individual: [0.00038799] in 1D, 0.000387 away from global optimum
The best individual is at [-0.01061882 -0.01849095] which is 0.021 away from optimum point. 

- Can you get as close as in the one-dimensional case by modifying the mutation magnitude and/or the number of generations?

By reducing the standard deviation we can get closer: 
Best Individual: [-0.0019081   0.00059136]
Distance from Global Optimum 0.001997633473678757

## Ex4

- Did you see any difference in the best fitness obtained? Try to explain the result.

There are differences depending on the value of standard deviation used, it seems 0.01 is too small and doesn't reach the optimal value, 
while 1.0 is too large and may skip over it.

## Final

- What is the genotype and what is the phenotype in the problems considered in this lab?

The genotype is the position of parent and child individuals
The phenotype is the manifestation of the genotype in the real world, 
in this case the closeness of the individual to the optimum point. 
Which can be considered the same as the fitness function in this example.

- What are the advantages and disadvantages of low/high mutation magnitudes in EAs?

Small mutation magnitudes allow better precision at the expense of computational resources 
and a slower approach to the optimum value.
Large mutation magnitudes provide faster improvements, but may overshoot the target and not converge to the absolute best value, 
but only to a relatively close point.