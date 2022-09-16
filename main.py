from mimetypes import init
import random
import numpy as np
from main import *

k = 100  # population size


class Path():
    def __init__(self, path, total_fitness):
        self.path = path
        self.total_fitness = total_fitness

    def calc_fitness(self, inital_population):
        print("reached calc fitness")

        for i in range(k - 1):
            temp1 = objs[i].path
            temp2 = objs[i + 1].path[1]

            #print(temp1)
            #x = [int(i) for i in temp1]
            #print(x)
            #temp1 = temp1.split(" ")
            # print(temp1)


objs = [Path(None, None) for i in range(100)]  # global list of objects


class Population():
    def __init__(self, size, parents, best):
        self.size = size
        self.parents = parents
        self.best = best


def create_mating_pool(population, rank_list):
    matingPool = []
    # your code goes here
    return matingPool


def crossover(parent1, parent2, start_index, end_index):
    child = []
    # your code goes here

    return child
    #path1.fitness(path2)



def create_init_pop(size, cities):
    for i in range(k):
        np.random.shuffle(cities)
        #objs[i].path = cities 
        
        setattr(objs[i], 'path', list(cities))
        #print(objs[i].path)

    #print(objs[0].path)
    #print(objs[1].path)


# return score

def agent(size, cities):
    num_of_loc = size
    coordinates = cities
    init_pop = create_init_pop(size = num_of_loc, cities = coordinates)

    path = Path(init_pop, 0 )
    print(objs[0].path)
    print(objs[99].path)
    path.calc_fitness(init_pop)

    return 0


if __name__ == "__main__":
    # PASS IN INPUT.TXT

    input = []
    # input = np.zeros(0)
    f = open("Test_Cases/input.txt", 'r')
    for x in f:
        x = x.strip()
        #temp = []
        #temp = x.split(" ")

        #x = [int(i) for i in temp]
        #print(temp)
        input.append(x)
    input = input[1:]
    input = np.asarray(input)
    #print((input))
    agent(size=len(input), cities=input)

    # agent(input)