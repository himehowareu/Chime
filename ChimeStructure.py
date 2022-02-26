from ChimeTypes import *

class S_List(Structure):
    def __init__(self,nodes:ParsedLine):
        super().__init__(nodes)
        self.name = "S_List"
    def __str__(self):
       return("*List[%s]"%(str(self.nodes)))
 
    def __repr__(self):
        return self.__str__()


class S_Dict(Structure):
    def __init__(self,nodes:ParsedLine):
        super().__init__(nodes)
        self.name = "S_Dict"
    def __str__(self):
       return("*Dict{%s}"%(str(self.nodes)))
 
    def __repr__(self):
        return self.__str__()