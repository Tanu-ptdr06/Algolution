n=5
for i in range(n):
    for j in range(1):
       if i==0 or i==n-1:
          for k in range(n):
            print('1',end='')
       else:
           print('1',end='')
           for l in range(1,n-1):
              print('0',end='')
           print('1',end='')
    print()
