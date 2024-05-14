import secrets


ROUNDS = 15
LEVEL = 0

def generate_pyramid(rows):
    pyramid = []
    for i in range(1, rows + 1):
        row = [secrets.randbelow(100) + 1 for _ in range(i)]
        pyramid.append(row) 
    return pyramid

       


def solve(pyramid, goal_idx):
    sums: list[list[int]] = [[]]*len(pyramid)
    sums[goal_idx] = [pyramid[-1][goal_idx]]

    for cur_line in range(len(pyramid)-1, 0, -1):

        start_idx = max(0, goal_idx - (len(pyramid)-1-cur_line))

        tmp: list[list[int]] = []
        for _ in range(len(pyramid)):
            tmp.append([])

        for i in range(start_idx, min(cur_line, goal_idx)+1):
            if i > 0:
                for j in sums[i]:
                    tmp[i-1].append(pyramid[cur_line-1][i-1] + j)
            if i < cur_line:
                for j in sums[i]:
                    tmp[i].append(pyramid[cur_line-1][i] + j)

        sums = tmp

    return max(sums[0])

def main():
    global LEVEL
    while(LEVEL < ROUNDS):
        print(f'Level {LEVEL+1}/{ROUNDS}')
        rows = secrets.randbelow(5) + 15
        pyramid = generate_pyramid(rows)
        print(f"Here is the map: \n{pyramid}")
        goal_idx = secrets.randbelow(len(pyramid[-1]))
        print(f"go to \n{goal_idx}")
        result = solve(pyramid, goal_idx)
        user_max = input('answer>')
        
        if(user_max != str(result)):
            print("Ghalt")
            print(f'Correct result is {result}')
            exit(1)
        else:
            LEVEL +=1
                
    


if __name__ == "__main__":
    print(f'In this game you need to complete all the {ROUNDS} LEVELS to get the flag')
    main() 
    if(LEVEL >= ROUNDS):
        print("ingeneer{to_hIm_$h@1L_cOM3_f!RE_wat3r_aND_P35tiL3nC3}")

    


