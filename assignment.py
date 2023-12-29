# (1)write a program to find odd or even number using conditional statement

num1=float(input("enter 1st number: "))
num2=float(input("enter 2nd number: "))
num3=float(input("enter 3rd number: "))
if num1>num2 and num3:
    print ("num 1 is biggest number")
elif num2>num3 and num1:
    print("num 2 is biggest number")
elif num3>num1 and num2:
    print("num 3 is biggest number")
else:
    print("three numbers are equal")
    
# (2)⁠find largest of three numbers

num=float(input("please enter the number: "))
if num%2==0:
    print("number is even")
else:
    print("number is odd")
    
#(3)⁠find leap year using conditional statement

num=float(input("enter year: "))
if num%4==0:
    print("leap year")
elif num%400==0:
        print("leap year")
elif num%100!=100:
        print("not a leap year")

