# Library to work with .gpx files
import gpxpy
import os


#
def decode_gpx(gpx_path):
    gpx_file = open(gpx_path, 'r')
    gpx = gpxpy.parse(gpx_file)

    return gpx

# for track in gpx.tracks:
#     for segment in track.segments:
#         for point in segment.points:
#             print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.comment))
