import array
arr=array.array('i',[44,56,25,56,44])
is_pall=True
for i in range(len(arr)):
    if(arr[i]!=arr[len(arr)-i-1]):
        is_pall=False
        break
if is_pall:
    print("true")
else:
    print("false")
