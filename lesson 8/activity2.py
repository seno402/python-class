print("enter a numerator")
numn=int(input())
print ("enter a demonenator")
numd=int(input())
if numn % numd== 0:
    print("\n"+str(numn)+ " is divisable by" +str(numd))
else:
    print("\n"+str(numn)+ "is not divisable by"+str(numd))