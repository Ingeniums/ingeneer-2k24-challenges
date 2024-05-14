#!/usr/bin/env/ python3

flag = "C0ngr4t5_x86_cH4mp10n_VEosA5MnKS"


secret = "wDMZkpwl5L69]fF7ks/3lnKS_VEosA5M"
key = b"4t#=\x19D\x03Yj4"

print(len(secret))

def decrypt(secret, key):
    res = b""
    for i in range(10):
        res += bytes([ord(secret[i]) ^ key[i]])
    
    for i in range(10, 10+11):
        if i % 2 == 0:
            res += bytes([ord(secret[i]) + 2])
        else:
            res += bytes([ord(secret[i]) - 3])

    #dec next 11
    tmp = secret[10+11:]
    for i in range(3):
        tmp = tmp[1:] + tmp[0]

    res += tmp.encode()

    print(res)
    return res

    
decrypt(secret, key)


