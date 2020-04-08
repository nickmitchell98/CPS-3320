#from PIL import Image
import json
from covid import Covid
import pydantic


# by default data source is "john_hopkins"
covid = Covid()

# or
covid = Covid(source="john_hopkins")

#Get Country id's
countries = json.dumps(covid.list_countries())

print (countries) 
#print("Country ID: " ,countries["id"] , "Country Name: " , countries["name"])


# get all data
world = json.dumps(covid.get_data())
#print(world)

#get stats by country
print (countries.id, countries.name) 

USA = json.dumps(covid.get_status_by_country_name("US"))
print(USA)


#See recovered

totalRecovered = covid.get_total_recovered()

print("Total Recovered Worldwide: ", totalRecovered)