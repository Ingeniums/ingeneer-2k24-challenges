import secrets
import numpy as np

LEVEL = 0
ROUNDS = 50


def generate_matrix(n, m):
    choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    matrix = np.random.choice(choices, size=(n, m))
    return matrix.tolist()

def pyramid_to_matrix(pyramid):
    height = len(pyramid)
    width = len(pyramid[-1])
    for i in range(height):
        columns_to_add = width - len(pyramid[i])
        add = [0 for _ in range(columns_to_add //2)]
        pyramid[i] = add + pyramid[i] + add
    return pyramid

def matrix_to_pyramid(matrix):
    start_idx = len(matrix[-1]) // 2 
    end_idx = start_idx
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[-1])):
            if(j >= start_idx and j <= end_idx):
                continue
            else:
                matrix[i][j] = 0
        start_idx -= 1
        end_idx += 1
    return [[value for value in row if value > 0] for row in matrix]

def string_to_matrix(string):
    return eval(string)

def largestRectangleArea(heights) -> int:
    maxArea = 0
    stack = []
    for i, h in enumerate(heights):
        start = i
        while(stack and stack[-1][1] > h):
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append([start,h])

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea 

          
def maximalRectangle(matrix, target) -> int:
    horizin = [0] * len(matrix[0])
    maxArea = 0
    for i in range(len(matrix)):
        for idx, v in enumerate(matrix[i]):
            if(v == target):
                horizin[idx] += target
            else:
                horizin[idx] = 0
        maxArea = max(maxArea, largestRectangleArea(horizin))
    return maxArea


def solve(matrix):
    maxAreas = [0] * 9
    for i in range(0,9):
        maxAreas[i] = maximalRectangle(matrix, i+1)
    max_value = max(maxAreas)
    max_targets = [index + 1 for index, value in enumerate(maxAreas) if value == max_value]
    return [max_value, max_targets]
    
def main():
    global LEVEL
    while(LEVEL < ROUNDS):
        print(f'Level {LEVEL+1}/{ROUNDS}')
        if(LEVEL == 0):
            n = 5
        elif(LEVEL in [1,2,3]):
            n = 15
        elif(LEVEL in [4,5]):
            n = 49
        elif(LEVEL in [6,7]):
            n = 99
        else:  
            n = secrets.randbelow(250) + 100
        if(n % 2 == 0):
            n += 1
        m = n * 2 - 1 

        matrix = generate_matrix(n,m)
        pyramid = matrix_to_pyramid(matrix)
        print(f"Here is your pyramid> {pyramid}")
        matrix = pyramid_to_matrix(pyramid)
        result = solve(matrix)
        user_max = input("Max>")
        user_target = input("Target>")
        if(int(user_max) == int(result[0]) and int(user_target) in result[1]):
            LEVEL += 1 
        else:
            print("Ghalt")
            exit(1)
            
if __name__ == "__main__":
    print(f'In this game you need to complete all the {ROUNDS} LEVELS to get the flag')
    main()
    if(LEVEL >= ROUNDS):
        print("ingeneer{clEAOPatRa_@TheR_1oV!nG_90ddE5$}")
        
        

