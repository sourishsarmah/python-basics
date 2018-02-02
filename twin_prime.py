x,y=int(input("Enter the starting number:")) ,int(input("Enter the ending number:"))
for i in range (x,y+1):
    if i==1:
        continue
    c=0
    for j in range (2,i):
        if(i%j==0):
            c+=1
    if c<=0:
        k=i+2
        n=0
        for l in range(2,k):
            if(k%l==0):
                n+=1
        if n<=0:
            print (i,k)
