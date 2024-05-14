from pwn import xor 
import os
from Crypto.Util.Padding import pad 
from secret import FLAG

key = os.urandom(51)
flag = FLAG
text = b" We found 4 different envolopes one of them seem to be "+flag
text_padded = pad(text , 51)


p = [ (text_padded[i : i+len(key) ] )for i in range( 0 , len(text) , len(key))]



c1 = xor(p[0] , key)
c2 = xor(p[1] , key)
c3 = xor(p[2] , key)

with open( "c1.txt" , "w") as f :
    f.write(c1.hex())
with open( "c2.txt" , "w") as f :
    f.write(c2.hex())
with open( "c3.txt" , "w") as f :
    f.write(c3.hex())
with open( "p1.txt" , "wb") as f :
    f.write(p[0])