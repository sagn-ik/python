word=input("Enter a word: ")
n=int(input("Enter number: "))
i=0
nwd=""
while(i<len(word)):
    ch=word[i]
    temp=ord(ch) + n
    if(temp>90) :
        temp=temp-26
    nwd=nwd+chr(temp)
    i=i+1

print(nwd)
