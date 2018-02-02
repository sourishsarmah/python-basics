n=int(input("Enter number="))
s=0
x=n
i=0
while n>0:
    n=n//10
    i+=1
n=x
while n>0:
    d=int(n%10)
    s=s+(d**i)
    n=n//10
if s==x:
    print("Armstrong Number")
else:
    print("NOT an Armstrong Number")
