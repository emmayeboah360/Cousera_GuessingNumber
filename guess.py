import random

# Set the secret_number variable here (between 1 and 10)
secret_number = 5
# Initialize the guess variable here with a value of 0
guess = 0
while  secret_number != guess:
	 # Add the while loop condition here
	guess = random.randint(1, 10)
	print("Guessing:",guess)

print("I guessed the right number! It was",secret_number)
