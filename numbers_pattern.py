n=5
for i in range(n):
    for j in range(1):
       if i%2==0:
        for m in range(n):
          print(m+1,end='')
       else:
          for k in range(n,0,-1):
            print(k,end='')
    for l in range(n):
        print('',end='')
    print()
