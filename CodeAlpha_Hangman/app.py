import random

words = ["python", "hangman", "codealpha", "project", "developer"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = set()

print("===== HANGMAN GAME =====")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("You already used that letter!")
        continue

    used_letters.add(guess)

    if guess in word:
        print("Correct!")
        for i, ch in enumerate(word):
            if ch == guess:
                guessed[i] = guess
    else:
        print("Wrong!")
        attempts -= 1

if "_" not in guessed:
    print("\n🎉 YOU WON! The word was:", word)
else:
    print("\n❌ GAME OVER! The word was:", word)
