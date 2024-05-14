from pwn import xor


#user='a'*10 


def get(ciphertext):
    print(ciphertext[:8*2])
    cipher = ciphertext[16:32]
    c = xor(xor(bytes.fromhex(cipher[12:14]),b'0'),b'1').hex()
    cipher = cipher[:12] + c + cipher[14:]
    return ciphertext[:16] + cipher + ciphertext[32:] 




