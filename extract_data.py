from geopy import distance
#import requests
#import pandas as pd


#work in progress
def add_poi_by_climb(points_of_interest, point_attribute):
    distance_from_last_point=point_attribute[0]
    altitude_from_last_point=point_attribute[1]

    grade = []
    for i in range (0, len(distance_from_last_point)-1):
        grade.append((altitude_from_last_point[i+1]-altitude_from_last_point[i])/(distance_from_last_point[i+1]-distance_from_last_point[i])*100)
    grade.append(0)

    return points_of_interest


def add_poi_by_distance(points_of_interest, point_attribute,inserted_poi):

    distance_from_last_point = point_attribute[0]
    altitude_from_last_point = point_attribute[1]

    poi_name = inserted_poi [0]
    poi_type = inserted_poi [1]
    poi_distance = inserted_poi [2]
    distance_from_start=0
    for i in range(0, len(point_attribute)):
        distance_from_start += distance_from_last_point[i]
        if poi_distance > distance_from_start:
            poi_identification = i-1
            poi_distance = distance_from_start - distance_from_last_point[i]
            break

    points_of_interest.append([poi_name,poi_type,poi_distance])

    return points_of_interest


def calculate_points_attributes(latitude_data,longitude_data,altitude_data):

    distance_from_last_point = []
    delta_altitude_from_last_point = []

    distance_from_last_point.append(0)
    delta_altitude_from_last_point(0)

    for i in range(1, len(latitude_data)):
        current_point=(latitude_data[i] / 1000000, longitude_data[i] / 1000000)
        last_point=(latitude_data[i - 1] / 1000000, longitude_data[i - 1] / 1000000)
        distance_from_last_point.append(distance.distance(current_point, last_point).m)
        delta_altitude_from_last_point.append(altitude_data[i] - altitude_data[i-1])

    point_attribute = [distance_from_last_point,delta_altitude_from_last_point]

    return point_attribute


def calculate_instruction_distance(instruction_data,latitude_data,longitude_data):

    current_instruction_point = (latitude_data[0], longitude_data[0])
    #iterates over each point excluding last
    current_instruction_distance = 0
    instruction_distance = []
    instruction_distance.append(0)
    for i in range(0,len(instruction_data)-1):

        current_point = (latitude_data[i]/1000000, longitude_data[i]/1000000)
        next_point = (latitude_data[i+1]/1000000, longitude_data[i+1]/1000000)
        current_instruction_distance += distance.distance(current_point, next_point).m

        if instruction_data[i+1] != b'\xff':
            instruction_distance.append(int(float(current_instruction_distance)))
            current_instruction_distance = 0
        else:
            instruction_distance.append(int(0))




    return instruction_distance



# script for returning elevation from lat, long, based on open elevation data
# which in turn is based on SRTM
#def get_elevation(lat, long):
#    query = ('https://api.open-elevation.com/api/v1/lookup'
#             f'?locations={lat},{long}')
#    r = requests.get(query).json()  # json object, various ways you can extract value
#    # one approach is to use pandas json functionality:
#    elevation = pd.json_normalize(r, 'results')['elevation'].values[0]
#    return elevation

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
        if instruction_point != b'\xff':
            number_instructions += 1

    number_data = [number_points, number_instructions]
    return number_data

def calculate_alt_bounding_box(altitude_data):

    maximum_altitude = max(altitude_data)
    minimum_altitude = min(altitude_data)

    alt_bounding_box = [maximum_altitude, minimum_altitude]
    return alt_bounding_box

def calculate_distance_between_points(latitude_data,longitude_data):

    #iterates over each point excluding last
    distance_between_points = []
    for i in range(0,len(latitude_data)-1):
        current_point = (latitude_data[i]/1000000,longitude_data[i]/1000000)
        next_point = (latitude_data[i+1]/1000000,longitude_data[i+1]/1000000)
        distance_between_points.append(distance.distance(current_point,next_point).m)

    return total_distance

def calculate_total_distance(latitude_data,longitude_data):

    #iterates over each point excluding last
    total_distance = 0
    for i in range(0,len(latitude_data)-1):
        current_point = (latitude_data[i]/1000000,longitude_data[i]/1000000)
        next_point = (latitude_data[i+1]/1000000,longitude_data[i+1]/1000000)
        total_distance +=  distance.distance(current_point,next_point).m

    return total_distance


def calculate_lat_lon_bounding_box(latitude_data, longitude_data):

    #maximum latitude
    lat_ne_bounding_box = max(latitude_data)
    #minimum latitude
    lat_sw_bounding_box = min(latitude_data)
    #maximum longitude
    lon_ne_bounding_box = max(longitude_data)
    #minimum longitude
    lon_sw_bounding_box = min(longitude_data)

    lat_lon_bounding_box = [lat_ne_bounding_box, lat_sw_bounding_box, lon_ne_bounding_box, lon_sw_bounding_box]
    return lat_lon_bounding_box

def extract_attributes(decoded_data,inserted_poi):

    latitude_data = decoded_data[0]
    longitude_data = decoded_data[1]
    altitude_data = decoded_data[2]
    instruction_data = decoded_data[3]
    points_of_interest = []

    lat_lon_bounding_box = calculate_lat_lon_bounding_box(latitude_data, longitude_data)

    total_distance = calculate_total_distance(latitude_data,longitude_data)

    alt_bounding_box = calculate_alt_bounding_box(altitude_data)

    number_data = calculate_number_data(instruction_data)

    instruction_distance = calculate_instruction_distance(instruction_data,latitude_data,longitude_data)

    point_attribute = calculate_points_attributes(latitude_data,longitude_data,altitude_data)

    points_of_interest = add_poi_by_distance(points_of_interest, point_attribute,inserted_poi)

    points_of_interest = add_poi_by_climb(points_of_interest, point_attribute)

    extracted_attributes = [lat_lon_bounding_box,total_distance,alt_bounding_box,number_data,instruction_distance]

    return  extracted_attributes