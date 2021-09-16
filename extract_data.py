from geopy import distance
import requests
import pandas as pd

def calculate_instruction_distance(instruction_data,latitude_data,longitude_data):

    current_instruction_point = (latitude_data[0], longitude_data[0])
    #iterates over each point excluding last
    current_instruction_distance = 0
    instruction_distance = []
    for i in range(0,len(instruction_data)-1):

        current_point = (latitude_data[i], longitude_data[i])
        next_point = (latitude_data[i+1], longitude_data[i+1])
        current_instruction_distance += distance.distance(current_point, next_point).m

        if instruction_data[i+1] != 'none':
            instruction_distance.append(current_instruction_distance)
            current_instruction_distance = 0
        else:
            instruction_distance.append(0)




    return instruction_distance



# script for returning elevation from lat, long, based on open elevation data
# which in turn is based on SRTM
def get_elevation(lat, long):
    query = ('https://api.open-elevation.com/api/v1/lookup'
             f'?locations={lat},{long}')
    r = requests.get(query).json()  # json object, various ways you can extract value
    # one approach is to use pandas json functionality:
    elevation = pd.json_normalize(r, 'results')['elevation'].values[0]
    return elevation

def add_altitude_data(decoded_data):

    latitude_data = decoded_data[0]
    longitude_data = decoded_data[1]
    altitude_data = decoded_data[2]
    instruction_data = decoded_data[3]

    for i in range(0,len(latitude_data)):
        altitude_data[i] = get_elevation(latitude_data[i],longitude_data[i])

    decoded_data = [latitude_data, longitude_data, altitude_data, instruction_data]
    return decoded_data

def calculate_number_data(instructions_data):

    number_points = len(instructions_data)
    number_instructions = 0
    for instruction_point in instructions_data:
        if instruction_point != 'none':
            number_instructions += 1

    number_data = [number_points, number_instructions]
    return number_data

def calculate_alt_bounding_box(altitude_data):

    maximum_altitude = altitude_data[0]
    minimum_altitude = altitude_data[0]
    for altitude_point in altitude_data:
        if altitude_point > maximum_altitude:
            maximum_altitude = altitude_point
        elif altitude_point < minimum_altitude:
            minimum_altitude = altitude_point

    alt_bounding_box = [maximum_altitude, minimum_altitude]
    return alt_bounding_box


def calculate_total_distance(latitude_data,longitude_data):

    #iterates over each point excluding last
    total_distance = 0
    for i in range(0,len(latitude_data)-1):
        current_point = (latitude_data[i],longitude_data[i])
        next_point = (latitude_data[i+1],longitude_data[i+1])
        total_distance +=  distance.distance(current_point,next_point).m

    return total_distance


def calculate_lat_lon_bounding_box(latitude_data, longitude_data):

    #maximum latitude
    lat_ne_bounding_box = latitude_data[0]
    #minimum latitude
    lat_sw_bounding_box = latitude_data[0]
    for latitude_point in latitude_data:
        if latitude_point > lat_ne_bounding_box:
            lat_ne_bounding_box = latitude_point
        elif latitude_point < lat_sw_bounding_box:
            lat_sw_bounding_box = latitude_point

    #maximum longitude
    lon_ne_bounding_box = longitude_data[0]
    #minimum longitude
    lon_sw_bounding_box = longitude_data[1]
    for longitude_point in longitude_data:
        if longitude_point > lon_ne_bounding_box:
            lon_ne_bounding_box = longitude_point
        elif longitude_point < lon_sw_bounding_box:
            lon_sw_bounding_box = longitude_point

    lat_lon_bounding_box = [lat_ne_bounding_box, lat_sw_bounding_box, lon_ne_bounding_box, lon_sw_bounding_box]
    return lat_lon_bounding_box

def extract_attributes(decoded_data):

    latitude_data = decoded_data[0]
    longitude_data = decoded_data[1]
    altitude_data = decoded_data[2]
    instruction_data = decoded_data[3]

    lat_lon_bounding_box = calculate_lat_lon_bounding_box(latitude_data, longitude_data)

    total_distance = calculate_total_distance(latitude_data,longitude_data)

    alt_bounding_box = calculate_alt_bounding_box(altitude_data)

    number_data = calculate_number_data(instruction_data)

    instruction_distance = calculate_instruction_distance(instruction_data,latitude_data,longitude_data)


    extracted_attributes = [lat_lon_bounding_box,total_distance,alt_bounding_box,number_data,instruction_distance]

    return  extracted_attributes