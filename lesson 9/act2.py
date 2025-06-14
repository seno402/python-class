print("enter your ride")
print("1.bike")
print("2.car")
choice= int (input("enter your choice"))
if(choice==1):
    print("what type of bike")
    print("1.scooty\n")
    print("2.scooter\n")
    choice2=int (input("enter your choice 2"))
    if choice2==1:
        print("you have selected the scooty")
    else:
        print("you ahve selected the scooter")
elif (choice==2):
    print("what type of car")
    print("1.sedan")
    print("2.xuv")
    choice3=int (input("enter you choice"))
    if choice3==1:
        print("you ahve selected sudan")
    else:
        print("you have selected xuv") 
else:
    print("wrong choice")