l=[[1,2,3],[4,5,6],[7,8,9]]
m=[]
n=[]
for i in l:
    for j in i:
        c=j*5
        n.append(c)
        #c=0
    m.append(n)
    n=[]
print(m)
