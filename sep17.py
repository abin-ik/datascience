l=[1,2,3,4,5,6,7,8]
s=[]
m=0
for i in l:
    for j in l:
        if j==i:
            m=i+j
            s.append(m)
            m=0
print(s) 