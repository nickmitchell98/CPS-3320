from operator import itemgetter
optionID = []

#print candidates prints all of the candidates with their id's
def printCandidates():
    print ("Candidate ID:\tCandidate Name:")
    for i in range (len(candidates)):
        for j in range (len(candidates[i]) - 1):
            print (candidates[i][j], end="\t\t")
        print()
f = open("options.txt",mode = "r",encoding = "utf-8")

'''retrieves every line of the file and stores it into a list. 
 Each line of the file is a new element.'''
options = f.read().split('\n')
f.close()
#creates and assigns numbers to the option ID list
optionID = [0] * len(options)
for i in range(len(optionID)):
    optionID[i] = i+1

#merges the optionID list with the options list
candidates = [list(i) for i in zip(optionID, options)]

#adds the vote count to the candidates array
for i in range (len(candidates)):
    candidates[i].append(0)

printCandidates()

#retreives vote from the user
while True:
                try:
                    vote = int(input("Please vote for candidate by candidate ID: "))
                    break
                except ValueError:
                    print("That is not a number.  Try again")

if vote in optionID:
    candidates [vote - 1][2] += 1
    keepRunning = input("Are there any other voters? y/n: ").lower()
    while keepRunning == "y":
        printCandidates()
        while True:
                try:
                    vote = int(input("Please vote for candidate by candidate ID: "))
                    break
                except ValueError:
                    print("That is not a number.  Try again")
        if vote in optionID:
            candidates [vote - 1][2] += 1
            keepRunning = input("Are there any other voters? y/n: ").lower()
        else:
            print ("Invalid Number! Please Try Again!!")
            while True:
                try:
                    vote = int(input("Please vote for candidate by candidate ID: "))
                    break
                except ValueError:
                    print("That is not a number.  Try again")
        if keepRunning == "n":
            break
else:
    print ("Invalid Number! Please Try Again!!")
    vote = int(input("Please vote for candidate by candidate ID: "))
    keepRunning = input("Are there any other voters? y/n: ").lower()
    while keepRunning == "y":
        printCandidates()
        while True:
                try:
                    vote = int(input("Please vote for candidate by candidate ID: "))
                    break
                except ValueError:
                    print("That is not a number.  Try again")
        if vote in optionID:
            candidates [vote - 1][2] += 1
            keepRunning = input("Are there any other voters? y/n: ").lower()
        else:
            print ("Invalid Number! Please Try Again!!")
            while True:
                try:
                    vote = int(input("Please vote for candidate by candidate ID: "))
                    break
                except ValueError:
                    print("That is not a number.  Try again")
            
        if keepRunning == "n":
            break
candidatesSort = sorted(candidates, key=itemgetter(2))
candidatesSort.reverse()

print("Results:")
print("Place:\tCandidate:\tNumber of Votes:")
for i in range(len(optionID)):
    print(optionID[i], "\t", candidatesSort[i][1], "\t\t", candidatesSort[i][2], end="\n")