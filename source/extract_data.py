from geopy import distance
#import requests
#import pandas as pd
import math

def get_mountains_data(mountain,distance_from_start,altitude_from_start):
    poi_name = []
    poi_type = []
    poi_distance = []
    poi_identification = []

    i=0
    while i < len(mountain)-1:
        distance = distance_from_start[mountain[i+1]]-distance_from_start[mountain[i]]
        altitude = altitude_from_start[mountain[i+1]]-altitude_from_start[mountain[i]]
        grade = (altitude/distance)*100
        climb_score = grade*distance

        if climb_score > 64000:
            cat='HC'
        elif climb_score > 48000:
            cat='1'
        elif climb_score > 32000:
            cat='2'
        elif climb_score > 16000:
            cat='3'
        elif climb_score > 8000:
            cat='4'
        else:
            cat='5'

        poi_name.append('C{} D{}km'.format(cat, round((distance_from_start[mountain[i+1]] - distance_from_start[mountain[i]]) / 1000.0, 2)))
        poi_type.append(b'\x64')
        poi_distance.append(distance_from_start[mountain[i]])
        poi_identification.append(mountain[i])

        #print('C{} D{}km'.format(cat, round((distance_from_start[mountain[i+1]] - distance_from_start[mountain[i]]) / 1000.0, 2)))
        print('C{} D{}km st{}m fin{}m G{}% A{}m'.format(cat, round(distance/1000, 2),round(distance_from_start[mountain[i]],2),round(distance_from_start[mountain[i+1]],2),grade,altitude))
        poi_name.append('C{} D{}km'.format(cat, round((distance_from_start[mountain[i+1]] - distance_from_start[mountain[i]]) / 1000.0, 2)))
        poi_type.append(b'\x65')
        poi_distance.append(distance_from_start[mountain[i+1]])
        poi_identification.append(mountain[i+1])
        i+=2

    points_of_interest=[poi_name, poi_type, poi_distance, poi_identification]
    return points_of_interest


def ordenate_mountains(mountain,mountains_found):


    j=0
    while j < len(mountain):
        i=0
        while i < len(mountain)-1:
            if mountain[i] > mountain[i+1]:
                temp = mountain[i+1]
                mountain[i+1] = mountain[i]
                mountain[i] = temp
            i+=1
        j+=1



    return mountain

def aggregate_mountains(mountain,distance_from_start,altitude_from_start):

    i=0
    mountains_found = 0
    while i < len(mountain) - 3:

        in_mountain=False
        current_distance=distance_from_start[mountain[i + 3]] - distance_from_start[mountain[i]]
        current_delta_altitude=altitude_from_start[mountain[i + 3]] - altitude_from_start[mountain[i]]
        if current_distance >= 500:
            grade=(current_delta_altitude / current_distance) * 100
            if (grade >= 3):
                climb_score=grade * current_distance
                if (climb_score >= 3500):
                    if not in_mountain:
                        mountain_start_point=mountain[i]
                        mountain_finish_point=mountain[i + 3]
                        in_mountain=True
        if in_mountain:
            mountain.remove(mountain[i])
            mountain.remove(mountain[i])
            mountain.remove(mountain[i])
            mountain.remove(mountain[i])
            mountain.append(mountain_start_point)
            mountain.append(mountain_finish_point)
            i+=2
        i+=2

    mountain = ordenate_mountains(mountain,mountains_found)

    return mountain

def safediv(num,den):
    if den == 0:
        if num == 0:
            return 0
        elif num >0:
            return 9999
        else:
            return -9999
    else:
        return num/den

def add_poi_to_instructions(instruction_distance,instruction_data,points_of_interest,name_data):
    poi_name=points_of_interest[0][0]
    poi_type=points_of_interest[0][1]
    poi_distance=points_of_interest[0][2]
    poi_identification=points_of_interest[0][3]

    for i in range(0,len(poi_name)):
        instruction_data.append(poi_type)
        instruction_distance.append(poi_distance)
        name_data.append(poi_name)


    return [instruction_data,instruction_distance,name_data,poi_identification]

#work in progress
def add_poi_by_climb(points_of_interest, point_attribute):
    distance_from_last_point=point_attribute[0]
    altitude_from_last_point=point_attribute[1]
    distance_from_start=point_attribute[2]
    altitude_from_start=point_attribute[3]
    mountain = []
    checkpoint_climb = []

    #start in second point
    i=1
    #iterates over all points excluding first and last to detect peaks and valleys
    while i < len(altitude_from_start)-1:
        # find peak
        if (altitude_from_start[i] > altitude_from_start[i+1]) and (altitude_from_start[i] > altitude_from_start[i-1]):
            checkpoint_climb.append(i)
            pass
        # find valley
        elif (altitude_from_start[i] < altitude_from_start[i+1]) and (altitude_from_start[i] < altitude_from_start[i-1]):
            checkpoint_climb.append(i)
            pass
        # find plane
        elif (altitude_from_start[i] == altitude_from_start[i + 1]) and (altitude_from_start[i] == altitude_from_start[i - 1]):
            checkpoint_climb.append(i)
            pass
        i+=1


    #iterates through peaks and climbs found above
    # detects if there is a climb between current and next point
    i= 0
    while i < len(checkpoint_climb)-1:
        in_mountain=False
        current_distance = distance_from_start[checkpoint_climb[i+1]] - distance_from_start[checkpoint_climb[i]]
        current_delta_altitude = altitude_from_start[checkpoint_climb[i+1]]- altitude_from_start[checkpoint_climb[i]]
        if current_distance >= 500:
            grade = (current_delta_altitude / current_distance) * 100
            if (grade >= 3):
                climb_score = grade * current_distance
                if (climb_score >= 3500):
                    if not in_mountain:
                        mountain_start_point = checkpoint_climb[i]
                        mountain_finish_point = checkpoint_climb[i+1]
                        in_mountain=True



        i += 1
        if in_mountain:
            mountain.append(mountain_start_point)
            mountain.append(mountain_finish_point)

    i=0
    while i < len(mountain)*2:
        mountain = aggregate_mountains(mountain,distance_from_start,altitude_from_start)
        i+=1

    points_of_interest = get_mountains_data(mountain,distance_from_start,altitude_from_start)

    return points_of_interest


def add_poi_by_distance(points_of_interest, point_attribute,inserted_poi):

    distance_from_last_point = point_attribute[0]
    altitude_from_last_point = point_attribute[1]

    poi_name = inserted_poi [0]
    poi_type = inserted_poi [1]
    poi_distance = inserted_poi [2]
    poi_identification = 0
    distance_from_start=0
    for i in range(0, len(point_attribute)):
        distance_from_start += distance_from_last_point[i]
        if float(poi_distance) < distance_from_start:
            poi_identification = i-1
            poi_distance = distance_from_start - distance_from_last_point[i]
            break

    points_of_interest.append([poi_name,poi_type,poi_distance,poi_identification])

    return points_of_interest


def calculate_points_attributes(latitude_data,longitude_data,altitude_data):


    distance_from_last_point = []
    delta_altitude_from_last_point = []
    distance_from_start =[]
    altitude_from_start = []

    distance_from_last_point.append(0)
    delta_altitude_from_last_point.append(0)
    distance_from_start.append(0)
    altitude_from_start.append(0)

    current_distance_from_start = 0
    current_altitude_from_start = 0
    for i in range(1, len(latitude_data)):
        current_point=(latitude_data[i] / 1000000, longitude_data[i] / 1000000)
        last_point=(latitude_data[i - 1] / 1000000, longitude_data[i - 1] / 1000000)
        current_distance = distance.distance(current_point, last_point).m
        distance_from_last_point.append(current_distance)
        current_distance_from_start += current_distance
        distance_from_start.append(current_distance_from_start)
        current_delta_altitude = (altitude_data[i] - altitude_data[i-1])
        delta_altitude_from_last_point.append(current_delta_altitude)
        current_altitude_from_start = (altitude_data[i]-altitude_data[0])/5
        altitude_from_start.append(current_altitude_from_start)
    point_attribute = [distance_from_last_point,delta_altitude_from_last_point,distance_from_start,altitude_from_start]

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

def calculate_number_data(instructions_data,points_of_interest):

    number_points = len(instructions_data)
    number_instructions = 0
    for instruction_point in instructions_data:
        if instruction_point != b'\xff':
            number_instructions += 1

    number_pois = len(points_of_interest[0])


    number_data = [number_points, number_instructions,number_pois]
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

def extract_attributes(decoded_data):

    latitude_data = decoded_data[0]
    longitude_data = decoded_data[1]
    altitude_data = decoded_data[2]
    instruction_data = decoded_data[3]
    name_data = decoded_data[4]
    points_of_interest = []


    lat_lon_bounding_box = calculate_lat_lon_bounding_box(latitude_data, longitude_data)

    total_distance = calculate_total_distance(latitude_data,longitude_data)

    alt_bounding_box = calculate_alt_bounding_box(altitude_data)

    instruction_distance = calculate_instruction_distance(instruction_data,latitude_data,longitude_data)

    point_attribute = calculate_points_attributes(latitude_data,longitude_data,altitude_data)

    #points_of_interest = add_poi_by_distance(points_of_interest, point_attribute,inserted_poi)

    points_of_interest = add_poi_by_climb(points_of_interest, point_attribute)

    number_data = calculate_number_data(instruction_data,points_of_interest)

    decoded_data = [latitude_data,longitude_data,altitude_data,instruction_data,name_data]

    extracted_attributes = [lat_lon_bounding_box,total_distance,alt_bounding_box,number_data,instruction_distance,points_of_interest]

    return  [extracted_attributes,decoded_data]

