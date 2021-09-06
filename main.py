# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import gpx_utilities
import zmap_utilities


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# gpx_path = os.path.join(os.path.dirname(__file__), 'files/', 'sample1.gpx')
# gpx_file = gpx_utilities.decode_gpx(gpx_path)

zmap_path = os.path.join(os.path.dirname(__file__), 'files/', '1465_1689.zmap')

zmap_utilities.decode_zmap(zmap_path)


# for track in gpx_file.tracks:
#     for segment in track.segments:
#         for point in segment.points:
#             print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.comment))