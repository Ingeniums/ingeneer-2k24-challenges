import random
from secret import FLAG

with open('words.txt', 'r') as f:
    words = f.readlines()

def shuffle_string(s):
    char_list = list(s)
    random.shuffle(char_list)
    shuffled_string = ''.join(char_list)
    return shuffled_string

word_length = 5
max_attempts = 3
correct_guesses = 0
current_level = 1

print("Welcome to Wordle Again !")
print("Try to recover the secret word before getting shuffled in ", max_attempts, "attempts.")
print("The word has", word_length, "letters.")

for _ in range(3):  # Three levels
    secret_word = random.choice(words)[:-1]
    print("\nLevel", current_level)
    print("Here's your shuffled word:")
    shuffled_word = shuffle_string(secret_word)
    print(shuffled_word)

    guessed_word = ['-'] * word_length
    attempts = 0

    while attempts < max_attempts:
        print("\nAttempt", attempts + 1)
        print("Current word:", ''.join(guessed_word))

        guess = input("Enter your guess: ").lower()

        if len(guess) != word_length:
            print("Please enter a word with", word_length, "letters.")
            continue

        if guess == secret_word:
            print("Congratulations! You guessed the word correctly!")
            correct_guesses += 1
            break

        for i in range(word_length):
            if guess[i] == secret_word[i]:
                guessed_word[i] = guess[i]

        print("Incorrect guess. Keep trying!")
        attempts += 1

    if attempts == max_attempts:
        print("\nSorry, you've run out of attempts.")
        print("The secret word was:", secret_word)
        break  # Exit immediately if the user loses a round

    current_level += 1

# Check if the user guessed all three words correctly
if correct_guesses == 3:
    print("\nCongratulations! You've completed all levels.")
    print("Here's the flag:", FLAG)
else:
    print("\nYou did not complete all levels successfully. Better luck next time!")
