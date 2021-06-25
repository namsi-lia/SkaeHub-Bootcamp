# import module
from geopy.geocoders import Nominatim

#Initialize Nominatim API
geolocator = Nominatim(user_agent="http")

#user input ZipCode
zipcode= input("Enter ZipCode :")

# Using geocode()
location = geolocator.geocode(zipcode)

print(location)