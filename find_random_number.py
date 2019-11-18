import random

guessed = False
guess_number = random.randrange(0, 100,1)

print("-"*40)
print("Find the number!")

while guessed == False:
	typed_number = int(input("Please select number between 0 and 100: "))

	if guess_number == typed_number:
		print("You guessed the number")
		guessed = True
	else:
		if guess_number > typed_number:
			print("The number you have to guess is lower than the you typed. Try again!")
		else:
			print("The number you have to guess is higher than the you typed. Try again!")