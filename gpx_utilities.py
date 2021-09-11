# Library to work with .gpx files
# gpxpy needs to be installed
import geopy.distance
import gpxpy
from geopy import distance


#
def decode_gpx(gpx_path):
    gpx_file = open(gpx_path, 'r')
    gpx = gpxpy.parse(gpx_file)
    l=0
    for track in gpx.tracks:
        for segment in track.segments:
            for i in range (0,len(segment.points)-1):
                if segment.points[i].comment is not None:
                    if l is 1:
                        pass
                        #print(distance.distance((segment.points[i].latitude, segment.points[i].longitude),(lat,lon)))
                    lat = segment.points[i].latitude
                    lon = segment.points[i].longitude
                    l = 1
                #print(distance.distance((segment.points[i].latitude, segment.points[i].longitude), (segment.points[i+1].latitude, segment.points[i+1].longitude)).km)


    return gpx