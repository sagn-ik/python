conv={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}

num=int(input("Enter a number: "))
word=""
while(num>0):
    b=num%10
    word=conv[b]+" "+word
    num//=10

print(word)
