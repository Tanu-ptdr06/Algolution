import array
arr=array.array('i',[])
ab=list(arr)
for i in range(5):
    a=int(input("enter value "))
    ab.append(a)
print(max(ab))
    
