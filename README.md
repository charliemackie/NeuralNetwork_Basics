# Neural Networks 
This is a basic tutorial/implementation for a neural network.
### Breakdown:
    Abstracted: Neural Networks are modelled after Neurons
    defined in neuroscience.
    
    This involves an series of inputs to a neuron. The inputs
    are multiplied by a weight which will map them to a new value.
    These weights are continuosly adjusted during the Learn Phase. 
 
    The new values are summed and a Bias Value may be added to
    the sum. The Bias could be thought of as an extra input 
    parameter to reach the new threshold of classification.
    
    The weighted sum is mapped through an activation function 
    (Sigmoid, Relu ... etc) that is typically Binary (1 || 0).
    Ex. If the summation is > a certian threshold -> 1
    
    After combining many layers beyond the input function,
    a classification can be made based on the original inputs.

Adapted from: https://www.python-course.eu/neural_networks.php
