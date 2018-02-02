n=int(input("Enter number="))
s=0
while n>0:
    d=int(n%10)
    s=s*10+d
    n=n//10
print("Reverse of Digits=",s)
