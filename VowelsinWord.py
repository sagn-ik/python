sentence=input("Enter a line: ")
words=sentence.split()
i=0
while(i<len(words)):
    print(words[i],end=" has vowels: ")
    j=0
    count=0
    while(j<len(words[i])):
        ch=(words[i])[j]
        if ch in "AEIOUaeiou":
            count+=1
        j+=1
    print (count)
    i+=1
