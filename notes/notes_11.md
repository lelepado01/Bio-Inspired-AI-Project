
# Lab 11

### Ex1

- Is the GP algorithm able to approximate the given polynomial, with the standard configuration? 

It seems the algorithm is able to approximate the given polynomial, as the fitness approaches 0.0 after 10 generations.

- What happens when you run the script multiple times? Do you always obtain the same results, or not? Why?

The results are not always the same, as the algorithm is stochastic. But it seems it is always able to approximate the given polynomial.
The reason might be this is a simple problem, and the algorithm is able to find the correct solution in a few generations.
    
- Try to change the generator function (e.g. to include trigonometric functions) defined in the method `generatorFunction`. Is the GP algorithm able to approximate more complicated generator functions? 

The algorithm is able to approximate trigonometric generator functions, and it can find some very quickly (5 generations). 
(math.sin(x)+math.cos(x)) -> almost perfectly
(math.sin(x)*x**2) -> the two functions are very different
(math.sin(x)+5*x**2) -> the two functions almost overlap

- Which parameters can you change to improve the results?

Taking into consideration: 
math.sin(x)*x**2

Increasing the mutation probability to 0.5 seems to improve the results, as the fitness approaches 0.0 after less than 5 generations.

### Ex2

- What kind of performance do you get, in general, on the tested problems? 

On the parity problem, the algorithm is able to find the correct solution in around 25 generations, with a fitness of 0.0. (6 inputs)

On the spam problem, the algorithm is not able to find the correct solution, and the fitnesss hovers around 150.

- What happens when you change the parametrization of GP? 

On the parity problem: 
By increasing the number of inputs to 10, the algorithm is far from finding the correct solution, and has considerably slowed down, taking around 15 seconds to execute 40 generations.

On the spam problem: 
Even increasing max generations to 100 and population size to 150, the algorithm is not able to find the correct solution, and fitness keeps increasing.

### Final Questions

 - What are the main strengths and limitations of GP, in your opinion?
 
 The main limitation of GP is the computational cost, as it is very slow and trees can become increasingly larger and more complex.
 This is such an issue that many reasearchers have tried to find ways to reduce the size of these trees (bloat).

 The main strength of GP is that it is a very flexible algorithm, and can be used to solve a wide variety of problems, and is especially performant when having to deal with mathematical functions.

 - In which kind of applications do you think that GP could be more useful than other kinds of black-box Machine Learning techniques, such as Neural Network? Why?

GP could be more useful than Neural Networks when the problem is not well defined, and the solution is not clear, as it might be able to find a solution without having to define the problem in a very specific way.