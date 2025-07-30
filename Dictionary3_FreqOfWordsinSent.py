sent=input("Enter a sentence: ")
freq={}

list_words=sent.split()

for i in range (0,len(list_words)) :
    wd=list_words[i]
    count=0
    if(wd not in freq) :
        for j in range (0,len(list_words)) :
            temp=list_words[j]
            if(wd==temp):
                count+=1
        freq[wd]=count

print(freq)
