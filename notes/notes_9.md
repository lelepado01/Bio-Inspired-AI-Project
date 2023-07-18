# Lab 9

### Ex1

- Is the Evolutionary Algorithm able to evolve a Neural Network controller that can reach the target? What kind of motion strategy does it use?

Yes, the evolutionary algorithm is able to evolve a Neural Network controller that can reach the target.
The motion strategy seems to be to do a full lap at the start, then go straight to the target.
By modifying some parameters, it is possible to make the robot go straight to the target, although it still takes a winding path.

- What is the minimum-complexity Neural Network controller that you can think of? Hint: think about the necessity of using all the available sensor inputs in this case, and if any of them can be discarded (see the configuration dictionary to disable inputs). Also, consider reducing the no. if hidden nodes and test different network configurations to identify the simplest controller.

the minimum-complexity Neural Network controller that I can think of is a controller with 3 input nodes, since we would need to test for the presence of walls only to the left and the right.

### Ex2

- Take the best Neural Network evolved in the previous exercise and run it in the new scenario, running the next cell.

The neural network is able to avoid walls, it however gets stuck in the long corridor section which results in a dead end.
This can be considered as analogous as finding a local minimum in a function. 
Maybe with a large enough mutation rate, the neural network would be able to get out of the local minimum, but I'm not sure this would be optimal for all other types of maps.

### Final Questions

- What do you think it could change between a simulated and a real-world experiment in the case of a maze navigation task?

The real world experiment would be more complex, since the robot would have to deal with real world physics, and the maze would be more complex.
Also we would have to deal with the fact that the robot might not be able to see the whole maze at once, or that the maze might change over time.

- Can you think of some possible applications where a maze navigation robot task could be used? Why would it make sense to use Swarm/Evolutionary Robotics in those cases?

A maze navigation robot could be used to navigate a warehouse, or a maze like structure in a mine.