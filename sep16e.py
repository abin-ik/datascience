l=[[1,2,3],[4,5,9]]
m=[]
d=[]
e=[]
for i in l:
    d=m
    m=[]
    for j in i:
        m.append(j)
        
print(m)
print(d)
f=0
for v in range(len(m)):
    
    z=m[v]+d[f]
    e.append(z)
    v=v+1
    f=v
   


print(e)