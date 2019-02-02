print("Enter a choice from 1 to 4")
print("1.Add")
print("2.Mul")
print("3.Sub")
print("4.Divide")
number1=0
number2=0
while 1:
    print("Enter a choice form 1 to 4")
    number1 = int(input("Enter first number"))
    number2 = int(input("Enter second number"))
    choose = int(input("Choose number"))
    if choose == 1:
        add = number1+number2
        print(add)
        number1 = int(input("Enter first number"))
        number2 = int(input("Enter second number"))
        choose = int(input("Choose number"))
    if choose==2:
        mul = number1 * number2
        print(mul)
        number1 = int(input("Enter first number"))
        number2 = int(input("Enter second number"))
        choose = int(input("Choose number"))
    if choose==3:
        sub = number1 - number2
        print(sub)
        number1 = int(input("Enter first number"))
        number2 = int(input("Enter second number"))
        choose = int(input("Choose number"))
    if choose==4:
        div = number1 / number2
        print(div)
        number1 = int(input("Enter first number"))
        number2 = int(input("Enter second number"))
        choose = int(input("Choose number"))
