n=int(input("Enter number="))
s=0
x=n
while n>0:
    d=int(n%10)
    s=s*10+d
    n=n//10
if s==x:
    print("Palindrome Number")
else:
    print("NOT an Palindrome Number")
