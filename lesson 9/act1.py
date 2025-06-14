medical_cause=input("did you have any medical reason yes or no?")
attendance= int (input(" enter you attendance"))
if medical_cause=="yes":
    print("you are allowed")
else:
    if attendance>=75:
        print("you are allowed")
    else: 
        print("you are not allowed")