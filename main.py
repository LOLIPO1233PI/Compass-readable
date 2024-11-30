print("Pascgolf")
i=input("Input your code:\n");p=0
o=0;e=0;v={"n":[],"v":[]};ts=[]
try:
   while len(i)>p:
      if e==1:break
      elif i[p]=="[":o=1
      elif i[p]=="]":o=0
      elif i[p+1]==":"and i[p]=="v"and o==1:
         v["n"].append(i[p+2]);p+=3
         while i[p]!=";":ts.append(i[p]);p+=1
         ts.reverse()
         while len(ts)>1:ts.append(ts.pop()+ts.pop())
         v["v"].append(ts.pop())
      else:e=1;print("not a valid pascgolf command",i[p])
      p+=1
except IndexError:...
