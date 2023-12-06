import random
def fitness_func(x):
    return 3 * pow(x,2) + 17 * x
def generate_random_individual():
    return random.randint(0, 31)

def fitness(y):
    return fitness_func(y)



def crossOver(parent1, parent2):
    crossoverPoint = random.randint(1, 4)
    mask = (1 << crossoverPoint) - 1
    OF1 = (parent1 & mask) | (parent2 & ~mask)
    OF2 = (parent2 & mask) | (parent1 & ~mask)
    return OF1,OF2

def mutate(x, mutRate):
    if random.random() < mutRate:
        bit_to_flip = 1 << random.randint(0, 4)
        x ^= bit_to_flip
    return x

population_size = 8
num_parents = 4
mutRate = 0.1

population = [generate_random_individual() for _ in range(population_size)]


fitness_values = [fitness(individual) for individual in population]
generations = 1


# Selecting Parents
def selectParents(population, num_parents):
    fitness_sum = sum(fitness(individual) for individual in population)
    parents = []
    for _ in range(num_parents):
        rand_value = random.uniform(0, fitness_sum)
        cumulative_sum = 0
        for x in population:
            cumulative_sum += fitness(x)
            if cumulative_sum >= rand_value:
                parents.append(x)
                break
    return parents

for generation in range(generations):
    print(f"Gen {generation}:")
    print("Population Taken :", population)
    print("Fitness values:", fitness_values)

    parents = selectParents(population, num_parents)

    offsprings = []
    while len(offsprings) < population_size - num_parents:
        parent1, parent2 = random.sample(parents, 2)
        offspring1, offspring2 = crossOver(parent1, parent2)
        offsprings.extend([offspring1, offspring2])

    offsprings = [mutate(offspring, mutRate) for offspring in offsprings]

    offspring_fitness = [fitness(offspring) for offspring in offsprings]

    combined_population = population + offsprings
    combined_fitness = fitness_values + offspring_fitness
    selected_indices = sorted(range(len(combined_fitness)), key=lambda i: combined_fitness[i], reverse=True)[:population_size]
    population = [combined_population[i] for i in selected_indices]
    fitness_values = [combined_fitness[i] for i in selected_indices]
    fittest_chromosome = population[fitness_values.index(max(fitness_values))]
    fittest_fitness = max(fitness_values)

print("Final population:", population)
print("Final fitness values:", fitness_values)
print("Fittest Chromosome:", fittest_chromosome)
print("Fitness of the Fittest Chromosome:", fittest_fitness)
