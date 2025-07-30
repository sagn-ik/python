A=[]
for i in range (0,3):
    B=[]
    for j in range (0,3):
        x=int(input("Enter a number: "))
        B.append(x)
    A.append(B)

max=A[0][0]
min=A[0][0]

for i in range (0,3):
    max=A[i][0]
    min=A[i][0]
    for j in range (0,3):
        print(A[i][j],end=" ")
        if(A[i][j]>max):
            max=A[i][j]
        if(A[i][j]<min):
            min=A[i][j]
    print("Max:",max,"Min: ",min)
