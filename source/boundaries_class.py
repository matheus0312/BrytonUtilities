class Boundary:

    def __init__(self):
        self.__max_latitude = 0
        self.__min_latitude = 999999999999
        self.__max_longitude = 0
        self.__min_longitude = 999999999999
        self.__max_altitude = 0
        self.__min_altitude = 999999999999

    def set_max_latitude(self,inp):
        self.__max_latitude = float(inp)

    def set_min_latitude(self,inp):
        self.__min_latitude = float(inp)

    def set_max_longitude(self,inp):
        self.__max_longitude = float(inp)

    def set_min_longitude(self,inp):
        self.__min_longitude = float(inp)

    def set_max_altitude(self,inp):
        self.__max_altitude = float(inp)

    def set_min_altitude(self,inp):
        self.__min_altitude = float(inp)

    def get_max_latitude(self):
        return self.__max_latitude

    def get_min_latitude(self):
        return self.__min_latitude

    def get_max_longitude(self):
        return self.__max_longitude

    def get_min_longitude(self):
        return self.__min_longitude

    def get_max_altitude(self):
        return self.__max_altitude

    def get_min_altitude(self):
        return self.__min_altitude