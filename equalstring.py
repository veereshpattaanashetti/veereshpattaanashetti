l=["ab","c"]
l2=["a","bc"]
s1=""
s2=""
for i in range(len(l)-1):
    s1=l[i]+l[i+1]
    s2=l2[i]+l2[i+1]
if s1==s2:
    print("true")
print(len(l))       




   
