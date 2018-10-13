import math
def paskal(n):
    c=[]
    for i in range(1,n+1,1):
        for k in range(0,i+1):
            c.append(math.trunc(math.factorial(i)/(math.factorial(k)*math.factorial(i-k))))
            
    return(c)
n=int(input())
print(1)
a=[]
a=paskal(n)
m=0
for i in range(0,len(a)):
    if a[i]==1:
        m=m+1
    if m==2:
        print(a[i])
    else:
        print(a[i], end=' ')