from Crypto.Util.number import bytes_to_long as bl , inverse as inv , getStrongPrime 

from secret import FLAG 



class RSA:
    def __init__(self, bits=1024):
        self.bits = bits
        self.e = 0x10001
        self.p = getStrongPrime(self.bits)
        self.q = getStrongPrime(self.bits)

    def cipher_enc(self , flag):
        e = self.e 
        p , q = self.p , self.q 
        n = p*q 
        ct = [pow(bl(c.encode()) , e , n) for c in flag]
        return n , ct


if __name__ == "__main__":
    cipher=RSA()
    e = cipher.e
    n , ct = cipher.cipher_enc(FLAG)
    with open('out.txt', 'w') as f :
        f.write('n : {}\n'.format(n))
        f.write('e : {}\n'.format(e))
        f.write('ct : {}\n'.format(ct))


