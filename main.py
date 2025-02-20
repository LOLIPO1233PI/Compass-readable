# Compass implementation by Gaham (Thevitebsk) Y25
# A language based on Pascal
from time import*
def Compass(x:str):
 var={};t=time()
 def phar(x):
  p=po=0
  x=x.strip().split("\n");oldx=x
  texts=[];funcs={}
  while len(x)>p:
   while len(x[p])>po:
    if x[p].startswith("begin "):
     po+=6
     while x[p][po]!=":":texts.append(x[p][po]);po+=1
     x.insert(p+1,x[p][po+1::]);x[p]=x[p][6:po]
     if not x[p+1]:print(f"ERROR:Function {x[p]} has no body");exit()
     else:funcs[x[p-1]]=x.pop(p+1)
    elif x[p][po]==":":
     while 0<po:po-=1
     while x[p][po]!=";":texts.append(x[p][po]);po+=1
     var["".join(texts[0:texts.index(":")])]="".join(texts[texts.index(":")+1::])
    po+=1
   po=0
   p+=1
  if"main"in funcs:x.append(funcs["main"]);x.pop(x.index("main"))
  return [x,funcs,var]
 def execu(x):
  p=po=0
  c=x[0];funcs=x[1];var=x[2]
  while len(c)>p:
   while len(c[p])>po:
    if c[p].startswith("text("):
     po+=5
     while c[p][po]!=")":print(c[p][po],end="");po+=1
    po+=1
   po=0
   p+=1
 execu(phar(x));print(f"\ntook {time()-t:.4f} seconds")
