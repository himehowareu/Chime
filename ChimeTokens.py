from ChimeTypes import * 
from ChimeNodes import * 

# class T_NotImp(Token):
#     def __init__(self):
#         super().__init__("NotImp")
#     def match(self,line:Line) -> bool:
#         return True
#     def node(self,line:Line) ->Node:
#         return  N_NotImp(line)

class T_Comment(Token):
    def __init__(self):
        super().__init__("commant")
    def match(self,line:Line) -> bool:
        return line.startswith("#")
    def node(self,line:Line) ->Node:
        return N_Comment(line)
    
class T_Semi(Token):
    def __init__(self):
        super().__init__("Semi")
    def match(self,line:Line) -> bool:
        return line == ";"
    def node(self,line:Line) -> Node:
        return N_Semi(line)

class T_While(Token):
    def __init__(self):
        super().__init__("While")
    def match(self,line:Line) -> bool:
        return line == "while"
    def node(self,line:Line) -> Node:
        return N_While(line)

class T_Else(Token):
    def __init__(self):
        super().__init__("Else")
    def match(self,line:Line) -> bool:
        return line == "else"
    def node(self,line:Line) -> Node:
        return N_Else(line)

class T_Pass(Token):
    def __init__(self):
        super().__init__("Pass")
    def match(self,line:Line) -> bool:
        return line == "pass"
    def node(self,line:Line) -> Node:
        return N_Pass(line)

class T_Object(Token):
    def __init__(self):
        super().__init__("Obj")
    def match(self,line:Line) -> bool:
        return line == "Obj"
    def node(self,line:Line) -> Node:
        return N_Object(line)

class T_Elif(Token):
    def __init__(self):
        super().__init__("Elif")
    def match(self,line:Line) -> bool:
        return line == "elif"
    def node(self,line:Line) -> Node:
        return N_Elif(line)

class T_Print(Token):
    def __init__(self):
        super().__init__("Print")
    def match(self,line:Line) -> bool:
        return line == "print"
    def node(self,line:Line) -> Node:
        return N_Print(line)

class T_Dref(Token):
    def __init__(self):
        super().__init__("Dref")
    def match(self,line:Line) -> bool:
        return line == "<-"
    def node(self,line:Line) -> Node:
        return N_Dref(line)
class T_Ref(Token):
    def __init__(self):
        super().__init__("Ref")
    def match(self,line:Line) -> bool:
        return line == "->"
    def node(self,line:Line)-> Node:
        return N_Ref(line)
class T_def(Token):
    def __init__(self):
        super().__init__("def")
    def match(self,line:Line) -> bool:
        return line == "def"
    def node(self,line:Line)-> Node:
        return N_def(line)
class T_from(Token):
    def __init__(self):
        super().__init__("from")
    def match(self,line:Line) -> bool:
        return line == "from"
    def node(self,line:Line)-> Node:
        return N_from(line)
class T_import(Token):
    def __init__(self):
        super().__init__("import")
    def match(self,line:Line) -> bool:
        return line == "import"
    def node(self,line:Line)-> Node:
        return N_import(line)
class T_in(Token):
    def __init__(self):
        super().__init__("in")
    def match(self,line:Line) -> bool:
        return line == "in"
    def node(self,line:Line)-> Node:
        return N_in(line)
class T_iF(Token):
    def __init__(self):
        super().__init__("if")
    def match(self,line:Line) -> bool:
        return line == "if"
    def node(self,line:Line)-> Node:
        return N_If(line)
class T_is(Token):
    def __init__(self):
        super().__init__("is")
    def match(self,line:Line) -> bool:
        return line == "is"
    def node(self,line:Line)-> Node:
        return N_is(line)
class T_comma(Token):
    def __init__(self):
        super().__init__("Comma")
    def match(self,line:Line) -> bool:
        return line == ","
    def node(self,line:Line)-> Node:
        return N_Comma(line)

class T_Int(Token):
    def __init__(self):
        super().__init__("Int")
    def match(self,line:Line) -> bool:
        return line == "Int"
    def node(self,line:Line)-> Node:
        return N_Int(line)
class T_Float(Token):
    def __init__(self):
        super().__init__("Float")
    def match(self,line:Line) -> bool:
        return line == "Float"
    def node(self,line:Line)-> Node:
        return N_Float(line)
class T_List(Token):
    def __init__(self):
        super().__init__("List")
    def match(self,line:Line) -> bool:
        return line == "List"
    def node(self,line:Line)-> Node:
        return N_List(line)
class T_Bool(Token):
    def __init__(self):
        super().__init__("Bool")
    def match(self,line:Line) -> bool:
        return line == "Bool"
    def node(self,line:Line)-> Node:
        return N_Bool(line)
class T_String(Token):
    def __init__(self):
        super().__init__("String")
    def match(self,line:Line) -> bool:
        return line == "String"
    def node(self,line:Line)-> Node:
        return N_String(line)
class T_Dict(Token):
    def __init__(self):
        super().__init__("Dict")
    def match(self,line:Line) -> bool:
        return line == "Dict"
    def node(self,line:Line)-> Node:
        return N_Dict(line)
class T_Pointer(Token):
    def __init__(self):
        super().__init__("Pointer")
    def match(self,line:Line) -> bool:
        return line == "Pointer"
    def node(self,line:Line)-> Node:
        return N_Pointer(line)
class T_assign(Token):
    def __init__(self):
        super().__init__("Assign")
    def match(self,line:Line)-> bool:
        return line == "="
    def node(self,line:Line)-> Node:
        return N_Assign(line)

class T_StringLit(Token):
    def __init__(self):
        super().__init__("StringLit")
    def match(self,line:Line)-> bool:
        return line.startswith("\"")
    def node(self,line:Line)-> Node:
        return N_StringLit(line)

class T_NumberLit(Token):
    def __init__(self):
        super().__init__("NumberLit")
    def match(self,line:Line)-> bool:
        return line.isnumeric()
    def node(self,line:Line)-> Node:
        return N_Number(line)

class T_Nothing(Token):
    def __init__(self):
        super().__init__("Nothing")
    def match(self,line:Line) -> bool:
        return line == "Nothing"
    def node(self,line:Line)-> Node:
        return N_Nothing(line)

class T_True(Token):
    def __init__(self):
        super().__init__("True")
    def match(self,line:Line) -> bool:
        return line == "True"
    def node(self,line:Line)-> Node:
        return N_True(line)

class T_False(Token):
    def __init__(self):
        super().__init__("False")
    def match(self,line:Line) -> bool:
        return line == "False"
    def node(self,line:Line)-> Node:
        return N_False(line)

class T_OpenSquareBracket(Token):
    def __init__(self):
        super().__init__("OpenSquareBracket")
    def match(self,line:Line) -> bool:
        return line == "["
    def node(self,line:Line)-> Node:
        return N_OpenSquareBracket(line)

class T_CloseSquareBracket(Token):
    def __init__(self):
        super().__init__("CloseSquareBracket")
    def match(self,line:Line) -> bool:
        return line == "]"
    def node(self,line:Line)-> Node:
        return N_CloseSquareBracket(line)

class T_OpenCrullyBracket(Token):
    def __init__(self):
        super().__init__("OpenCrullyBracket")
    def match(self,line:Line) -> bool:
        return line == "{"
    def node(self,line:Line)-> Node:
        return N_OpenCrullyBracket(line)

class T_CloseCrullyBracket(Token):
    def __init__(self):
        super().__init__("CloseCrullyBracket")
    def match(self,line:Line) -> bool:
        return line == "}"
    def node(self,line:Line)-> Node:
        return N_CloseCrullyBracket(line)

class T_OpenParentheses(Token):
    def __init__(self):
        super().__init__("OpenParentheses")
    def match(self,line:Line) -> bool:
        return line == "("
    def node(self,line:Line)-> Node:
        return N_OpenParentheses(line)

class T_CloseParentheses(Token):
    def __init__(self):
        super().__init__("CloseParentheses")
    def node(self,line:Line)-> Node:
        return N_CloseParentheses(line)
    def match(self,line:Line) -> bool:
        return line == ")"

class T_Period(Token):
    def __init__(self):
        super().__init__("Period")
    def node(self,line:Line)-> Node:
        return N_Period(line)
    def match(self,line:Line) -> bool:
        return line == "."

class T_Colin(Token):
    def __init__(self):
        super().__init__("Colin")
    def node(self,line:Line)-> Node:
        return N_Colin(line)
    def match(self,line:Line) -> bool:
        return line == ":"


class T_DivEqu(Token):
    def __init__(self):
        super().__init__("T_DivEqu")
    def node(self,line:Line)-> Node:
        return N_DivEqu(line)
    def match(self,line:Line) -> bool:
        return line == "/="

class T_MulEqu(Token):
    def __init__(self):
        super().__init__("T_MulEqu")
    def match(self,line:Line) -> bool:
        return line == "*="
    def node(self,line:Line)-> Node:
        return N_MulEqu(line)

class T_AddEqu(Token):
    def __init__(self):
        super().__init__("T_AddEqu")
    def match(self,line:Line) -> bool:
        return line == "+="
    def node(self,line:Line)-> Node:
        return N_AddEqu(line)

class T_MinEqu(Token):
    def __init__(self):
        super().__init__("T_MinEqu")
    def match(self,line:Line) -> bool:
        return line == "-="
    def node(self,line:Line)-> Node:
        return N_MinEqu(line)

class T_NotEqu(Token):
    def __init__(self):
        super().__init__("T_NotEqu")
    def match(self,line:Line) -> bool:
        return line == "!="
    def node(self,line:Line)-> Node:
        return N_NotEqu(line)

class T_ModEqu(Token):
    def __init__(self):
        super().__init__("T_ModEqu")
    def match(self,line:Line) -> bool:
        return line == "%="
    def node(self,line:Line)-> Node:
        return N_ModEqu(line)

class T_XorEqu(Token):
    def __init__(self):
        super().__init__("T_XorEqu")
    def match(self,line:Line) -> bool:
        return line == "^="
    def node(self,line:Line)-> Node:
        return N_XorEqu(line)


class T_AndEqu(Token):
    def __init__(self):
        super().__init__("AndEqu")
    def match(self,line:Line) -> bool:
        return line == "&="
    def node(self,line:Line)-> Node:
        return N_AndEqu(line)


class T_Div(Token):
    def __init__(self):
        super().__init__("T_Div")
    def match(self,line:Line) -> bool:
        return line == "/"
    def node(self,line:Line)-> Node:
        return N_Div(line)

class T_Mul(Token):
    def __init__(self):
        super().__init__("T_Mul")
    def match(self,line:Line) -> bool:
        return line == "*"
    def node(self,line:Line)-> Node:
        return N_Mul(line)

class T_Min(Token):
    def __init__(self):
        super().__init__("T_Min")
    def match(self,line:Line) -> bool:
        return line == "-"
    def node(self,line:Line)-> Node:
        return N_Min(line)

class T_Add(Token):
    def __init__(self):
        super().__init__("T_Add")
    def match(self,line:Line) -> bool:
        return line == "+"
    def node(self,line:Line)-> Node:
        return N_Add(line)

class T_Not(Token):
    def __init__(self):
        super().__init__("T_Not")
    def match(self,line:Line) -> bool:
        return line == "!"
    def node(self,line:Line)-> Node:
        return N_Not(line)

class T_Mod(Token):
    def __init__(self):
        super().__init__("T_Mod")
    def match(self,line:Line) -> bool:
        return line == "%"
    def node(self,line:Line)-> Node:
        return N_Mod(line)

class T_Xor(Token):
    def __init__(self):
        super().__init__("T_Xor")
    def match(self,line:Line) -> bool:
        return line == "^"
    def node(self,line:Line)-> Node:
        return N_Xor(line)

class T_And(Token):
    def __init__(self):
        super().__init__("T_And")
    def match(self,line:Line) -> bool:
        return line == "&"
    def node(self,line:Line)-> Node:
        return N_And(line)


class T_Name(Token):
    def __init__(self):
        super().__init__("T_Name")
    def match(self,line:Line) -> bool:
        return True
    def node(self,line:Line)-> Node:
        return N_Name(line)


def Tokens() -> list[Token]:
    return [globals()[x]() for x in globals().keys() if x.startswith("T_")]