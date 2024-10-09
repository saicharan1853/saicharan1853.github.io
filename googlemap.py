import googlemaps
from datetime import datetime

# Initialize the Google Maps client
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# 1. Geocoding an address to get its coordinates
address = "VNIT Nagpur"
geocode_result = gmaps.geocode(address)
print(f"Geocode result for {address}: {geocode_result}")

# 2. Directions from VNIT to Nagpur Railway Station
origin = "VNIT Nagpur"
destination = "Nagpur Railway Station"
directions_result = gmaps.directions(origin, destination, mode="driving", departure_time=datetime.now())
print(f"Directions from {origin} to {destination}: {directions_result}")

# 3. Distance between VNIT and Nagpur Airport
distance_result = gmaps.distance_matrix(origin, "Nagpur Airport", mode="driving")
print(f"Distance between {origin} and Nagpur Airport: {distance_result}")

# 4. Finding nearby places (e.g., restaurants) around VNIT
places_result = gmaps.places_nearby(location=geocode_result[0]['geometry']['location'], radius=1000, type='restaurant')
print(f"Nearby restaurants around VNIT: {places_result}")

# 5. Reverse Geocoding (getting address from coordinates)
coordinates = (21.1236, 79.0511)
reverse_geocode_result = gmaps.reverse_geocode(coordinates)
print(f"Reverse geocode result for {coordinates}: {reverse_geocode_result}")
