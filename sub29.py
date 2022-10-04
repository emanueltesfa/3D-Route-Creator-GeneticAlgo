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
import copy as cp
import time

k = 180  # population size


class Path():
    def __init__(self, path, path_cost, fitness):
        self.path = path
        self.path_cost = path_cost
        self.fitness = fitness

    def calc_fitness(self):
        dist_arr = []
        total_cost = 0.00
        for i in range(k):
            dist = 0.0000000
            for j in range(len(objs[i].path)-1):
                point1 = np.asarray(objs[i].path[j])
                point2 = np.asarray(objs[i].path[j+1])
                dist += np.linalg.norm(point1 - point2)
            dist_arr.append(dist)
            objs[i].path_cost = dist
            total_cost += 1 / dist

        for i in range(k):
            fitness = (1 / objs[i].path_cost) / total_cost
            setattr(objs[i], "fitness", fitness)


objs = [Path(None, None, None) for i in range(k)]  # global list of objects


class Population():
    def __init__(self, size, parents, best):
        self.size = size
        self.parents = parents
        self.best = best


def create_init_pop(size, cities):
    for i in range(k):
        np.random.shuffle(cities)
        temp_cities = cp.deepcopy(cities)
        temp_cities.append(cities[0])
        setattr(objs[i], 'path', list(temp_cities))
    # define set gloabally


def nn(size, cities):
    init_pop = []

    for j in range(size):
        if len(cities) == 0:
            break
        # calc closest city
        temp_list = []
        nn_dist = 0.0
        nn_path = []
        pop_index = None
        for i in range(size):
            size_city = len(cities)
            if i >= size_city:
                break
            dist = 0.000
            if len(init_pop) != 0:
                point1 = init_pop[-1]
            else:
                point1 = np.asarray(cities[j])
            point2 = np.asarray(cities[i])

            if i == 0 and j == 0:
                temp_list.append(point1)
                init_pop.append(list(point1))
                nn_path = list(point1)

            dist += np.linalg.norm(point1 - point2)
            if i == 1 or i == 0:
                nn_dist = dist
                if len(cities) > 1:
                    nn_path = list(cities[1])
                else:
                    nn_path = list(cities[0])

            if nn_dist >= dist:
                nn_path = cities[i]
                nn_dist = dist
                pop_index = i

        temp_list.append(nn_path)

        init_pop.append(list(nn_path))
        cities.pop(pop_index)
        if j == 0:
            cities.pop(0)
        size1 = len(cities)
    init_pop.append(init_pop[0])
    return init_pop


def check_chromosome_validity(offspring, parent):

    temp_offspring = offspring[:-1]
    temp_parent = parent[:-1]
    bool_arr_parent = ["F" for i in range(len(temp_parent))]
    permutation, indices = np.unique(
        temp_offspring, axis=0, return_index=True)
    indices.sort()

    for item in range(len(temp_parent)):
        if temp_parent[item] in temp_offspring:  # if crossover array elem is in parent
            bool_arr_parent[item] = "T"
        else:
            bool_arr_parent[item] = "F"

    for i in range(len(temp_parent)):
        if i not in indices:

            for j in range(len(bool_arr_parent)):
                if bool_arr_parent[j] == "F":
                    temp_offspring[i] = list(temp_parent[j])
                    bool_arr_parent[j] = "T"
                    break
    temp_offspring.append(temp_offspring[0])
    return temp_offspring


def crossover(parent1, parent2, start, end):
    offspring_paths = []
    _parent = parent1
    _parent2 = parent2

    if parent1 != parent2:
        _sub = _parent[start:end]
        _left, _right = [], []
        _left = _parent2[:start]
        _right = _parent2[end:]
        _cross1 = [*_left, *_sub, *_right]
        _cross1[-1] = _cross1[0]
        _cross1 = check_chromosome_validity(_cross1, parent1)
        offspring_paths += [_cross1]
    else:
        _parent2 = mutation(parent2)
        _sub = _parent[start:end]
        _left, _right = [], []
        _left = _parent2[:start]
        _right = _parent2[end:]
        _cross1 = [*_left, *_sub, *_right]
        _cross1[-1] = _cross1[0]
        _cross1 = check_chromosome_validity(_cross1, parent1)
        offspring_paths += [_cross1]

    if parent1 != parent2:
        sub = parent1[start:end]
        left, right = [], []
        left = parent2[:start]
        right = parent2[end:]
        cross1 = [*left, *sub, *right]
        cross1[-1] = cross1[0]
        cross1 = check_chromosome_validity(cross1, parent1)
        offspring_paths += [cross1]

    else:
        parent2 = mutation(parent2)
        sub = parent1[start:end]
        left, right = [], []
        left = parent2[:start]
        right = parent2[end:]
        cross1 = [*left, *sub, *right]
        cross1[-1] = cross1[0]
        cross1 = check_chromosome_validity(cross1, parent1)
        offspring_paths += [cross1]

        return offspring_paths
    return offspring_paths


def mutation(parent):
    rand1 = random.randint(0, len(parent) - 3)
    rand2 = random.randint(rand1 + 1, len(parent) - 1)


    # Swap indicies
    if (np.random.randint(0, 2) == 0):

        temp = parent[rand1]
        parent[rand1] = parent[rand2]
        parent[rand2] = temp

    # Permutation 
    else:
        offspring = np.random.permutation(parent[rand1:rand2])
        parent[rand1:rand2] = [list(x) for x in offspring]

    return parent



def Agent(size, cities):
    print(size)
    num_of_loc = size
    coordinates = cities
    init_pop = create_init_pop(size=num_of_loc, cities=coordinates)
    path = Path(init_pop, 0.00, 0.00)
    
    if size < 52:
        temp_size = k * 2

    else:
        temp_size = k

    for y in range(int(k/6)):
        path.calc_fitness()
        objs.sort(key=lambda x: x.path_cost)

        offspring, mom, dad = [], [], []

        mom = [x.path for x in objs[:15]]
        dad = [x.path for x in objs[15:30]]

        neighbor = nn(size, list(cities))
   
        offspring.append(neighbor)


        # PUT MOM AND DAD THROUGH VALDIATION

        offspring += mom
        offspring += dad

        for i in range(len(mom)):

            rand = random.randint(1, size - 3)
            rand_temp = random.randint(rand + 1, size - 2)
            offspring += crossover(mom[i],
                                    dad[len(mom) - i -1], rand, rand_temp)
            offspring += crossover(mom[i],
                                    dad[i], rand, rand_temp)
            offspring += crossover(mom[len(mom) - i- 1],
                                    dad[i], rand, rand_temp)
            offspring += crossover(mom[len(mom) - i- 1],
                                    dad[len(mom) - i- 1], rand, rand_temp)

            temp = mutation(mom[i])
            offspring.append(temp)
            temp1 = mutation(dad[i])
            offspring.append(temp1)

        np.random.shuffle(offspring)
        if y != (k-1):
            for item in range(k):
                objs[item].path = offspring[item]

        print(f"{y} Cost is: ", objs[i].path_cost)

    return objs


if __name__ == "__main__":
    # PASS IN INPUT.TXT

    start_time = time.time()
    input = []
    f = open("input3.txt", 'r')

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

    output = open("output.txt", "w")
    for item in range(len(objs[0].path)):
        temp = objs[0].path[item]
        listToStr = ' '.join([str(item) for item in temp])
        output.write(listToStr)

        if item != (len(objs[0].path) - 1):
            output.write("\n")

    output.close()
    print("--- %s seconds ---" % (time.time() - start_time))
