from system import print;
from syslib import ref,dref,asm,dvd,store,fetch,malloc;

import screen;

String hi = "hello";
Int age = 1;
Float percent = 1.8;
List tests = [String "act",Int 24,Float .3];
Bool running = True;
String name;
String user_input;
Dict book = {String "name":String "red", String "age": Int 18};

Pointer mem = malloc(10);

age @ book["age"];
age = dvd(book["age"]);

free(mem);

decimal @ percent/100;
decimal = dvd(percent/100);

Pointer run -> running ;
Pointer run = ref(running); 

Bool n <- run;
Bool n = dref(run);

print(<- run);


# these registers can be defined in build config otherwise a RANDOM REG WILL BE USED 

store(age,"$reg1");
asm("ls reg1 reg1");
fetch(age,"$reg1");

print("the name of the book is" + book["name"]);

print(age);
age += 2;
print(book["age");

tests.index(25);

name = input("what's your name?");


if(name is "himehowareu"){
  print("Hello".lower() + "Master".upper());
};


for(item in tests){
  print(item);
  if(item is Int){
    print("is an intinger");
  }elif(item is Float){
    print("is a float");
  }elif(item is String){
    print("is a string");
  }elif(item is Bool){
    print("is a bool");
  }else{
    print("is a list");
  };
  print("with length of " + len(item));#or item.length()
};


List path = "c:/user/himehowareu/desktop".)split("/");

Int place = "abc".find("c");

List keys;
key = book.key();


Obj person(){
  String name = "default";
  def Nothing foo(){
    print(parent.name);
    parent.times += 1;
  };
  Int times = 0;
};

person john;
john.name = "john";
john.foo();
john.foo();
john.foo();
john.foo();
print(john.times);

def Bool foo(String name){
  if (name is ""){
    return(False);
  }else{
    return(True);
  };
};


tests.append(Dict {String "d",Int 4});

print(int("3")+4);
print(2-1);
print(1+1);
print(2*1);
print(7/2);
print(7.0/2);
print(2*8);
print(7%2);

print(int(.2+4.9));

print("the answer is" + str(25));#{
                                    or item.string()
                                    curly brackets make the commit multiline 
                                    }#


while(running){ 
  user_input = input(">");
  if (foo(user_input)){
    pass;
  }elif (user_input.lower() is "exit"){
    running.invert();#or
  }elif (user_input.lower() is "user"){
    if (name is "himehowareu"){
      print( "master " + name);
    }else{
      print(name);
    };
  }else{
    print("not valid input");
  };
};


screen.backgroundcolor(screen.black);
screen.foregroundcolor(screen.green);
screen.write("Hello world");

screen.size temp = screen.size;
#{
obj size(){
  int x;
  int y;
}
}#

Int x = temp.x;
Int y = temp.y;

screen.box test = screen.box(5,5);

screen.draw(test,(x-5)/2,(y-5)/2);