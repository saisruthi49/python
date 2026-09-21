
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))


operation=input("enter operation(+,-,*,/):")

sum=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2


if operation=="+":
    print("result is",sum)
elif operation=="-":
    print("result is",sub)
elif operation=="*":
    print("result is",mul)
elif operation=="/":
    print("result is",div)
else:
    print("invalid operation")
