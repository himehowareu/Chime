from errors import *
from ChimeTypes import *


class Line(object):
    def __init__(self,lineNumber:int,text:str):
        self.lineNumber = lineNumber
        self.text = text
    def __eq__(self,other:object):
        return self.text == other
    def __ne__(self,other:object):
        return self.text != other
    def __str__(self):
        return("line %i : %s"%(self.lineNumber,self.text))
    def __repr__(self):
        return self.__str__()
    def __add__(self,other:object):
        return Line(self.lineNumber,self.text+other.text)
    def startswith(self, text:str):
        return self.text.startswith(text)
    def isnumeric(self):
        return self.text.isnumeric()
    
class Node(object):
    def __init__(self,name:str,line:Line):
        self.name = name
        self.line = line
    def __eq__(self,Other: object):
        return self.name == Other.name
    def __str__(self):
        return "%s" % ( self.line.text)
    def __repr__(self) -> str:
        return("%i:%s: %s"%(self.line.lineNumber,self.name,self.line.text))
    def isNode(self):
        return True
    def compile(self) -> str:
        raise NodeNotImplimented

class Token(object):
    def __init__(self,Name: str):
        self.name = Name
    def __repr__(self) -> str:
        return ("%s token"%(self.name))
    def match(self,line:Line) -> bool:
        raise TokenMatchNotDefined
    def node(self,line:Line) ->Node:
        raise TokenMatchNotDefined

class ParsedLine(object):
    def __init__(self,nodes:list[Node]):
        self.nodes = nodes
        self._index = -1
    def isNode(self):
        return False
    def __len__(self):
        return len(self.nodes)
    def __contains__(self,other:Node|object) -> bool:
        if other.isNode():
            for line in self.nodes:
                if isinstance(line,type(other)):
                    return True
        else:
            for i in range(len(self.nodes)):
                if self.nodes[i] == other[0] and self.nodes[i:i+len(other)] == other.nodes:
                    return True
        return False
    def __iter__(self):
        return self
    def index(self,other:object):
        for i in range(len(self.nodes)):
            if self.nodes[i] == other[0] and self.nodes[i:i+len(other)] == other.nodes:
                return i
        return -1
    def __next__(self):
        self._index += 1
        if self._index >= len(self.nodes):
            self._index = -1
            raise StopIteration
        else:
            return self.nodes[self._index]
    def __getitem__(self, lineNumber:int):
        return self.nodes[lineNumber]
    def __setitem__(self, lineNumber:int,node:Node):
        self.nodes[lineNumber] = node
    def __str__(self):
        return " ".join([str(node) for node in self.nodes])
    def __len__(self):
        return len(self.nodes)
    def __repr__(self):
        return self.__str__()

class Structure(ParsedLine):
    def __init__(self,nodes:ParsedLine):
        super().__init__(nodes)