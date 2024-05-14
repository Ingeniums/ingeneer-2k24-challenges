import os

MAX_TRIES = 3

def main():
    total1 = os.environ.get('TOTAL_1')
    total2 = os.environ.get('TOTAL_2')

    # FIRST ROUND
    # os.fork() or (os.fork() and os.fork()) or os.fork() or (os.fork() and os.fork()) or os.fork() or os.fork()

    # SECOND ROUND
    # for _ in range(20):
    #     os.fork()

    tries = 0
    while(MAX_TRIES > tries):
        print("FIRST ROUND")
        print("os.fork() or (os.fork() and os.fork()) or os.fork() or (os.fork() and os.fork()) or os.fork() or os.fork()")
        guess = input('Total number of process from the first round is\n')
        tries += 1
        if(guess == total1):
            print("Damn you are good!")
            break
        elif(tries == MAX_TRIES):
            print('Better luck next time!')
            exit()
        else:
            print("Nope, try again")
    
    tries = 0
    while(MAX_TRIES > tries):
        print("SECOND ROUND")
        print("for _ in range(20):\n\tos.fork()")
        guess = input('Total number of process from the second round is\n')
        tries += 1
        if(guess == total2):
            print("Damn you are good!")
            print("ingeneer{y0u_4r3_4mr4n3_f4v_stud3nt}")
            exit()
        elif(tries == MAX_TRIES):
            print('Better luck next time!')
            exit()
        else:
            print("Nope, try again")
        
    exit()      


if __name__ == "__main__":
    main()