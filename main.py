import phonenumbers
from myPhone import number
import opencage
import folium
from phonenumbers import  geocoder

pepNumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepNumber,"en")
print(location)

from phonenumbers import  carrier
serviceProvider = phonenumbers.parse(number)
print(carrier.name_for_number(serviceProvider,"en"))

from opencage.geocoder import OpenCageGeocode

key = '333ca10042554a85922b4b7564dac205'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("myLocation.html")