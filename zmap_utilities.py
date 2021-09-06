

def decode_zmap(zmap_path):
    zmap_file = open(zmap_path, 'rb')

    byte = zmap_file.read(1)
    byte2 = zmap_file.read(1)
    byte3 = zmap_file.read(1)
    byte4 = zmap_file.read(1)
    while byte != b'':
        print(byte, byte2, byte3, byte4)
        byte = zmap_file.read(1)
        byte2 = zmap_file.read(1)
        byte3 = zmap_file.read(1)
        byte4 = zmap_file.read(1)

    # return zmap_file