code=input("Enter number: ")
nwd=""
i=0
temp=0
while(i<len(code)):
    ch=code[i]
    temp=(temp*10)+int(ch)
    if(temp<123 and temp>96):
        p=chr(temp)
        temp=0
        nwd=nwd+p
    elif(temp<92 and temp>64):
        p=chr(temp)
        temp=0
        nwd=nwd+p
    elif(temp==32):
        p=chr(temp)
        temp=0
        nwd=nwd+p
    elif(temp<58 and temp>47):
        p=chr(temp)
        temp=0
        nwd=nwd+p
    i=i+1

print(nwd)
