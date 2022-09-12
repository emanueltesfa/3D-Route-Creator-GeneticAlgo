def create_init_pop(size, cities):
    inital_population = [] 
    # your code goes here


    return inital_population

def create_mapping_pool(population, rankList): 
    matingPool  = [] 
    # your code goes here 

    return matingPool

def crossover(parent1, parent2, start_index, end_index):
    child = []
    # your code goes here

    return child 

def search_best_paths():

    return None

def agent(coordinate_list):
    return 0

if __name__=="__main__":
    #PASS IN INPUT.TXT
    
    input = []
    f = open("input.txt", 'r')
    for x in f: 
        x = x.strip()
        input.append(x)

    agent(input)

