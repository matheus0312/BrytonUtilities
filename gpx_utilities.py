# Library to work with .gpx files
# gpxpy needs to be installed
# geopy needs to be installed
import gpxpy
# from geopy import distance


#
from gpxpy.gpx import GPX


def decode_gpx(gpx_path):
    gpx_file = open(gpx_path, 'r')
    #gpx: GPX = gpxpy.parse(gpx_file)
    latitude = []
    longitude = []
    altitude = []
    instruction = []
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
        if line.find('<cmt>') !=-1:
            ins = line.lstrip().removeprefix('<cmt>').removesuffix('</cmt>\n')
            instruction.pop()
            instruction.append(ins)
        if line.find('<ele>') != -1:
            alt = line.lstrip().removeprefix('<ele>').removesuffix('</ele>\n')
            altitude.pop()
            altitude.append(alt)

    decoded_gpx = [latitude,longitude,altitude,instruction]

    return decoded_gpx
        #if line.find()

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


    return gpx