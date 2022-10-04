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


# 0.8
# 1.1
# 1.1


import random
import numpy as np
import copy as cp
import time

k = 150  # population size


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
                #print("point 1 is :", (point1), "point 2 is: ", point2)
                dist += np.linalg.norm(point1 - point2)
            dist_arr.append(dist)
            objs[i].path_cost = dist
            #total_cost += 1 / dist

        # for i in range(k):
            #fitness = (1 / objs[i].path_cost) / total_cost
            #setattr(objs[i], "fitness", fitness)


objs = [Path(None, None, None) for i in range(k)]  # global list of objects


class Population():
    def __init__(self, size, parents, best):
        self.size = size
        self.parents = parents
        self.best = best


def create_init_pop1(size, cities):

    print(cities)
    # print(np.array(init_pop).shape)
    for i in range(k):

        np.random.shuffle(cities)
        temp_cities = cp.deepcopy(cities)
        temp_cities.append(cities[0])
        setattr(objs[i], 'path', temp_cities[i])
    print(np.array(temp_cities).shape)


def create_init_pop(size, cities):
    #print("NN is :", nn_path, nn_dist)
    #print('total cost is: ', total_cost, len(init_pop))
    # t
    # print(cities)
    # print(np.array(init_pop).shape)
    first = cities[0]
    temp_cities = []
    for i in range(k):
        if i <= (k/2):
            cities = np.roll(cities, 1, axis=0)
            neighbor = nn(size, list(cities))
            # print(neighbor)
            temp_cities.append(neighbor)
            setattr(objs[i], 'path', temp_cities[i])
        else:
            fake_cities = []
            double_temp_cities = cp.deepcopy(cities)
            np.random.shuffle(double_temp_cities)
            fake_cities = list(cp.deepcopy(double_temp_cities))
            fake_cities.append(double_temp_cities[0])
            setattr(objs[i], 'path', fake_cities)

        # np.random.shuffle(cities)
        # print("Before, ", len(cities), cities[0], cities[-1])
        #temp_cities = cp.deepcopy(cities)
        # temp_cities.append(cities[0])
        # print("after: ", len(cities), cities[0], cities[-1])
        #[print(x) for x in temp_cities]
        #temp_cities = [*temp_cities]

       
        # print(objs[i].path)
    # print(np.array(temp_cities).shape)


# return score
def nn(size, cities):
    init_pop = []
    # print(cities)

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
                # print(cities[i])
                nn_path = list(point1)

            dist += np.linalg.norm(point1 - point2)
            if i == 1 or i == 0:
                nn_dist = dist
                if len(cities) > 1:
                    nn_path = list(cities[1])
                else:
                    nn_path = list(cities[0])

            # print("point 1 is :", (point1), "point 2 is: ",point2, "distance betwee 2 is: ", dist)

            if nn_dist >= dist:
                # set NN to new [point,dist]
                nn_path = cities[i]
                nn_dist = dist
                pop_index = i

        temp_list.append(nn_path)

        init_pop.append(list(nn_path))
        cities.pop(pop_index)
        if j == 0:
            cities.pop(0)
        size1 = len(cities)
    # print(init_pop)
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

    #print("\n", parent1, "\n", parent2)
    if (parent1 != parent2):
        _sub = _parent[start:end]
        _left, _right = [], []
        _left = _parent2[:start]
        _right = _parent2[end:]
        _cross1 = [*_left, *_sub, *_right]
        _cross1[-1] = _cross1[0]
        # print(_cross1)
        _cross1 = check_chromosome_validity(_cross1, parent1)
        # print(len(_cross1))
        offspring_paths += [_cross1]
    else:
        # or i in range(5):
        # print("first else ")
        # print(np.array(_parent2).shape)
        _parent2 = mutation(parent2)
        _sub = _parent[start:end]
        _left, _right = [], []
        _left = _parent2[:start]
        _right = _parent2[end:]
        _cross1 = [*_left, *_sub, *_right]
        _cross1[-1] = _cross1[0]
        # print(_cross1)

        _cross1 = check_chromosome_validity(_cross1, parent1)
        # print(len(_cross1))
        offspring_paths += [_cross1]

    if (parent1 != parent2):
        sub = parent1[start:end]
        left, right = [], []
        left = parent2[:start]
        right = parent2[end:]
        cross1 = [*left, *sub, *right]
        cross1[-1] = cross1[0]
        # print(cross1)
        cross1 = check_chromosome_validity(cross1, parent1)
        # print(len(cross1))
        offspring_paths += [cross1]

    else:
        # for i in range(5):
        # print("second else")
        parent2 = mutation(parent2)
        sub = parent1[start:end]
        left, right = [], []
        left = parent2[:start]
        right = parent2[end:]
        cross1 = [*left, *sub, *right]
        cross1[-1] = cross1[0]

        cross1 = check_chromosome_validity(cross1, parent1)

        # print(len(cross1))
        offspring_paths += [cross1]

        return offspring_paths
    #

 # print to see parent and offspring
    # print("\nParent 1: ", _parent, "\nParent 2: ",
    # _parent2,  "\nFinal Offspring: ", offspring_paths)clear
    # print(offspring_paths)
    return offspring_paths


def mutation(parent):
    # print("len parent", len(parent))
    rand1 = random.randint(0, len(parent) - 3)
    rand2 = random.randint(rand1 + 1, len(parent) - 1)
    # print(rand1,rand2)

    if (np.random.randint(0, 2) == 0):
        # print("swap")
        temp = parent[rand1]
        parent[rand1] = parent[rand2]
        parent[rand2] = temp

    else:
        # print("permutate subection")
        offspring = np.random.permutation(parent[rand1:rand2])
        parent[rand1:rand2] = [list(x) for x in offspring]

    return parent


def Agent(size, cities):
    num_of_loc = size
    coordinates = cities
    init_pop = create_init_pop(size=num_of_loc, cities=coordinates)
    path = Path(init_pop, 0.00, 0.00)

    for y in range(k):
        path.calc_fitness()
        objs.sort(key=lambda x: x.path_cost)
        print(f"{y} Cost is: ", objs[0].path_cost)


        offspring, mom, dad = [], [], []

        mom = [x.path for x in objs[:15]]
        dad = [x.path for x in objs[15:30]]
        objs[0].path = mom[0]
        # print(len(dad[0]))
        # parents.append(mom)
        # parents.append(dad)

        # print(len(mom)+len(dad) - 1)

        # PUT MOM AND DAD THROUGH VALDIATION
        # if y < (k/2):
        #print("mom index 0, best ",mom[0])
        offspring += mom
        offspring += dad

        for i in range(len(mom)):
            # for i in range(len(dad)):
            rand = random.randint(1, size - 3)
            rand_temp = random.randint(rand + 1, size - 2)
            offspring += crossover(mom[i],
                                   dad[len(mom) - i - 1], rand, rand_temp)
            offspring += crossover(mom[i],
                                   dad[i], rand, rand_temp)
            offspring += crossover(mom[len(mom) - i - 1],
                                   dad[i], rand, rand_temp)
            offspring += crossover(mom[len(mom) - i - 1],
                                   dad[len(mom) - i - 1], rand, rand_temp)
            # print("[i]",np.array(mom[i]).shape)
            # print("full", np.array(mom).shape)
            temp = mutation(mom[i])
            offspring.append(temp)
            temp1 = mutation(dad[i])
            offspring.append(temp1)
            # print(len(temp1))

        # offspring += mututation(dad[i])
            """ if np.random.randint(0, 3) == 0:
            # print("mutate")
                if np.random.randint(0, 2) == 0:
                    mom[i] = mututation(mom[i])
                else:
                    mom[j] = mututation(mom[j])
            elif np.random.randint(0, 3) == 1:
            # print("mutate")
                if np.random.randint(0, 2) == 0:
                    dad[i] = mututation(dad[i])
                else:
                    dad[j] = mututation(dad[j])"""

            # print(np.random.randint(0, 2))
            # print('Mom is ', np.array(mom).shape)

        # print("Offspring is: ", len(offspring))
        # temp_arr = np.asarray(offspring)
        # print(temp_arr.shape)
        # print(len(objs))

        # print("objs before is: ", objs[i].path)
        #np.random.shuffle(offspring)
        # offspring.sort()
        if y != (k-1):
            for item in range(k -1 ):
                # objs[i].path, objs[i].path_cost, objs[i].fitness = None, None, None
                #print("shape citites ", np.array(cities).shape)
                objs[item +1].path = offspring[item]
                # print(f"{y}")
        # or i in range(k):

    return objs


if __name__ == "__main__":
    # PASS IN INPUT.TXT

    start_time = time.time()

    input = []
    f = open("input2.txt", 'r')
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
    objs.sort(key=lambda x: x.path_cost)
    output = open("output.txt", "w")
    for item in range(len(objs[0].path)):

        temp = objs[0].path[item]
        temp_cost = objs[0].path_cost
        listToStr = ' '.join([str(item) for item in temp])

        output.write(listToStr)
        
        if item != (len(objs[0].path) - 1):
            output.write("\n")
    str = " " + str(temp_cost)
    output.write(str)
    output.close()
    # for i in range(k):
    print("--- %s seconds ---" % (time.time() - start_time))
