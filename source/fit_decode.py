
#code TBDs:
# fix conversion of int data (currently it is considered as UINT)
# fix register of ASCII data
# create class to agregate file data
import os

def byte_to_int(byte):
    if len(byte) == 2:
        return 256 * byte[1] + byte[0]
    elif len(byte) == 4:
        return 16777216 * byte[3] + 65536 * byte[2] + 256 * byte[1] + byte[0]
    else:
        return 0


def verify_header(expected_header, actual_header):
    # File header
    if expected_header != actual_header:
        print('header is erroneous')
        print('exp: ' + expected_header)
        print('act: ' + actual_header)
        return False
    else:
        return True


def decode_fit(fit_path):
    fit_file = open(fit_path, 'rb')

    error_id = 0


    bytes_in_current_word = 4
    byte = fit_file.read(bytes_in_current_word)

    # File header
    if not verify_header('0e106c00', byte.hex()):
        return 'Error in fit file ID=' +str(error_id)
    else:
        error_id += 1

    bytes_in_current_word = 4
    byte = fit_file.read(bytes_in_current_word)

    # File size information
    file_size = byte_to_int(byte) + 16
    size = os.path.getsize(fit_path)
    if file_size != size:
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1

    bytes_in_current_word = 4
    byte = fit_file.read(bytes_in_current_word)

    # File header
    if not verify_header('2e464954', byte.hex()):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1

    bytes_in_current_word = 2
    byte = fit_file.read(bytes_in_current_word)

    # Don't know what this data is
    unindentified_data = byte_to_int(byte)

    bytes_in_current_word = 31
    byte = fit_file.read(bytes_in_current_word)

    # File header
    if not verify_header('410000fe000801028402048503048504048505048506048607028408028401', byte.hex()):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1

    bytes_in_current_word = 2
    byte = fit_file.read(bytes_in_current_word)

    # Number of points
    number_of_points = byte_to_int(byte)

    bytes_in_current_word = 4
    byte = fit_file.read(bytes_in_current_word)

    # LAT NE Bounding Box
    lat_ne_bounding_box = byte_to_int(byte)

    bytes_in_current_word = 4
    byte = fit_file.read(bytes_in_current_word)

    # LAT SW Bounding Box
    lat_sw_bounding_box = byte_to_int(byte)

    bytes_in_current_word = 4
    byte = fit_file.read(bytes_in_current_word)

    # LON NE Bounding Box
    lon_ne_bounding_box = byte_to_int(byte)

    bytes_in_current_word = 4
    byte = fit_file.read(bytes_in_current_word)

    # LON SW Bounding Box
    lon_sw_bounding_box = byte_to_int(byte)

    bytes_in_current_word = 4
    byte = fit_file.read(bytes_in_current_word)

    # Total Distance
    total_distance = byte_to_int(byte)

    bytes_in_current_word = 2
    byte = fit_file.read(bytes_in_current_word)

    # Maximum altitude
    maximum_altitude = byte_to_int(byte)

    bytes_in_current_word = 2
    byte = fit_file.read(bytes_in_current_word)

    # Minimum altitude TBD??
    minimum_altitude = byte_to_int(byte)

    bytes_in_current_word = 9
    byte = fit_file.read(bytes_in_current_word)

    # File header
    if not verify_header('420000fb0001010284', byte.hex()):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1

    i = 0
    # iterate over alphabet
    alphabet_size = 0
    alphabet = []
    while i == 0:

        bytes_in_current_word = 1
        byte = fit_file.read(bytes_in_current_word)

        # verifies header correcteness and exit condition
        if '43' == byte.hex():
            break
        elif not verify_header('02', byte.hex()):
            return 'Error in fit file ID=' + str(error_id)
        else:
            error_id += 1

        bytes_in_current_word = 2
        byte = fit_file.read(bytes_in_current_word)

        alphabet.append(byte)
        alphabet_size += 1

    bytes_in_current_word = 9
    byte = fit_file.read(bytes_in_current_word)

    # File header
    if not verify_header('0000fd000101028403', byte.hex()):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1

    bytes_in_current_word = 2
    byte = fit_file.read(bytes_in_current_word)

    # Number of instructions
    number_of_instructions = byte_to_int(byte)

    bytes_in_current_word = 21
    byte = fit_file.read(bytes_in_current_word)

    # File header
    if not verify_header('440000fa0005010284020100030486040486052007', byte.hex()):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1

    # iterate over instructions (turns and POIs)
    i = 0
    instruction_point_identification = []
    instruction_type = []
    instruction_distance = []
    instruction_text = []
    while i == 0:
        bytes_in_current_word = 1
        byte = fit_file.read(bytes_in_current_word)

        # verifies header correcteness and exit condition
        if '45' == byte.hex():
            break
        elif not verify_header('04', byte.hex()):
            return 'Error in fit file ID=' + str(error_id)
        else:
            error_id += 1

        bytes_in_current_word = 2
        byte = fit_file.read(bytes_in_current_word)

        instruction_point_identification.append(byte_to_int(byte))

        bytes_in_current_word = 1
        byte = fit_file.read(bytes_in_current_word)

        instruction_type.append(byte)

        bytes_in_current_word = 4
        byte = fit_file.read(bytes_in_current_word)

        instruction_distance.append(byte_to_int(byte))

        bytes_in_current_word = 4
        byte = fit_file.read(bytes_in_current_word)

        if 'ffffffff' != byte.hex():
            if '00000000' != byte.hex():
                verify_header('ffffffff', byte.hex())
                verify_header('00000000', byte.hex())
                return 'Error in fit file ID=' + str(error_id)
            else:
                error_id += 1

        bytes_in_current_word = 32
        byte = fit_file.read(bytes_in_current_word)

        # TBD update to import data as ascii
        instruction_text.append(byte)

    if number_of_instructions != len(instruction_text):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1


    bytes_in_current_word = 9
    byte = fit_file.read(bytes_in_current_word)

    # File header
    if not verify_header('0000fc000101028405', byte.hex()):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1

    bytes_in_current_word = 2
    byte = fit_file.read(bytes_in_current_word)

    # Number of points (again?)
    number_of_points2 = byte_to_int(byte)

    if number_of_points != number_of_points2:
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1

    bytes_in_current_word = 15
    byte = fit_file.read(bytes_in_current_word)

    # File header
    if not verify_header('460000f90003010485020485030284', byte.hex()):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1

    # iterate over points
    i = 0
    point_latitude = []
    point_longitude = []
    point_altitude = []
    while i < number_of_points2:

        bytes_in_current_word = 1
        byte = fit_file.read(bytes_in_current_word)

        if not verify_header('06', byte.hex()):
            return 'Error in fit file ID=' + str(error_id)
        else:
            error_id += 1

        bytes_in_current_word = 4
        byte = fit_file.read(bytes_in_current_word)

        point_latitude.append(byte_to_int(byte))

        bytes_in_current_word = 4
        byte = fit_file.read(bytes_in_current_word)

        point_longitude.append(byte_to_int(byte))

        bytes_in_current_word = 2
        byte = fit_file.read(bytes_in_current_word)

        point_altitude.append(byte_to_int(byte))

        i += 1

    if lat_ne_bounding_box != max(point_latitude):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1
    if lat_sw_bounding_box != min(point_latitude):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1
    if lon_ne_bounding_box != max(point_longitude):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1
    if lon_sw_bounding_box != min(point_longitude):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1
    if maximum_altitude != max(point_altitude):
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1

    bytes_in_current_word = 2
    byte = fit_file.read(bytes_in_current_word)

    unindentified_data2 = byte_to_int(byte)
    if unindentified_data2 != 0:
        return 'Error in fit file ID=' + str(error_id)
    else:
        error_id += 1

    return 'Success in fit file'
