import hangman_data
# from hangman_data import ...
import random

print(hangman_data.logo)

chosen_word = hangman_data.word_list[random.randint(0, len(hangman_data.word_list) - 1)]

display = ['_' for i in range(len(chosen_word))]

lives = 6

win = False

while lives > 0:
    guess = input("Guess your letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}. Pick a different letter.")
        continue

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives = lives - 1

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess

    print(f"{' '.join(display)}")

    if "_" not in display:
        print("You win!")
        win = True
        break

    print(hangman_data.stages[lives])

if not win:
    print("You lose!")
    print(f"The word was {chosen_word}!")
