def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n= int(input("Enter value of n="))
r= int(input("Enter value of r="))
p=fact(n)/fact(r)

print("Permutation=",p)
