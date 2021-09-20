# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import gpx_utilities
import bin_utilities
import fit_decode
import fit_encode
import fit_utilities
import analysis
import extract_data
import units_conversion
from sys import argv

###################################################
# configuration

# location of input gpx file
gpx_path = argv[1]

#defines tipe of files to be analyzed (options: none, fit)
analysis_mode = 'none'




###################################################
# analyzing files

# function to help decode fit files
analysis.analyze_fit_files(analysis_mode)


###################################################
# decoding input

#decoding gpx file
decoded_data = gpx_utilities.decode_gpx(gpx_path)

###################################################
# working with data

decoded_data = units_conversion.convert_input_units(decoded_data)
#INSERTED_POI = [POI NAME, POI ID, DISTANCE FROM START IN METERS]
#inserted_poi = ['BIG', b'\x66', 40000]

[extrated_attributes, decoded_data] = extract_data.extract_attributes(decoded_data)

###################################################
# encoding output

fit_path = gpx_path.replace('.gpx','.fit')
fit_encode.encode_fit(fit_path,decoded_data,extrated_attributes)


