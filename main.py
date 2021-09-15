# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os

import fit_encode
import gpx_utilities
import bin_utilities
import fit_decode
import fit_utilities
import analysis

###################################################
# configuration

# location of input gpx file
inputgpx = 'TestTrack5.gpx'
outputfit = 'out.fit'

#defines tipe of files to be analyzed (options: none, fit)
analysis_mode = 'fit'




###################################################
# analyzing files

# function to help decode fit files
#analysis.analyze_fit_files(analysis_mode)


###################################################
# decoding input

#decoding gpx file
gpx_path = os.path.join(os.path.dirname(__file__) + '/files/' + inputgpx)
gpx_file = gpx_utilities.decode_gpx(gpx_path)

###################################################
# decoding input

# working with data


###################################################
# encoding output

#fit_path = os.path.join(os.path.dirname(__file__) + '/files/' + outputfit)
#fit_encode.encode_fit(fit_path)
print()


