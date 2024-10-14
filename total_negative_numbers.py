import array
arr=array.array('i',[12,-1,-3,5,6,-9])
l=0
for i in range(len(arr)):
    if(arr[i]<0):
        l+=1
print(l)
        