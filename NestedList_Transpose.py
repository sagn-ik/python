A=[]
for i in range (0,3):
    B=[]
    for j in range (0,3):
        x=int(input("Enter a number: "))
        B.append(x)
    A.append(B)

T=[]
for i in range (0,3):
    C=[]
    for j in range (0,3):
        x=A[j][i]
        C.append(x)
    T.append(C)

print("Transpose: ")
for i in range (0,3):
    for j in range (0,3):
        x=T[i][j]
        print(x,end=" ")
    print()
