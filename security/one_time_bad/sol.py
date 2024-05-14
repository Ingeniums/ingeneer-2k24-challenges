from pwn import xor 


with open ('c1.txt' , 'r') as f :
    c1 = f.read()
with open ('c2.txt' , 'r') as f :
    c2 = f.read()
with open ('c3.txt' , 'r') as f :
    c3 = f.read()
with open ('p1.txt' , 'r') as f :
    p1 = f.read()

print(c1)
print(c2)
print(c3)

key = xor(p1 , bytes.fromhex(c1))
p2 = xor(bytes.fromhex(c2) , key).decode()
p3 = xor(bytes.fromhex(c3) , key).decode()

print(p2+p3)

