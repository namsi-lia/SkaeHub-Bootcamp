from geopy.geocoders import Nominatim
geolocator =Nominatim(user_agent="http")

state =input("Enter state of choice :")
#print("state name:",state)
location =geolocator.geocode(state)

latitude = location.latitude
longitude = location.longitude

# implement reverse function 
location = geolocator.reverse("{},{}".format(latitude, longitude))

# get city, state, and country of location
address = location.raw['address']
country = address.get('country', '')

print ('country :',country)
