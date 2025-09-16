l=[2,4,3,5,7,8,9]
m=[]
a=[]
c=[]

for i in l:
    for j in l:
        m=[]
        if i+j==9:
            m=(i,j)
            if m not in a and m[::-1] not in a:
                a.append(m)

                

            
print(a)
