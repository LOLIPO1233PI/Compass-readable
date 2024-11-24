c=" 'Hello, everyone'\""
#^INPUT HERE^
p=-1;s=[];ts=[]
while len(c)>p:
  p+=1
  if c[p]==" ":
    s.append(c[p+1]);p+=1
    if c[p+1]=="'":
      p+=2
      while c[p]!="'":ts.append(c[p]);p+=1
      while len(ts)>0:ts.append(ts.pop(0)+ts.pop(0))
  elif c[p]=="!":s.append("0" if s.pop()=="0" else "1")
  elif c[p]=="\"":print("".join(s))
