#!/usr/bin/env python3
from pwn import *

# r = process(['python3', 'source.py'])
r = remote("localhost", 11008)

for _ in range(10):
    r.sendlineafter(b"round number pls: ", str(_).encode())
    r.recvuntil(b"arr: ")
    arr = r.recvline().strip().decode()
    arr = eval(arr)
    r.sendlineafter(b"sum pls: ", str(sum(arr)).encode())
    r.recvuntil(b"matrix: ")
    matrix = r.recvline().strip().decode()
    matrix = eval(matrix)
    r.sendlineafter(b"diagonal arr pls: ", str([matrix[i][i] for i in range(3)]).encode())


r.interactive()