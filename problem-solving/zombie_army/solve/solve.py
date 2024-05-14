#!/usr/bin/env python3
from pwn import *
from collections import defaultdict, deque
context.terminal = 'kitty -e sh -c'.split()


    

def build_graph(constraints):
    graph = defaultdict(list)
    for z1, z2 in constraints:
        graph[z2].append(z1)
    # print(graph)
    return graph

def calc_InDegree(constraints, zombi_count):
    res = [0] * zombi_count
    for z1, z2 in constraints:
        res[z1] += 1  
    return res
     
def sort_zombies(zombie_count, InDegree, graph):
    queue = deque()
    for i in range(zombie_count):
        if InDegree[i] == 0:
            queue.append(i)
    
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            InDegree[neighbor] -= 1
            if InDegree[neighbor] == 0:
                queue.append(neighbor)
                
    return result

def solve(constraints, zombie_count):
    g = build_graph(constraints)
    d = calc_InDegree(constraints, zombie_count)
    res = sort_zombies(zombie_count, d, g)
    
    if (len(res) != zombie_count):
        res = []
    # print(f'result ==> {res}')
    return res


r = remote('localhost', 8080)

for i in range(100):
    log.info(f'Round {i+1}')
    r.recvuntil(b'zombie_count ')
    zombie_count = int(r.recvline().strip())
    r.recvuntil(b'constraints ')
    constraints = eval(r.recvline().strip())
    res = solve(constraints, zombie_count)
    r.sendlineafter(b'answer:', str(res).encode())

r.interactive()