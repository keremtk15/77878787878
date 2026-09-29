import random

# Generate a secret number between 1 and 50
secret = random.randint(1, 50)
max_attempts = 5
current_attempt = 0
won = False

print("=== Welcome to the Number Guessing Game! ===")
print("I have picked a secret number between 1 and 50.")
print(f"You have {max_attempts} attempts to guess it. Good luck!\n")

while current_attempt < max_attempts and not won:
    # Read the player's guess using int(input())
    guess = int(input(f"Attempt {current_attempt + 1}/{max_attempts} - Enter your guess: "))
    
    if guess == secret:
        print(f"\n🎉 Congratulations! You guessed the secret number {secret} correctly!")
        won = True
    else:
        current_attempt += 1
        remaining_lives = max_attempts - current_attempt
        
        # Hint system based on absolute distance
        diff = abs(guess - secret)
        if diff <= 3:
            print("🔥 Hot!", end=" ")
        elif diff <= 8:
            print("🌡️ Warm!", end=" ")
        elif diff <= 15:
            print("🥶 Cold!", end=" ")
        else:
            print("🧊 Ice cold!", end=" ")
            
        # Extra hint for direction
        if guess < secret:
            print("(Go higher!)")
        else:
            print("(Go lower!)")
            
        # Show remaining hearts using a for loop
        print("Remaining lives: ", end="")
        for _ in range(remaining_lives):
            print("❤️", end="")
        print("\n" + "-" * 40)

# Loss message / reveal if attempts run out
if not won:
    print(f"\n❌ Game Over! You've run out of attempts.")
    print(f"The secret number was: {secret}")