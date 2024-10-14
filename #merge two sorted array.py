#merge two sorted array
import array
a = array.array('i', [1, 2, 3, 7])
b=array.array('i',[4,5,8,9])
c=array.array('i',[])
i=0
j=0
while(i<len(a) and j<len(b)):
    if(a[i]<b[j]):
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1

while(i<len(a)):
    c.append(a[i])
    i+=1

while(j<len(b)):
    c.append(b[j])
    j+=1
print(c)