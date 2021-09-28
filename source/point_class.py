class Point:

    def __init__(self):
        pass

    def set_latitude(self, latitude):
        self.__latitude = latitude

    def set_longitude(self, longitude):
        self.__longitude = longitude

    def set_altitude(self, altitude):
        self.__altitude = altitude

    def set_instruction(self, instruction):
        self.__instruction = instruction

    def set_name(self, name):
        self.__name = name

    def get_latitude(self):
        return self.__latitude

    def get_longitude(self):
        return self.__longitude

    def get_altitude(self):
        return self.__altitude

    def get_instruction(self):
        return self.__instruction

    def get_name(self):
        return self.__name