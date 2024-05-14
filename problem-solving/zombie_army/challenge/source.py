#!/usr/bin/env python3
from random import randint, choice
from collections import defaultdict, deque


def gen_constraints(zombie_count):
    max_len = zombie_count
    constraints_len = randint(0, max_len)
    army = [i for i in range(zombie_count)]
    constraints = []
    seen = set()
    for i in range(constraints_len):
        z1, z2 = choice(army), choice(army)
        while (z2 == z1):
            z2 = choice(army)
        if (z1, z2) not in seen:
            constraints.append((z1, z2))
            seen.add((z1, z2))
    
    return constraints
    
    
def build_graph(constraints):
    graph = defaultdict(list)
    for z1, z2 in constraints:
        graph[z2].append(z1)
    return graph

def calc_Indegree(constraints, zombi_count):
    res = [0] * zombi_count
    for z1, z2 in constraints:
        res[z1] += 1  
    return res
     
def sort_zombies(zombie_count, Indegree, graph):
    queue = deque()
    for i in range(zombie_count):
        if Indegree[i] == 0:
            queue.append(i)
    
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            Indegree[neighbor] -= 1
            if Indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return result

def solve(constraints, zombie_count):
    g = build_graph(constraints)
    d = calc_Indegree(constraints, zombie_count)
    res = sort_zombies(zombie_count, d, g)
    
    if (len(res) != zombie_count):
        res = []
    return res



def fail():
    print("WRONG")
    exit(1)

def success():
    print("CORRECT")

def check(constraints, ans, zombie_count):
    if (len(ans) == 0):
        noPath = len(solve(constraints, zombie_count)) == 0
        if not(noPath):
            fail()
        success()
        return noPath
    if (len(ans) != zombie_count):
        fail()
    
    for z1, z2 in constraints:
        try:
            if (ans.index(z2) > ans.index(z1)):
                fail()
        except:
            # in case a number is not in the answer
            fail()
    success()
    return True


ROUNDS = 100

def main():
    for _ in range(ROUNDS):
        zombie_count = randint(20, 40)
        constraints = gen_constraints(zombie_count)
        print(f"zombie_count {zombie_count}")
        print(f"constraints {constraints}")
        ans = input("Enter your answer: ")
        ans = eval(ans)
        check(constraints, ans, zombie_count)

    print("YOU WON")
    print(f"here is your flag: {'ingeneer{niCe_JOB_$uRV1VIn9_tHAT}'}")

if __name__ == "__main__":
    main()