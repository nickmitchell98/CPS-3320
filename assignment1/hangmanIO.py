
def fileIO(A):
        import random
        f = open("words.txt",mode = "r",encoding = "utf-8") 
        #print(f.read())
        lineCount = 0
        with open("words.txt") as wordFile:
        	for i in wordFile:
        		lineCount+=1
        #print(lineCount)
        #Generates random number "rand" to pick a word randomly
        endRand = lineCount - 1
        #print(endRand)
        rand = random.randint(0,endRand)

        #print(rand)
        file = open('words.txt')
        all_lines = file.readlines()
        word = all_lines[rand]
        wordLength = len(word) - 1
        #print(word)
        f.close()

       #Appends each character of the word into a list called A
        for i in range (wordLength):
                A.append(word[i])
L = []
A = []
fileIO(A)
#generates L same length of A in '_'
for i in range(len(A)):
        L.append('_')
print(*L)
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
                        print("word was: ",*A)

