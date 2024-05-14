from pwn import *


def pyramid_to_matrix(pyramid):
    height = len(pyramid)
    width = len(pyramid[-1])
    for i in range(height):
        columns_to_add = width - len(pyramid[i])
        add = [0 for j in range(columns_to_add //2)]
        pyramid[i] = add + pyramid[i] + add
    return pyramid

def largestRectangleArea(heights):
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

          
def maximalRectangle(matrix, target):
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
    print(matrix)
    maxAreas = [0] * 9
    for i in range(0,9):
        maxAreas[i] = maximalRectangle(matrix, i+1)
    max_value = max(maxAreas)
    max_target = maxAreas.index(max_value) + 1
    return [max_value, max_target]

con = remote("localhost", 14005)

for i in range(50):
    print(f"round {i}")
    con.recvuntil(b"pyramid> ")
    pyramid = eval(con.recvline().decode())
    matrix = pyramid_to_matrix(pyramid)
    result = solve(matrix)
    print(result)
    con.sendlineafter(b"Max>", str(result[0]).encode())
    con.sendlineafter(b"Target>", str(result[1]).encode())
con.interactive()