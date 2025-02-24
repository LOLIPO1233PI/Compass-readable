# Compass implementation by Gaham (Thevitebsk) Y25
# A language based on Pascal
from time import*;import sys
from manual import*
VER=1.0;LUD="Febuary 24 2025"
def Compass(x:str)->None:
 var={};t=time()
 def phar(x)->list:
  x=x.strip().split("\n")
  p=po=int(0);oldx=x
  texts=[];funcs={}
  while len(x)>p:
   while len(x[p])>po:
    if x[p].startswith("func "):
     po+=6
     while x[p][po]!=":":texts.append(x[p][po]);po+=1
     x.insert(p+1,x[p][po+1::])
     x[p]=x[p][6:po]
     if not x[p+1]:
      print(f"ERROR:Function {x[p]} has no body at line {p+1}");break
     else:
      funcs[x[p-1]]=x.pop(p+1)
     x.pop(p+1)
    elif x[p][po]==":":
     while 0<po:po-=1
     while x[p][po]!=";":
      texts.append(x[p][po]);po+=1
     var["".join(texts[0:texts.index(":")])]="".join(texts[texts.index(":")+1::])
    elif x[p+1]in funcs:x[p+1]=funcs[x[p+1]]
    po+=1
   po=0;p+=1
  if"main"in funcs:
    x.append(funcs["main"])
    x.pop(x.index("main"))
  return[x,funcs,var,oldx]
 def execu(x)->None:
  p=po=0
  c=x[0]#commenting this out since these aren't used YET;funcs=x[1];var=x[2]
  while len(c)>p:
   while len(c[p])>po:
    if c[p].startswith("text("):
     po+=5
     try:
      while c[p][po]!=")":
       print(c[p][po],end="");po+=1
     except IndexError:print(f"ERROR: IndexError occured at line {p+1},\nperhaps you forgot to add a closing parenthesis?")
    else:print(f"\"{x[3][p]}\"\nERROR: Unknown command found in line {p+1}");break
    po+=1
   po=0;p+=1
 execu(phar(x))
 print(f"\ntook {time()-t:.4f} seconds")
def CPEC():
 """**C**ompass **P**harsing and **E**xcution **C**onsole
 
 An IDLE like console if no file for executing is added to the langauge's command arguments list"""
 print(f"Compass v {VER} {LUD} by Gaham (Thevitebsk)","="*55,"Type \"$clear\" to reset code memory, \"$exec\" to execute code memory","And \"$exit\" to end this sesion",sep="\n")
 code=[]
 while 1:
  code.append(input("»"))
  if"$help"in code:code.pop();manual()
  elif"$clear"in code:
   code.pop()
   code.clear()if code else print("There is no memory to clear")
  elif"$exit"in code:exit()
  elif"$exec"in code:code.pop();Compass("\n".join(code))
try:Compass(open(sys.argv[1]).read()) if sys.argv[1:] else CPEC()
except Exception as e:print(f"NOTICE:\"{e}\" got emitted. Notify the creator in discord (belarusianflag) or make a issue detailing the problem")
