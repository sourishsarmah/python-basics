x=[]
n=int(input("Enter the no. of elements in Array"))
print("Enter the Elements of the Array")
for i in range(0,n):
    x.append(input())
c=100
while(c!=0):
    c=int(input('Choose:1.Insertion\t2.Remove'))
    if(c==1):
        l=int(input("Location="))
        v=input("Enter value=")
        x.insert(l,v)
    elif(c==2):
        v=input("Value to remove=")
        x.remove(v)
    else:
        print("Incorrect option")
    print(x)

