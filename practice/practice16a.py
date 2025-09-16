l=[[1,2],[4,5,6,7],[8,[9,3]]]
print(l)
n=[]
for i in l:
    for j in i:
        #a=type(j)
        if type(j) is list:
            for h in j:
                n.append(h)
        else:
            n.append(j)
print(n)