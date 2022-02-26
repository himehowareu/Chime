from ChimeTypes import *


class N_NotImp(Node):
    def __init__(self,line:Line):
        super().__init__("NotImp",line)

class N_Comment(Node):
    def __init__(self,line:Line):
        super().__init__("Comment",line)
    def compile(self) -> str:
        return ""

class N_Semi(Node):
    def __init__(self,line:Line):
        super().__init__("Semi",line)

class  N_Object(Node):
    def __init__(self,line:Line):
        super().__init__("Object",line)

class N_Dref(Node):
    def __init__(self,line:Line):
        super().__init__("Dref",line)
    
class N_Ref(Node):
    def __init__(self,line:Line):
        super().__init__("Ref",line)

class N_def(Node):
    def __init__(self,line:Line):
        super().__init__("def",line)
class N_from(Node):
    def __init__(self,line:Line):
        super().__init__("from",line)
class N_import(Node):
    def __init__(self,line:Line):
        super().__init__("import",line)
class N_in(Node):
    def __init__(self,line:Line):
        super().__init__("in",line)
class N_is(Node):
    def __init__(self,line:Line):
        super().__init__("is",line)

class N_Comma(Node):
    def __init__(self,line:Line):
        super().__init__("comma",line)

class N_Int(Node):
    def __init__(self,line:Line):
        super().__init__("Int",line)
class N_Float(Node):
    def __init__(self,line:Line):
        super().__init__("Float",line)
class N_List(Node):
    def __init__(self,line:Line):
        super().__init__("List",line)
class N_Bool(Node):
    def __init__(self,line:Line):
        super().__init__("Bool",line)
class N_String(Node):
    def __init__(self,line:Line):
        super().__init__("String",line)
class N_Dict(Node):
    def __init__(self,line:Line):
        super().__init__("Dict",line)
class N_Pointer(Node):
    def __init__(self,line:Line):
        super().__init__("Pointer",line)

class N_EndOfTokens(Node):
    def __init__(self,line:Line):
        super().__init__("EndofTokens",line)


class N_Assign(Node):
    def __init__(self,line:Line):
        super().__init__("Assign",line)
class N_FloatLit(Node):
    def __init__(self,line:Line):
        super().__init__("FloatLit",line)
class N_StringLit(Node):
    def __init__(self,line:Line):
        super().__init__("StringLit",line)
class N_Number(Node):
    def __init__(self,line:Line):
        super().__init__("Number",line)
class N_Nothing(Node):
    def __init__(self,line:Line):
        super().__init__("Nothing",line)
class N_True(Node):
    def __init__(self,line:Line):
        super().__init__("True",line)
class N_False(Node):
    def __init__(self,line:Line):
        super().__init__("False",line)
class N_OpenSquareBracket(Node):
    def __init__(self,line:Line):
        super().__init__("OpenSquareBracket",line)
class N_CloseSquareBracket(Node):
    def __init__(self,line:Line):
        super().__init__("CloseSquareBracket",line)
class N_OpenCrullyBracket(Node):
    def __init__(self,line:Line):
        super().__init__("OpenCrullyBracket",line)
class N_CloseCrullyBracket(Node):
    def __init__(self,line:Line):
        super().__init__("CloseCrullyBracket",line)
class N_OpenParentheses(Node):
    def __init__(self,line:Line):
        super().__init__("OpenParentheses",line)
class N_CloseParentheses(Node):
    def __init__(self,line:Line):
        super().__init__("CloseParentheses",line)
class N_Period(Node):
    def __init__(self,line:Line):
        super().__init__("Period",line)
class N_Colin(Node):
    def __init__(self,line:Line):
        super().__init__("Colin",line)
class N_DivEqu(Node):
    def __init__(self,line:Line):
        super().__init__("DivEqu",line)
class N_MulEqu(Node):
    def __init__(self,line:Line):
        super().__init__("MulEqu",line)
class N_AddEqu(Node):
    def __init__(self,line:Line):
        super().__init__("AddEqu",line)
class N_MinEqu(Node):
    def __init__(self,line:Line):
        super().__init__("MinEqu",line)
class N_NotEqu(Node):
    def __init__(self,line:Line):
        super().__init__("NotEqu",line)
class N_ModEqu(Node):
    def __init__(self,line:Line):
        super().__init__("ModEqu",line)
class N_XorEqu(Node):
    def __init__(self,line:Line):
        super().__init__("XorEqu",line)
class N_AndEqu(Node):
    def __init__(self,line:Line):
        super().__init__("AndEqu",line)
class N_Div(Node):
    def __init__(self,line:Line):
        super().__init__("Div",line)
class N_Mul(Node):
    def __init__(self,line:Line):
        super().__init__("Mul",line)
class N_Min(Node):
    def __init__(self,line:Line):
        super().__init__("Min",line)
class N_Add(Node):
    def __init__(self,line:Line):
        super().__init__("Add",line)
class N_Not(Node):
    def __init__(self,line:Line):
        super().__init__("Not",line)
class N_Mod(Node):
    def __init__(self,line:Line):
        super().__init__("Mod",line)
class N_Xor(Node):
    def __init__(self,line:Line):
        super().__init__("Xor",line)
class N_And(Node):
    def __init__(self,line:Line):
        super().__init__("And",line)

class N_While(Node):
    def __init__(self,line:Line):
        super().__init__("While",line)

class N_Name(Node):
    def __init__(self,line:Line):
        super().__init__("Name",line)
class N_If(Node):
    def __init__(self,line:Line):
        super().__init__("If",line)

class N_Print(Node):
    def __init__(self,line:Line):
        super().__init__("Print",line)

class N_Elif(Node):
    def __init__(self,line:Line):
        super().__init__("Elif",line)

class N_Else(Node):
    def __init__(self,line:Line):
        super().__init__("Else",line)

class N_Pass(Node):
    def __init__(self,line:Line):
        super().__init__("Pass",line)


