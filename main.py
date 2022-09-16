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
        # (change to string )
        final =  []
        dist_arr = []

        #print(objs[0].path)
        for i in range(100):
            temp = objs[i].path
            mid_store = []
            for j in range(len(temp)):
                mytuple = list(map(int, temp[j].split(' ')))
                mid_store.append(mytuple)
            final.append(mid_store)
        #print(final[0][0][0])
        
        for i in range(k):
            #print(len(point1))
            dist = 0.0000000
           
            print(f"set {i} of 100")
            for j in range(len(final[i])-1):
                point1 = np.asarray(final[i][j])
                point2 = np.asarray(final[i][j+1])
                #print("Point1 is ", point1, " \n Point2 is ", point2)
                dist += np.linalg.norm(point1 - point2)
                #print("distance is ", dist)
            dist_arr.append(dist)
            setattr(objs[i], "total_fitness", dist)
        print(dist_arr)

 
            #x = [int(i) for i in temp1]
            #temp1 = temp1.split(" ")


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


def create_init_pop(size, cities):
    for i in range(k):
        np.random.shuffle(cities)
        setattr(objs[i], 'path', list(cities))

# return score

def agent(size, cities):
    num_of_loc = size
    coordinates = cities
    init_pop = create_init_pop(size = num_of_loc, cities = coordinates)

    path = Path(init_pop, 0 )
    #print(objs[0].path)
    #print(objs[99].path)
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