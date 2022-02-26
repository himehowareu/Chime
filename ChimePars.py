from ChimeTypes import ParsedLine
from ChimeStructure import *
from ChimeNodes import *

def lines(tokens):
    current=0
    token=tokens[current]
    brackets=0
    output=[]
    line = []
    while current < len(tokens):
        token=tokens[current]
        if token.line == "{":
            brackets+=1
        if token.line == "}":
            brackets-=1
        line.append(token)
        endLine = token.line ==";"
        endFile = token.line == "<EOF>"
        ending = endLine or endFile
        if ending and not brackets:
            output.append(ParsedLine(line))
            line=[]
        current+=1
    return(output)

def P_Float(Pline:ParsedLine) -> ParsedLine:
    dotNumber = ParsedLine([N_Period(Line(8,".")),N_Number(Line(8,"10"))])
    numberDotNumber = ParsedLine([N_Number(Line(8,"10")),N_Period(Line(8,".")),N_Number(Line(8,"10"))])

    while numberDotNumber in Pline:
        start = Pline.index(numberDotNumber)
        testLine  = Pline[start].line + Pline[start+1].line + Pline[start+2].line
        new = N_FloatLit(testLine)
        out = Pline[0:start] + [new] + Pline[start+3:]
        Pline = ParsedLine(out)

    while dotNumber in Pline:
        start = Pline.index(dotNumber)
        testLine  = Pline[start].line + Pline[start+1].line
        new = N_FloatLit(testLine)
        out = Pline[0:start] + [new] + Pline[start+2:]
        Pline = ParsedLine(out)
    return(Pline)
        

def parenthetic_contents(string:ParsedLine) -> list[Line] | None:
    """Generate parenthesized contents in string as pairs (level, contents)."""
    stack = []
    for i, c in enumerate(string):
        if c == N_OpenSquareBracket(Line(0,"test")):
            stack.append(i)
        elif c == N_CloseSquareBracket(Line(0,"test")) and stack:
            start = stack.pop()
            return( [N_OpenSquareBracket(Line(0,"test"))]+string[start + 1: i]+[N_CloseSquareBracket(Line(0,"test"))])

def FilterList(Pline: ParsedLine) -> ParsedLine:
    s= parenthetic_contents(Pline)
    while s:
        search = ParsedLine(s)
        start = Pline.index(search)
        new = S_List(search)
        out = Pline[0:start] + [new] + Pline[start+len(search):]
        Pline = ParsedLine(out)
        s = parenthetic_contents(Pline)
    return(Pline)


def curlly_contents(string:ParsedLine) -> list[Line] | None:
    """Generate parenthesized contents in string as pairs (level, contents)."""
    stack = []
    for i, c in enumerate(string):
        if c == N_OpenCrullyBracket(Line(0,"test")):
            stack.append(i)
        elif c == N_CloseCrullyBracket(Line(0,"test")) and stack:
            start = stack.pop()
            return( [N_OpenCrullyBracket(Line(0,"test"))]+string[start + 1: i]+[N_CloseCrullyBracket(Line(0,"test"))])

def FilterDict(Pline: ParsedLine) -> ParsedLine:
    s= curlly_contents(Pline)
    while s:
        search = ParsedLine(s)
        start = Pline.index(search)
        new = S_Dict(search)
        out = Pline[0:start] + [new] + Pline[start+len(search):]
        Pline = ParsedLine(out)
        s = curlly_contents(Pline)
    return(Pline)