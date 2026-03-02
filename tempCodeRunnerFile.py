n=input("Enter a number:")
r=0
while len(n)>1:
    for i in n:
        r=r+int(i)
    n=str(r)
print(n)
        