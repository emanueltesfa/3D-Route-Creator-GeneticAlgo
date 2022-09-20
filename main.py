# must be one file for submission purposes
# 10% of population is used to create next genetation

# Posible issues
#  - selection process of mates
#  - crossover


# Next steps
#  - create evolution loop
#  - for crossover loop until 100
#  -  if( any path used twice) then (compare to input)
#  - append first to end

"""if offspring[0] == offspring[len(offspring)-1]:
        print("end matches beginning")

    else:
        print("change end element")"""

from itertools import permutations
import random
import numpy as np
from main import *
import copy as cp

k = 100  # population size


class Path():
    def __init__(self, path, path_cost, fitness):
        self.path = path
        self.path_cost = path_cost
        self.fitness = fitness

    def calc_fitness(self):
        # print("in calc fitness")
        # (change to string )
        dist_arr = []
        # (final[0][0][0])
        total_cost = 0.00
        for i in range(k):
            dist = 0.0000000

            for j in range(len(objs[i].path)-1):
                point1 = np.asarray(objs[i].path[j])
                point2 = np.asarray(objs[i].path[j+1])
                # print("point 1 is :", (point1), "point 2 is: ", point2)
                dist += np.linalg.norm(point1 - point2)
            dist_arr.append(dist)
            objs[i].path_cost = dist
            total_cost += 1 / dist

        for i in range(k):
            fitness = (1 / objs[i].path_cost) / total_cost
            setattr(objs[i], "fitness", fitness)
            # print("path is", "path cost is",
            #    objs[i].path_cost, "fitness is", objs[i].fitness)


objs = [Path(None, None, None) for i in range(100)]  # global list of objects


class Population():
    def __init__(self, size, parents, best):
        self.size = size
        self.parents = parents
        self.best = best


def mating_pool_two(population):
    new_parents = []  # this is 10% of pop
    population.sort(key=lambda x: x.path_cost)
    for i in range(10):
        print(objs[i].path_cost)
        new_parents.append(objs[i].path)
        objs.pop(i)
    return new_parents

 # return matingPool


def check_chromosome_validity(offspring, parent):
    temp = offspring
    bool_arr_parent = [False for i in range(len(parent))]

    permutation, unique_indices = np.unique(temp, axis=0, return_index=True)
    unique_indices.sort()
    print(unique_indices)

    # i want ... all indicies that need to repalced from parent to be false if they are missing in offspring
    for item in range(len(parent)):
        if parent[item] in offspring:  # if crossover array elem is in parent
            bool_arr_parent[item] = True
        else:
            bool_arr_parent[item] = False

    # given all indexs that need to be replace (indicies)
    # iterate to each
    # check bool_parent_arr and which ever is first false(not used)
    # get index from above and swap with parent[i]
    # change bool to true

    for i in range(len(parent)):
        print("hi")
        if i not in unique_indices:
            # print("i is: ", i)
            print("gello")
            for j in range(len(bool_arr_parent)): # lin searc for first bool that is false ie. parent that hasn't been used
                if bool_arr_parent[j] == False: # 
                    print("how are we")
                    # print("j is ", j)
                    offspring[i] = parent[j] # change offspring at index where it isn't a unique index
                    bool_arr_parent[j] = True # update the bool_arr to ensure same parent path isnt appeneded twice

    perm, ind = np.unique(offspring, axis=0, return_index=True)
    ind.sort()
    print("Indexs that are valid after function: ", len(ind)) # should be all 50 indicies 

    # print("\n Bool arr ", *bool_arr_parent)


def crossover(parent1, parent2, start, end, size):
    # parent1 = [120 199 34], [137 199 93], [199 173 30], [144 39 130], [175 53 76], [153 196 97], [0
    # start = 2 && end = 6
    # size = 7 ,, 0 - 6
    # sub = [199 173 30], [144 39 130], [175 53 76], [153 196 97], [173 101 186]

    # should equal 100
    # start off with 10 from pop
    # crossover makes 20 = 2 * 10 pop
    # loop till len(offspring_paths) = 20

    # loop path of len = 5 (which is 5 pairs = 10)
    # randomize indexs 5 times

    offspring_paths = []
    # while len(offspring_paths) > 20:
    _parent = parent1
    _parent2 = parent2

    _sub = _parent[start:end]
    _left, _right = [], []
    _left = _parent2[:start]
    _right = _parent2[end:]
    _cross1 = [*_left, *_sub, *_right]
    check_chromosome_validity(_cross1, parent1)
    offspring_paths += [_cross1]

    # print("\nParent 1: ", _parent, "\n_Sub arr", _sub, "\nParent 2: ", _parent2,  "start  : ", start,
    #     "end: ", end, "\nleft side: ", _left, "\nRight side: ", _right, "\nFinal Offspring: ", _cross1)

    sub = parent1[start:end]
    left, right = [], []
    left = parent2[:start]
    right = parent2[end:]
    cross1 = [*left, *sub, *right]
    #check_chromosome_validity(cross1, parent1)

    offspring_paths += [cross1]

 # print to see parent and offspring
    # print("\nParent 1: ", _parent, "\nParent 2: ",
    # _parent2,  "\nFinal Offspring: ", offspring_paths)
    # print(offspring_paths)
    return offspring_paths


def create_init_pop(size, cities):
    for i in range(k):
        np.random.shuffle(cities)
        setattr(objs[i], 'path', list(cities))

# return score


def Agent(size, cities):
    num_of_loc = size
    coordinates = cities
    init_pop = create_init_pop(size=num_of_loc, cities=coordinates)
    path = Path(init_pop, 0.00, 0.00)

    for y in range(3):
        path.calc_fitness()
        objs.sort(key=lambda x: x.path_cost)

        offspring, mom, dad = [], [], []

        mom = [x.path for x in objs[:10]]
        dad = [x.path for x in objs[10:20]]
        # print(len(mom))
        # parents.append(mom)
        # parents.append(dad)

        # print(len(mom)+len(dad) - 1)
        offspring += mom
        offspring += dad
        for i in range(len(mom)):
            for j in range(len(dad)):
                rand = random.randint(1, size - 3)
                rand_temp = random.randint(rand + 1, size - 2)

                offspring += crossover(mom[i],
                                       dad[j], rand, rand_temp, size)

        # print("Offspring is: ", (offspring))
        temp_arr = np.asarray(offspring)
        # print(temp_arr.shape)
        # print(len(objs))

        # print("objs before is: ", objs[i].path)
        if y != (k-1):
            for item in range(k):
                # objs[i].path, objs[i].path_cost, objs[i].fitness = None, None, None
                objs[item].path = offspring[item]

        # or i in range(k):
        print(f"{y} Cost is: ", objs[0].path_cost)
    return objs


if __name__ == "__main__":
    # PASS IN INPUT.TXT
    input = []
    f = open("input.txt", 'r')
    for x in f:
        x = x.strip()
        input.append(x)
    input = input[1:]
    input = np.asarray(input)
    f.close()
    final = []
    for j in range(len(input)):
        mytuple = list(map(int, input[j].split(' ')))
        final.append(mytuple)
    population = Agent(size=len(final), cities=final)

    # print((objs[0].path_cost))
    # print((population[0].path_cost))
    output = open("output.txt", "w")
    for item in range(len(objs[0].path)):

        temp = objs[0].path[item]
        listToStr = ' '.join([str(item) for item in temp])
        # print(type(listToStr))
        # output.write(" ")
        # output.write(str(objs[0].path_cost))
        output.write(listToStr)
        if item != (len(objs[0].path) - 1):
            output.write("\n")

    output.close()
    # for i in range(k):
