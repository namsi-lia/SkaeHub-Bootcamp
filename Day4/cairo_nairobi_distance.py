#import geodesic module 
from geopy.distance import geodesic
#initialize lattitude and longitude values of  Nairobi and Cairo

cairo = (30.0444, 31.235)
nairobi = (1.2921, 36.8219)
  
# Print the distance calculated in km
print(geodesic(cairo, nairobi).km)
