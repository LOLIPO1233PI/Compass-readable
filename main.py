print("Pascgolf")
i=input("Input your code:\n");p=int(0)
o=bool(0);e=bool(0)
while len(i)>p and e!=1:
   if i[p]=="s":o=not o;print(o)
   p+=1
