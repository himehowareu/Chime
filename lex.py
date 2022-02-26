
from ChimeTypes import Line

def clean(thing:list[Line]) -> list[Line]:
    out =[]
    for token in thing:
        if token !="":
            out.append(token)
    return out
    


# tokens.append(FileName)
def lexer(file:str) -> list[Line]:
    splits=",:%@[](){!};"
    math = "/*-+<=>|^"
    checkMath=False
    tokens = []
    inString=False
    comment=False
    checklongcomment=False
    longComment=False
    token=""
    escaped=False
    floating =False
    line = 1

    for char in file:
        if char=="\n":
            line+=1
        if escaped:
            token+=char
            escaped = False
            continue
        if not inString and not comment:
            if char in math:
                if checkMath:
                    checkMath = False
                    token+=char
                    tokens.append(Line(line,token))
                    token=""
                    continue
                checkMath=True
                tokens.append(Line(line,token))
                token=char
                continue 
            elif checkMath:
               tokens.append(Line(line,token))
               token=""
               continue
            if floating:
                if char.isnumeric():
                    token+=char
                else:
                    tokens.append(Line(line,token))
                    # tokens.append(Line(line,"."))
                    token+=char
                floating=False
                continue
            if char == "#":
                tokens.append(Line(line,token))
                token=""
                checklongcomment = True
                comment = True
                continue
            if char =="\"":
                tokens.append(Line(line,token))
                token="\""
                inString = True
                continue 
            if char =="\\":
                escaped=True
                continue
            if char in " ":
                tokens.append(Line(line,token))
                token=""
                continue
            if char == ".":
                if token.isnumeric() or token == "":
                    floating = True
                tokens.append(Line(line,token))
                token = ""
                tokens.append(Line(line,"."))
                continue

            if char in splits:
                tokens.append(Line(line,token))
                tokens.append(Line(line,char))
                token=""
                continue
        if comment:
            if checklongcomment:
                if char == "{":
                    longComment = True
                checklongcomment = False
                if char == "#":
                    comment = False
                    longComment = False
            if char == "}":
                checklongcomment = True
            if not longComment:
                if char == "\n" or char == "\r":
                    comment = False
                    longComment = False
            continue
        if inString:
            token+=char
            if char == "\"":
                inString = False
                tokens.append(Line(line,token))
                token=""
            continue 

        token += char 
    output = clean(tokens)
    return output

# from pprint import pprint
# pprint(lexer())
