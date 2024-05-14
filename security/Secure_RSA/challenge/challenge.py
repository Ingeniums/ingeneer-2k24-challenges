from Crypto.Util.number import bytes_to_long as bl ,getPrime, isPrime
from secret import FLAG 
from random import randint 


def getsecondparameter(num):
    while True :
        num += randint(1,getPrime(128))
        if isPrime(num):
            return num 


p = getPrime(2048)
q = getsecondparameter(p)

n = p*q 
e = 0x10001

ct = pow(bl(FLAG) , e , n)
with open('out.txt', 'w') as f :
    f.write('ct : {}\n'.format(ct))
    f.write('e : {}\n'.format(e))
    f.write('n : {}\n'.format(n))