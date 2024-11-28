import array
arr=array.array('i',[12,2,2,11,4,5,5,11,2,12,7])
dict={}
for i in range(len(arr)):
    if arr[i] in dict:
        dict[arr[i]]+=1
    else:
        dict[arr[i]]=1
print(dict)

    
