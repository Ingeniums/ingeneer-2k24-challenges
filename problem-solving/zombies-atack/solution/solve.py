from collections import deque
from pwn import *

ROUNDS = 200

con = remote("ingeneer-2k24.ingeniums.club", 14001)

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
    
    return list(not_affected)

def main():
    for i in range(1000):
        con.recvuntil(b"initial: ")
        initial = eval(con.recvline().decode())
        con.recvuntil(b"adjacency matrix: ")
        matrix = eval(con.recvline().decode())
        print(f"initial: {initial}")
        print(f"adjacency matrix: {matrix}\n")
        result = solve(matrix, initial)
        con.sendlineafter(b"answer>", str(result).encode())
    con.interactive() 
    
main()    

  
       
 


    


