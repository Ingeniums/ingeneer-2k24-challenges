#!/usr/bin/env python3

from Crypto.Cipher import AES
import base64


def decrypt_string(key, nonce, ciphertext):
    nonce = base64.b64decode(nonce)
    ciphertext = base64.b64decode(ciphertext)
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext).decode('utf-8')
    return plaintext


key = b"\xc6z)\x86>\xba\x0bh\xcc\x1dV'\x06#\xbf\x1c"
nonce = 'jWzO1GHLJr0='
enc = 'ruNkO4Q/+mpVoL1rEN4pEBtrVRTT5qLpqOfvCKf6Sn4fMd2n5PSw9JLtPNJuGB52Bv+/9FaBu1H7'


print(decrypt_string(key, nonce, enc))
