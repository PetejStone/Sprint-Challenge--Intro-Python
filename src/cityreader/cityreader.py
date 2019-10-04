# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
    def __init__(self, name, lat, lon):
      self.name = name
      self.lon = lon
      self.lat = lat
    def __repr__(self):
        return f"City{repr(self.name), repr(self.lat), repr(self.lon)}".replace("'","")

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv
cities = []

with open('cities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
           # print(f'\tCity: {row[0]}, State: {row[1]}, County: {row[2]}, Lat: {row[3]}, Lon: {row[4]}, Population: {row[5]}, Density: {row[6]}, Timezone: {row[7]}, Zips: {row[8]}')
            line_count += 1

            
            cities.append(City(row[0], float(row[3]), float(row[4])))
    print(f'Processed {line_count} lines.')

#print(cities)

def cityreader():  
    return cities

cityreader()

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# todooo Get latitude and longitude values from the user

# lat1 = input('Please enter lat coordinates: ')
# lon1 = input('Please enter lon coordinaties: ')

# lat2 = input('Please enter lat2 coordinates: ')
# lon2 = input('Please enter lon2 coordinates: ')


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
   
    # Setting up an array to hold range of latitudes 
    lat_range = []
    if lat2 < lat1: # if lat2 is > that lat 1 we want it to be the first in the range (from lowest to greatest)
        for number in range(lat2,lat1): #get all numbers from lat2 to lat1
            lat_range.append(number) # append each number to the lat range array
    else: #if lat 1 is the bigger number, we want that to be first
        for number in range(lat1,lat2): #get all numbers from lat1 to lat2
            lat_range.append(number) #append each number to the lat range array

        
    lon_range = [] # getting a range of numbers for longitude
    if lon2 < lon1:   # same as above but with lon
        for number2 in range(lon2,lon1):
            lon_range.append(number2)
    else:
        for number2 in range(lon1,lon2):
            lon_range.append(number2)

    
    within = [] #empty within array to add cities in if they are within range
    for c in cities: #loop through all cities
        # if the city's longitude is long_range AND latitude is in lat_range
        if c.lon//1 in lon_range and c.lat//1 in lat_range: # //1 truncates all numbers that have decimal as no decimals are in our range, just whole numbers
            within.append(c) #if they are withing range, append the whole city to the within array
            print(within)
      
            # if 35.1055 in range(lat_range[0], lat_range[len(lat_range) -1]):
            #     print('True')
            # else:
            #     print('False')
        #print(lon_range)


  
  # todooo Ensure that the lat and l
  # on valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

    return within
