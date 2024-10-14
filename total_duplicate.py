import array
arr=array.array('i',[1,2,3,4,1,2])
b=0
c=[]
for i in range(len(arr)):
    for j in range(len(arr)):
         if (i!=j and arr[i]==arr[j] and arr[i] not in c) :
             c.append(arr[i])
             b+=1
print(b)