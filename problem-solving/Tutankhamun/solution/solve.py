from pwn import *

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

con = remote("localhost", 14004)
con.recvline()
for i in range(15):
    con.recvuntil(b"map:")
    con.recvline()
    pyramid = eval(con.recvline().decode())
    con.recvuntil(b"go to")
    con.recvline()
    goal_idx = int(con.recvline().decode())
    result = solve(pyramid, goal_idx)
    con.sendlineafter(b"answer>", str(result).encode())
con.interactive()
