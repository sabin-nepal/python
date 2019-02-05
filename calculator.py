while 1:
    number1 = int(input("Enter first number"))
    number2 = int(input("Enter second number"))
    print("Choices are")
    print("1.Add")
    print("2.Mul")
    print("3.Sub")
    print("4.Divide")
    print("5.Exit")
    choose = int(input("Enter a choice form 1 to 4"))

    if choose == 1:
        add = number1+number2
        print(add)
    if choose==2:
        mul = number1 * number2
        print(mul)

    if choose==3:
        sub = number1 - number2
        print(sub)
    if choose==4:
        div = number1 / number2
        print(div)
    if choose==5:
        print('Exiting..')
        break