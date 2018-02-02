x,y=int(input("Enter the starting number=")) ,int(input("Enter the ending number="))

print("Prime Numbers:")

for i in range (x,y+1):
    c=0
    for j in range (2,i):
        if(i%j==0):
            c+=1
    if c<=0 and i!=1:
        print (i)
