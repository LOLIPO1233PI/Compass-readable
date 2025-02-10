# Compass implementation Y25 @Gaham (Thevitebsk)
# A language based on Pascal
class Compass:
 def phar(x:str):
  x=x.strip().split("\n")
  p=po=0
  texts=[];funcs={}
  while len(x)>p:
   while len(x[p])>po:
    if x[p][po:po+6]=="begin ":
     po+=6
     while x[p][po]!=":":texts.append(x[p][po]);po+=1
     x.insert(p+1,x[p][po+1::]);x[p]=x[p][6:po];funcs[x[p-1]]=x.pop(p+1)
    po+=1
   p+=1
  print(x)
Compass.phar("""begin main:print("Hello, world!")""")
