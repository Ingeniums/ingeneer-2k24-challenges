#!/usr/bin/env python3
from random import randint

WELCOME = """
this challenge is to get you on you feet with pwntools,
"""


print(WELCOME)


ROUNDS = 10

def fail():
    print("you failed, try again")
    exit(1)

for _ in range(ROUNDS):
    curr = input("round number pls: ").strip()
    if curr != str(_):
        fail()
    
    arr = [randint(1, 20) for i in range(randint(1, 20))]
    print(f"arr: {arr}")

    summ = input("sum pls: ").strip()
    if summ != str(sum(arr)):
        fail()

    matrix = []
    for i in range(3):
        matrix.append([randint(1, 100) for j in range(3)])
    
    print(f"matrix: {matrix}")

    diag_arr = input("diagonal arr pls: ").strip()
    diag_arr = eval(diag_arr)
    if diag_arr != [matrix[i][i] for i in range(3)]:
        fail()
    

print("gg ez")
with open("flag.txt", "r") as f:
    print(f.read())
    exit(0)
