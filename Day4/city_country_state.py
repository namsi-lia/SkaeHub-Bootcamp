from geopy.geocoders import Nominatim
geolocator =Nominatim(user_agent="http")

state =input("Enter state of choice :")
location =geolocator.geocode(state)


print(location.address)
