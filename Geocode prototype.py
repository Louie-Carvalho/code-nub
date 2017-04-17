import os
from geopy.geocoders import GoogleV3 # ensure the GeoCoding plugin is installed
geocoder = GoogleV3()

file = os.path.abspath("C:\\Python27\\address.txt") #specify the file path in " ", folders serapated with \\

for line in file:
    location = geocoder.geocode(line)
    print location.address, location.longitude, location.latitude