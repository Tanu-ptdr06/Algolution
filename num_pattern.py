n=5
for i in range(1):
    for j in range(n):
        for k in range(j+1,n+1):
            print(k,end='')
        for l in range(j+1):
            print('5',end='')
        print()
    print()