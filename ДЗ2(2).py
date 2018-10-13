def search(n):
    m=0
    for i in range(n-1,0,-1):
        if n%i==0:
            m=m+i
    return(m)
n=int(input())
m=search(n)
if n==m:
    print('TRUE')
else :
    print('FALSE')