import numpy as np

parent1 = np.array([0,0,1,0,1,0])
parent2 = np.array([1,1,1,0,0,1])

best_value = -1000

def crossover(parent1, parent2):
    cp = np.random.randint(0,len(parent1))
    child1 = np.concatenate((parent1[:cp], parent2[cp:]))
    child2 = np.concatenate((parent2[:cp], parent1[cp:]))
    return child1, child2

def mutation(child):
    mp = np.random.randint(0,len(parent1))
    if child[mp]==1:
        child[mp]=0
    elif child[mp]==0:
        child[mp]=1
    return child

mutation_probability = 0.2
weights = np.array([1,2,3,4,5,6])
values =  np.array([2,4,4,5,7,9])

for i in range(50):

    child1, child2 = crossover(parent1, parent2)

    if np.random.uniform(0,1) < mutation_probability:
        child1 = mutation(child1)
    if np.random.uniform(0,1) < mutation_probability:
        child2 = mutation(child2)

    weight1 = np.sum(child1*weights)
    weight2 = np.sum(child2*weights)

    if weight1 <= 10:
        value1 = np.sum(child1*values)
        if value1>= best_value:
            best_value = value1
            best_child = child1

    if weight2 <= 10:
        value2 = np.sum(child2*values)
        if value2>= best_value:
            best_value = value2
            best_child = child2
    
    parent1, parent2 = child1, child2

    print("iteration: ",i, "best_value: ", best_value, "best_child: ", best_child)