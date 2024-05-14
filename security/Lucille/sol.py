from Crypto.Util.number import bytes_to_long as bl , long_to_bytes as lb , inverse  

def legendre(a, p):
    return pow(a, (p - 1) // 2, p)


def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


def final_reverse(element):
    element_map = {"Alpha": "00", "Beta": "01", "lydia": "10", "Gamma": "11"}
    return element_map.get(element)  


def reverse_func(lst, j):
    for _ in range(j):
        lst = lst[1:] + lst[0]
    return lst


def reverse_book2(enc):
    plain = []
    for c in enc:
        plain.append(min(tonelli(bl(c),251) , -tonelli(bl(c),251)%251))
    return bytes(plain)


def reverse_book1(enc):
    plain = ''
    enc = enc.decode()
    for i in range(0, len(enc), 3):
        plain += enc[i+1]
        plain += enc[i+2]
        plain += enc[i]
    return plain


def reverse_book3(enc):
    plain = []
    enc = [ enc[k:k+8] for k in range(0, len(enc) , 8)]
    for i , c in enumerate(enc):
        j = i+1 % 8
        plain.append(lb(int(reverse_func(c, j),2)))
    return plain 



def reverse_book4(enc):
    blocks = []
    for sub_enc in enc:
        block = ""
        for element in sub_enc:
            binary = final_reverse(element)  
            if binary:  
                block += binary
        blocks.append(block)
    return "".join(blocks)


with open('./challenge/out.txt' , 'r') as f :
    ct = f.read()


ctt = eval(ct)


print(reverse_book1(reverse_book2(reverse_book3(reverse_book4(ctt)))))