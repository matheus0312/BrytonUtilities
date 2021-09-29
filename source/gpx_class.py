import point_class
import boundaries_class
import copy

class Gpx:


    def __init__(self,gpx_path):
        self.__gpx_path = gpx_path
        self.__gpx_file = ''
        self.__gpx_lines = ''
        self.__current_line = ''
        self.__gpx_type = ''
        self.__current_point = point_class.Point()
        self.__points = []
        self.__current_number_of_items = 0
        self.__boundaries = boundaries_class.Boundary()

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

    def __search_for_lat_lon(self):
        if self.__current_line.find('lat=') != -1:
            self.__current_point.set_latitude(self.__current_line.split('"')[1])
            self.__current_point.set_longitude(self.__current_line.split('"')[3])
            self.__current_number_of_items += 2

    def __search_for_alt(self):
        if self.__current_line.find('<ele>') != -1 and self.__current_number_of_items > 0:
            self.__current_point.set_altitude(self.__current_line.lstrip().removeprefix('<ele>'))
            self.__current_number_of_items += 1

    def __search_for_ins(self):
        if self.__current_line.find('<type>') != -1 and self.__current_number_of_items > 0:
            self.__current_point.set_instruction(int(self.__current_line.lstrip().removeprefix('<type>')))
            self.__current_number_of_items += 1

    def __search_for_nam(self):
        if self.__current_line.find('<name>') != -1 and self.__current_number_of_items > 0:
            self.__current_point.set_name(self.__current_line.strip().removeprefix('<name>'))
            self.__current_number_of_items += 1

    def __point_is_complete(self):
        if self.__current_number_of_items%5 == 0 and self.__current_number_of_items != 0:
            self.__current_number_of_items = 0
            return True
        else:
            return False

    def __set_default_point(self):

        self.__current_point.set_latitude(0)
        self.__current_point.set_longitude(0)
        self.__current_point.set_altitude(0)
        self.__current_point.set_instruction(15)
        self.__current_point.set_name('')

    def __search_for_bound(self):
        if self.__current_line.find('<bounds') != -1:
            self.__boundaries.set_max_latitude(self.__current_line.split('"')[1])
            self.__boundaries.set_max_longitude(self.__current_line.split('"')[3])
            self.__boundaries.set_min_latitude(self.__current_line.split('"')[5])
            self.__boundaries.set_min_longitude(self.__current_line.split('"')[7])

    def __decode_ors(self):

        self.__open_ors()
        for self.__current_line in self.__gpx_lines:
            self.__current_line = '<' + self.__current_line


            self.__search_for_bound()
            self.__search_for_lat_lon()
            self.__search_for_alt()
            self.__search_for_ins()
            self.__search_for_nam()


            if self.__point_is_complete():
                # in here the append is adding a reference to current point, so all items are the same, need to understand how to fix it.
                self.__points.append(copy.deepcopy(self.__current_point))
                self.__set_default_point()

    def get_points(self):
        return self.__points

