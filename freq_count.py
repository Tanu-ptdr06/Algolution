#count frequency of each element
import array
arr=array.array('i',[12,2,2,11,4,5,5,11,2,12,7])

d=[]
e=[]
for i in range(len(arr)):
    if arr[i] not in d:
        c=0
        for j in range(len(arr)):
          if (arr[i]==arr[j] ):
            c+=1

        d.append(arr[i])
        if c>1:
          e.append(c)

#print(d)
print(e)