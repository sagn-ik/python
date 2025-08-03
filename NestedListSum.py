A=[]
for i in range (0,3):
    B=[]
    for j in range (0,3):
        x=int(input("Enter a number: "))
        B.append(x)
    A.append(B)

sum=0

for i in range (0,3):
    for j in range (0,3):
        print(A[i][j],end=" ")
        sum=sum+A[i][j]
    print("Sum:",sum)
    sum=0
