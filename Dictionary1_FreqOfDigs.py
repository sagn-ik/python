freq={}
num=int(input("Enter a number: "))
while(num>0) :
    i=num%10
    if(i not in freq):
        n=num
        count=0
        while(n>0):
            b=n%10
            if(b==i):
                count+=1
            n//=10
    freq[i]=count
    num//=10

print(freq)
