import random

ROUNDS = 3
MAX_TRIES = 16

def main():
    LEVEL = 1
    for i in range(ROUNDS):
        MAX_TRIES = 16
        print(f'Round number {LEVEL}/{ROUNDS}')
        print("Welcome to the Number Guessing Game!")
        print("I've chosen a number between 1 and 65,536.")
        print("Your mission is to guess this number within a limited number of attempts.")
        print("After each guess, I'll give you a clue to guide you closer to the answer.")
        print("Let's see if you can uncover the mystery within the given tries!")

        tries = 0
        true_value = random.randint(1, 65536)
        while MAX_TRIES > tries:
            guess = int(input('Enter your guess:\n'))
            tries += 1
            if guess > true_value:
                print("My number is lower.")
            elif guess < true_value:
                print("My number is higher.")
            else:
                LEVEL += 1
                print("Congratulations! You've guessed it right.")
                break
            
            if MAX_TRIES == tries:
                print('You have reached the maximum number of tries. Good luck with the next round!')
                exit()
                
    if LEVEL >= ROUNDS:  
        print("Congratulations! You've successfully completed all rounds.")
        print("Now, let's see if you can uncover the hidden message: 'ingeneer{worst-case_CoMp13Xi7Y_iS_O(l0G_N)}'")
        

if __name__ == "__main__":
    main()
