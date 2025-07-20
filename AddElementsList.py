# Add elements of 2 lists and store it into one.

A=[0]*5
B=[0]*5
C=[0]*5

for i in range(0,5):
    A[i]=int(input("Enter a number for list A: "))
    B[i]=int(input("Enter a number for list B: "))
    C[i]=A[i]+B[i]

print(C)
