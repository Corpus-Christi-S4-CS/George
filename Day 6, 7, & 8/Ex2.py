import numpy as np

inputArray = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
outputArray = np.array([0, 1, 1, 0])

synapticWeights = np.random.uniform(-1, 1, 3)

def sigmoid(x):

    return 1 / (1 + np.exp(-x))

def derivativeSigmoid(x):

    return sigmoid(x) * (1 - sigmoid(x))

for x in range(5):

    initOutput = np.dot(inputArray,synapticWeights)
    output1 = sigmoid(initOutput)
    error = outputArray - output1
    gradient = np.dot(inputArray.T, error*derivativeSigmoid(initOutput))
    synapticWeights += gradient

situation = np.array([1, 0, 0])
output2 = sigmoid(np.dot(situation, synapticWeights))
print(output2)