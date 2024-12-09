c="A man, a plan, a canal :panama"
a=c.lower().replace(" ","").replace(',',"").replace(':',"")
is_pall=True
for i in range(len(a)//2):

    if(a[i]!=a[len(a)-1-i]):
        is_pall=False
        break
if is_pall:
    print("yup")
else:
    print("nop")
