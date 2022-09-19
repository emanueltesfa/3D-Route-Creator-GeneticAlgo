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
        print("in calc fitness")
        # (change to string )
        dist_arr = []
        # (final[0][0][0])
        total_cost = 0.00
        for i in range(k):
            dist = 0.0000000

            for j in range(len(objs[i].path)-1):
                point1 = np.asarray(objs[i].path[j])
                point2 = np.asarray(objs[i].path[j+1])
                #print("point 1 is :", (point1), "point 2 is: ", point2)
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


def create_mating_pool(population, rank_list):
    max = sum([c.fitness for c in population])
    selection_probs = [c.fitness/max for c in population]
    return (population[np.random.choice(len(population), p=selection_probs)]).path

 # return matingPool


def crossover(parent1, parent2, start, end, size):
    # parent1 = [120 199 34], [137 199 93], [199 173 30], [144 39 130], [175 53 76], [153 196 97], [173 101 186]
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
    offspring_paths += [_cross1]

    # print("\nParent 1: ", _parent, "\n_Sub arr", _sub, "\nParent 2: ", _parent2,  "start  : ", start,
    #     "end: ", end, "\nleft side: ", _left, "\nRight side: ", _right, "\nFinal Offspring: ", _cross1)

    sub = parent1[start:end]
    left, right = [], []
    left = parent2[:start]
    right = parent2[end:]
    cross1 = [*left, *sub, *right]
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

    for y in range(k):
        path.calc_fitness()
        objs.sort(key=lambda x: x.path_cost)

        parents, offspring, mom, dad = [], [], [], []

        for j in range(10):
            mom = create_mating_pool(objs, None)
            dad = create_mating_pool(objs, None)
            # print(type(mom))
            parents.append(mom)
            parents.append(dad)

        # print(len(parents))
        offspring += parents
        for i in range(len(parents) - 1):
            for j in range(int((len(parents) - 1)/6)):
                rand = random.randint(1, size - 3)
                rand_temp = random.randint(rand + 1, size - 2)

                offspring += crossover(parents[i],
                                       parents[j], rand, rand_temp, size)

        #print("Offspring is: ", len(offspring))

        # print("objs before is: ", objs[i].path)
        if y != (k-1):
            for i in range(k):
                #objs[i].path, objs[i].path_cost, objs[i].fitness = None, None, None
                objs[i].path = offspring[i]

        for i in range(k):
            print(f"{y}   {i} objs is: ",
                  objs[i].path, "Cost is: ", objs[i].path_cost)


if __name__ == "__main__":
    # PASS IN INPUT.TXT
    input = []
    f = open("Test_Cases/input.txt", 'r')
    for x in f:
        x = x.strip()
        input.append(x)
    input = input[1:]
    input = np.asarray(input)

    final = []
    for j in range(len(input)):
        mytuple = list(map(int, input[j].split(' ')))
        final.append(mytuple)
    Agent(size=len(final), cities=final)
