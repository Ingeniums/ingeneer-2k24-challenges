from pwn import xor 
from Crypto.Util.number import long_to_bytes as lb
from Crypto.Util.Padding import unpad


IV = b'daryylll'
BLOCK_SIZE = 8

def sol(p,known,iv=IV):
    pl = [p[i:i+16] for i in range(0,len(p),16)]
    result = xor(IV,known)
    permuted_indices = [6, 0, 4, 2]
    encrypted = ''
    for c in result :
        b = bin(c)[2:].zfill(8)
        permuted_string = ''.join(str(b[i:i+2]) for i in permuted_indices)
        encrypted+= permuted_string
    encrypted = lb(int(encrypted,2))
    r = xor(encrypted,bytes.fromhex(pl[0]))
    return r 



def decrypt_CBC(ciphertext, key,iv=IV ,block_size=BLOCK_SIZE):
    decrypted_blocks = []
    previous_block = iv
    ciphertext = bytes.fromhex(ciphertext)
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        decrypted_block = decrypt(block,key)
        decrypted_block = xor(decrypted_block, previous_block)
        decrypted_blocks.append(decrypted_block)
        previous_block = block

    return unpad(b''.join(decrypted_blocks), block_size)



def decrypt(encrypted_message, key):
    encrypted_message = xor(encrypted_message,key)
    decrypted = ''
    permuted_indices = [2,6,4,0]
    for byte in encrypted_message :
        b = bin(byte)[2:].zfill(8)
        permuted_string = ''.join(str(b[i:i+2]) for i in permuted_indices)
        decrypted+= permuted_string
    plain = lb(int(decrypted,2))
    return plain

p = "3357b29a9abc6897674548e22601e72df3def5e648f30b13dbf458f2d194350f5271e9b87506608db10c4978ccb4f6b2"
known = b'ingeneer'
key = sol(p,known)
print(decrypt_CBC(p,key))