n=input("Enter a number:")
r=0
k=0
if len(n)>1:
    while True:
        for i in n:
            r=r+int(i)
        print(r)
        c=str(r)
        for j in c:
            k=k+int(j)
        print(k)
        if len(n)==1:
            break
else:
    print(n)