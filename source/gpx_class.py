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


    def __decode_ors(self):

        self.__open_ors()

        for self.__line in self.__gpx_lines:
            self.__line = '<' + self.__line

            # work in progress
