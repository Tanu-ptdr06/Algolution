import itertools
a="motor"
p=itertools.permutations(a)
l=[]
for i in p:
    #print(''.join(i))
    l.append(''.join(i))
#print(l)
c=0
for j in l:
    b=j[::-1]
    #print("hfdd",b)
    if(b==j):
        c+=1
        print(j)
        break
if(c!=0):
    print("yes")
else:
    print("nope")
