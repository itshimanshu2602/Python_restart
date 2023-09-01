string = "aaabbccccdaajj"
mylist = list(string)
mylist.append(" ")

z = 0
c = []
for y in range(len(mylist)-1):
    z = z+1
    if mylist[y] != mylist[y+1]:
        c.append(z)
        z=0
   
a = []
for x in range(0, len(string)-1):
    if string[x] == string[x+1]:
        a.append(int(x))

k = ""
for x in a:
    mylist[int(x)] = ""
    
for v in range(0, len(mylist)-1):
    k = k + str(mylist[v])
    
list2 = list(k) 
for h in range(len(c)):
    list2.insert(2*h+1, c[h])
    
k=""    
for v in range(0, len(list2)):
    k = k + str(list2[v])
    
  
print(k)

