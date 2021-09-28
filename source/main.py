import gpx_utilities
import bin_utilities
import fit_decode
import fit_encode
import fit_utilities
import analysis
import extract_data
import units_conversion
from sys import argv
import gpx_class

###################################################
# configuration

# Creates an object gpx located at the input location
gpx = gpx_class.Gpx(argv[1])





###################################################
# analyzing files

# function to help decode fit files


###################################################
# decoding input

#decoding gpx file
gpx.decode_gpx()

gpx_points = gpx.get_points()

latitude = []
longitude = []
altitude = []
instruction = []
name = []
for gpx_point in gpx_points:
    latitude.append(gpx_point.get_latitude())
    longitude.append(gpx_point.get_longitude())
    altitude.append(gpx_point.get_altitude())
    instruction.append(gpx_point.get_instruction())
    name.append(gpx_point.get_name())
print()

decoded_data = [latitude, longitude, altitude, instruction, name]
decoded_data_old = gpx_utilities.decode_gpx_ors(argv[1])
###################################################
# working with data

decoded_data = units_conversion.convert_input_units(decoded_data)
#INSERTED_POI = [POI NAME, POI ID, DISTANCE FROM START IN METERS]
#inserted_poi = ['BIG', b'\x66', 40000]

[extrated_attributes, decoded_data] = extract_data.extract_attributes(decoded_data)

###################################################
# encoding output

fit_path = argv[1].replace('.gpx','.fit')
fit_encode.encode_fit(fit_path,decoded_data,extrated_attributes)


