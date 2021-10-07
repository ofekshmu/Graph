import math
from enum import Enum
from typing import Union

class Color(Enum):
    black = "black",
    gray = "gray",
    white = "white"

class Vertice:
    def __init__(self, id):       
        self.__id = id
        self.__color = Color.white
        self.__distance = math.inf

    # GETTERS
    @property
    def id(self):
        """ return the vertice Id """
        return self.__id
    
    @property
    def color(self) -> Color:
        """ return the vertice color 
            white - undiscovered
            gray - discovered
            black - finished discovering
        """
        return self.__color
    
    @color.setter
    def color(self, color: Color):
        if isinstance(color, Color):
            self.__color = color
        else:
            raise ValueError
    
    @property    
    def distance(self):
        """ return distance from init node """
        return self.__distance
    
    @distance.setter
    def distance(self, new_distance : Union[float, int]):
        """ set the distnace of the vertice"""
        self.__distance = new_distance
    
    def _accDistance(self, acc_distance : Union[float, int]):
        """ accumulate to the current distance of the vertice """
        self.__distance += acc_distance

    def isUnvisited(self):
        return self.color == Color.white
    
    def unvisit(self):
        self.color = Color.white
    # ETC

    def __eq__(self, other): # equality is determined by id only
        if other is None:
            return False
        return self.__id
        
    def __repr__(self):
        return f"'{self.__id}'"