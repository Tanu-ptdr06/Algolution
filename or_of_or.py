import array
arr=array.array('i',[10,100,1000])
ors=[]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        l=[]
        for k in range(i,j+1):
            #print(arr[k])
            l.append(arr[k])
        #print(l)
        b=0
        for m in range(len(l)):
            b=b|l[m]
        ors.append(b)
        #print(b)
#print(ors)
c=0
for n in range(len(ors)):
    c=c|ors[n]
print("OR of OR of subarrays is",c)
