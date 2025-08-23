word=input("Enter a word: ")
nwd=""
i=0
while(i<len(word)):
    ch=word[i]
    if(ch in "aeiou"):
        ch=word[i+1]
        nwd=nwd+ch
    else:
        ch=word[i-1]
        nwd=nwd+ch
    i+=1

print(nwd)
