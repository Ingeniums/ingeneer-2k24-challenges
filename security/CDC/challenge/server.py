from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from os import urandom 
from Crypto.Util.number import long_to_bytes as lb
from secret import FLAG

key = urandom(8)
IV = urandom(8)
BLOCK_SIZE = 8


initial_msg = '##################### Helllllo #############################\n'+\
              'Authentificate first so you can continue'



def encrypt( plaintext ,key=key, iv=IV):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = pad(plaintext, BLOCK_SIZE)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext.hex()

def decrypt(ciphertext,key=key, iv=IV):
    ciphertext = bytes.fromhex(ciphertext)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def check(dec):
    if b'admin=1&authentificated=true' in dec and b'admin=0' not in dec :
        return 1 
    return 0 

def authentificate():
    user = input('username:')
    if not user or "admin"  in user:
        print("Invalid username")
        exit()
    return 'user=' + user +'&admin=0&authentificated=true'

def main():
    print(initial_msg)
    session = authentificate().encode()
    enc = encrypt(session)
    print('Your encrypted session: '+str(enc))
    print('############### Only Admins are allowed hear : ################')
    while True :
        enc_session = input('Give me your session : ')
        try :
            dec_session =decrypt(enc_session)
            if (check(dec_session)):
                print('GG here is your flag ' + str(FLAG))
            else :
                print('Still not an admin , Here is Your session '+ str(dec_session))
        except Exception as e:
            print(str(e))
            exit()
            
if __name__ == '__main__':
    main()
