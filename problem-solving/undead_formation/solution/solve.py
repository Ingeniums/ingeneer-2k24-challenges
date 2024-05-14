from pwn import *

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
                if strengths[x] == strengths[y]:
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
        
            
    r = [x for x in strengths]
    return r

con = remote("ingeneer-2k24.ingeniums.club", 14003)


for i in range(150):
    print(i)
    con.recvuntil(b'survivorCounts: ')
    strengths = eval(con.recvline().decode())
    print(f"survivorCounts {strengths}")
    con.recvuntil(b'positions: ')
    positions = eval(con.recvline().decode())
    print(f"positions {positions}")
    con.recvuntil(b'directions:')
    directions = eval(con.recvline().decode())
    print(f"directions {directions}")
    res = solve(positions, strengths, directions)
    print(res)
    con.sendlineafter(b"answer>",str(res).encode())

con.interactive()