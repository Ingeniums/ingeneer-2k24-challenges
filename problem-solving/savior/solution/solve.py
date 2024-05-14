from pwn import *

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
    con = remote("ingeneer-2k24.ingeniums.club", 14009)
    for _ in range(150):
        con.recvuntil(b"adjacency matrix: ")
        matrix = eval(con.recvline().decode())
        con.recvuntil(B"initial: ")
        initial = eval(con.recvline().decode())
        print(f"initial {initial}")
        result = solve(matrix, initial)
        print(result)
        con.sendlineafter(b"answer>", str(result).encode())
    con.interactive()
        

            
    
if __name__=="__main__":
    main()