import random, time

def nqueens():
    generation = 1
    mutation_chance = 0.5
    numberOfQueens = int(input("Enter Number Of Queens: "))
    change_mutation = input("Would you like to change the default mutation(50%): ")
    if change_mutation in ['y', 'Y', 'YES', 'yes', 'Yes']:
        mutation_chance = float(input("Enter mutation chance (0.01 - 1):"))
    while numberOfQueens == 2 or numberOfQueens == 3:
        print("!!!There is not a solution for 2x2 and 3x3 boards!!!")
        numberOfQueens = int(input("Enter Number of Queens: "))
    maxFitness = find_max_fitness(numberOfQueens)
    boards = [random_board(numberOfQueens) for _ in range(100)]
    start = time.time()
    while not maxFitness in [fitness(board, maxFitness) for board in boards]:
        boards = generate_board(boards, mutation_chance, maxFitness, generation, numberOfQueens)
        print("\nGeneration :", generation, "\nMaximum Fitness :", (max([fitness(n, maxFitness) for n in boards])), "       Minimum Fitness :", (min([fitness(n, maxFitness) for n in boards])))
        generation += 1
    finish = time.time()
    print("Time:", finish - start)
    print("Mutation Probability:", int(mutation_chance * 100), "%\n")

def find_max_fitness(numberOfQueens):
    if numberOfQueens - 1 == 0:
        return 0
    return numberOfQueens - 1 + find_max_fitness(numberOfQueens - 1)

def random_board(numberOfQueens):
    return [random.randint(1, numberOfQueens) for position in range(numberOfQueens)]

def fitness(board, maxFitness):
	counter = 0
	for i in range(len(board)):
		counter += check_queen(board, i)
	return maxFitness - counter

def check_queen(board, currentQuuen):
	check = 1
	collisions = 0
	for i in range(currentQuuen + 1, len(board)):
		if board[currentQuuen] - check == board[i] or board[currentQuuen] + check == board[i] or board[currentQuuen] == board[i]:
			collisions += 1
		check += 1
	return collisions

def generate_board(boards, mutation_probability, maxFitness, generation, numberOfQueens):
    new_boards = []
    fit = [fitness(n, maxFitness) for n in boards]
    output = zip(boards, fit)
    zipped = list(output)
    res = sorted(zipped, key=lambda x: x[1])
    for i in range(99,92, -1):
        for j in range(i-1, 88, -1):
            mama = res[i][0]
            papa = res[j][0]
            x = baby_board(mama, papa, maxFitness, new_boards, mutation_probability, generation, numberOfQueens)
            if x == 1:
                break
        if x == 1:
            break
    mama = res[92][0]
    papa = res[91][0]
    baby_board(mama, papa, maxFitness, new_boards, mutation_probability, generation, numberOfQueens)
    return new_boards

def baby_board(mama, papa, maxFitness, new_boards, mutation_probability, generation, numberOfQueens):
    cutting_point = random.randint(1, len(mama) - 1)
    babyBoard1 = reproduce(mama, papa, cutting_point)
    babyBoard2 = reproduce(papa, mama, cutting_point)
    if random.random() < mutation_probability:
        babyBoard1 = mutate(babyBoard1)
    if random.random() < mutation_probability:
        babyBoard2 = mutate(babyBoard2)
    new_boards.append(babyBoard1)
    new_boards.append(babyBoard2)
    if fitness(babyBoard1, maxFitness) == maxFitness:
        print("\nSolved in Generation:", generation, "\nThe solution: Board =", babyBoard1, "Fitness =", fitness(babyBoard1, maxFitness), "\n")
        print_board(babyBoard1, numberOfQueens)
        return 1
    if fitness(babyBoard2, maxFitness) == maxFitness:
        print("\nSolved in Generation:", generation, "\n""The solution: Board =", babyBoard2, "Fitness =", fitness(babyBoard2, maxFitness), "\n")
        print_board(babyBoard2, numberOfQueens)
        return 1

def reproduce(mom, dad, cutting_point):
    return mom[0:cutting_point] + dad[cutting_point:len(mom)]

def mutate(child):
    position = random.randint(0, len(child) - 1)
    value = random.randint(1, len(child))
    child[position] = value
    return child

def print_board(maxFitnessBoard, numberOfQueens):
    for i in range(numberOfQueens, 0, -1):
        print((maxFitnessBoard.index(i)) * 'x ' + 'Q ' + (numberOfQueens - maxFitnessBoard.index(i) - 1) * 'x ')



if __name__ == "__main__":
    print("\n███╗   ██╗       ██████╗ ██╗   ██╗███████╗███████╗███╗   ██╗███████╗     █████╗ ██╗\n████╗  ██║      ██╔═══██╗██║   ██║██╔════╝██╔════╝████╗  ██║██╔════╝    ██╔══██╗██║\n██╔██╗ ██║█████╗██║   ██║██║   ██║█████╗  █████╗  ██╔██╗ ██║███████╗    ███████║██║\n██║╚██╗██║╚════╝██║▄▄ ██║██║   ██║██╔══╝  ██╔══╝  ██║╚██╗██║╚════██║    ██╔══██║██║\n██║ ╚████║      ╚██████╔╝╚██████╔╝███████╗███████╗██║ ╚████║███████║    ██║  ██║██║\n╚═╝  ╚═══╝       ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝    ╚═╝  ╚═╝╚═╝\n")
    nqueens()