# Compass implementation Y25 @Gaham (Thevitebsk)
# A language based on Pascal
class Compass:
 def phar(x:str):
  oldx=x.strip().split("\n")
  x=x.strip().split("\n")
  p=po=0
  texts=[];funcs={}
  while len(x)>p:
   while len(x[p])>po:
    if x[p].startswith("begin "):
     po+=6
     while x[p][po]!=":":texts.append(x[p][po]);po+=1
     x.insert(p+1,x[p][po+1::]);x[p]=x[p][6:po]
     if not x[p+1]:print(f"ERROR:Function {x[p]} has no body");exit()
     else:funcs[x[p-1]]=x.pop(p+1)
    po+=1
   p+=1
   if"main"not in x:print(f"\"{oldx[0]}\"\nERROR:Function main requiers to be initated");exit()
  print(x,funcs)
Compass.phar("""""")