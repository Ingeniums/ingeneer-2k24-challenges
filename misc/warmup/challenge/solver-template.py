#!/usr/bin/env python3
from pwn import *

r = process(['python3', 'source.py'])
# r = remote("ingeneer-2k24.ingeniums.club", 31909)

# tips 
# to receive some value from the server you can use 
# val = r.recvline(), r.recvuntil("number: "); val = r.recvline()
# same with receiving you can send values using:
# r.sendline(value_encoded_to_bytes), r.send(value_encoded_to_bytes),
# r.sendlineafter("prompt msg", value_encoded_to_bytes)

# you can convert received bytes to python objects using eval:
# received--> "val : [1, 2, 3]"
# r.recvuntil("val : "); arr = eval(r.recvline().strop())

# you can always read the docs for more info
## GOOD LUCK

r.interactive()