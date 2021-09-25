import point_class

class Gpx:


    def __init__(self,gpx_path):
        self.__gpx_path = gpx_path

    def decode_gpx(self):
        self.__find_gpx_type()
        if self.__gpx_type == 'ors':
            self.__decode_ors()

    def __find_gpx_type(self):
        self.__gpx_file = open(self.__gpx_path, 'r')
        line = self.__gpx_file.read()
        self.__gpx_file.close()
        if '<name>openrouteservice</name>' in line:
            self.__gpx_type = 'ors'
        else:
            # to be updated with other gpx types
            gpx_type = 'gmaps'

    def __open_ors(self):
        self.__gpx_file = open(self.__gpx_path,'r')
        self.__gpx_lines = self.__gpx_file.read()
        # breaks single line file in multiple lines
        self.__gpx_lines = self.__gpx_lines.split('<')

    def __set_latitude(self,point):

        if self.__line.find('lat=') != -1:
            point

    def __search_for_lat_lon(self):
        if self.__line.find('lat=') != -1:
            self.__point.set_latitude(self.__line.split('"')[1])
            self.__point.set_longitude(self.__line.split('"')[3])
            self.__number_of_items += 1

    def __search_for_alt(self):
        if self.__line.find('<ele>') != -1 and self.__number_of_items > 0:
            self.__point.set_altitude(self.__line.lstrip().removeprefix('<ele>'))
            self.__number_of_items += 1

    def __search_for_ins(self):
        if self.__line.find('<type>') != -1 and self.__number_of_items > 0:
            self.__point.set_instruction(int(self.__line.lstrip().removeprefix('<type>')))
            self.__number_of_items += 1

    def __search_for_nam(self):
        if self.__line.find('<name>') != -1 and self.__number_of_items > 0:
            self.__point.set_name(self.__line.strip().removeprefix('<name>'))
            self.__number_of_items += 1

    def __point_is_complete(self):
        if self.__number_of_items%5 == 0:
            return True
        else:
            return False

    def __decode_ors(self):

        self.__open_ors()

        self.__point = point_class.Point()
        self.__points = []
        self.__number_of_items = 0

        for self.__line in self.__gpx_lines:
            self.__line = '<' + self.__line

            self.__search_for_lat_lon()
            self.__search_for_alt()
            self.__search_for_ins()
            self.__search_for_nam()

            if self.__point_is_complete():
                self.__points.append(self.__point)

