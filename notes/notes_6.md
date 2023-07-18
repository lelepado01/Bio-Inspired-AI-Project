
# Lab 6

## Ex1

- What is the effect of each behavior coefficient?

Alignment: describes how much each individual's flight is aligned with the global flock direction
Cohesion: describes how close individuals of the same flock fly
Separation: describes how much distance individuals of the same flock will keep between themselves.

- Which combination of coefficients leads to the most ``natural'' flock behavior? 

The default values of 0.5 seem to produce a good result, where individuals fly along side each other, splitting and joining groups.

## Ex2

-  What kind of behavior does PSO have on different benchmark functions (change the parameter `args["problem_class"]` to try at least a couple of functions), in comparison with the EAs? Does it show better or worse results? Does it converge faster or not?

Griewank: all 3 algorithms struggle (especially ES plateaus really early)
Rastrigin: GA is much worst, PSO barely converges
Schwefel: PSO gets stuck in local minima, can be visualized really well in two dimensions

All unimodals seem to work very well on the other hand.

- What happens if you run the script multiple times? Do the various algorithms (and especially PSO) show consistent behavior?

The best fitness achieved varies a lot:
PSO yields a best fitness between 510 and 550 (this with 100 variables)
With 2 dimensions on the other hand PSO almost always finds the lowest fitness

To check consistency, I ran 10 epochs of each algorithm, calculating the mean and standard deviation of the best fitness achieved: 
GA fitness: 0.0027 +- 0.0036
ES fitness: 0.0030 +- 0.0044
PSO fitness: 0.0034 +- 0.0085

It seems the algorithm showing more variance is PSO, although the deviation is still extremely low.

- Increase the problem dimensionality (`num_vars`, by default set to 2), e.g. to 10 or more. What do you observe in this case?

With 100 variables PSO finds the highest fitness among all the algorithms. This means the other two struggle with the larger search space and may not be as suited as the former.

-  Change the population size (by changing`args["pop_size"]`, by default set to 50) and the number of generations (by changing `args["max_generations"]`, by default set to 100), such that their product is fixed (e.g. $50 \times 100$, $100 \times 100$, etc.). Try two or three different combinations and observe the behavior of the three different algorithms. What do you observe in this case? Is it better to have smaller/larger populations or a smaller/larger number of generations? Why?

Having a larger number of individuals doesn't seem to improve the optimal fitness (100 pop size, 100 offspring).
With 10 pop size, 100 offspring not much seems to change.

Increasing max iterations however, the first experiment (100, 100) has improvements, meaning PSO struggles to converge in 100 iterations.

## Final Questions

- When do you think it is useful to have a lower (higher) cognitive learning rate? What about the social learning rate?

A higher social learning rate means information will be shared in an easier way, making population less diverse and favoring exploitation. 
Higher cognitive learning rate on the other hand pushes for more exploration.

- From a biological point of view, which neighborhood topology do you consider as the most plausible?

From a biological point of view, it makes sense that information is shared in a distance-based topology, (distance-based neighbourhood)
so either von-neumann or ring. 
This is because very often information is often shared orally or with other visual means (in animals). 
If we consider on the other hand today's information sharing means, then it's more of a broadcasting system, where everybody is connected to all or almost all individuals.