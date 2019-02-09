from tkinter import *

win = Tk()
operators =""
def no(numbers):
    global operators
    operators = operators + str(numbers)
    a.set(operators)

def eqaul_to(num):
    global operators
    total = str(eval(operators))
    a.set(total)

def clear():
    global operators
    operators=""
    a.set(operators)
win.geometry("300x300")
win.configure(background="#A9A9A9")
a=StringVar()
text = Entry(win,bd="10",textvariable=a,font=("",20))
text.grid(rowspan="3",columnspan="90")
btn1 = Button(win,width="4",text="1",font=("",10),command=lambda:no(1) )
btn1.grid(row="4",column="1")
btn2 = Button(win,width="4",text="2",font=("",10),command=lambda:no(2))
btn2.grid(row="4",column="2")
btn3 = Button(win,width="4",text="3",font=("",10),command=lambda:no(3))
btn3.grid(row="4",column="3")
clr = Button(win,width="4",text="C",bg="red",font=("",10),command=lambda:clear())
clr.grid(row="4",column="4")
btn4 = Button(win,width="4",text="4",font=("",10),command=lambda:no(4))
btn4.grid(row="5",column="1")
btn5 = Button(win,width="4",text="5",font=("",10),command=lambda:no(5))
btn5.grid(row="5",column="2")
btn6 = Button(win,width="4",text="6",font=("",10),command=lambda:no(6))
btn6.grid(row="5",column="3")
div = Button(win,width="4",text="/",font=("",10),command=lambda:no("/"))
div.grid(row="5",column="4")
btn7 = Button(win,width="4",text="7",font=("",10),command=lambda:no(7))
btn7.grid(row="6",column="1")
btn8 = Button(win,width="4",text="8",font=("",10),command=lambda:no(8))
btn8.grid(row="6",column="2")
btn9 = Button(win,width="4",text="9",font=("",10),command=lambda:no(9))
btn9.grid(row="6",column="3")
mul = Button(win,width="4",text="*",font=("",10),command=lambda:no("*"))
mul.grid(row="6",column="4")
plus = Button(win,width="4",text="+",font=("",10),command=lambda:no("+"))
plus.grid(row="7",column="1")
btn0 = Button(win,width="4",text="0",font=("",10),command=lambda:no(0))
btn0.grid(row="7",column="2")
minus = Button(win,width="4",text="-",font=("",10),command=lambda:no("-"))
minus.grid(row="7",column="3")
equalto = Button(win,width="4",text="=",font=("",10),command=lambda:eqaul_to("="))
equalto.grid(row="7",column="4")
win.mainloop()
