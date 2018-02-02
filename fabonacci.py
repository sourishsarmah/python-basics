n=int(input("Enter no. of terms="))
a=1
b=1
print(a)
print(b)
for i in range(1,n-1):
    s=a+b
    a=b
    b=s
    print(b)
