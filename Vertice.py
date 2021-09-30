import math
import enum
from typing import Union
class Color(enum):
    black = "black",
    gray = "gray",
    white = "white"

class Vertice:
    def __init__(self, id):       
        self.__id = id
        self.__color = Color.White
        self.__distance = math.inf

    # GETTERS
    def _getId(self):
        """ return the vertice Id """
        return self.__id
    
    def _getColor(self) -> Color:
        """ return the vertice color 
            white - undiscovered
            gray - discovered
            black - finished discovering
        """
        return self.__color
        
    def _getDistance(self):
        """ return distance from init node """
        return self.__distance
    
    # SETTERS
    def _setDistnace(self, new_distance : Union[float, int]):
        """ set the distnace of the vertice"""
        self.__distance = new_distance
    
    def _accDistance(self, acc_distance : Union[float, int]):
        """ accumulate to the current distance of the vertice """
        self.__distance += acc_distance
    
    def _setColor(self, color: Color):
        self.__color = color
    # ETC

    def __eq__(self, other): #TODO: might invoke a problem. checks only per id.
        return self.id == other.id

    def __repr__(self):
        return f"'{self.id}'"