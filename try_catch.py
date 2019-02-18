# try:
#     a=int(input("Enter a number"))
#     div = a/0
#     print(div)
# except ZeroDivisionError:
#     print("Nothing can be divided by zero")
# except:
#     print("something wrong with your input")


class LowAgeError(Exception):
    def __init__(self):
        super(LowAgeError,self).__init__("Age matter")
 
age = int(input("enter the age"))
if age <18:
    raise LowAgeError
else:
    print('accepted')
 