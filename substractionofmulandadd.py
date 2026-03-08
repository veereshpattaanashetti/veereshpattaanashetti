n=int(input("Enter size:"))
l=[]
for i in range(n):
    e=int(input())
    l.append(e)
print(l,end=" ")
s=0
for i in l:
    s=s+i
print("\nsum is",s)
m=1
for j in l:
    m=m*j
print("product is",m)
print("final ouput",m-s)