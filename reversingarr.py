#reversing array
import array
arr=array.array('i',[])
for i in range(7):
    a=int(input("enter numbers"))
    arr.append(a)
print(arr)
arr.reverse()
print(arr)