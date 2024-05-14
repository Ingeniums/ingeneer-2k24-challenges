from collections import deque
import numpy as np
import random

ROUNDS = 200



def generate_symmetric_binary_matrix(size, p_1=0.1, p_0=0.9):
    choices = [1, 0]
    probabilities = [p_1, p_0]
    upper_triangular = np.random.choice(choices, size=(size, size), p=probabilities)
    symmetric_matrix = np.triu(upper_triangular) + np.triu(upper_triangular, 1).T
    np.fill_diagonal(symmetric_matrix, 1)
    return symmetric_matrix.tolist()



def solve(graph, initial):
    n = len(graph)
    infected_nodes = set(initial)
    not_affected = set(range(n))
    
    for node in initial:
        if node in not_affected:
            queue = deque([node])
            component_nodes = set()
            while queue:
                current_node = queue.popleft()
                infected_nodes.add(current_node)
                component_nodes.add(current_node)
                not_affected.discard(current_node)
                for neighbor, is_connected in enumerate(graph[current_node]):
                    if is_connected and neighbor not in infected_nodes:
                        queue.append(neighbor)
                        not_affected.discard(neighbor)

            if len(initial) > 1:
                infected_nodes -= component_nodes
    
    return sorted(list(not_affected))



def main():
    for level in range(ROUNDS):
        print(f"ROUND {level+1}/{ROUNDS}")
        size = random.randint(15, 25)
        matrix = generate_symmetric_binary_matrix(size)
        initial = list(set([random.randint(0, size - 1) for _ in range(random.randint(0, size))]))
        print(f"initial: {initial}")
        print(f"adjacency matrix: {matrix}\n")
        result = solve(matrix, initial)
        user_answer = sorted(eval(input("answer>")))
        if user_answer == result:
            print("correct")
        else:
            print("wrong")
            exit(1)
            
    print("ingeneer{fIr$t_iN_fiR$t_OUT}")


if __name__ == "__main__":
    main()
    




