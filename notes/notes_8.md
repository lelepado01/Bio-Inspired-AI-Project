# Lab 8

## Ex1

For the OR problem, the MSE is very low: 0.0014190444755019928

Try running the code again after changing ``problem_class`` to ``Xor``.
- Can you solve it? If you are unable to solve it, why is that?

For XOR, the MSE is very high: 0.6681554582717202
It means that the network is not able to solve the problem, as the average error is more than 0.5.

- Does this allow you to solve the problem? What if you change this value to 2 or more?

Increasing the number of hidden units to 2, the fitness returns very low: 0.0038413472304833123.

- How many hidden nodes are required to solve this problem? Can you provide an explanation for why that is the case?

The problem is not linearly separable, so at least 2 hidden nodes are required to solve it. The reason is that the network needs to be able to separate the two classes of the problem.

## Ex2

Run the jupyter block code to solve ``Temporal Or``.
- Can you solve it? If you are unable to solve it, why is that?

The problem is not solved, as the average error is more than 0.5. The reason is that the network is not able to remember the previous states.

- If you set ``recurrent`` to be ``True``, can you now evolve a successful network?

Yes, the network develops a recurrent layer and fitness is lower.

- Why might recurrence be important for solving a temporal problem such as this?

Recurrence is important because it allows the network to remember the previous states. In this way, the network can learn the temporal pattern of the problem.

- Do the same EA parameters that solved ``Temporal Or`` also work for ``Temporal And``?

Yes

- Why, or why not?

The reason is that the two problems are very similar, so the same parameters are able to solve both of them.

- Are you able to find a successful network?

Yes, the network is able to solve the problem.
(using 100 max generations)

- If not, think back to what you just saw in the previous exercise. What combination of recurrence and no. of hidden nodes is needed to solve ``Temporal Xor`` and why is that?

Temporal Xor is not solved, by adding another hidden layer the problem is solved.
Although the fitness is still decreasing, so it may help to increase the number of generations.
With 200 the problem is solved.

## Ex3

- First, run a single instance of each of the two configurations (with/without elitism, simply change ``config_files[0]`` to ``config_files[1]``). What do you observe? 

Without elitism, the fitness is lower but the network is able to solve the problem.

Output:
input (0.0, 0.0), expected output (0.0,), got [0.038508139628068185]
input (0.0, 1.0), expected output (1.0,), got [0.8295829954299518]
input (1.0, 0.0), expected output (1.0,), got [0.9999790089941012]
input (1.0, 1.0), expected output (0.0,), got [0.28866452968971507]

With elitism, the network is still able to solve the problem. With a better fitness.

Output:
input (0.0, 0.0), expected output (0.0,), got [6.43450722452155e-05]
input (0.0, 1.0), expected output (1.0,), got [0.8670940124357195]
input (1.0, 0.0), expected output (1.0,), got [0.997066100187981]
input (1.0, 1.0), expected output (0.0,), got [0.020836081080091905]

- Is the algorithm without elitism able to converge to the optimal fitness value? What about the algorithm with elitism? 

Elitism improves the algorithm, as it is able to converge to a better fitness value.

- What is the effect of elitism on convergence? What about the number of species and their dynamics?

The number of species is much lower with elitism. Especially when the number of generations is high, the number of species remains very low.

- Change the parameter ``num_runs`` to $10$ or more. Does the boxplot confirm -in statistical terms- what you observed on a single run? (**NOTE**: it takes 1-2 minutes to execute 10 runs for both configurations.)

Yes, with elitism the fitness is much higher.

## Ex4 

- What do you observe in this case when you execute a single run of each configuration?

The algorithm is able to solve the problem, as the output is correct.
In 2000 generations, however.

Output:
input (0.0, 0.0, 0.0), expected output (0.0,), got [0.08675566809795467]
input (0.0, 0.0, 1.0), expected output (1.0,), got [0.9999999999148392]
input (0.0, 1.0, 0.0), expected output (1.0,), got [0.9327663001376818]
input (0.0, 1.0, 1.0), expected output (0.0,), got [5.2336810448783857e-08]
input (1.0, 0.0, 0.0), expected output (1.0,), got [0.9987713931853373]
input (1.0, 0.0, 1.0), expected output (0.0,), got [1.3880506980914702e-16]
input (1.0, 1.0, 0.0), expected output (0.0,), got [1.6293897863249507e-11]
input (1.0, 1.0, 1.0), expected output (0.0,), got [2.7329572962435886e-15]

- What is the effect of using hidden nodes in the initial population?

The effect is that the algorithm is able to solve the problem much quicker.
Even after 100 generations, the algorithm is able to solve the problem.

Output:
input (0.0, 0.0, 0.0), expected output (0.0,), got [0.5858232151486494]
input (0.0, 0.0, 1.0), expected output (1.0,), got [0.5857355521040126]
input (0.0, 1.0, 0.0), expected output (1.0,), got [0.5857883659533609]
input (0.0, 1.0, 1.0), expected output (0.0,), got [0.05445225611910085]
input (1.0, 0.0, 0.0), expected output (1.0,), got [0.9404258907947931]
input (1.0, 0.0, 1.0), expected output (0.0,), got [0.007003077051286871]
input (1.0, 1.0, 0.0), expected output (0.0,), got [0.009910409385151862]
input (1.0, 1.0, 1.0), expected output (0.0,), got [0.005463187775378414]

- What happens when you configure the script to execute multiple runs? 

With hidden nodes, the fitness is much higher.

- Does the boxplot confirm -in statistical terms- what you observed on a single run? (**NOTE**: it takes 1-2 minutes to execute 10 runs for both configurations.)

Yes, the boxplot confirms that the algorithm with hidden nodes is able to solve the problem much quicker. (and achieve a better fitness)

## Final Questions

- What is the genotype and what is the phenotype in the problems considered in this lab?

The genotype can be considered as the weights of the neural network. The phenotype is the output of the neural network. 

- Why are hidden nodes sometimes needed for a Neural Network to solve a given task? 

Hidden nodes are needed to solve the task when it is not linearly separable. 
Or when the problems becomes too complex to be solved with a single layer.

- What is the defining feature of problems that networks without hidden nodes are unable to solve? 

The defining feature is that the problem is not linearly separable.

- Why are recurrent connections needed to solve certain problems? 

Recurrent connections are needed to solve certain problems because they allow the network to have a memory of the previous states. 
Having a recurrent connection allows the network to have a memory of the previous states.

- What is the defining feature of problems that networks without recurrent connections are unable to solve? 

The defining feature is that the problem requires memory of previous states to be solved (for example language comprehension).

- Are there problems that require recurrent connections and multiple hidden nodes?

Yes, there are problems that require recurrent connections and multiple hidden nodes. For example, NLP tasks are computationally intensive tasks that require both recurrent connections and multiple hidden nodes.