def distancef(i,j):
  ''' i and j are two points where i = (x1,y1) and j = (x2,y2) and i[0] = x1 , i[1] = y1 , j[0] = x2 , j[1] = y2'''
  return ((j[1]-i[1])**2 + (j[0]-i[0])**2)

n = int(input("Enter number of points: "))
e=int(input("enter radius"))
mini=int(input("enter min points"))
'''n=12
e=2
mini=4'''
numbers=[]
l=[]
d=[]
li=[]
cc=[]
''' i in range(n):
    x = float(input("Enter X"+str(i)+": "))
    y = float(input("Enter Y"+str(i)+": "))
    numbers.append([x,y])
print(numbers)'''
#numbers=[[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,5],[4,9]]
numbers=[[3,7],[4,6],[5,5],[6,4],[7,3],[6,2],[7,2],[8,4],[3,3],[2,6],[3,5],[2,4]]
for i in numbers :
    temp=[]
    for j in numbers:
        temp.append(distancef(i,j))
        l=temp
    d.append(l)
#print(d)         #list to store distance matrix
new=[]
core=[]
rest=[]
Noise=[]
bb=[]
c=0
f=1
for i in range(n):
    for j in range(n):
        if(d[i][j]<=(e**2)):
            li.append(j)
    cc=li.copy()
    new.append(cc)
    li.clear()
#print(new)
n=-1
for i in new:
    n=n+1
    if(len(i)>=mini):
        l=i
        core.append([[n],l])
    else:
        rest.append([[new.index(i)],i])
#print(rest)
print("CORE"+str(core))
b=[]
border=[]
for i in range(len(core)):
    for j in range(len(rest)):
        if(core[i][c][c] in rest[j][f]):
            l=j
            b.append([[rest[l][c][c]],rest[j][f]])
border = []
for x in b:
    if x not in border:
        border.append(x)
print("border"+str(border))
xx=[]
zz=[]
xx1=[]
Noise=[]
zz1=[]
yy=[]
for j in core:                 #core 1d
    xx1.append(j[f])
#print(xx)
for i in new:               #diff b/w new and core
    if(i not in xx1):
        l=i
        zz.append([[new.index(l)],l])
#print(zz)
xx3=[]
for j in zz:            #zz 1d
    zz1.append(j[f])
for j in border:        #border 1d
    xx3.append(j[f])
for i in zz1:               #diff b/w zz1 and border
    if(i not in xx3):
        l=i
        yy.append(l)
#print(yy)
for i in new:
    if i in yy:
        m=i
        Noise.append([[new.index(m)],i])
print("noise"+str(Noise))
