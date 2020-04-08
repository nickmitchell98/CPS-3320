import arrow
import time

now = arrow.now()
tDate = arrow.now().format('MM/DD/YYYY')
curtime = arrow.now().format('hh:mm:ss A')
timeZone = arrow.now().format('ZZZ')

print("Today is ",tDate," It is currently ",curtime, "and the timezone is ",timeZone)

#West Coast
print("On the west coast it is",now.to('US/Pacific').format('hh:mm:ss A'))
print("On the east coast it is",now.to('EDT').format('hh:mm:ss A'))

#print("The current time was ",now.shift(hours=timeZone).humanize(), ago)
#
#Using the now class, this prints out 
#prints "in 30 seconds"
sec30 = now.shift(seconds=30).humanize()
print(sec30)
#prints "15 minutes ago"
min15 = now.shift(minutes=-15)#.humanize()
print("John posted a photo",min15)
#prints "In 5 hours"
hr5 = now.shift(hours=5).humanize()
print("This project will de done",hr5)
#a month ago
day25 = now.shift(days=-30).humanize()
print("Joe finished the project",day25)


