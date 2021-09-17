import unidecode

def convert_input_units(decoded_data):
    latitude_data = decoded_data[0]
    longitude_data = decoded_data[1]
    altitude_data = decoded_data[2]
    instruction_data = decoded_data[3]
    name_data = decoded_data[4]

    latitude_data_converted=[]
    longitude_data_converted=[]
    altitude_data_converted=[]
    instruction_data_converted=[]
    name_data_converted=[] #tbd update

    # converting lat, lon and alt to units used in .fit files
    for latitude in latitude_data:
        latitude_data_converted.append(int(float(latitude)*1000000))
    for longitude in longitude_data:
        longitude_data_converted.append(int(float(longitude)*1000000))
    for altitude in altitude_data:
        altitude_data_converted.append(int((float(altitude)*5)+2500))

    for instruction in instruction_data:
        if instruction == 0:
            ins = b'\x03' # left
        elif instruction == 1:
            ins = b'\x02' # right
        elif instruction == 2:
            ins = b'\x07' # close left
        elif instruction == 3:
            ins = b'\x06' # close right
        elif instruction == 4:
            ins = b'\x05' # slight left
        elif instruction == 5:
            ins = b'\x04' # slight right
        elif instruction == 6:
            ins = b'\x01' # go ahead
        elif instruction == 7:
            ins = b'\x01' # go ahead
        elif instruction == 8:
            ins = b'\x08' # exit right
        elif instruction == 9:
            ins = b'\x07' # uturn left
        elif instruction == 10:
            ins = b'\x01' # go ahead
        elif instruction == 11:
            ins = b'\x01' # go ahead
        elif instruction == 12:
            ins = b'\x09' # exit left
        elif instruction == 13:
            ins = b'\x08' # exit right
        elif instruction == 14:
            ins = b'\x01' # go ahead
        else:
            ins = b'\xff' # none
        instruction_data_converted.append(ins)

    for name in name_data:
        name = unidecode.unidecode(name)

        name = name.replace('A(c)','e')
        name = name.replace('A!','a')
        name = name.replace('A\'','o')
        name=name.replace('ASS', 'c')
        name=name.replace('APS', 'a')
        name=name.replace('A3', 'o')

        name = name.replace('Rua','R')
        name = name.replace('Avenida', 'Av')
        name = name.replace('Professora', 'Prf')
        name = name.replace('Professor', 'Prf')
        name = name.replace('Doutora', 'Dr')
        name = name.replace('Doutor', 'Dr')
        name = name.replace('Estrada', 'Est')

        name = name.replace('Eduardo', 'Edu')
        name = name.replace('Monte', 'Mt')
        name = name.replace('Viaduto', 'Via')
        name=name.replace('Passagem', 'Ps')
        name=name.replace('NAvel', 'Nv')
        name = name.replace('Engenheira', 'Eng')
        name = name.replace('Engenheiro', 'Eng')
        name = name.replace('Marechal', 'Mrc')



        name_data_converted.append(name[:32])

        print()


    decoded_data = [latitude_data_converted,longitude_data_converted,altitude_data_converted,instruction_data_converted,name_data_converted]

    return decoded_data