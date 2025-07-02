# Prograam to sort a sentence

sent=input("Enter a sentence: ")
L=sent.split()
L.sort()
print(L)
length=len(L)

'''for j in range (65,91):
    i=0
    while(i<length):
        word=L[i]
        ch=word[0]
        if(ch== (chr(j)) ):
            fin.append(word)
        i+=1
for i in range (0,length):
    for j in range (0,length-i-1):
        if(L[j]<L[j+1]):
            wd=L[j]
            L[j]=L[j+1]
            L[j+1]=wd

# sent.sort()
print(L)'''
