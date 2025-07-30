Prime=[]
count=0
i=2
while(count!=9):
    fact=0
    for j in range (2,i):
       if(i%j ==0):
           fact+=1
    if(fact==0):
        Prime.append(i)
        count+=1
    i+=1

count=0
A=[]
for i in range (0,3):
    B=[]
    for j in range (0,3):
        x=Prime[count]
        count+=1
        B.append(x)
    A.append(B)

print("Prime Numbers: ")
for i in range (0,3):
    for j in range (0,3):
        print(A[i][j],end="\t")
    print()

