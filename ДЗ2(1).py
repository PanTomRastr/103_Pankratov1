def factorial1(n):
    f=1
    if (n < 0) or (type(n) != int): 
        return ValueError 
    for i in range(1,n+1):
       f=i*f
    return(f)
m=int(input())
print(factorial1(m))


def factorial2(n):
    if n < 0 or type(n) != int: 
        return ValueError 
    if n==0:
        return 1
    else:
        return n*factorial2(n-1)
print(factorial2(m))
