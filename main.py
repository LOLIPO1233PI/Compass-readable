print("Pascgolf")
i=input("Input your code:\n");p=int(0)
o=0;e=0
while len(i)>p and e!=1:
   if i[p]=="[":o=1
   elif i[p]=="]":o=0
   p+=1