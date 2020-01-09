# Neural Networks 
This is a basic tutorial/implementation for a Neural network.

Includes:
1. A Line separation tutorial to explain a Decision Boundary 
2. Functional Neural Network using random data and weights
3. Neural Network that uses a Bias Factor as a parameter 
### Breakdown: Simple Neural Network (Linearly Separable)
Abstracted: Neural Networks are modelled after Neurons
defined in neuroscience.

This involves an series of inputs to a neuron. The inputs
are multiplied by a weight which will map them to a new value.
These weights are continuously adjusted during the Learn Phase. 

The new values are summed and a Bias Value may be added to
the sum. The Bias could be thought of as an extra input 
parameter to reach the new threshold of classification.

The weighted sum is mapped through an activation function 
(Sigmoid, Relu ... etc) that is typically Binary (1 || 0).
Ex. If the summation is > a certain threshold -> 1

After combining many layers beyond the input function,
a classification can be made based on the original inputs.

### Breakdown: Neural Network (Not Linearly Separable)
    
Once we start dealing with clusters of data that cannot be separated linearly, we need to introduce "Hidden Layers".
This is adding a level of neurons. 
    
Adapted from: https://www.python-course.eu/neural_networks.php
