a="()[]{})("
c=0
d=0
e=0
for i in range(len(a)):
    if('(' ==a[i]):
        c+=1
    elif(')'==a[i]):
        c-=1
    elif('['==a[i]):
        d+=1
    elif(']'==a[i]):
        d-=1
    elif('{'==a[i]):
        e+=1
    elif('}'==a[i]):
        e-=1
    if(c<0 or d<0 or e<0):
        break
if(c==0 and d==0 and e==0):
    print("val")
else:
    print("nop")
