#W.A.P TO FIND THE MIDDLE NUMBER IN GROUP OF THREE NUMBER 
a = int(input("Enter your number a:"))
b = int(input("Enter your number b:"))
c = int(input("Enter your number c:"))
if(a>b and a<c) or (a<b and a>c):
    print("Middle number is : ",a)
elif (b>a and b<c) or (b<a and b>c):
    print("Middle number is:",b)
else:
    print("Middle number is:",c)