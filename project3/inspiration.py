import requests as req
import datetime
import csv
import matplotlib.pyplot as plt

#File personalStats.csv required
#quote API
url = "https://freequote.herokuapp.com/"

#Load quote into dictionary
response = req.request("GET", url)
data = response.json()

#print quote
print(data["quote"])

#Print author
if len(data["author"]) > 0:
	print("–",data["author"],"\n")
else:
	#Anonymous authors tend to be blank. This replaces the empty string with "Anonymous"
	print("– Anonymous\n")

goal = input("What are your goals for today? ")

#affirmative Statement
print("Today I will",goal+ "!\n")

print("For the following questions will be answered on a scale of 1 to 10.")
print("1 being the worst and 10 being the best\n")

#This makes sure that the user enters a number between 1 and 10
while True:
	try:
		mood = int(input("How am I feeling today? "))
		if mood > 0 and mood <= 10:
			break
		else:
			print("Number is not between 1 and 10. Try again! ")
	except ValueError:
		print("That is not a valid number.  Try again")

while True:
	try:
		motivation = int(input("How motivated am I to achieve my goal today? "))
		if motivation > 0 and motivation <= 10:
			break
		else:
			print("Number is not between 1 and 10. Try again! ")
	except ValueError:
		print("That is not a valid number.  Try again")

#currentdate
curdate = datetime.datetime.now()
curdt = curdate.strftime("%x")
writeValue = str( mood) + "," + str(motivation) + "," + curdt + "\n"
file = open('personalStats.csv','a')

file.write(writeValue)
file.close()

data = list(csv.reader(open('personalStats.csv')))

#1 to skip file header

moods = []
motivations = []
dates = []

#Separate 2d array for graphs
for i in range (1,len(data)):
	moods.append(int(data[i][0]))
	motivations.append(int(data[i][1]))
	dates.append(data[i][2])

print("\nThis is a list of the days (refer to graphs)\n")
for i in range (len(dates)):
	print("\tDay", i, "––––––––––", dates[i])


#moods graph
f1 = plt.figure(1)
plt.title(data[0][0])
plt.ylabel("R 1 = 10")
plt.xlabel("Days")
plt.plot(moods)



#Motivations graph
f2 = plt.figure(2)
plt.plot(motivations)
plt.ylabel("Range 1 = 10")
plt.xlabel("Days")
plt.title(data[0][1])

#Figures 1 and 2 will show in a separate window
plt.show()
