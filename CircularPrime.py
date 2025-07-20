snum=input("Enter a number: ")
tnum=snum
length=len(snum)
flag=0
fact=0
i=2
num=int(tnum)
while i<num:
    if(num%i==0):
        fact+=1
    i+=1
if fact!=0:
    flag=1
s1=tnum[0:length]
s2=tnum[-1]
sf=s2+s1
num=int(sf)
while snum!=tnum and flag!=1:
    i=2
    fact=0
    while i<num:
        if num % i==0:
            fact+=1
        i+=1
    if fact!=0:
        flag=1
        break
    s1=tnum[0:length]
    s2=tnum[-1]
    sf=s2+s1
    num=int(sf)
    tnum=sf

if(flag==0):
    print("Cyclic Prime!!")
else:
    print("Not Cyclic Prime!!")

