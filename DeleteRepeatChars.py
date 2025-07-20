word=input("Enter string: ")
i=0
nwd=""
while(i<len(word)):
    ch=word[i]
    if(ch not in nwd):
        nwd=nwd+ch
    i+=1
print(nwd)

'''
for ch in S:
    if ch not in S1:
        s1=s1+ch
'''
