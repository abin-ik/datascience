l=[[1,2,3],[4,5,6]]
m=[]
d=[]
c=[]
e=[]
for i in l:
    d=m
    m=[]
    for j in i:
        m.append(j)
        
print(m)
print(d)
for v in m:
    for f in d:
        z=v+f
        e.append(z)
        break
print(x)