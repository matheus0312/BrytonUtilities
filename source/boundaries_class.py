class Boundary:

    def __init__(self):
        self.__max_latitude = 0
        self.__min_latitude = 0
        self.__max_longitude = 0
        self.__min_longitude = 0
        self.__max_altitude = 0
        self.__min_altitude = 0

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