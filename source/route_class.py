import copy

import boundaries_class
import point_class
from geopy import distance
import unidecode
import poi_class

class Route:

    def __init__(self,points,boundaries):
        self.__current_point = point_class.Point()
        self.__points = points
        self.__number_of_points = 0
        self.__boundaries = boundaries
        self.__length = 0
        self.__poi = poi_class.Poi()
        self.__pois = []

    def __calculate_length(self):
        first_point = True
        for point in self.__points:
            if first_point:
                first_point = False
                last_point = point.convert_lat_lon()
            else:
                current_point = point.convert_lat_lon()
                self.__length += distance.distance(current_point,last_point).m
                last_point = point.convert_lat_lon()

    def __calculate_num_points(self):
        self.__number_of_points = len(self.__points)

    def __calculate_alt_bound_box(self):
        for point in self.__points:
            if (self.__boundaries.get_max_altitude()) < (point.get_altitude()):
               self.__boundaries.set_max_altitude(point.get_altitude())
            elif (self.__boundaries.get_min_altitude()) > (point.get_altitude()):
               self.__boundaries.set_min_altitude(point.get_altitude())

    def __translate_instruction(self):
        if self.__current_point.get_instruction() == 0:
            self.__current_point.set_instruction('left')
        elif self.__current_point.get_instruction() == 1:
            self.__current_point.set_instruction('right')
        elif self.__current_point.get_instruction() == 2:
            self.__current_point.set_instruction('close left')
        elif self.__current_point.get_instruction() == 3:
            self.__current_point.set_instruction('close right')
        elif self.__current_point.get_instruction() == 4:
            self.__current_point.set_instruction('slight left')
        elif self.__current_point.get_instruction() == 5:
            self.__current_point.set_instruction('slight right')
        elif self.__current_point.get_instruction() == 6:
            self.__current_point.set_instruction('go ahead')
        elif self.__current_point.get_instruction() == 7:
            self.__current_point.set_instruction('go ahead')
        elif self.__current_point.get_instruction() == 8:
            self.__current_point.set_instruction('exit right')
        elif self.__current_point.get_instruction() == 9:
            self.__current_point.set_instruction('uturn left')
        elif self.__current_point.get_instruction() == 10:
            self.__current_point.set_instruction('go ahead')
        elif self.__current_point.get_instruction() == 11:
            self.__current_point.set_instruction('go ahead')
        elif self.__current_point.get_instruction() == 12:
            self.__current_point.set_instruction('exit left')
        elif self.__current_point.get_instruction() == 13:
            self.__current_point.set_instruction('exit right')
        elif self.__current_point.get_instruction() == 14:
            self.__current_point.set_instruction('go ahead')
        else:
            self.__current_point.set_instruction('none')

    def __remove_duplicated_instruction(self):
        first_point = True
        for point in self.__points:
            self.__current_point = point
            self.__translate_instruction()
            point = self.__current_point
            if first_point:
                first_point = False
                last_point = copy.copy(point)
                point.set_instruction('none')
            else:
                if point.get_instruction() == last_point.get_instruction():
                    last_point = copy.copy(point)
                    point.set_instruction('none')
                else:
                    last_point = copy.copy(point)


    def __calculate_instruction(self):
        self.__remove_duplicated_instruction()

    def __calculate__names(self):

        for point in self.__points:
            self.__current_point = point
            name = point.get_name()

            name = unidecode.unidecode(name)
            name = name.replace('A(c)', 'e')
            name = name.replace('A!', 'a')
            name = name.replace('A\'', 'o')
            name = name.replace('ASS', 'c')
            name = name.replace('APS', 'a')
            name = name.replace('A3', 'o')

            name = name.replace('Rua', 'R')
            name = name.replace('Avenida', 'Av')
            name = name.replace('Professora', 'Prf')
            name = name.replace('Professor', 'Prf')
            name = name.replace('Doutora', 'Dr')
            name = name.replace('Doutor', 'Dr')
            name = name.replace('Estrada', 'Est')

            name = name.replace('Eduardo', 'Edu')
            name = name.replace('Monte', 'Mt')
            name = name.replace('Viaduto', 'Via')
            name = name.replace('Passagem', 'Ps')
            name = name.replace('NAvel', 'Nv')
            name = name.replace('Engenheira', 'Eng')
            name = name.replace('Engenheiro', 'Eng')
            name = name.replace('Marechal', 'Mrc')

            point.set_name(name)

    def calculate_route(self):

        self.__calculate_num_points()
        self.__calculate_length()
        self.__calculate_alt_bound_box()
        self.__calculate_instruction()
        self.__calculate__names()
        print()




