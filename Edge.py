from typing import Union
import math
class Edge:
    def __init__(self, start, end, weight: int = 1):
        self.__start = start
        self.__end = end
        self.__weight = weight

    # Getters
    @property
    def start(self):
        """ get starting vertice Id"""
        return self.__start

    @property    
    def end(self):
        """ get ending vertice Id"""
        return self.__end    
    
    @property
    def weight(self) -> Union[int, float]:
        """ get Weight of the edge"""
        return self.__weight
    
    @weight.setter
    def weight(self, new_Weight: Union[int, float]):
        """ resets the value of weight to @new_Weight"""
        try:
            if new_Weight != math.inf: 
                int(new_Weight)
            self.__weight = new_Weight
        except:
            raise ValueError("None numeric value was given for Edge Weight") 

    def _accWeight(self, acc_Weight):
        """ adds @acc_Weight to the current edge weight"""
        try:
            if acc_Weight != math.inf: 
                int(acc_Weight)
            self.__weight += acc_Weight
        except:
            raise ValueError("None numeric value was given for Edge accWeight") 

    # ETC
    def isLoop(self) -> bool:
        return self.__start == self.__end

    def __eq__(self,other):
        if other is None:
            return False
        return self.__start == other.start and self.__end == other.end
        
    def __repr__(self):
        raise NotImplemented()
        #connector = "-->" if self.direction else "--"
        #return f"({self.start}){connector}({self.end})"