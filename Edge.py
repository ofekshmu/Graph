from typing import Union


class Edge:
    def __init__(self, start, end, weight: int = 1):
        self.__start = start
        self.__end = end
        self.__weight = weight

    # Getters
    def _getS(self):
        """ get starting vertice Id"""
        return self.start

    def _getE(self):
        """ get ending vertice Id"""
        return self.end    
    
    def _getWeight(self) -> Union[int, float]:
        """ get Weight of the edge"""
        return self.weight
    # Setters
    def _setWeight(self, new_Weight: Union[int, float]):
        """ resets the value of weight to @new_Weight"""
        self.__weight = new_Weight

    def _accWeight(self, acc_Weight):
        """ adds @acc_Weight to the current edge weight"""
        self.__weight += acc_Weight
    # ETC
    def isLoop(self):
        return self.__start == self.__end

    def __eq__(self,other):
        raise NotImplemented()

    def __repr__(self):
        raise NotImplemented()
        #connector = "-->" if self.direction else "--"
        #return f"({self.start}){connector}({self.end})"