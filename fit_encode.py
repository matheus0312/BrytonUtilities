import struct
from geopy import distance

def write_instructions(fit_file):
    for i in range (0,50): #TBD Update number of points
        # 1 byte
        byte=b'\x04'
        fit_file.write(byte)

        # 2 bytes
        # instruction identification
        instruction_identification = 0
        byte = struct.pack('<H',instruction_identification)
        fit_file.write(byte)

        # 1 bytes
        # instruction direction
        instruction_direction = 0
        byte = struct.pack('<H',instruction_identification)
        fit_file.write(byte)

        # 4 bytes
        # instruction distance
        instruction_distance = 0
        byte=struct.pack('<I', instruction_identification)
        fit_file.write(byte)

        # 4 bytes
        # header FF FF FF FF

        # 32 bytes
        # instruction description


def write_alphabet(fit_file):

    for i in range(0, 1500):
        # 1 byte
        byte=b'\x02'
        fit_file.write(byte)
        # 2 bytes
        alphabet_instruction=i
        byte = struct.pack('<H',alphabet_instruction)
        fit_file.write(byte)


def encode_fit (fit_path):

    fit_file = open(fit_path, 'wb')

    # 4 bytes
    # header
    byte = b'\x0E\x10\x6C\x00'
    fit_file.write(byte)

    # 4 bytes
    # file size
    file_size = 0
    byte = struct.pack('<i',file_size)
    fit_file.write(byte)

    # 4 bytes
    # header
    byte = b'\x2E\x46\x49\x54'
    fit_file.write(byte)

    # 2 bytes
    # checksum
    byte=b'\x00\x00'
    fit_file.write(byte)

    # 32 bytes
    # header
    byte=b'\x41\x00\x00\xFE\x00\x08\x01\x02\x84\x02\x04\x85\x03\x04\x85\x04\x04\x85\x05\x04\x85\x06\x04\x86\x07\x02\x84\x08\x02\x84\x01'
    fit_file.write(byte)

    # 2 bytes
    # number of points
    number_points = 0
    byte=struct.pack('<H',number_points)
    fit_file.write(byte)

    # 4 bytes
    # lat ne bounding box
    lat_ne_bounding_box = 0
    byte = struct.pack('<i',lat_ne_bounding_box)
    fit_file.write(byte)

    # 4 bytes
    # lat sw bounding box
    lat_sw_bounding_box = 0
    byte = struct.pack('<i',lat_sw_bounding_box)
    fit_file.write(byte)

    # 4 bytes
    # lon ne bounding box
    lon_ne_bounding_box = 0
    byte = struct.pack('<i',lon_ne_bounding_box)
    fit_file.write(byte)

    # 4 bytes
    # lon sw bounding box
    lon_sw_bounding_box = 0
    byte = struct.pack('<i',lon_sw_bounding_box)
    fit_file.write(byte)

    # 4 bytes
    # total distance in meters
    total_distance = 0
    byte=struct.pack('<I', total_distance)
    fit_file.write(byte)

    # 2 bytes
    # maximum altitude
    maximum_altitude = 0
    byte=struct.pack('<H',maximum_altitude)
    fit_file.write(byte)

    # 2 bytes
    # minimum altitude
    minimum_altitude = 0
    byte=struct.pack('<H',maximum_altitude)
    fit_file.write(byte)

    # 9 bytes
    # header
    byte=b'\x42\x00\x00\xFB\x00\x01\x01\x02\x84'
    fit_file.write(byte)

    write_alphabet(fit_file)

    # 10 bytes
    # header
    byte=b'\x43\x00\x00\xFD\x00\x01\x01\x02\x84\x03'
    fit_file.write(byte)

    # 2 bytes
    number_instructions = 0
    byte=struct.pack('<H', number_instructions)
    fit_file.write(byte)

    # 21 bytes
    # header
    byte=b'\x44\x00\x00\xFA\x00\x05\x01\x02\x84\x02\x01\x00\x03\x04\x86\x04\x04\x86\x05\x20\x07'
    fit_file.write(byte)

    write_instructions(fit_file)




    # 15 bytes
    # header
    byte=b'\x46\x00\x00\xF9\x00\x03\x01\x04\x85\x02\x04\x85\x03\x02\x84'
    fit_file.write(byte)

