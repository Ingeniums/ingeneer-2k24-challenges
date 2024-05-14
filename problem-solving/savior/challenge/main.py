import random
import numpy as np


ROUNDS = 150

def generate_symmetric_binary_matrix(size, p_1=0.1, p_0=0.9):
    choices = [1, 0]
    probabilities = [p_1, p_0]
    matrix = np.random.choice(choices, size=(size, size), p=probabilities)
    symmetric_matrix = np.triu(matrix) + np.triu(matrix, 1).T
    np.fill_diagonal(symmetric_matrix, 1)
    return symmetric_matrix.tolist()


def solve(graph, initial):
    num_nodes = len(graph)
    parent = list(range(num_nodes))
    component_size = [1] * num_nodes

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if graph[i][j] == 1:
                parent_i, parent_j = find(i), find(j)
                if parent_i != parent_j:
                    parent[parent_i] = parent_j
                    component_size[parent_j] += component_size[parent_i]

    min_infected = float('inf')
    result_node = initial[0]

    initial.sort()

    

    for i in range(len(initial)):
        total_infected = 0
        infected_set = set()
        for j in range(len(initial)):
            if i == j:
                continue
            parent_node = find(initial[j])
            if parent_node in infected_set:
                continue
            infected_set.add(parent_node)
            total_infected += component_size[parent_node]
            
        if min_infected > total_infected:
            min_infected = total_infected
            result_node = initial[i]

    return result_node


def main():
    for level in range(ROUNDS):
        print(f"ROUND {level+1}/{ROUNDS}")
        size = random.randint(5, 50)
        matrix = generate_symmetric_binary_matrix(size)
        initial = list(set([random.randint(0, size -1) for _ in range(random.randint(1, size))]))
        print(f"adjacency matrix: {matrix}")
        print(f"initial: {initial}")
        result = solve(matrix, initial)
        user_result = int(input("answer>"))
        if(result != user_result):
            print("GHaLt")
            print(f"correct was {result}")
            exit(1)
    print("ingeneer{I_knOW_@_9uy_wHo_kn0w$_@_9UY_WHO_c4N_Do_TH!5}")
    exit(0)
            
    
if __name__=="__main__":
    main()