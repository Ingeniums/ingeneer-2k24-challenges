import random
import numpy as np

LEVEL = 0
ROUNDS = 150    


def generate_unique_list(n):
    numbers = list(range(0, n))  
    random.shuffle(numbers)  
    return numbers

def solve(positions, strengths, directions):
    n = len(positions)
    idxs = [i for i in range(n)] 
    idxs.sort(key=lambda x: positions[x]) # like sorting the zombies based on thier positions
    s = []
    for x in idxs:
        if directions[x] == 1:
            s.append(x)
        else:
            while s:
                y = s[-1]
                if strengths[x] == strengths[y]: # if they have the same strength but x has posittion > y posittion in the positive direction
                        strengths[x] -= strengths[x] // 2
                        strengths[y] = 0
                        s.pop()
                elif strengths[x] > strengths[y]:
                    strengths[x] -= strengths[x] // 2
                    strengths[y] = 0
                    s.pop()
                else: # strengths[x] < strengths[y]
                    strengths[x] = 0
                    strengths[y] -= strengths[y] // 2
                    break
        
            
    return strengths

def main():
    global LEVEL
    while(LEVEL < ROUNDS):
        print(f"Level {LEVEL+1}/{ROUNDS}")
        n = random.randint(6,10)
        strengths = [random.randint(3, 10) for _ in range(n)]
        positions = generate_unique_list(n)
        directions = np.random.choice([0,1], size=(n,), p=[0.2, 0.8]).tolist()
        print(f"survivorCounts: {strengths}")
        print(f"positions: {positions}")
        print(f"directions: {directions}")
        res = solve(positions, strengths, directions)
        print(res)
        user_strengths = input("answer>")
        if(res) != eval(user_strengths):
            print("WRONG")
            exit(1)
        LEVEL += 1
        
if __name__ == "__main__":
    main()
    if(LEVEL >= ROUNDS):
        print("ingeneer{9Ood_J08_$URvIVin6_THe_W@LKeRs}")