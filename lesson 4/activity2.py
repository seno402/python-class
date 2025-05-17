#taking total amount imput from user
amount=int(input("please enter amount to be withdrawn"))
#calculating the number of notes on different denominations 
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("notse of 100 rupee", note1)
print("notes of 50 rupee", note2)
print("notes of 10 rupee", note3)