from ChimeTypes import *
from ChimeNodes import *
from ChimePars import *
from ChimeTokens import Tokens
from ChimeStructure import *
from lex import lexer
from pprint import pprint

import sys

# with open(sys.argv[1]) as f:
with open("c:\\users\\himehowareu\\projects\\chime\\sample.chime") as f:
    program = f.read()

def Tokenize(line: Line) -> Node:
    for token in Tokens():
        if token.match(line):
            return token.node(line)
    return Node("EndOfTokens",Line(666,"<EOF>"))


lexed :list[Line] = lexer(program)

nodes : list[Node] = [Tokenize(node) for node in lexed] 
linedUpNodes: list[ParsedLine] = lines(nodes)

floatLitFixed = [P_Float(node) for node in linedUpNodes]
# pprint(floatLitFixed[6])

# print(S_List(ParsedLine(parenthetic_contents(floatLitFixed[6]))))

# print(floatLitFixed[6].nodes)

# print(FilterList(floatLitFixed[6]))

listFixed = [FilterList(line) for line in floatLitFixed]

dictFixed = [FilterDict(line) for line in listFixed]

pprint(dictFixed)