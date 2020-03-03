optionID = []
#def fileIO(candidates):
f = open("options.txt",mode = "r",encoding = "utf-8")

#retrieves every line of the file and stores it into a list
options = f.read().split('\n')
print(options)
lineCount = 0

#creates and assigns numbers to the option ID list
optionID = [0] * len(options)
for i in range(len(optionID)):
    optionID[i] = i+1

#merges the optionID list with the options list
candidates = [list(i) for i in zip(optionID, options)]


for i in range (len(candidates)):
    candidates[i].append(0)
print(candidates) 

print ("Candidate ID:\tCandidate Name:")
for i in range (len(candidates)):
    for j in range (len(candidates[i]) - 1):
        print (candidates[i][j], end="\t\t")
    print()
f.close()



