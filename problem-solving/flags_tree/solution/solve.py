from pwn import *

con = remote("20.199.93.34", 14010)

file = open("../challenge/flag.txt", "r")

for i in range(20):
    con.sendlineafter(b"exit): ", file.readline().strip().encode())
    print('done')
    
con.interactive()
    