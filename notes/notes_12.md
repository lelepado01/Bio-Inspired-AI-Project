
# Lab 12

### Ex1

 - What kind of considerations can you make regarding the fitness trend (Is the algorithm able to converge to a reasonably low fitness function? How quick is the convergence?), and the activity grid (For instance, are there regions of the feature space that are visited/updated more frequently than others?). What kind of illumination pattern do you observe? Do you see any trend/correlation between performance and features of the map?

The algorithm converges to a reasonably low value of the fitness function, but it takes a lot of time to do so. The convergence is very slow, and the fitness trend is not very smooth. 
The activity grid is not uniform, it almost seems the cells are updated at random.  There is a strong correlation between the performance and the features of the map, to the point that the performance map starts resembling the Rastrigin function.
    
 - Try to change the parameters of the MAP-Elites algorithm, i.e.,: `NO_BINS`, `MAX_ITEMS_BIN`, `BUDGET`, `BATCH_SIZE`, which indicate, respectively, the number of bins (that is the same for both features), the maximum number of items stored in each bin of the grid, the total budget of the evolutionary process (number of function evaluations), and the batch size, i.e., how many solutions are evaluated at each iteration of MAP-Elites. Focus in particular on `NO_BINS`. What is the effect on the fitness trend and the performance map when you increase or decrease the number of bins?
    
With 4 bin:
Best fitness is 0.002074443162963169
Activity grid from 0 to 15
Performance grid is very fuzzy, without much detail, but still shows a global minimum in the center.

With 64 bins:
Best fitness is 0.009493624381236647
Activity grid from 0 to 5
Performance grid is more detailed, however many cells are not visited at all. 

 - Try to change the problem dimension (`PROBLEM_DIM`) to a much larger value, for instance 10 (remember that Rastrigin is a scalable benchmark problem, meaning that it can be defined for any number of variables). Note that in any case the first two variables are taken as features for MAP-Elites. What kind of considerations can you make in this case regarding the illumination pattern and the other aspects (i.e., the fitness trend and the activity grid) of the results? Does illumination become more difficult (i.e., less bins are visited, with poorer performance)? Why?

With 3 dimensions:
Activity grid from 0 to 8
Performance grid is much closer to the rastrigin function, with spikes and a global minimum in the center.

With 10 dimensions: 
Activity grid from 0 to 10
Performance grid is very light compared to the one with 3 dimensions

### Ex2

 - What kind of considerations can you make in this case regarding the fitness trend and illumination pattern?

 There are many cells which are not accessed, as they are not feasible due to constraints
 
 -  Also in this case, try to change `NO_BINS` and `PROBLEM_DIM`, and see if you can confirm the observations made in the previous experiment.

By increasing the number of bins, the algorithm is not able to test all possible combinations of features, leaving lots of cells not visited.
By increasing the number of dimensions the pattern in activity and performance grid changes, maybe because the features visualized are not the same, of the other dimensions change the feasible space, making some cells not accessible.
 
 - If you want, you could try to change the custom function definition in `eval_fn` and replicate the experiment with a different setting. What kind of results do you obtain?

By adding this constraint:
fit0 > 0. and fit0 < 0.3
and making it return a large value, the algorithm is eliminates all cells to the left, favoring better spots on the right.

### Ex3

 - Is the algorithm able to approximate the given polynomial? If not, try to change some parameters of the algorithm and see if you can improve the results. Note that in this case there is an additional parameter (`INIT_BATCH_SIZE`), that is the size of the first batch (used to initialize the map). This is usually set to be bigger than the batch size at the subsequent iterations of the algorithm.

It seems the algorithm is able to approximate the given polynomial, as the fitness value returned is very low.

 - Try to change the generator function (e.g., to include trigonometric functions) defined in the method `generatorFunction`. Is the algorithm able to approximate more complicated generator functions? Which parameters can you change to improve the results?

For math.sin(x)*x**2, which had caused issues for GP in the earlier lab, the algorithm is able to approximate it very well.
The fitness returned is 0.0021567229978618385

Even all other problems seem to be solved well, with fitness values close to 0.

If I needed to improve the search, I would increase the number of bins, the tree size, and the number of generations.
Also I may have to change the mutation and crossover rate, to speed up the search.

 - What kind of illumination pattern do you observe in the various trials? Do you see any trend/correlation between performance and features (i.e., the size and depth of the tree)?

The illumination pattern shows more activity with larger and deeper trees (in general), as lighter colors are present in the top right corner of the activity grid.
The performance grid doesn't really correlate with either the two features, or the activity map. Most of the high scores are on the left side of the performance grid, with some exceptions.
This leads me to believe that it's not really the shape of the tree that matters, but the actual types of nodes it contains.

### Final Questions

 - Do you think there is a trade-off between quality and diversity, or one aspect is more important than the other? If so, which one, and in which circumstances?

I think there is a trade-off between quality and diversity, as the algorithm can't really explore the whole space, and it has to focus on the best areas. However, if it focuses too much on the best areas, it may miss completely the global best, and only focus on local optima.
 
 - In which kind of applications do you think that MAP-Elites (and quality-diversity algorithms in general) could be useful? Why?

I think MAP-Elites could be useful in applications where the search space is very large, and the fitness function isnt well defined. In this case, the algorithm may excel by exploring all the space, and find the best areas, without getting stuck in local optima.