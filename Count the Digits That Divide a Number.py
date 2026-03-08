
def divisible(n):
    count=0
    for i in n:
        if int(n)%int(i)==0:
            count+=1
    print(count)
n=input("Enter a number:")

divisible(n)