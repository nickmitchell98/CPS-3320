from covid import Covid
import json


# by default data source is The Johns Hopkins API
covid = Covid()

# or
covid = Covid(source="john_hopkins")

#Get Country id's
countries = json.dumps(covid.list_countries(),sort_keys = True, indent = 4)
countryData = json.loads(countries)


print("This is a list of infected countries associated with their id's:")
#neatly prints out countries
for i in countryData:
	print("CountryName:",i['name'])
	print("Country ID:",i['id'])
	print()
print()
print()


# get all data
world = json.dumps(covid.get_data(), sort_keys = True, indent = 4)
worldData = json.loads(world)

print("This is a list of world data by countries:")
#neatly prints out world data
for i in worldData:
	print("Country Name:",i['country'])
	print("Country ID:",i['id'])
	print("Total Confirmed Cases: ",i['confirmed'])
	print("Total Existing Cases: ",i['active'])
	print("Total Deaths:",i['deaths'])
	print("Total Recovered: ",i['recovered'])
	print("Country", i['country'], "is located at", i["longitude"], "longitude and",i["latitude"],"latitude.")
	print()
print()
print()


#get stats by country

USA = json.dumps(covid.get_status_by_country_name("US"), sort_keys = True, indent = 4)
US = json.loads(USA)

#Retrieved Data from US
print("This is a list of data specifically from the US:")
print("Country ID:",US['id'])
print("Country:", US['country'])
print("Country", US['country'],"currently has",US['confirmed'],"cases")
print("Total Existing Cases: ",US['active'])
print("Deaths", US['country'],":",US['deaths'])
print("Recovered in", US['country'],":",US['confirmed'])
print("Country", US['country'], "is located at", US["longitude"], "longitude and",US["latitude"],"latitude.")
print()
print()


#Prints World Total

totalRecovered = covid.get_total_recovered()
totalDeaths = covid.get_total_deaths()
Confirmed = covid.get_total_confirmed_cases()
Existing = covid.get_total_active_cases()

print("This is a list of the world data as a whole")
print("Confirmed Cases Worldwide: ", Confirmed)
print("Existing Cases Worldwide: ", Existing)
print("Total Deaths Worldwide: ", totalDeaths)
print("Total Recovered Worldwide: ", totalRecovered)