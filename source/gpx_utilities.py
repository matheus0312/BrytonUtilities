# Library to work with .gpx files
# gpxpy needs to be installed
# geopy needs to be installed
import gpxpy
# from geopy import distance

from sys import argv
from os.path import splitext
from struct import pack
import re

from gpxpy.gpx import GPX

orst2brt = {
0: 3,
1: 2,
2: 7,
3: 6,
4: 5,
5: 4,
6: 1,
7: 10,
8: 8,
9: 12,
10: 1,
11: 1,
12: 9,
13: 8,
14: 1
    }



def decode_gpx_ors(gpx_path):
    gpx_file = open(gpx_path,'r')
    gpx_file = gpx_file.read()
    # breaks single line file in multiple files
    gpx_file = gpx_file.split('<')

    latitude = []
    longitude = []
    altitude = []
    instruction = []
    name = []
    number_items = 0
    for line in gpx_file:
        line = '<'+line
        if line.find('lat=') != -1:
            lat = line.split('"')[1]
            latitude.append(lat)
            lon = line.split('"')[3]
            longitude.append(lon)
            ins = 15
            instruction.append(ins)
            alt = 0
            altitude.append(alt)
            nam = 'none'
            name.append(nam)
            number_items +=1
        elif line.find('<type>') != -1 and number_items>0:
            ins = int(line.lstrip().removeprefix('<type>'))
            instruction.pop()
            instruction.append(ins)
        elif line.find('<name>') != -1 and number_items>0:
            nam = line.strip().removeprefix('<name>')
            name.pop()
            name.append(nam)
        elif line.find('<ele>') != -1 and number_items>0:
            alt = line.lstrip().removeprefix('<ele>')
            altitude.pop()
            altitude.append(alt)

    for i in range(0,len(name)-1):
        if name[i] == name[i+1]:
            instruction[i+1] = 15
    decoded_gpx = [latitude, longitude, altitude, instruction,name]
    return decoded_gpx

def decode_gpx_gmaps(gpx_path):
    gpx_file = open(gpx_path, 'r')
    latitude = []
    longitude = []
    altitude = []
    instruction = []
    name = []
    for line in gpx_file:
        ins = 'null'
        if line.find('lat=') != -1:
            lat = line.split('"')[1]
            latitude.append(lat)
            lon = line.split('"')[3]
            longitude.append(lon)
            ins = 'none'
            instruction.append(ins)
            alt = 0
            altitude.append(alt)
            nam = ''
            name.append(nam)
        if line.find('<cmt>') !=-1:
            ins = line.lstrip().removeprefix('<cmt>').removesuffix('</cmt>\n')
            instruction.pop()
            instruction.append(ins)
        if line.find('<ele>') != -1:
            alt = line.lstrip().removeprefix('<ele>').removesuffix('</ele>\n')
            altitude.pop()
            altitude.append(alt)

    decoded_gpx = [latitude,longitude,altitude,instruction,name]

    return decoded_gpx
        #if line.find()

def decode_gpx(gpx_path):
    gpx_file=open(gpx_path, 'r')
    line = gpx_file.read()
    if '<name>openrouteservice</name>' in line:
        decoded_gpx = decode_gpx_ors(gpx_path)
    else:
        decoded_gpx = decode_gpx_gmaps(gpx_path)


  #  l=0
   # for track in gpx.tracks:
    #    for segment in track.segments:
     #       for i in range (0,len(segment.points)-1):
      #          if segment.points[i].comment is not None:
       #             if l is 1:
        #                pass
         #               #print(distance.distance((segment.points[i].latitude, segment.points[i].longitude),(lat,lon)))
          #          lat = segment.points[i].latitude
           #         lon = segment.points[i].longitude
            #        l = 1
             #   #print(distance.distance((segment.points[i].latitude, segment.points[i].longitude), (segment.points[i+1].latitude, segment.points[i+1].longitude)).km)


    return decoded_gpx