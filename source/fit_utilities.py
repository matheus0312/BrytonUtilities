class alphabet:
    def __init__(self):
        for i in range(0,1500):
            # 1 byte
            header_1 = b'\x02'
            # 2 bytes
            alphabet_instruction = i

class instruction:
    def __init__(self):
        # 1 byte
        header_1 = b'\x04'
        # 2 bytes
        instruction_identification = 0
        # 1 byte
        instruction_instruction = 0
        # 4 bytes
        instruction_distance = 0
        # 4 bytes
        header_2 = 0 #b'\xFF\xFF\xFF\xFF' OR b'\x00\x00\x00\x00'
        # 32 bytes
        instruction_description = 0

class point:
    def __init__(self):
        # 1 byte
        header_1 = b'\x06'
        # 4 bytes
        point_latitude = 0
        # 4 bytes
        point_longitude = 0
        # 2 bytes
        point_altitude = 0


class fit_data:

    def __init__(self):
        # 4 bytes
        header_1=b'\x0E\x10\x6C\x00'
        # 2 bytes
        file_size = 0
        # 4 bytes
        header_2=b'\x2E\x46\x49\x54'
        # 2 bytes
        checksum_1=b'\x00\x00'

        # 32 bytes
        header_3=b'\x41\x00\x00\xFE\x00\x08\x01\x02\x84\x02\x04\x85\x03\x04\x85\x04\x04\x85\x05\x04\x85\x06\x04\x86\x07\x02\x84\x08\x02\x84\x01'
        # 2 bytes
        number_of_points = 0
        # 4 bytes
        lat_neb_bounding_box = 0
        # 4 bytes
        lat_sw_bounding_box = 0
        # 4 bytes
        lon_ne_bounding_box = 0
        # 4 bytes
        lon_sw_bounding_box = 0
        # 4 bytes
        total_distance = 0
        # 2 bytes
        maximum_altitude = 0
        # 2 bytes
        minimum_altitude = 0

        # 9 bytes
        header_4=b'\x42\x00\x00\xFB\x00\x01\x01\x02\x84'
        # 3 bytes x n
        fit_alphabet=alphabet()

        # 10 bytes
        header_5=b'\x43\x00\x00\xFD\x00\x01\x01\x02\x84\x03'
        # 2 bytes
        number_of_instructions = 0

        # 21 bytes
        header_6=b'\x44\x00\x00\xFA\x00\x05\x01\x02\x84\x02\x01\x00\x03\x04\x86\x04\x04\x86\x05\x20\x07'
        # 44 bytes x n
        fit_instruction=instruction()

        # 10 bytes
        header_7=b'\x45\x00\x00\xFC\x00\x01\x01\x02\x84\x05'
        # 2 bytes
        number_of_points2 = 0

        # 15 bytes
        header_8=b'\x46\x00\x00\xF9\x00\x03\x01\x04\x85\x02\x04\x85\x03\x02\x84'
        # 11 bytes x n
        points = []
        # 2 bytes
        checksum_2=b'\x00\x00'

def decode_fit(fit_path):
    fit_file=open(fit_path, 'rb')

    fit_file.read()

    fit_contents = fit_data()


