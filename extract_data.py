from main import gpx_file
from geopy import distance


def extract_data(gpx:gpx_file):

    total_distance = 0

    for track in gpx.tracks:
        for segment in track.segments:
            for i in range (0,len(segment.points)):
                total_distance += distance.distance((segment.points[i].latitude, segment.points[i].longitude), (segment.points[i+1].latitude, segment.points[i+1].longitude)).km)
            for point in segment.points:
                lat = points

                latitude
                lon = point..longitude