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

        for i in range(k):
            temp = objs[i].path
            mid_store = []
            for j in range(len(temp)):
                mytuple = list(map(int, temp[j].split(' ')))
                mid_store.append(mytuple)
            final.append(mid_store)
        # (final[0][0][0])
        total_cost = 0.00
        for i in range(k):
            dist = 0.0000000
            for j in range(len(final[i])-1):
                point1 = np.asarray(final[i][j])
                point2 = np.asarray(final[i][j+1])
                dist += np.linalg.norm(point1 - point2)

            dist_arr.append(dist)
            objs[i].path_cost = dist
            #setattr(objs[i], "path_cost", dist)
            total_cost += 1 / dist

        for i in range(k):
            fitness = (1 / objs[i].path_cost) / total_cost
            setattr(objs[i], "fitness", fitness)


objs = [Path(None, None, None) for i in range(100)]  # global list of objects


class Population():
    def __init__(self, size, parents, best):
        self.size = size
        self.parents = parents
        self.best = best


def create_mating_pool(population, rank_list):
    max = sum([c.fitness for c in population])
    selection_probs = [c.fitness/max for c in population]
    return population[np.random.choice(len(population), p=selection_probs)]

 # return matingPool


def crossover(parent1, parent2, start_index, end_index):
    # parent1 = [120 199 34], [137 199 93], [199 173 30], [144 39 130], [175 53 76], [153 196 97], [173 101 186]
    child = []

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
          idk.path_cost, "\n Fitness is: ", idk.fitness)


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
