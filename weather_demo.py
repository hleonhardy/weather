
#http://api.wunderground.com/api/Your_Key/conditions/q/CA/San_Francisco.json

from urllib2 import urlopen
from json import load

################################ DEMO ##########################################


#get API key from https://www.wunderground.com/
api_key = "insert your key here!"


print "Please enter the state (2 letter abbreviation, e.g. WA, CA, AZ, etc): "
state = raw_input("> ")
#making it so it fits the URL format
state = state.upper()
state = state.strip()

print "Please enter the city: "
city_before = raw_input("> ")
#making it so it fits the URL format
#cities are capitalized and words are separated by underscores
city_before = city_before.title()
city_before = city_before.strip()
city = city_before.replace(" ", "_")


api_url = "http://api.wunderground.com/api/{}/conditions/q/{}/{}.json".format(api_key, state, city)
response = urlopen(api_url)
json_obj = load(response)


#different things I picked out from the api
#object is a dictionaries with other dictionaries inside of it:
#the first dictionary is current observation and the others are inside of current observation
current_obs = json_obj["current_observation"]
weather = current_obs["weather"]
windchill_f = current_obs["windchill_f"]
wind_mph = current_obs["wind_mph"]
feelslike_f = current_obs["feelslike_f"]
temp_f = current_obs["temp_f"]


print "The temperature(f) in {}, {} is {} degrees.".format(city_before, state, temp_f)
print "Skies are {}.".format(weather)