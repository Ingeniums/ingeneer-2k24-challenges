import random
from secret import FLAG 
with open('words.txt' , 'r') as f:
    words = f.readlines()



secret_word = random.choice(words)[:-1]
word_length =  5 

max_attempts = 5
guessed_word = ['-'] * word_length

print("Welcome to Wordle!")
print("Try to guess the secret word in", max_attempts, "attempts.")
print("The word has", word_length, "letters.")

attempts = 0
while attempts < max_attempts:
    print("\nAttempt", attempts + 1)
    print("Current word:", ''.join(guessed_word))

    guess = input("Enter your guess: ").lower()

    if len(guess) != word_length:
        print("Please enter a word with", word_length, "letters.")
        continue

    if guess == secret_word:
        print("Congratulations! You guessed the word correctly Here's the Flag:")
        print(FLAG.decode())
        break

    for i in range(word_length):
        if guess[i] == secret_word[i]:
            guessed_word[i] = guess[i]
        elif guess[i] in secret_word:
            print(f"The letter '{guess[i]}' is in the word, but in the wrong position.")

    print("Incorrect guess. Keep trying!")

    attempts += 1

if attempts == max_attempts:
    print("\nSorry, you've run out of attempts.")
    print("The secret word was:", secret_word)
