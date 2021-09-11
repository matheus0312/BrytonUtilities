# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import gpx_utilities
import bin_utilities
import fit_utilities

filename = 'VoltaAelDouglas-1'

# gpx_path = os.path.join(os.path.dirname(__file__), + '/files/', filename + '.gpx')
# gpx_file = gpx_utilities.decode_gpx(gpx_path)

# print('tinfo')
# tinfo_path = os.path.join(os.path.dirname(__file__) + '/files/', filename + '.tinfo')
# tinfo_file = bin_utilities.decode_bin(tinfo_path)
#
# print('smy')
# smy_path = os.path.join(os.path.dirname(__file__) + '/files/', filename + '.smy')
# smy_file = bin_utilities.decode_bin(smy_path)
#
# print('zinfo')
# zinfo_path = os.path.join(os.path.dirname(__file__) + '/files/',  filename + '/'+ filename + '.zinfo')
# zinfo_file = bin_utilities.decode_bin(zinfo_path)

print('fit')
fit_path = os.path.join(os.path.dirname(__file__) + '/files/', filename + '.fit')
fit_file = bin_utilities.decode_bin(fit_path)



