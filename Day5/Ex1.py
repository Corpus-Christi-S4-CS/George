import numpy as np
import random

def mutation(child):

    mutationPoint = random.randint(0, len(parent1))

    if child[mutationPoint] == 1:

        child[mutationPoint] = 0

    elif child[mutationPoint] == 0:

        child[mutationPoint] = 1
    
    return child

def crossover(parent1, parent2):

    crossoverPoint = random.randint(0, len(parent1))

    child1 = np.concatenate((parent1[:crossoverPoint], parent2[crossoverPoint:]))
    child2 = np.concatenate((parent2[:crossoverPoint], parent1[crossoverPoint:]))

    return child, child2

parent1 = np.array([0, 0, 1, 0, 1, 0])
parent2 = np.array([1, 1, 1, 0, 0, 1])

crossoverPoint = random.randint(0,5)

child1 = np.concatenate((parent1[:crossoverPoint],parent2[crossoverPoint:]))
child2 = np.concatenate((parent1[crossoverPoint:],parent2[:crossoverPoint]))

print(child1)
print(child2)