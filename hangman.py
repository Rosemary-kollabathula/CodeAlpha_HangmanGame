import random

words = ["python", "apple", "coding", "computer", "student"]
word = random.choice(words)
guessed = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
display = ""
for letter in word:
if letter in guessed:
display += letter + " "
else:
display += "_ "

print("\nWord:", display)
print("Attempts left:", attempts)

if all(letter in guessed for letter in word):
    print("Congratulations! You won!")
    break

guess = input("Guess a letter: ").lower()

if len(guess) != 1 or not guess.isalpha():
    print("Enter only one letter!")
    continue

if guess in guessed:
    print("You already guessed that letter!")
elif guess in word:
    guessed.append(guess)
    print("Correct guess!")
else:
    guessed.append(guess)
    attempts -= 1
    print("Wrong guess!")

if attempts == 0:
print("Game Over! The word was:", word)