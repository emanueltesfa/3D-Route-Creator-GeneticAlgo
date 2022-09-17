from mimetypes import init
import random
import numpy as np
from main import *

k = 100  # population size


class Path():
    def __init__(self, path, path_cost, fitness):
        self.path = path
        self.path_cost = path_cost
        self.fitness = fitness

    def calc_fitness(self, inital_population):
        # (change to string )
        final = []
        dist_arr = []

        # print(objs[0].path)
        for i in range(k):
            temp = objs[i].path
            mid_store = []
            for j in range(len(temp)):
                mytuple = list(map(int, temp[j].split(' ')))
                mid_store.append(mytuple)
            final.append(mid_store)
        # print(final[0][0][0])
        total_cost = 0.00
        for i in range(k):
            # print(len(point1))
            dist = 0.0000000

            #print(f"set {i} of 100")
            for j in range(len(final[i])-1):
                point1 = np.asarray(final[i][j])
                point2 = np.asarray(final[i][j+1])
                #print("Point1 is ", point1, " \n Point2 is ", point2)
                dist += np.linalg.norm(point1 - point2)
                #print("distance is ", dist)
                #total_cost += (1/dist)
            dist_arr.append(dist)
            setattr(objs[i], "path_cost", (dist))
            total_cost += 1 / dist
        print("total cost of generation is: ", total_cost)
        # total_cost = 1 / total_cost
        delete_count = 0.000
        delete_fitness = 0.00
        for i in range(k):

            fitness = (1 / objs[i].path_cost) / total_cost
            setattr(objs[i], "fitness", fitness)

            delete_count += objs[i].path_cost
            delete_fitness += fitness
            #print(total_cost, objs[i].path_cost, fitness)
        # print(delete_fitness)
        # print(dist_arr)
        #
        #x = [int(i) for i in temp1]
        #temp1 = temp1.split(" ")


objs = [Path(None, None, None) for i in range(100)]  # global list of objects


class Population():
    def __init__(self, size, parents, best):
        self.size = size
        self.parents = parents
        self.best = best


def create_mating_pool(population, rank_list):
    matingPool = []

    max = sum([c.fitness for c in population])
    print("Max is ", max)
    selection_probs = [c.fitness/max for c in population]
    return population[np.random.choice(len(population), p=selection_probs)]

 # return matingPool


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
    init_pop = create_init_pop(size=num_of_loc, cities=coordinates)
    path = Path(init_pop, 0.00, 0.00)
    path.calc_fitness(init_pop)
    objs.sort(key=lambda x: x.path_cost)
    idk = create_mating_pool(objs, None)
    print("idk is: ", idk.path, "\n Path cost is: ",
          idk.fitness, "\n Fitness is: ", idk.fitness)
    dist = 0.00
    for j in range(len(idk)-1):
        point1 = np.asarray(idk[j])
        point2 = np.asarray(idk[j+1])
        #print("Point1 is ", point1, " \n Point2 is ", point2)
        dist += np.linalg.norm(point1 - point2)
    print(dist)


def parse_input():
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
        # print(temp)
        input.append(x)
    input = input[1:]
    input = np.asarray(input)
    # print((input))
    agent(size=len(input), cities=input)

    # agent(input)
