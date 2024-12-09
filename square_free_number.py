#set-3 qu-1 square free number
import math
a=72
l=[]
d=[]
for i in range(2,a):
    if(a%i==0):
        l.append(i)
for j in range(len(l)):
    b=math.isqrt(l[j])
    if(b*b==l[j]):
        d.append(l[j])
for k in range(1,len(l)):
    c=[]
    for m in range(1,l[k]+1):
        if(l[k]%m==0):
            c.append(m)
    print("factors ",l[k],c)
for o in l[:]:
    for p in d:
        if o != p and o % p == 0:  #
           l.remove(o)
           break
for r in d:
    if r in l:
        l.remove(r)




print(l)
#print(d)
print(len(l))
