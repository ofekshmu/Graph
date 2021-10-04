from typing import Union


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
        self.__weight = new_Weight

    def _accWeight(self, acc_Weight):
        """ adds @acc_Weight to the current edge weight"""
        self.__weight += acc_Weight
    # ETC
    def isLoop(self):
        return self.__start == self.__end

    def __eq__(self,other):
        if not isinstance(other, Edge):
            return False
        c1 = self.__start == other.start
        c2 = self.__end == other.end
        c3 = self.__weight == other.weight
        return c1 and c2 and c3
        
    def __repr__(self):
        raise NotImplemented()
        #connector = "-->" if self.direction else "--"
        #return f"({self.start}){connector}({self.end})"