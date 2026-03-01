import math
while True:
    print("Simple Calculator")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue
    choice = input("enter 1 for add, 2 for subtract, 3 for multiply, "
              "4 for divide, 5 for power**, 6 for modulus%, "
              "7 for square root: ")
    if choice =="1":
                print("result is:",num1+num2)
    elif choice =="2":
                print("result is:",num1-num2)
    elif choice =="3":
                print("result is:",num1*num2)
    elif choice=="4":
                if num2!=0:
                 print("result is:",num1/num2)
                else:
                 print("cannot divide by zero")
    elif choice=="5":
                print("result is :",num1**num2)
    elif choice=="6":
                if num2!=0:
                    print("result is:,num1 % num2")
                else:
                    print("cannot divide by zero")
    elif choice == "7":
        if num1 >= 0:
            print("Result:", math.sqrt(num1))
        else:
            print("cannot take square root of negative number")

    else:
        print("invalid choice")
    repeat=input("continue?(yes/no):")
    if repeat=="no":
        break
