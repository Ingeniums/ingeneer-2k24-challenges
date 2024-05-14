from Crypto.Util.number import bytes_to_long as bl , long_to_bytes as lb 
from secret import FLAG


def func(lst, j):
    for _ in range(j):
        lst = lst[-1] + lst[:-1]
    return lst

final = lambda k: {"00": "Alpha", "01": "Beta", "10": "lydia", "11": "Gamma"}.get(k)

def book1(plain):
    enc = ''
    for i in range(0, len(plain), 3):
        enc += plain[i+2]
        enc += plain[i]
        enc += plain[i+1]
    return enc

def book2(plain):
    enc = []
    for c in plain:
        x = min(ord(c), -ord(c)%251)
        enc.append(lb(pow(x,2,251)))
    return enc

def book3(plain):
    enc = ''
    for i , c in enumerate(plain):
        j = i+1 % 8
        enc += func(bin(bl(c))[2:].zfill(8) , j)
    return enc 

def book4(plain):
    blocks = [ plain[i:i+8] for i in range(0,len(plain), 8)]
    enc = []
    for block in blocks:
        mini_blocks = [ block[i:i+2] for i in range(0,len(block), 2)]
        sub_enc =[]
        for k in mini_blocks:
            sub_enc.append(final(k))
        enc.append(sub_enc)
    return enc
            
def main():
    return str(book4(book3(book2(book1(FLAG)))))

if __name__ == "__main__":
    enc = main()
    with open('out.txt', 'w') as f:
      f.write(enc)


