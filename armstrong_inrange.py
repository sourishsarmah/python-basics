x,y=int(input("Enter the starting number=")) ,int(input("Enter the ending number="))
print("Amrstrong Numbers:")
for i in range (x,y+1):
    s=0
    n=i
    x=0
    while n>0:
        n=n//10
        x+=1
    n=i
    while n>0:
        d=int(n%10)
        s=s+(d**x)
        n=n//10
    if s==i:
        print(i)
