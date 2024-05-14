#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt_string(key, plaintext):
    cipher = AES.new(key, AES.MODE_CTR)
    ciphertext = cipher.encrypt(plaintext.encode())
    nonce = base64.b64encode(cipher.nonce).decode('utf-8')
    ciphertext = base64.b64encode(ciphertext).decode('utf-8')
    return nonce, ciphertext

def decrypt_string(key, nonce, ciphertext):
    nonce = base64.b64decode(nonce)
    ciphertext = base64.b64decode(ciphertext)
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext).decode('utf-8')
    return plaintext


key = get_random_bytes(16)
plaintext = "ingeneer{7H!s_!5_why_YOu_neEd_7O_3ncRYP7_Y0uR_cHaT_TeXtS}"
nonce, ciphertext = encrypt_string(key, plaintext)
print("Key:", key)
print("Nonce:", nonce)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt_string(key, nonce, ciphertext)
print("Decrypted text:", decrypted_text)

# "\xc6z)\x86>\xba\x0bh\xcc\x1dV'\x06#\xbf\x1c" 
# "\\xc6z)\\x86>\\xba\\x0bh\\xcc\\x1dV'\\x06#\\xbf\\x1c\"
# jWzO1GHLJr0=
# ruNkO4Q/+mpVoL1rEN4pEBtrVRTT5qLpqOfvCKf6Sn4fMd2n5PSw9JLtPNJuGB52Bv+/9FaBu1H7