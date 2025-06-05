a=7
if (type(a)is int):
    print("true")
else:
    print("false")

a=2.4
if (type(a)is not float):
    print("true")
else:
    print("false")

x=20
y=20

if (x is y):
    print("x and y same identity")
y=25
if (x is not y):
    print("x and y have different identity")