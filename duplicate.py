x=[]
n=int(input("Enter the no. of elements in array="))
print("Enter the elements of the array:")

for i in range(0,n):
    x.append(int(input()))

for a in range(0,n):
    c=-1
    for j in range(0,n):
        if(x[a]==x[j]):
                c+=1
    if(c>0):
        for k in range(0,c):
            x.remove(x[a])

print(x)
