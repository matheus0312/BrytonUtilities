import codecs

def decode_bin(bin_path):
    bin_file = open(bin_path, 'rb')
    bytes_in_word = 1
    byte = bin_file.read(bytes_in_word)
    count = 2
    ascii_contents = list()
    bin_contents = list()
    line_bytes = 3
    while byte != b'':

        # print(codecs.decode(byte, encoding = 'utf-8', errors = 'ignore')+' ',end = '')
        ascii_contents.append(codecs.decode(byte, encoding = 'latin-1', errors = 'ignore'))
        print(byte.hex(),end = '')
        # if count%2:
        #     print(' ',end='')
        if count == line_bytes+1:
            print('')
            for char in ascii_contents:
                print(char,end=' ')
            ascii_contents.clear()
            print('')
            count = 1
        byte = bin_file.read(bytes_in_word)
        count += 1
    print('')
    return bin_contents