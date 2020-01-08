# Train a neural network to classify two clusters and
# Create the random points with a line
# This will be modelled after a Logical AND structure (separates points)

import numpy as np


class Perceptron:  # takes inputs and weights as vectors

    # Constructor takes in no. of inputs and wieghts matrix
    def __init__(self, input_length, weights=None):
        if weights is None:
            self.weights = np.ones(input_length) * 0.5
        else:
            self.weights = weights  # Initialize the weights

    @staticmethod  # can be used without making an object
    def unit_step_function(x):
        if x > 0.5:  # if the weighted sum hits threshold
            return 1
        return 0  # has not met standard

    def __call__(self, in_data):  # driver method
        weighted_input = self.weights * in_data
        weighted_sum = weighted_input.sum()  # sum weighted
        return Perceptron.unit_step_function(weighted_sum)


p = Perceptron(2, np.array([0.5, 0.5]))

data_in = np.empty((2,))
for in1 in range(2):  # These two loops iterate values
    for in2 in range(2):
        data_in = (in1, in2)
        data_out = p(data_in)
        print(data_in, data_out)

# Now we can make our Decision Boundary that will be trained
# to classify different data that we give it. Think of the
# Decision boundary like a line that passes throughout the origin.
# Eventually a Bias can be added.

import numpy as np
from collections import Counter


class Perceptron:

    def __init__(self, input_length, weights=None):
        if weights == None:  # if weights are not specified
            # create random weights
            self.weights = np.random.random((input_length)) * 2 - 1
        self.learning_rate = 0.1

    @staticmethod
    def unit_step_function(x):
        if x < 0:
            return 0
        return 1

    def __call__(self, in_data):
        weighted_input = self.weights * in_data
        weighted_sum = weighted_input.sum()
        return Perceptron.unit_step_function(weighted_sum)

    # now initiate the learning phase
    def adjust(self,
               target_result,
               calculated_result,
               in_data):
        error = target_result - calculated_result

        # geometric sequence that is eventually reaches the target
        for i in range(len(in_data)):
            # multiply the data value by its error
            # Do this gradually at the learning rate desired
            correction = error * in_data[i] * self.learning_rate
            self.weights[i] += correction


def above_line(point, line_func):  # Determine if the threshold is met
    x, y = point
    if y > line_func(x):
        return 1
    else:
        return 0


# initialize random test data
points = np.random.randint(1, 100, (100, 2))
p = Perceptron(2)  # make a perceptron with 2 inputs


def lin1(x):  # random line to start with
    return x + 4


for point in points:  # begin the adjustment of the decision boundary
    p.adjust(above_line(point, lin1),  # target result
             p(point),  # result calculated
             point)  # data to pass in

evaluation = Counter()
for point in points:
    if p(point) == above_line(point, lin1):
        evaluation["correct"] += 1
    else:
        evaluation["wrong"] += 1
print(" ")
print("Adjusted Trials results:")
print(evaluation.most_common())
