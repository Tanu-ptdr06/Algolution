import array
arr=array.array('i',[23,45,12,67,45,2,9,23,12,67])
unique=[]
c=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if(arr.count(arr[i]) == 1 and arr[i] not in unique):
        unique.append(arr[i])
        
print(unique)
