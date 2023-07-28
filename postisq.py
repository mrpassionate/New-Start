a=input("Enter a number: ")
a=int(a)

if a < 0:
    print("Sorry , We count only postive integers")
if a > 0:
    for i in range(1,11,1):
        print(a ,"*" ,i, "=", a*i)