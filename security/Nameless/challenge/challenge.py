from os import  urandom 
from Crypto.Util.Padding import pad , unpad
from Crypto.Util.number import long_to_bytes as lb
from pwn import xor
from secret import FLAG

key = urandom(8)
IV = b'daryylll'
BLOCK_SIZE = 8



def encrypt(message,key=key):
    ct = b''
    permuted_indices = [6, 0, 4, 2]
    encrypted = ''
    for c in message :
        b = bin(c)[2:].zfill(8)
        permuted_string = ''.join(str(b[i:i+2]) for i in permuted_indices)
        encrypted+= permuted_string
    enc = lb(int(encrypted,2))
    enc = xor(enc,key)
    return enc


def encrypt_CBC(plaintext, key=key, iv=IV ,block_size=BLOCK_SIZE):
    encrypted_blocks = []
    previous_block = iv
    plaintext = pad(plaintext, block_size)
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        xored_block = xor(block, previous_block)
        encrypted_block = encrypt(xored_block)
        encrypted_blocks.append(encrypted_block)
        previous_block = encrypted_block
    encrypted = b''.join(encrypted_blocks)
    return encrypted.hex()



def main():
    enc = encrypt_CBC(FLAG)
    with open('out.txt' , 'w') as f :
        f.write(enc)
if __name__ == "__main__":
    main()
