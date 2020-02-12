#Function "letterScore" defines score of letter
def letterScore(letter):
	if letter in 'AEILNORSTU':
		return 1
	elif letter in 'DG':
		return 2
	elif letter in 'BCMP':
		return 3
	elif letter in 'FHVWY':
		return 4
	elif letter == 'K':
		return 5
	elif letter in 'JX':
		return 8
	elif letter in 'QZ':
		return 10
		#If letter isn't from A to Z
	else:
		return 0
#determines the score of word "word" entered by user
def wordScore(word):
	score = 0
	length = len(word)
	for i in range(length):
		score += letterScore(word[i])
	return score
word = input("Enter a word: ")
#This makes the input word from the user not case sensitive
word = word.upper()
print("Word Entered: ", word)
print("Your Score: ", wordScore(word))


