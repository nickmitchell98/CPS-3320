# Hangman game!
# Assume the answer is a list in list "words"
import random
#list of different words
words = [
['h','a','n','g','m','a','n'],
['c','o','m','p','u','t','e','r'],
['s','c','i','e','n','c','e'],
['g','r','e','a','t']
]
#Generates random number "rand" to pick a word randomly
endRand = len(words) - 1
rand = random.randint(0,endRand)
A = words[rand]
L = []
#generates L same length of A in '_'
for i in range(len(A)):
	L.append('_')
#wrong is a counter for how many times the user answered wrong
wrong = 0
play = True
while play == True:
	# Ask the user to guess a letter
	letter = str(input("Guess a letter: "))
	#makes the program not case sensitive
	letter = letter.lower()
	# Check to see if that letter is in the Answer
#if the letter is part of the word
	if letter in A:
		for currentletter in A:

			# If the letter the user guessed is found in the answer,
			# set the underscore in the user's answer to that letter

			for i in range (len(L)):
				if letter == A[i]:
					L[i] = letter
			
		# Display what the player has thus far (L) with a space
		# separating each letter
		print(' '.join(str(n) for n in L))
		# Test to see if the word has been successfully completed,
		# and if so, end the loop
		if A == L:
			play = False
			print("GREAT JOB!")
	

	#If the letter not part of the word
	else:
		print(' '.join(str(n) for n in L))

		print ("BAD GUESS!")
		#one more wrong answer
		wrong+=1
		#If the user guesses wrong six times, the game will end
		if wrong == 6:
			play = False
			print("GAME OVER!")
	
