from population import Population
import random 

def create_init_pop(size, cities):
    inital_population = [] 
    keys = range(5)
    pop_setup = [None] * 5
    pop_dict = {}

    population = []
    for k in range(100):
        for i in range(5):  # setting random val to value var
            pop_setup[i] = random.random()
        for i in keys:
            pop_dict[i] = pop_setup[i] # create dict

        temp = (sorted(pop_dict.items(), key=lambda kv: kv[1])) # sort

        temp = dict(temp)
        temp = list(temp.keys())
        population.append(temp)  # create list of dict
        
    # print(population)
    # print(type(population))

    return population

def calc_fitness (inital_population):
    score = 0 

    for subarr in inital_population:
        subarr
    
    return score

def create_mating_pool(population, rank_list): 
    matingPool  = [] 
    # your code goes here 

    return matingPool

def crossover(parent1, parent2, start_index, end_index):
    child = []
    # your code goes here

    return child 

def agent(size, cities):
    num_of_loc = size 
    coordinates = cities 
    inital_pop = create_init_pop(size = num_of_loc, cities = coordinates)
    print(inital_pop)
    calc_fitness(inital_population=inital_pop)
    return 0

if __name__=="__main__":
    #PASS IN INPUT.TXT
    
    input = []
    f = open("Test_Cases/input.txt", 'r')
    for x in f: 
        x = x.strip()
        input.append(x)
    input = input[1:]
    agent(size = len(input), cities=input)

    #agent(input)