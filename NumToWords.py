num = input("Enter number: ")
l= len(num)
word=""
cnt=3-l

ones=["","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
tens=["","TEN","TWENTY","THIRTY","FORTY","FIFTY","SIXTY","SEVENTY","EIGHTY","NINTY"]
hundreds=["","ONE HUNDRED","TWO HUNDRED","THREE HUNDRED","FOUR  HUNDRED","FIVE  HUNDRED","SIX  HUNDRED","SEVEN  HUNDRED","EIGHT  HUNDRED","NINE  HUNDRED"]
tens_ex=["","ELEVEN","TWELVE","THIRTEEN","FOURTEEN","FIFTEEN","SIXTEEN","SEVENTEEN","EIGHTEEN","NINETEEN"]

while cnt<l:
    ldg=num[cnt]
    ldg=int(ldg)
    if cnt == 0 :
        word= word+" "+hundreds[ldg]
    elif cnt == 1:
        if(ldg==1):
            word= word+" "+tens_ex[ldg]
            break
        word= word+" "+tens[ldg]
    elif cnt==2:
        word= word+" "+ones[ldg]
    cnt+=1

print (word)
