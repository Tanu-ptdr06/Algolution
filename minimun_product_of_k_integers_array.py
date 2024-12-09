import array
arr=array.array('i',[11,8,5,7,5,100])
k=int(input("enter value"))
l=[]
for i in range(len(arr)-k+1):
    c=[]
    for j in range(i,k+i):
        c.append(arr[j])
    #print(c)
    p=1
    for m in range(len(c)):
        p=p*c[m]
    #print(p)
    l.append(p)
#print(l)
print(min(l))
