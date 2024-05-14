from pwn import *

def connect():
    return remote('localhost', 14006)

def main():
    con = connect()
    for i in range(3):
        print(f"Round {i + 1}")
        a = 1
        b = 65536
        while True:
            c = (a + b) // 2
            con.sendlineafter(b"Enter your guess:", str(c).encode())
            info = con.recvuntil(b".").decode()
            if "higher." in info:
                a = c + 1
            elif "lower." in info:
                b = c - 1
            else:
                break
    con.interactive()
    
if __name__ == "__main__":
    main()