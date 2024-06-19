import math
def addition(num1,num2):
    add=num1+num2
    return add

def subtraction(num1,num2):
    subs=num1-num2
    return subtraction

def multiplication(num1,num2):
    mul=num1*num2
    return mul

def division(num1,num2):
    if num2==0:
        print("NOT DEFINED")
    else:
        div=num1/num2
        return div

def modulus(num1,num2):
    mod=num1%num2
    return mod

def power(num1,num2):
    math.pow(num1,num2)
    return pow

def trigonometric(num):
    print("\n===CHOOSE TRIGNOMETRIC IDENTITIY===")
    print("1.SIN")
    print("2.COS")
    print("3.TAN")
    print("4.COT")
    print("5.SEC")
    print("6.COSEC")
    print("===================================")
    ch=int(input("ENTER IDENTITY : "))
    if ch==1:
        return math.sin(num)
    elif ch==2:
        return math.cos(num)
    elif ch==3:
        return math.tan(num)
    elif ch==4:
        return math.cot(num)
    elif ch==5:
        return math.sec(num)
    elif ch==6:
        return math.cosec(num)
    else:
        print("Incorrect Choice")

def logarithmic(num):
    log=math.log(num)
    return log

def sqrt(num):
    return math.sqrt(num)

def cbrt(num):
    return math.cbrt(num)

def main():
    while True:
        print("\n=====CALCULATOR=====")
        print("1.ADDITION")
        print("2.SUBTRACTION")
        print("3.MULTIPLICATION")
        print("4.DIVISION")
        print("5.EXPONENTIAL")
        print("6.TRIGONOMETRIC")
        print("7.LOGARITHMIC")
        print("8.SQUARE ROOT")
        print("9.CUBE ROOT")
        print("====================")
        choice=int(input("enter your choice : "))
        if choice==1:
            num1=float(input("Enter First Number : "))
            num2=float(input("Enter Second Number :"))
            print(addition(num1,num2))
        elif choice==2:
            num1=float(input("Enter First Number : "))
            num2=float(input("Enter Second Number :"))
            print(subtraction(num1,num2))
        elif choice==3:
            num1=float(input("Enter First Number : "))
            num2=float(input("Enter Second Number :"))
            print(multiplication(num1,num2))
        elif choice==4:
            num1=float(input("Enter First Number : "))
            num2=float(input("Enter Second Number :"))
            print(division(num1,num2))
        elif choice==5:
            num1=float(input("Enter First Number : "))
            num2=float(input("Enter Second Number :"))
            print(power(num1,num2))
        elif choice==6:
            num=float(input("Enter Number : "))
            print(trigonometric(num))
        elif choice==7:
            num=float(input("Enter Number : "))
            print(logarithmic(num))
        elif choice==8:
            num=float(input("Enter Number : "))
            print(sqrt(num))
        elif choice==9:
            num=float(input("Enter Number : "))
            print(cbrt(num))
            
        else:
            print("Incorrect Choice")
main()