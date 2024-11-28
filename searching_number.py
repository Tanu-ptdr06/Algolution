import array
a=int(input("enter value "))
arr=array.array('i',[23,45,12,67,45,2,9,23])
c=0
for i in range(len(arr)):
    if(a==arr[i]):
        print(i)
        c+=1
        break
if(c==0):
    print("-1")
